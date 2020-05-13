from numpy import mean
from typing import List, Dict
from binpacking.experimentations.exp_backtracking import ExpBacktracking
from itertools import cycle
import matplotlib
from binpacking.experimentations.manage_parallel_run import ManageParallelRun


# Colors, markers and lines
lines = ["-"]  # ,"--","-.",":"]
markers = [
    "o",
    "v",
    "^",
    "^",
    ">",
    "1",
    "2",
    "3",
    "4",
    "8",
    "s",
    "p",
    "*",
    "h",
    "H",
    "+",
    "<",
    "D",
]
colors = [
    "xkcd:black",
    "xkcd:blue",
    "xkcd:green",
    "xkcd:red",
    "xkcd:brown",
    "xkcd:magenta",
    "xkcd:silver",
    "xkcd:pink",
]
linecycler = cycle(lines)
markercycler = cycle(markers)
colorcycler = cycle(colors)

if __name__ == '__main__':
    exp = ExpBacktracking()

    number_of_runs = 32
    list_of_budget = range(100, 2050, 50)

    resultats: Dict[int, List[float]] = {}
    for budget in list_of_budget:
        args = [budget] * number_of_runs
        resultats[budget] = ManageParallelRun.run_parallel(exp.run, args, ret=True)

    print(resultats)
    y: List[float] = []
    for budget in list_of_budget:
        y.append(mean(resultats[budget]))

    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.margins(0.1)
    plt.ylabel("fitness", fontsize=15)
    plt.xlabel("budget", fontsize=15)
    plt.grid(True, linestyle='--', linewidth=0.1, alpha=0.7)
    plt.plot(
        list_of_budget,
        y,
        linestyle=next(linecycler),
        marker=next(markercycler),
        linewidth=1,
        markersize=(1 * 5),
        markeredgewidth=0.0,
        color=next(colorcycler),
    )
    plt.savefig("backtracking-run_randomize.pdf", bbox_inches='tight')
