import argparse

from binpacking.solver.statistics import Statistics, StatisticSolution, StatisticFitness
from binpacking.solver.stop_criteria import StopCriteria, CriterionBudget
import Solution
from binpacking.solver.instance_loader import InstanceLoader
from binpacking.plot.plot_handler import PlotHandler
from binpacking.solver.optimisation.metaheuristic.tabu_search import TabuSearch
from binpacking.solver.optimisation.metaheuristic.atomic_operator.neighborhood import Neighborhood


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

    statistics = Statistics()
    statistics.add_statistic(StatisticFitness())
    statistics.add_statistic(StatisticSolution())
    stop_criteria = StopCriteria()
    stop_criteria.add_criterion(CriterionBudget(args.max_iterations))

    tabu_size = 5
    max_iterations = args.max_iterations
    ts = TabuSearch(
        bin_packing,
        statistics,
        stop_criteria,
        tabu_size,
        max_iterations,
        getattr(Neighborhood, 'find_one_mutation_neighbor'),
    )

    solutions = ts.run(sol_init)
    print('best solutions')
    print(solutions)

    for i, solution in enumerate(solutions):
        plot_handler = PlotHandler(bin_packing, solution)
        results_filepath = plot_handler.save_to_file(f'cool_plot_{i}_.png')
