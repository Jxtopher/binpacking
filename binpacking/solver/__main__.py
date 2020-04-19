from binpacking.solver.solution import Solution
from binpacking.solver.instanceLoader import InstanceLoader
from binpacking.solver.tabuSearch import TabuSearch
from binpacking.solver.neighbor import Neighbor


if __name__ == '__main__':
    bin_packing = InstanceLoader.get_bin_packing('binpacking2d-5-1.json')
    neighbor = Neighbor(bin_packing)
    sol_init = Solution(5)

    ts = TabuSearch(bin_packing, 5, 300, neighbor)
    ts.run(sol_init)
    # TODO: the above doesn't return a value, what to print?
