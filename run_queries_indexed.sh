#!/bin/bash
set -e

CURDIR=$(cd `dirname $0`; pwd)
OUTDIR=$CURDIR/test-results/upper_bound_4_levels_incremental_0_2/

if [ ! -e $OUTDIR ]; then
  mkdir -p $OUTDIR
fi

cd $CURDIR

NC='\033[0m' 
BIWhite='\033[1;97m'

mysql_client="/home/leag/MySQL/mysql-server-robust-planning/cmake-build-release/bin/mysql"
mysql_sock="/home/leag/MySQL/mysql-server-robust-planning/cmake-build-release/mysql-test/var/tmp/mysqld.1.sock"

export mysql_connect="$mysql_client -u root -S $mysql_sock -D imdbload -t"

eval "$mysql_connect<<eof
UPDATE mysql.engine_cost SET cost_value = 0.25 WHERE cost_name = 'io_block_read_cost';
UPDATE mysql.engine_cost SET cost_value = 0.25 WHERE cost_name = 'memory_block_read_cost';
FLUSH OPTIMIZER_COSTS;

SET PERSIST innodb_stats_persistent = 1;
SET PERSIST innodb_stats_auto_recalc = 0;

SET GLOBAL optimizer_switch='hypergraph_optimizer=on';
eof"

modes=("2" "3")
histogram_added=false
index_added=false

for mode in "${modes[@]}"; do
  if [ "$mode" = "2" ];
  then
    echo -e "With indexes"
    output_folder="${OUTDIR}indexes/"
    histogram=false
    index=true
  else
    echo -e "Both histogram and indexes"
    output_folder="${OUTDIR}histograms_and_indexes/"
    histogram=true
    index=true
  fi

  if [ ! -e $output_folder ]; then
    mkdir -p $output_folder
  fi

  for file in `ls queries/*.sql`; do
    bname=`basename $file`
    name=${bname%.*}
    outputjson=$output_folder/$name.json
    echo -e "${BIWhite}+-------------+${NC}"
    echo -e "${BIWhite}| Run $name.sql |${NC}"
    echo -e "${BIWhite}+-------------+${NC}"

    original_query=$(<$file)
    query=${original_query/";"/"\G"}
    query=${query/"SELECT "/"SELECT /*+ SET_VAR(sql_buffer_result=1) */ "}
    if [ $histogram == true ] && [ $histogram_added == false ]
    then
        histogram_added=true
        eval "$mysql_connect<<eof
ANALYZE TABLE imdbload.aka_name UPDATE HISTOGRAM ON person_id, name, imdb_index, name_pcode_cf, name_pcode_nf, surname_pcode, md5sum WITH 32 BUCKETS;
ANALYZE TABLE imdbload.aka_title UPDATE HISTOGRAM ON movie_id, title, imdb_index, kind_id, production_year, phonetic_code, episode_of_id, season_nr, episode_nr, note, md5sum WITH 32 BUCKETS;
ANALYZE TABLE imdbload.cast_info UPDATE HISTOGRAM ON person_id, movie_id, person_role_id, note, nr_order, role_id WITH 32 BUCKETS;
ANALYZE TABLE imdbload.char_name UPDATE HISTOGRAM ON name, imdb_index, imdb_id, name_pcode_nf, surname_pcode, md5sum WITH 32 BUCKETS;
ANALYZE TABLE imdbload.comp_cast_type UPDATE HISTOGRAM ON kind WITH 32 BUCKETS;
ANALYZE TABLE imdbload.company_name UPDATE HISTOGRAM ON name, country_code, imdb_id, name_pcode_nf, name_pcode_sf, md5sum WITH 32 BUCKETS;
ANALYZE TABLE imdbload.company_type UPDATE HISTOGRAM ON kind WITH 32 BUCKETS;
ANALYZE TABLE imdbload.complete_cast UPDATE HISTOGRAM ON movie_id, subject_id, status_id WITH 32 BUCKETS;
ANALYZE TABLE imdbload.info_type UPDATE HISTOGRAM ON info WITH 32 BUCKETS;
ANALYZE TABLE imdbload.keyword UPDATE HISTOGRAM ON keyword, phonetic_code WITH 32 BUCKETS;
ANALYZE TABLE imdbload.kind_type UPDATE HISTOGRAM ON kind WITH 32 BUCKETS;
ANALYZE TABLE imdbload.link_type UPDATE HISTOGRAM ON link WITH 32 BUCKETS;
ANALYZE TABLE imdbload.movie_companies UPDATE HISTOGRAM ON movie_id, company_id, company_type_id, note WITH 32 BUCKETS;
ANALYZE TABLE imdbload.movie_info_idx UPDATE HISTOGRAM ON movie_id, info_type_id, info, note WITH 32 BUCKETS;
ANALYZE TABLE imdbload.movie_keyword UPDATE HISTOGRAM ON movie_id, keyword_id WITH 32 BUCKETS;
ANALYZE TABLE imdbload.movie_link UPDATE HISTOGRAM ON movie_id, linked_movie_id, link_type_id WITH 32 BUCKETS;
ANALYZE TABLE imdbload.name UPDATE HISTOGRAM ON name, imdb_index, imdb_id, gender, name_pcode_cf, name_pcode_nf, surname_pcode, md5sum WITH 32 BUCKETS;
ANALYZE TABLE imdbload.role_type UPDATE HISTOGRAM ON role WITH 32 BUCKETS;
ANALYZE TABLE imdbload.title UPDATE HISTOGRAM ON title, imdb_index, kind_id, production_year, imdb_id, phonetic_code, episode_of_id, season_nr, episode_nr, series_years, md5sum WITH 32 BUCKETS;
ANALYZE TABLE imdbload.movie_info UPDATE HISTOGRAM ON movie_id, info_type_id, info, note WITH 32 BUCKETS;
ANALYZE TABLE imdbload.person_info UPDATE HISTOGRAM ON person_id, info_type_id, info, note WITH 32 BUCKETS;
eof"
    elif [ $histogram == false ] && [ $histogram_added == true ]
    then
        histogram_added=false
        eval "$mysql_connect<<eof
ANALYZE TABLE imdbload.aka_name DROP HISTOGRAM ON person_id, name, imdb_index, name_pcode_cf, name_pcode_nf, surname_pcode, md5sum;
ANALYZE TABLE imdbload.aka_title DROP HISTOGRAM ON movie_id, title, imdb_index, kind_id, production_year, phonetic_code, episode_of_id, season_nr, episode_nr, note, md5sum;
ANALYZE TABLE imdbload.cast_info DROP HISTOGRAM ON person_id, movie_id, person_role_id, note, nr_order, role_id;
ANALYZE TABLE imdbload.char_name DROP HISTOGRAM ON name, imdb_index, imdb_id, name_pcode_nf, surname_pcode, md5sum;
ANALYZE TABLE imdbload.comp_cast_type DROP HISTOGRAM ON kind;
ANALYZE TABLE imdbload.company_name DROP HISTOGRAM ON name, country_code, imdb_id, name_pcode_nf, name_pcode_sf, md5sum;
ANALYZE TABLE imdbload.company_type DROP HISTOGRAM ON kind;
ANALYZE TABLE imdbload.complete_cast DROP HISTOGRAM ON movie_id, subject_id, status_id;
ANALYZE TABLE imdbload.info_type DROP HISTOGRAM ON info;
ANALYZE TABLE imdbload.keyword DROP HISTOGRAM ON keyword, phonetic_code;
ANALYZE TABLE imdbload.kind_type DROP HISTOGRAM ON kind;
ANALYZE TABLE imdbload.link_type DROP HISTOGRAM ON link;
ANALYZE TABLE imdbload.movie_companies DROP HISTOGRAM ON movie_id, company_id, company_type_id, note;
ANALYZE TABLE imdbload.movie_info_idx DROP HISTOGRAM ON movie_id, info_type_id, info, note;
ANALYZE TABLE imdbload.movie_keyword DROP HISTOGRAM ON movie_id, keyword_id;
ANALYZE TABLE imdbload.movie_link DROP HISTOGRAM ON movie_id, linked_movie_id, link_type_id;
ANALYZE TABLE imdbload.name DROP HISTOGRAM ON name, imdb_index, imdb_id, gender, name_pcode_cf, name_pcode_nf, surname_pcode, md5sum;
ANALYZE TABLE imdbload.role_type DROP HISTOGRAM ON role;
ANALYZE TABLE imdbload.title DROP HISTOGRAM ON title, imdb_index, kind_id, production_year, imdb_id, phonetic_code, episode_of_id, season_nr, episode_nr, series_years, md5sum;
ANALYZE TABLE imdbload.movie_info DROP HISTOGRAM ON movie_id, info_type_id, info, note;
ANALYZE TABLE imdbload.person_info DROP HISTOGRAM ON person_id, info_type_id, info, note;
eof"
    fi

    if [ $index == true ] && [ $index_added == false ]
    then 
        index_added=true
    fi

    if [ -s "$outputjson" ]
    then
      echo "Results for $name already collected, skipping..."
      continue
    fi

    hyperfine \
      --warmup 2 \
      -r 10 \
      --export-json $outputjson \
      -n "job" "$mysql_connect -e \"$query\""
  done
done