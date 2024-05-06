##  1a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.23 | 0.64 | 0.03 | 0.03 | 2.04 | 1.0
| Nested loop join | 0.24 | 0.65 | 0.03 | 0.03 | 2.1 | 1.026
| Hash join | 3.05 | 0.02 | 3.04 | 3.03 | 3.11 | 13.161
##  1b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0
| Nested loop join | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.019
| Hash join | 2.55 | 0.02 | 2.55 | 2.53 | 2.58 | 640.958
##  1c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.85 | 0.87 | 0.84 | 0.03 | 1.72 | 1.035
| Nested loop join | 0.82 | 0.84 | 0.82 | 0.01 | 1.68 | 1.0
| Hash join | 2.47 | 0.02 | 2.47 | 2.44 | 2.52 | 3.002
##  1d

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0
| Nested loop join | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.089
| Hash join | 2.57 | 0.01 | 2.57 | 2.55 | 2.58 | 695.719
##  2a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.09 | 0.07 | 1.08 | 1.01 | 1.23 | 1.0
| Nested loop join | 9.9 | 0.4 | 9.87 | 9.47 | 10.78 | 9.047
| Hash join | 2.75 | 0.27 | 2.94 | 2.44 | 2.98 | 2.513
##  2b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.55 | 0.01 | 0.55 | 0.54 | 0.58 | 1.0
| Nested loop join | 9.25 | 0.53 | 9.34 | 8.65 | 10.39 | 16.819
| Hash join | 2.44 | 0.26 | 2.25 | 2.23 | 2.76 | 4.428
##  2c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.22 | 0.01 | 0.22 | 0.22 | 0.24 | 3.299
| Nested loop join | 0.07 | 0.0 | 0.07 | 0.07 | 0.07 | 1.0
| Hash join | 1.33 | 0.01 | 1.33 | 1.31 | 1.35 | 19.549
##  2d

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 8.99 | 0.33 | 9.04 | 8.45 | 9.43 | 2.529
| Nested loop join | 65.29 | 2.61 | 65.02 | 61.82 | 71.01 | 18.362
| Hash join | 3.56 | 0.65 | 3.18 | 3.12 | 4.53 | 1.0
##  3a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.8 | 0.24 | 1.91 | 1.32 | 1.95 | 3.571
| Nested loop join | 0.51 | 0.02 | 0.5 | 0.48 | 0.54 | 1.0
| Hash join | 9.62 | 0.04 | 9.62 | 9.55 | 9.68 | 19.039
##  3b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.12 | 0.26 | 1.0 | 0.97 | 1.62 | 4.434
| Nested loop join | 0.25 | 0.01 | 0.25 | 0.24 | 0.27 | 1.0
| Hash join | 8.74 | 0.1 | 8.73 | 8.63 | 8.91 | 34.602
##  3c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 2.39 | 0.28 | 2.39 | 2.09 | 2.68 | 2.119
| Nested loop join | 1.13 | 0.06 | 1.13 | 1.03 | 1.24 | 1.0
| Hash join | 10.04 | 0.07 | 10.04 | 9.92 | 10.16 | 8.921
## ❗ 4a

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 4.36 | 0.26 | 4.32 | 4.02 | 4.74 | 1.104
| Nested loop join | 4.77 | 0.13 | 4.8 | 4.55 | 4.93 | 1.208
| Hash join | 3.95 | 0.03 | 3.95 | 3.91 | 3.99 | 1.0
## ❗ 4b

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 3.15 | 0.31 | 3.16 | 2.52 | 3.64 | 1.449
| Nested loop join | 3.07 | 0.28 | 3.12 | 2.53 | 3.41 | 1.412
| Hash join | 2.18 | 0.01 | 2.17 | 2.15 | 2.19 | 1.0
## ❗ 4c

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 7.86 | 0.88 | 7.5 | 6.89 | 9.19 | 1.286
| Nested loop join | 8.68 | 0.11 | 8.68 | 8.49 | 8.94 | 1.421
| Hash join | 6.11 | 0.06 | 6.14 | 6.01 | 6.17 | 1.0
##  5a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.79 | 0.02 | 1.79 | 1.76 | 1.82 | 1.0
| Nested loop join | 1.81 | 0.02 | 1.81 | 1.79 | 1.85 | 1.015
| Hash join | 11.79 | 0.12 | 11.8 | 11.6 | 11.93 | 6.595
##  5b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.76 | 0.02 | 1.77 | 1.73 | 1.79 | 1.0
| Nested loop join | 1.77 | 0.02 | 1.77 | 1.74 | 1.79 | 1.005
| Hash join | 3.4 | 0.03 | 3.4 | 3.37 | 3.46 | 1.93
##  5c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.88 | 0.02 | 1.88 | 1.86 | 1.9 | 1.0
| Nested loop join | 1.89 | 0.02 | 1.88 | 1.87 | 1.92 | 1.004
| Hash join | 11.81 | 0.07 | 11.79 | 11.73 | 11.93 | 6.287
## ❗ 6a

Nested loop was not chosen, but it was faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.04 | 0.02 | 1.04 | 1.01 | 1.06 | 18.679
| Nested loop join | 0.06 | 0.0 | 0.06 | 0.05 | 0.06 | 1.0
| Hash join | 1.04 | 0.02 | 1.04 | 1.01 | 1.06 | 18.558
## ❗ 6b

Nested loop was not chosen, but it was faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.87 | 0.68 | 1.88 | 1.2 | 2.53 | 1.526
| Nested loop join | 1.22 | 0.02 | 1.22 | 1.2 | 1.25 | 1.0
| Hash join | 2.49 | 0.02 | 2.48 | 2.46 | 2.52 | 2.031
## ❗ 6c

Nested loop was not chosen, but it was faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.01 | 0.01 | 1.0 | 1.0 | 1.02 | 28.16
| Nested loop join | 0.04 | 0.0 | 0.04 | 0.03 | 0.04 | 1.0
| Hash join | 1.01 | 0.02 | 1.0 | 1.0 | 1.04 | 28.276
## ❗ 6d

Nested loop was not chosen, but it was faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 2.89 | 1.16 | 3.59 | 1.21 | 3.65 | 2.395
| Nested loop join | 1.21 | 0.01 | 1.2 | 1.2 | 1.22 | 1.0
| Hash join | 3.6 | 0.03 | 3.59 | 3.58 | 3.66 | 2.98
## ❗ 6e

Nested loop was not chosen, but it was faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.02 | 0.01 | 1.02 | 1.01 | 1.05 | 18.047
| Nested loop join | 0.06 | 0.0 | 0.06 | 0.05 | 0.06 | 1.0
| Hash join | 1.01 | 0.01 | 1.01 | 1.0 | 1.03 | 17.842
##  6f

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 15.62 | 0.14 | 15.59 | 15.44 | 15.82 | 1.0
| Nested loop join | 18.85 | 0.29 | 18.87 | 18.52 | 19.42 | 1.207
| Hash join | 15.68 | 0.09 | 15.67 | 15.56 | 15.85 | 1.004
## ❗ 7a

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 3.51 | 1.69 | 2.24 | 2.1 | 5.5 | 1.244
| Nested loop join | 3.45 | 1.72 | 2.17 | 2.06 | 5.51 | 1.225
| Hash join | 2.82 | 0.02 | 2.82 | 2.79 | 2.85 | 1.0
##  7b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.93 | 0.38 | 0.75 | 0.72 | 1.65 | 1.0
| Nested loop join | 1.18 | 0.49 | 1.19 | 0.69 | 1.67 | 1.272
| Hash join | 2.7 | 0.02 | 2.7 | 2.68 | 2.75 | 2.905
## ❗ 7c

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 20.92 | 0.16 | 20.91 | 20.69 | 21.22 | 2.012
| Nested loop join | 20.61 | 0.2 | 20.59 | 20.29 | 20.86 | 1.982
| Hash join | 10.4 | 0.14 | 10.38 | 10.23 | 10.74 | 1.0
##  8a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 11.81 | 0.45 | 11.75 | 11.17 | 12.65 | 1.009
| Nested loop join | 11.71 | 0.42 | 11.72 | 11.06 | 12.47 | 1.0
| Hash join | 25.4 | 0.22 | 25.47 | 24.95 | 25.71 | 2.169
##  8b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.73 | 0.04 | 0.73 | 0.67 | 0.81 | 1.0
| Nested loop join | 0.76 | 0.07 | 0.77 | 0.66 | 0.85 | 1.039
| Hash join | 24.52 | 0.35 | 24.43 | 23.99 | 25.18 | 33.669
##  8c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 43.91 | 78.07 | 19.31 | 18.48 | 266.09 | 2.041
| Nested loop join | 272.81 | 4.53 | 274.5 | 264.46 | 277.76 | 12.68
| Hash join | 21.51 | 3.79 | 23.88 | 17.07 | 25.17 | 1.0
##  8d

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 78.6 | 112.73 | 10.0 | 6.87 | 247.36 | 5.63
| Nested loop join | 246.44 | 2.01 | 246.69 | 242.58 | 249.31 | 17.652
| Hash join | 13.96 | 3.51 | 11.83 | 11.61 | 19.11 | 1.0
## ❗ 9a

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 38.76 | 2.0 | 37.98 | 36.27 | 41.74 | 1.39
| Nested loop join | 40.12 | 1.67 | 39.21 | 38.62 | 42.73 | 1.438
| Hash join | 27.89 | 0.17 | 27.84 | 27.7 | 28.24 | 1.0
##  9b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 15.17 | 0.39 | 15.09 | 14.76 | 15.81 | 1.0
| Nested loop join | 15.23 | 0.42 | 15.34 | 14.71 | 15.76 | 1.004
| Hash join | 24.15 | 0.21 | 24.05 | 23.92 | 24.46 | 1.591
##  9c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.21 | 0.01 | 1.21 | 1.2 | 1.23 | 1.002
| Nested loop join | 1.21 | 0.01 | 1.21 | 1.2 | 1.24 | 1.0
| Hash join | 25.69 | 0.92 | 25.29 | 24.99 | 27.4 | 21.185
##  9d

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.79 | 0.04 | 1.78 | 1.75 | 1.84 | 1.087
| Nested loop join | 1.65 | 0.02 | 1.65 | 1.63 | 1.67 | 1.0
| Hash join | 27.29 | 0.29 | 27.13 | 26.98 | 27.78 | 16.529

##  10a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.58 | 0.05 | 1.56 | 1.52 | 1.68 | 1.012
| Nested loop join | 1.56 | 0.03 | 1.55 | 1.51 | 1.63 | 1.0
| Hash join | 23.4 | 0.17 | 23.45 | 23.04 | 23.6 | 14.972
##  10b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.51 | 0.03 | 0.49 | 0.47 | 0.55 | 1.0
| Nested loop join | 0.55 | 0.02 | 0.55 | 0.53 | 0.59 | 1.094
| Hash join | 22.9 | 0.32 | 22.73 | 22.54 | 23.51 | 45.332
## ❗ 10c

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 166.66 | 1.58 | 166.62 | 164.5 | 168.7 | 6.515
| Nested loop join | 165.88 | 0.97 | 165.78 | 164.35 | 167.68 | 6.485
| Hash join | 25.58 | 0.16 | 25.64 | 25.32 | 25.77 | 1.0
##  11a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.02 | 0.0 | 0.02 | 0.02 | 0.03 | 1.0
| Nested loop join | 0.02 | 0.0 | 0.02 | 0.02 | 0.03 | 1.058
| Hash join | 1.36 | 0.09 | 1.4 | 1.18 | 1.4 | 58.275
##  11b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.01 | 0.0 | 0.01 | 0.01 | 0.01 | 1.0
| Nested loop join | 0.01 | 0.0 | 0.01 | 0.01 | 0.01 | 1.021
| Hash join | 1.33 | 0.03 | 1.32 | 1.31 | 1.43 | 170.598
##  11c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.58 | 0.03 | 1.58 | 1.55 | 1.63 | 1.0
| Nested loop join | 1.62 | 0.02 | 1.63 | 1.59 | 1.65 | 1.025
| Hash join | 4.34 | 0.06 | 4.33 | 4.2 | 4.43 | 2.737
##  11d

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.16 | 1.67 | 0.63 | 0.62 | 5.91 | 1.0
| Nested loop join | 2.76 | 2.76 | 0.63 | 0.62 | 6.01 | 2.378
| Hash join | 4.63 | 0.33 | 4.76 | 3.76 | 4.82 | 3.99
##  12a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.51 | 0.07 | 1.48 | 1.41 | 1.62 | 1.003
| Nested loop join | 1.5 | 0.1 | 1.52 | 1.3 | 1.64 | 1.0
| Hash join | 11.14 | 0.07 | 11.16 | 11.03 | 11.24 | 7.422
##  12b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.01 | 0.0 | 0.01 | 0.01 | 0.01 | 1.0
| Nested loop join | 0.01 | 0.0 | 0.01 | 0.01 | 0.01 | 1.023
| Hash join | 9.81 | 0.07 | 9.8 | 9.7 | 9.94 | 1502.25
##  12c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 4.5 | 0.28 | 4.4 | 4.24 | 5.01 | 1.0
| Nested loop join | 4.65 | 0.3 | 4.54 | 4.27 | 5.03 | 1.034
| Hash join | 14.58 | 0.13 | 14.54 | 14.42 | 14.83 | 3.242
##  13a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 6.98 | 0.72 | 6.81 | 6.24 | 8.33 | 1.013
| Nested loop join | 6.89 | 0.65 | 6.74 | 6.11 | 8.01 | 1.0
| Hash join | 22.38 | 6.47 | 23.18 | 15.14 | 32.63 | 3.249
##  13b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 2.99 | 0.16 | 2.95 | 2.8 | 3.37 | 1.0
| Nested loop join | 3.08 | 0.48 | 2.89 | 2.76 | 4.22 | 1.029
| Hash join | 5.49 | 0.05 | 5.47 | 5.45 | 5.57 | 1.834
## ❗ 13c

Nested loop was not chosen, but it was faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 3.37 | 0.32 | 3.32 | 2.96 | 3.95 | 1.006
| Nested loop join | 3.35 | 0.42 | 3.19 | 2.86 | 4.14 | 1.0
| Hash join | 5.02 | 0.07 | 4.98 | 4.95 | 5.12 | 1.496
##  13d

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 16.48 | 0.47 | 16.53 | 15.93 | 17.08 | 1.019
| Nested loop join | 16.17 | 0.74 | 16.32 | 15.13 | 17.24 | 1.0
| Hash join | 48.35 | 7.0 | 44.03 | 41.91 | 56.88 | 2.99
##  14a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 4.25 | 0.43 | 4.21 | 3.66 | 4.89 | 1.164
| Nested loop join | 3.65 | 0.24 | 3.65 | 3.12 | 4.02 | 1.0
| Hash join | 12.4 | 0.13 | 12.43 | 12.21 | 12.61 | 3.394
##  14b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 3.23 | 0.37 | 3.21 | 2.68 | 3.86 | 1.007
| Nested loop join | 3.21 | 0.41 | 3.32 | 2.45 | 3.64 | 1.0
| Hash join | 11.61 | 0.04 | 11.59 | 11.57 | 11.68 | 3.62
## ❗ 14c

Nested loop was not chosen, but it was faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 10.04 | 0.41 | 9.98 | 9.41 | 10.73 | 1.147
| Nested loop join | 8.76 | 2.12 | 9.9 | 5.64 | 10.59 | 1.0
| Hash join | 14.16 | 0.1 | 14.12 | 14.04 | 14.37 | 1.616
##  15a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 8.3 | 3.06 | 9.33 | 2.74 | 10.75 | 1.0
| Nested loop join | 8.99 | 0.69 | 8.83 | 8.17 | 10.34 | 1.084
| Hash join | 12.76 | 1.79 | 12.76 | 11.07 | 16.27 | 1.538
##  15b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.1 | 0.0 | 0.1 | 0.09 | 0.1 | 1.0
| Nested loop join | 0.1 | 0.01 | 0.1 | 0.09 | 0.11 | 1.038
| Hash join | 10.93 | 0.08 | 10.9 | 10.85 | 11.1 | 113.423
## ❗ 15c

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 48.38 | 0.32 | 48.37 | 47.92 | 48.95 | 4.33
| Nested loop join | 84.01 | 7.84 | 82.84 | 70.48 | 96.45 | 7.52
| Hash join | 11.17 | 0.06 | 11.17 | 11.08 | 11.28 | 1.0
## ❗ 15d

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 48.4 | 0.35 | 48.43 | 47.59 | 48.81 | 2.085
| Nested loop join | 87.12 | 7.63 | 87.67 | 75.45 | 99.46 | 3.752
| Hash join | 23.22 | 0.23 | 23.11 | 23.01 | 23.68 | 1.0
## ❗ 16a

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 10.9 | 0.31 | 10.82 | 10.56 | 11.36 | 1.153
| Nested loop join | 10.77 | 0.3 | 10.79 | 10.31 | 11.19 | 1.139
| Hash join | 9.46 | 0.08 | 9.46 | 9.36 | 9.61 | 1.0
##  16b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 30.1 | 10.82 | 28.27 | 23.83 | 60.37 | 1.406
| Nested loop join | 109.0 | 2.9 | 107.53 | 106.6 | 115.21 | 5.092
| Hash join | 21.41 | 0.49 | 21.18 | 20.98 | 22.32 | 1.0
## ❗ 16c

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 66.08 | 1.67 | 66.23 | 63.83 | 68.64 | 3.087
| Nested loop join | 116.1 | 3.62 | 115.21 | 112.19 | 123.27 | 5.424
| Hash join | 21.4 | 0.15 | 21.41 | 21.13 | 21.71 | 1.0
## ❗ 16d

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 14.45 | 0.21 | 14.41 | 14.24 | 14.95 | 1.035
| Nested loop join | 15.12 | 0.32 | 15.13 | 14.57 | 15.66 | 1.083
| Hash join | 13.96 | 0.06 | 13.96 | 13.86 | 14.06 | 1.0
##  17a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 27.11 | 11.34 | 24.41 | 20.24 | 59.06 | 1.884
| Nested loop join | 88.5 | 1.82 | 88.28 | 85.99 | 90.93 | 6.149
| Hash join | 14.39 | 0.6 | 14.06 | 13.82 | 15.41 | 1.0
##  17b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 8.59 | 2.18 | 9.24 | 2.39 | 9.43 | 1.0
| Nested loop join | 59.93 | 16.06 | 64.93 | 14.24 | 65.96 | 6.981
| Hash join | 9.79 | 0.05 | 9.78 | 9.73 | 9.86 | 1.141
##  17c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 6.54 | 3.63 | 9.28 | 2.3 | 9.5 | 1.0
| Nested loop join | 65.03 | 0.3 | 65.08 | 64.43 | 65.41 | 9.945
| Hash join | 9.82 | 0.1 | 9.77 | 9.75 | 10.02 | 1.501
##  17d

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 11.37 | 2.98 | 12.24 | 2.9 | 12.61 | 1.0
| Nested loop join | 60.77 | 16.21 | 65.61 | 14.72 | 68.52 | 5.346
| Hash join | 12.89 | 0.13 | 12.86 | 12.76 | 13.18 | 1.134
##  17e

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 28.74 | 5.69 | 27.82 | 23.95 | 44.33 | 1.858
| Nested loop join | 88.15 | 1.46 | 87.79 | 86.62 | 91.66 | 5.698
| Hash join | 15.47 | 0.57 | 15.14 | 15.06 | 16.32 | 1.0
##  17f

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 15.58 | 4.0 | 13.73 | 13.59 | 24.21 | 1.091
| Nested loop join | 65.83 | 0.41 | 65.8 | 65.23 | 66.52 | 4.609
| Hash join | 14.28 | 0.15 | 14.27 | 14.06 | 14.54 | 1.0
##  18a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.09 | 0.01 | 1.09 | 1.08 | 1.11 | 1.0
| Nested loop join | 1.1 | 0.0 | 1.1 | 1.09 | 1.1 | 1.001
| Hash join | 18.79 | 0.12 | 18.77 | 18.65 | 19.04 | 17.165
##  18b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.38 | 0.11 | 1.38 | 1.23 | 1.59 | 1.001
| Nested loop join | 1.38 | 0.04 | 1.39 | 1.3 | 1.46 | 1.0
| Hash join | 8.36 | 0.45 | 8.19 | 7.6 | 8.94 | 6.05
## ❗ 18c

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 44.76 | 1.16 | 44.93 | 42.52 | 46.67 | 1.488
| Nested loop join | 43.91 | 0.9 | 43.46 | 42.97 | 45.61 | 1.459
| Hash join | 30.09 | 0.21 | 30.01 | 29.94 | 30.66 | 1.0
## ❗ 19a

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 40.95 | 1.8 | 40.4 | 38.92 | 44.25 | 1.351
| Nested loop join | 42.02 | 1.97 | 41.7 | 40.15 | 46.12 | 1.386
| Hash join | 30.31 | 1.32 | 30.18 | 27.67 | 32.37 | 1.0
##  19b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 7.84 | 2.04 | 8.75 | 2.33 | 9.01 | 1.0
| Nested loop join | 8.71 | 0.32 | 8.62 | 8.26 | 9.14 | 1.11
| Hash join | 24.34 | 0.27 | 24.35 | 24.02 | 24.8 | 3.105
##  19c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.22 | 0.02 | 1.22 | 1.17 | 1.24 | 1.018
| Nested loop join | 1.19 | 0.01 | 1.19 | 1.18 | 1.22 | 1.0
| Hash join | 30.51 | 0.24 | 30.53 | 30.16 | 31.04 | 25.56
##  19d

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.76 | 0.03 | 1.76 | 1.71 | 1.81 | 1.04
| Nested loop join | 1.69 | 0.02 | 1.69 | 1.67 | 1.75 | 1.0
| Hash join | 27.74 | 0.39 | 27.68 | 27.39 | 28.77 | 16.4
##  20a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 8.34 | 0.12 | 8.28 | 8.23 | 8.56 | 1.0
| Nested loop join | 8.34 | 0.09 | 8.33 | 8.21 | 8.47 | 1.0
| Hash join | 29.57 | 0.04 | 29.57 | 29.52 | 29.64 | 3.547
## ❗ 20b

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 4.06 | 0.07 | 4.05 | 3.97 | 4.19 | 3.521
| Nested loop join | 4.2 | 0.05 | 4.18 | 4.16 | 4.31 | 3.636
| Hash join | 1.15 | 0.06 | 1.16 | 0.98 | 1.21 | 1.0
##  20c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 2.98 | 0.03 | 2.97 | 2.94 | 3.05 | 1.01
| Nested loop join | 2.94 | 0.02 | 2.94 | 2.92 | 2.97 | 1.0
| Hash join | 16.43 | 0.09 | 16.41 | 16.31 | 16.57 | 5.578
##  21a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.03 | 0.0 | 0.03 | 0.02 | 0.03 | 1.029
| Nested loop join | 0.03 | 0.0 | 0.03 | 0.02 | 0.03 | 1.0
| Hash join | 2.15 | 0.05 | 2.14 | 2.08 | 2.23 | 81.573
##  21b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.03 | 0.0 | 0.03 | 0.02 | 0.03 | 1.027
| Nested loop join | 0.02 | 0.0 | 0.03 | 0.02 | 0.03 | 1.0
| Hash join | 2.13 | 0.08 | 2.13 | 2.05 | 2.29 | 86.606
##  21c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.03 | 0.0 | 0.03 | 0.03 | 0.03 | 1.092
| Nested loop join | 0.03 | 0.0 | 0.03 | 0.03 | 0.03 | 1.0
| Hash join | 2.12 | 0.04 | 2.11 | 2.08 | 2.2 | 76.189
##  22a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 4.43 | 0.75 | 4.08 | 3.9 | 6.03 | 1.0
| Nested loop join | 4.59 | 0.87 | 4.04 | 3.7 | 5.84 | 1.035
| Hash join | 15.59 | 1.67 | 14.56 | 13.89 | 17.56 | 3.517
##  22b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 3.44 | 1.23 | 3.45 | 2.19 | 4.78 | 1.0
| Nested loop join | 3.52 | 1.12 | 4.18 | 2.13 | 4.54 | 1.023
| Hash join | 14.34 | 2.16 | 13.15 | 12.73 | 17.54 | 4.171
##  22c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 16.84 | 1.3 | 17.0 | 14.85 | 19.16 | 1.0
| Nested loop join | 16.98 | 1.32 | 16.87 | 15.01 | 18.93 | 1.008
| Hash join | 23.28 | 1.43 | 24.0 | 21.15 | 24.52 | 1.382
## ❗ 22d

Nested loop was not chosen, but it was faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 10.13 | 0.37 | 10.06 | 9.65 | 10.73 | 1.28
| Nested loop join | 7.91 | 2.21 | 7.81 | 5.78 | 10.49 | 1.0
| Hash join | 13.96 | 0.18 | 14.07 | 13.64 | 14.13 | 1.764
##  23a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 2.89 | 0.05 | 2.89 | 2.83 | 2.96 | 1.004
| Nested loop join | 2.88 | 0.05 | 2.89 | 2.83 | 2.94 | 1.0
| Hash join | 10.85 | 0.88 | 10.87 | 9.35 | 11.66 | 3.763
##  23b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 2.92 | 0.03 | 2.93 | 2.88 | 2.97 | 1.0
| Nested loop join | 2.93 | 0.04 | 2.92 | 2.86 | 2.98 | 1.001
| Hash join | 9.65 | 0.46 | 9.51 | 9.39 | 10.95 | 3.301
##  23c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 8.21 | 0.17 | 8.27 | 7.92 | 8.35 | 1.0
| Nested loop join | 8.24 | 0.07 | 8.24 | 8.1 | 8.36 | 1.004
| Hash join | 19.97 | 1.05 | 19.48 | 19.39 | 21.96 | 2.433
##  24a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.24 | 0.02 | 1.24 | 1.22 | 1.29 | 1.03
| Nested loop join | 1.21 | 0.03 | 1.21 | 1.18 | 1.24 | 1.0
| Hash join | 26.03 | 1.13 | 25.61 | 25.21 | 28.15 | 21.535
##  24b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.13 | 0.0 | 0.13 | 0.12 | 0.13 | 1.32
| Nested loop join | 0.1 | 0.0 | 0.1 | 0.09 | 0.1 | 1.0
| Hash join | 26.6 | 2.25 | 26.79 | 24.17 | 28.9 | 276.63
## ❗ 25a

Nested loop was not chosen, but it was faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 29.95 | 1.89 | 30.57 | 26.23 | 31.79 | 1.026
| Nested loop join | 29.19 | 2.04 | 29.22 | 25.98 | 31.83 | 1.0
| Hash join | 31.84 | 0.66 | 31.9 | 30.95 | 32.6 | 1.091
##  25b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 2.44 | 0.1 | 2.45 | 2.29 | 2.6 | 1.003
| Nested loop join | 2.43 | 0.2 | 2.38 | 2.23 | 2.69 | 1.0
| Hash join | 23.37 | 1.3 | 23.87 | 21.93 | 25.75 | 9.604
## ❗ 25c

Hash join was not chosen, but is faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 44.4 | 5.6 | 42.34 | 39.66 | 55.86 | 1.343
| Nested loop join | 43.37 | 1.05 | 43.53 | 42.03 | 45.02 | 1.312
| Hash join | 33.07 | 2.52 | 34.89 | 29.86 | 35.17 | 1.0
##  26a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.36 | 0.29 | 1.24 | 1.17 | 2.0 | 1.074
| Nested loop join | 1.26 | 0.21 | 1.18 | 1.16 | 1.85 | 1.0
| Hash join | 18.25 | 9.55 | 13.82 | 12.15 | 40.66 | 14.471
##  26b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.99 | 0.55 | 0.94 | 0.46 | 1.84 | 2.093
| Nested loop join | 0.47 | 0.01 | 0.47 | 0.46 | 0.49 | 1.0
| Hash join | 12.19 | 0.7 | 12.05 | 11.33 | 13.7 | 25.857
##  26c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 11.25 | 23.83 | 3.7 | 3.07 | 79.03 | 2.904
| Nested loop join | 3.88 | 1.39 | 3.1 | 2.97 | 7.41 | 1.0
| Hash join | 29.9 | 1.44 | 29.63 | 26.79 | 31.68 | 7.716
##  27a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.06 | 0.0 | 0.06 | 0.06 | 0.07 | 1.43
| Nested loop join | 0.04 | 0.01 | 0.04 | 0.04 | 0.05 | 1.0
| Hash join | 2.1 | 0.05 | 2.11 | 1.99 | 2.15 | 48.073
##  27b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.06 | 0.0 | 0.06 | 0.06 | 0.07 | 1.671
| Nested loop join | 0.04 | 0.0 | 0.04 | 0.03 | 0.04 | 1.0
| Hash join | 2.1 | 0.04 | 2.11 | 2.0 | 2.15 | 57.47
##  27c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.08 | 0.03 | 0.06 | 0.06 | 0.16 | 1.747
| Nested loop join | 0.04 | 0.02 | 0.04 | 0.03 | 0.08 | 1.0
| Hash join | 2.05 | 0.27 | 2.12 | 1.29 | 2.19 | 46.881
##  28a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 6.75 | 3.77 | 5.02 | 4.82 | 15.66 | 1.441
| Nested loop join | 4.69 | 0.95 | 4.38 | 3.66 | 6.81 | 1.0
| Hash join | 54.58 | 34.68 | 77.37 | 14.27 | 83.68 | 11.646
## ❗ 28b

Nested loop was not chosen, but it was faster 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 24.58 | 71.04 | 2.05 | 1.74 | 226.77 | 14.253
| Nested loop join | 1.72 | 0.22 | 1.72 | 1.23 | 1.95 | 1.0
| Hash join | 15.37 | 0.13 | 15.35 | 15.24 | 15.65 | 8.912
##  28c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 36.4 | 81.2 | 10.01 | 6.77 | 267.24 | 1.0
| Nested loop join | 86.31 | 127.59 | 6.69 | 5.81 | 274.87 | 2.372
| Hash join | 101.48 | 15.19 | 105.7 | 80.92 | 125.84 | 2.788
##  29a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.25 | 0.48 | 1.03 | 0.97 | 2.38 | 1.739
| Nested loop join | 0.72 | 1.21 | 0.33 | 0.32 | 4.16 | 1.0
| Hash join | 28.43 | 1.84 | 28.34 | 26.75 | 33.22 | 39.593
##  29b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 1.05 | 0.15 | 0.98 | 0.92 | 1.36 | 3.057
| Nested loop join | 0.34 | 0.04 | 0.32 | 0.32 | 0.46 | 1.0
| Hash join | 28.74 | 2.84 | 27.25 | 26.42 | 33.07 | 83.596
##  30a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 2.0 | 0.02 | 2.0 | 1.97 | 2.03 | 1.076
| Nested loop join | 1.86 | 0.44 | 1.82 | 1.26 | 2.57 | 1.0
| Hash join | 28.97 | 3.66 | 29.11 | 24.99 | 32.74 | 15.557
##  30b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.56 | 0.03 | 0.55 | 0.52 | 0.62 | 2.67
| Nested loop join | 0.21 | 0.01 | 0.21 | 0.2 | 0.22 | 1.0
| Hash join | 32.04 | 0.3 | 31.96 | 31.67 | 32.51 | 153.265
##  30c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 10.55 | 0.09 | 10.55 | 10.39 | 10.71 | 1.0
| Nested loop join | 10.8 | 1.26 | 10.7 | 7.66 | 12.09 | 1.024
| Hash join | 28.56 | 0.25 | 28.5 | 28.3 | 29.1 | 2.706
##  31a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 6.27 | 0.68 | 6.48 | 5.23 | 7.16 | 1.0
| Nested loop join | 8.39 | 0.4 | 8.57 | 7.58 | 8.89 | 1.338
| Hash join | 26.59 | 1.21 | 25.99 | 25.55 | 28.68 | 4.241
##  31b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 4.35 | 2.21 | 2.77 | 2.49 | 7.16 | 1.116
| Nested loop join | 3.9 | 1.94 | 2.62 | 2.23 | 6.72 | 1.0
| Hash join | 33.35 | 0.17 | 33.32 | 33.11 | 33.74 | 8.551
##  31c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 6.84 | 0.54 | 6.86 | 6.18 | 7.85 | 1.0
| Nested loop join | 9.24 | 0.33 | 9.29 | 8.6 | 9.66 | 1.351
| Hash join | 34.19 | 0.48 | 34.25 | 33.35 | 34.93 | 4.996
##  32a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.03 | 0.0 | 0.03 | 0.03 | 0.03 | 1.0
| Nested loop join | 0.58 | 0.0 | 0.58 | 0.57 | 0.59 | 21.116
| Hash join | 0.03 | 0.0 | 0.03 | 0.03 | 0.03 | 1.053
##  32b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.42 | 0.0 | 0.42 | 0.41 | 0.42 | 1.0
| Nested loop join | 0.62 | 0.01 | 0.62 | 0.61 | 0.64 | 1.49
| Hash join | 3.06 | 0.02 | 3.06 | 3.03 | 3.1 | 7.343
##  33a

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.07 | 0.01 | 0.07 | 0.06 | 0.08 | 1.719
| Nested loop join | 0.04 | 0.0 | 0.04 | 0.04 | 0.05 | 1.0
| Hash join | 4.55 | 0.05 | 4.53 | 4.5 | 4.65 | 115.244
##  33b

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.05 | 0.0 | 0.05 | 0.05 | 0.06 | 1.549
| Nested loop join | 0.03 | 0.0 | 0.03 | 0.03 | 0.04 | 1.0
| Hash join | 3.75 | 0.08 | 3.72 | 3.68 | 3.89 | 107.212
##  33c

Not interesting 

| Join method | Mean | StdDev | Median | Min | Max | Relative |
| ----------- | ---- | ------ | ------ | --- | --- | ---------|
| No forced join | 0.1 | 0.0 | 0.1 | 0.1 | 0.11 | 2.114
| Nested loop join | 0.05 | 0.0 | 0.05 | 0.05 | 0.05 | 1.0
| Hash join | 4.27 | 0.14 | 4.21 | 4.17 | 4.59 | 87.264
