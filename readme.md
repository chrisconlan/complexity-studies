# complexity-studies
Educational scripts for Feb 2020 Bethesda Data Science Meetup


#### Sample

See `cumulative_sum.py`

```
                        function  n_values  t_milliseconds  values_per_ms
0            slow_cumulative_sum        10           0.014            699
1            slow_cumulative_sum       100           0.093           1070
2            slow_cumulative_sum      1000           4.516            221
3            slow_cumulative_sum     10000         420.019             24
4   slow_cumulative_sum_expanded        10           0.012            839
5   slow_cumulative_sum_expanded       100           0.329            304
6   slow_cumulative_sum_expanded      1000          29.129             34
7   slow_cumulative_sum_expanded     10000        3100.200              3
8            fast_cumulative_sum        10           0.004           2330
9            fast_cumulative_sum       100           0.010           9533
10           fast_cumulative_sum      1000           0.080          12483
11           fast_cumulative_sum     10000           0.799          12517
12           fast_cumulative_sum    100000           9.506          10520
13           fast_cumulative_sum   1000000          94.953          10532
14    pandas_fast_cumulative_sum        10           0.413             24
15    pandas_fast_cumulative_sum       100           0.290            344
16    pandas_fast_cumulative_sum      1000           0.267           3745
17    pandas_fast_cumulative_sum     10000           0.328          30460
18    pandas_fast_cumulative_sum    100000           0.858         116541
19    pandas_fast_cumulative_sum   1000000           8.911         112222

```

