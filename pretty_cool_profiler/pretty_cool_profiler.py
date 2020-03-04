from timeit import default_timer
import pandas as pd
from contextlib import contextmanager
from typing import List, Dict, Any
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (7, 4)
plt.rcParams['figure.dpi'] = 150

mpl.rcParams['grid.color'] = 'k'
mpl.rcParams['grid.linestyle'] = ':'
mpl.rcParams['grid.linewidth'] = 0.5

__all__ = ["time_this", "report_results", "timed_report"]
# A module-level store of all the evaluation times of things you ran with the 
# @time_this decorator
runtime_table: List[Dict[str, Any]] = list()


def time_this(method):
    """
    A decorator that stores the evaluation time some information about the first
    argument to estimate computational efficiency relative to it.
    """

    def timed_function(*args, **kwargs):
        ts = default_timer()
        result = method(*args, **kwargs)
        te = default_timer()
        print(f'{method.__name__}')

        n = len(args[0])
        t = (te - ts) * 1000
        n_over_t = round(n / t)
        print(f'    n   = {n} values')
        print(f'    t   = {round(t, 3)} ms')
        print(f'    n/t = {n_over_t} values per ms')
        print()
        runtime_table.append({
            'function': method.__name__,
            'n_values': n,
            't_milliseconds': round(t, 3),
            'values_per_ms': n_over_t,
        })
        return result

    return timed_function


def report_results():
    """
    Plot and print some information about the efficiency of the algorithms you
    just ran
    """
    df = pd.DataFrame(runtime_table)
    print(df)
    pivot_table = df.pivot(
        index='n_values',
        columns='function',
        values='t_milliseconds',
    )
    ax = pivot_table.plot(
        logx=True,
        logy=True,
        title='Milliseconds to complete',
    )
    ax.set_ylabel('milliseconds')
    ax.set_xlabel('input length')
    plt.grid()
    plt.savefig('milliseconds_to_complete.png')

    pivot_table = df.pivot(
        index='n_values',
        columns='function',
        values='values_per_ms',
    )
    ax = pivot_table.plot(
        logx=True,
        logy=True,
        title='Values processed per millisecond',
    )
    ax.set_ylabel('values per millisecond')
    ax.set_xlabel('input length')
    plt.grid()
    plt.savefig('values_processed_per_millisecond.png')
    plt.show()


@contextmanager
def timed_report():
    """
    e a s e   o f   u s e
    """
    yield
    report_results()
