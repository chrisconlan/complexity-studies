# complexity-studies
Educational scripts for Feb 2020 Bethesda Data Science Meetup


#### Sample

See `cumulative_sum.py`

```
                        function   n_values  t_milliseconds  values_per_ms
0            slow_cumulative_sum         10           0.010            999
1            slow_cumulative_sum        100           0.094           1067
2            slow_cumulative_sum       1000           4.466            224
3            slow_cumulative_sum      10000         389.667             26
4   slow_cumulative_sum_expanded         10           0.010            953
5   slow_cumulative_sum_expanded        100           0.286            350
6   slow_cumulative_sum_expanded       1000          26.299             38
7   slow_cumulative_sum_expanded      10000        2828.294              4
8            fast_cumulative_sum         10           0.003           2996
9            fast_cumulative_sum        100           0.009          11038
10           fast_cumulative_sum       1000           0.074          13574
11           fast_cumulative_sum      10000           0.696          14369
12           fast_cumulative_sum     100000           8.910          11223
13           fast_cumulative_sum    1000000          92.171          10849
14           fast_cumulative_sum   10000000         884.232          11309
15           fast_cumulative_sum  100000000        8532.659          11720
16    pandas_fast_cumulative_sum         10           0.503             20
17    pandas_fast_cumulative_sum        100           0.253            396
18    pandas_fast_cumulative_sum       1000           0.230           4351
19    pandas_fast_cumulative_sum      10000           0.295          33880
20    pandas_fast_cumulative_sum     100000           0.811         123326
21    pandas_fast_cumulative_sum    1000000           8.140         122856
22    pandas_fast_cumulative_sum   10000000          76.779         130244
23    pandas_fast_cumulative_sum  100000000        1294.202          77268
```

![Cumulative sum time]('cumulative_sum_time.png')
![Cumulative sum efficiency]('cumulative_sum_efficiency.png')




