#!/bin/bash
set -e

CURDIR=$(cd `dirname $0`; pwd)
OUTDIR=$CURDIR/results/round3/

if [ ! -e $OUTDIR ]; then
  mkdir -p $OUTDIR
fi

cd $CURDIR

mysql_sock="/var/folders/k0/qhfn3fhn0wd8t_kc0ksszklh0000gp/T/Fb7pMsFHE5/mysqld.1.sock"
mysql_client="~/Documents/Master/Code/mysql-server-robust-planning/build-release/bin/mysql"

export mysql_connect="$mysql_client -u root -S $mysql_sock -D imdbload -t"

eval "$mysql_connect<<eof
UPDATE mysql.engine_cost SET cost_value = 0.25 WHERE cost_name = 'io_block_read_cost';
UPDATE mysql.engine_cost SET cost_value = 0.25 WHERE cost_name = 'memory_block_read_cost';
FLUSH OPTIMIZER_COSTS;

SET PERSIST innodb_stats_persistent = 1;
SET PERSIST innodb_stats_auto_recalc = 0;
-- SET PERSIST innodb_stats_persistent = 0;

SET GLOBAL optimizer_switch='hypergraph_optimizer=on';
eof"

analyze="$mysql_connect<<eof
ANALYZE TABLE aka_name;
ANALYZE TABLE aka_title;
ANALYZE TABLE cast_info;
ANALYZE TABLE char_name;
ANALYZE TABLE company_name;
ANALYZE TABLE company_type;
ANALYZE TABLE comp_cast_type;
ANALYZE TABLE complete_cast;
ANALYZE TABLE info_type;
ANALYZE TABLE keyword;
ANALYZE TABLE kind_type;
ANALYZE TABLE link_type;
ANALYZE TABLE movie_companies;
ANALYZE TABLE movie_info;
ANALYZE TABLE movie_info_idx;
ANALYZE TABLE movie_keyword;
ANALYZE TABLE movie_link;
ANALYZE TABLE name;
ANALYZE TABLE person_info;
ANALYZE TABLE role_type;
ANALYZE TABLE title;
eof"

for file in `ls queries/*.sql`; do
  bname=`basename $file`
  name=${bname%.*}
  outputmarkdown=$OUTDIR/$name.md
  outputjson=$OUTDIR/$name.json
  echo "Run $file"

  original_query=$(<$file)
  export query=${original_query/";"/"\G"}
  export query_normal=${query}
  
  export query_hash_join=${query/"SELECT "/"SELECT /*+ FORCE_JOIN(HJ) */ "}
  export query_nested_loop_join=${query/"SELECT "/"SELECT /*+ FORCE_JOIN(NLJ) */ "}


  function normal_run {
    eval "$mysql_connect<<eof
$query_normal
eof"
}

  function with_nested_loop_join {
    eval "$mysql_connect<<eof
$query_nested_loop_join
eof"
}

  function with_hash_join {
    eval "$mysql_connect<<eof
$query_hash_join
eof"
}

  export -f normal_run
  export -f with_nested_loop_join
  export -f with_hash_join

  hyperfine --prepare "eval $analyze" --warmup 2 -r 10 --export-json $outputjson --export-markdown $outputmarkdown --shell=bash normal_run with_nested_loop_join with_hash_join
done
