from binpacking.solver.solution import Solution
from binpacking.solver.instance_loader import InstanceLoader
from binpacking.solver.tabu_search import TabuSearch
from binpacking.solver.neighbor import Neighbor


if __name__ == '__main__':
    bin_packing = InstanceLoader.get_bin_packing('binpacking2d-6-1.json')
    neighbor = Neighbor(bin_packing)
    sol_init = Solution(5)
    bin_packing.evaluation(sol_init)
    print(sol_init)

    ts = TabuSearch(bin_packing, 5, 300, neighbor)
    s_star = ts.run(sol_init)
    print("best solution")
    print(s_star)
    # TODO: the above doesn't return a value, what to print?
