#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: *
# @License: *
# @Date: *
# @Version: *
# @Purpose: *
#

from binpacking.solver.solution import Solution
from binpacking.solver.binPacking2D import BinPacking2D
from binpacking.solver.instanceLoader import InstanceLoader
from binpacking.solver.tabuSearch import TabuSearch
from binpacking.solver.neighbor import Neighbor


if __name__ == "__main__":
    bin_packing = InstanceLoader.get_bin_packing("instances/binpacking2d-5-1.json")
    sol_init = Solution(5)

    ts = TabuSearch(bin_packing, 5, 300, Neighbor.random)
    print(ts.run(sol_init))