/Users/nora/Documents/Master/Code/Helper/JOB/join-order-benchmark/csv_files/SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE '/Users/nora/Documents/Master/Code/Helper/JOB/join-order-benchmark/csv_files/movie_keyword.csv' INTO TABLE movie_keyword FIELDS TERMINATED BY ',';

LOAD DATA LOCAL INFILE '/Users/nora/Documents/Master/Code/Helper/JOB/join-order-benchmark/csv_files/movie_link.csv' INTO TABLE movie_link FIELDS TERMINATED BY ',';

LOAD DATA LOCAL INFILE '/Users/nora/Documents/Master/Code/Helper/JOB/join-order-benchmark/csv_files/name.csv' INTO TABLE name FIELDS TERMINATED BY ',';
