from typing import Tuple, Set, Dict

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution, Coordinate


DomainsType = Dict[int, Set[Coordinate]]


class AC3:
    def __init__(self, bin_packing: BinPacking2D):
        self.bin_packing = bin_packing

    def run(self, sol: Solution, accept_invalid_coordinates: bool = True) -> DomainsType:
        width, height = self.bin_packing.capacity.get_width_height()

        domains = {
            i: set(
                Coordinate(x, y, rotation == 90)
                for rotation in (0, 90)
                for x in range(width)
                for y in range(height)
            )
            for i in range(len(sol))
        }
        if accept_invalid_coordinates:
            for i in range(len(sol)):
                domains[i].add(Coordinate(*Coordinate.INVALID_COORDINATE))

        self.ac3(sol, domains)

        return domains

    def ac3(self, sol: Solution, domains: DomainsType) -> None:
        for i in range(len(sol)):
            domains[i] -= set(
                vx
                for vx in domains[i]
                if (
                    vx.is_valid()
                    and not self.bin_packing.is_inside(vx, self.bin_packing.get_item(i))
                )
            )

            worklist = set((i, j) for j in range(len(sol)) if j != i)

            while len(worklist) != 0:
                arc = worklist.pop()
                if self.arc_reduce(arc, domains):
                    if len(domains[i]) == 0:
                        raise Exception('Total kaput!')
                    else:
                        worklist = worklist.union(
                            set((i, j) for j in range(len(sol)) if j != i and j != arc[1])
                        )

    def arc_reduce(self, arc: Tuple[int, int], domains: DomainsType) -> bool:
        i, j = arc
        bad_ones = []
        for vx in domains[i]:
            if vx.is_valid() and not any(
                not self.bin_packing.has_collision(
                    vx, self.bin_packing.get_item(i), vy, self.bin_packing.get_item(j)
                )
                for vy in domains[j]
            ):
                bad_ones.append(vx)
        for bad_one in bad_ones:
            domains[i].remove(bad_one)
        return len(bad_ones) > 0
