import argparse

from binpacking.solver.solution import Solution
from binpacking.solver.instance_loader import InstanceLoader
from binpacking.solver.tabu_search import TabuSearch
from binpacking.solver.neighborhood import Neighborhood
from binpacking.plot.plot_handler import PlotHandler


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--instance',
        type=str,
        default='binpacking2d-6-1.json',
        help='Instance path of bin packing',
    )
    parser.add_argument(
        '--max_iterations', type=int, default=300, help='Maximum number of iterations'
    )
    args = parser.parse_args()

    bin_packing = InstanceLoader.get_bin_packing(args.instance)
    sol_init = Solution(bin_packing.get_instance_size())

    tabu_size = 5
    max_iterations = args.max_iterations
    ts = TabuSearch(bin_packing, tabu_size, max_iterations, Neighborhood.find_one_mutation_neighbor)

    s_star = ts.run(sol_init)
    print('best solution')
    print(s_star)

    plot_handler = PlotHandler(bin_packing, s_star)
    results_filepath = plot_handler.save_to_file('cool_plot.png')
