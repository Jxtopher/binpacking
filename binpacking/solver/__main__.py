from binpacking.solver.solution import Solution
from binpacking.solver.instance_loader import InstanceLoader
from binpacking.solver.tabu_search import TabuSearch
from binpacking.solver.neighborhood import Neighborhood
from binpacking.plot.plot_handler import PlotHandler


if __name__ == '__main__':
    bin_packing = InstanceLoader.get_bin_packing('binpacking2d-6-1.json')
    neighborhood = Neighborhood(bin_packing)
    sol_init = Solution(bin_packing.get_instance_size())
    bin_packing.evaluation(sol_init)
    print(sol_init)

    ts = TabuSearch(bin_packing, 5, 300, neighborhood)
    s_star = ts.run(sol_init)
    print('best solution')
    print(s_star)

    plot_handler = PlotHandler(bin_packing, s_star)
    results_filepath = plot_handler.save_to_file('cool_plot.png')
