from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution

from binpacking.plot.plot_handler import PlotHandler


if __name__ == '__main__':
    print('Processing and printing to file...')

    instance = BinPacking2D((5, 5), [(1, 1), (1, 1), (1, 1), (1, 1)])
    solution = Solution(instance.get_instance_size())
    solution[0] = (0, 0, 0)
    solution[1] = (1, 1, 0)
    solution[2] = (2, 2, 0)
    solution[3] = (3, 3, 0)

    plot_handler = PlotHandler(instance, solution)
    results_filepath = plot_handler.save_to_file('cool_plot.png')

    print(f'Done! You may look at the results in {results_filepath}')
