SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE '/Users/nora/Documents/Master/Code/Helper/JOB/join-order-benchmark/csv_files/movie_info.csv' INTO TABLE movie_info FIELDS TERMINATED BY ',';
