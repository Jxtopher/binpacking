import argparse

from binpacking.solver.statistics import Statistics, StatisticSolution, StatisticFitness
from binpacking.solver.stop_criteria import StopCriteria, CriterionBudget
from binpacking.solver.data_structure.solution import Solution
from binpacking.solver.instance_loader import InstanceLoader
from binpacking.plot.plot_handler import PlotHandler
from binpacking.solver.optimisation.metaheuristic.tabu_search import TabuSearch
from binpacking.solver.optimisation.metaheuristic.atomic_operator.neighborhood import (
    Neighborhood_one_mutation,
)
from binpacking.solver.factory import Factory


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
        '-c',
        '--config',
        type=str,
        default='',
        help='Solver configuration',
    )
    parser.add_argument(
        '--max_iterations', type=int, default=300, help='Maximum number of iterations'
    )
    args = parser.parse_args()

    if args.config != '':
        config = Factory.load_json(args.config)
        instance = Factory.build_config(config)
        results = Factory.run_solver(config, instance)
        print(results)
        exit(0)

    bin_packing = InstanceLoader.get_bin_packing(args.instance)
    sol_init = Solution(bin_packing.get_instance_size())

    statistics = Statistics()
    statistics.add_statistic(StatisticFitness())
    statistics.add_statistic(StatisticSolution())
    stop_criteria = StopCriteria()
    stop_criteria.add_criterion(CriterionBudget(args.max_iterations))

    neighborhood_one_mutation = Neighborhood_one_mutation(bin_packing)

    tabu_size = 5
    ts = TabuSearch(
        bin_packing,
        statistics,
        stop_criteria,
        tabu_size,
        neighborhood_one_mutation,
    )

    solutions = ts.run(sol_init)
    print('best solutions')
    print(solutions)

    for i, solution in enumerate(solutions):
        plot_handler = PlotHandler(bin_packing, solution)
        results_filepath = plot_handler.save_to_file(f'cool_plot_{i}_.png')
