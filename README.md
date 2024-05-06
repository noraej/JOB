#### 1. Obtain data
    
```shell
    cd csv_files/
    wget http://homepages.cwi.nl/~boncz/job/imdb.tgz
    tar -xvzf imdb.tgz
```

#### 2. Launch the database server
First time: 
 ```shell
    ./mtr --mem --start   
 ```

 Dirty start:
  ```shell
    ./mtr --mem --start-dirty
 ```

 ### 3. Connect to the database server

 ```shell
~/mysql-server-join-hint/build/bin/mysql --local-infile=1 -u root -S /var/folders/k0/qhfn3fhn0wd8t_kc0ksszklh0000gp/T/s4wGH1Wb5i/mysqld.1.sock
 ```

 

 ### 4. Create IMDB tables in MySQL
 ```sqlmysql
SOURCE JOB/join-order-benchmark/csv_files/imdb-create-tables.sql;
```

### 5. Load the data in MySQL 

Do this one by one to allow recovery to happen if anything goes wrong. 

```sqlmysql
SOURCE JOB/join-order-benchmark/csv_files/imdb-load-data-1.sql;
```
Back up folder from `(../../mysql-server-join-hint/build/mysql-test/var/data)`

```sqlmysql
SOURCE JOB/join-order-benchmark/csv_files/imdb-load-data-2.sql;
```
Back up folder from `(../../mysql-server-join-hint/build/mysql-test/var/data)`
```sqlmysql
SOURCE JOB/join-order-benchmark/csv_files/imdb-load-data-3.sql;
```
Back up folder from `(../../mysql-server-join-hint/build/mysql-test/var/data)`
```sqlmysql
SOURCE JOB/join-order-benchmark/csv_files/imdb-load-data-4.sql;
```
Back up folder from `(../../mysql-server-join-hint/build/mysql-test/var/data)`
```sqlmysql
SOURCE JOB/join-order-benchmark/csv_files/imdb-load-data-5.sql;
```
Back up folder from `(../../mysql-server-join-hint/build/mysql-test/var/data)`
### 6. Add idexes to the imdb databse
```sqlmysql
SOURCE JOB/join-order-benchmark/csv_files/imdb-index-tables.sql
```

### 7. Running the queries
We use hyperfine as a benchmarking-tool to measure the queries, you'll therefore need to install it before running the queries. To run all queries for the force join method, run the following in your terminal:
```sqlmysql
$ ./run_queries.sh
```
This will run the queries in the queries-folder one-by-one, both with and without re-optimization, and output the results into the results-folder as both markdown and json-files for each query. You'll be able to see the progress in the terminal as the queries are being executed.


To run queries for the robust query optimization implementation, run the following in your terminal: 

```sqlmysql
$ ./run_queries_indexed.sh
```
This runs the expiriments on our implementation and outputs the results into the results-folder as both markdown and json-files for each query. You'll be able to see the progress in the terminal as the queries are being executed.


### 8. Order Problem
Please note that `queries/17b.sql` and `queries/8d.sql` may exhibit order issues due to the use of different order rules from MySQL. This is not a real bug.

### 9. Collect results

Run 

```shell
/usr/local/bin/python3 JOB/join-order-benchmark/gatherResults.py 
```