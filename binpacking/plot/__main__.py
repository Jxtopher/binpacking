from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle
from binpacking.solver.data_structure.solution import Solution, Coordinate
from binpacking.plot.plot_handler import PlotHandler


if __name__ == '__main__':
    print('Processing and printing to file...')

    instance = BinPacking2D(
        Rectangle(5, 5), [Rectangle(1, 1), Rectangle(1, 1), Rectangle(1, 1), Rectangle(1, 1)]
    )
    sol = Solution(instance.get_instance_size())
    sol[0] = Coordinate(0, 0)
    sol[1] = Coordinate(1, 1)
    sol[2] = Coordinate(2, 2)
    sol[3] = Coordinate(3, 3)

    plot_handler = PlotHandler(instance, sol)
    results_filepath = plot_handler.save_to_file('test1_plt.png')

    instance = BinPacking2D(
        Rectangle(5, 5), [Rectangle(1, 1), Rectangle(1, 1), Rectangle(1, 1), Rectangle(1, 1)]
    )
    sol = Solution(instance.get_instance_size())
    sol[0] = Coordinate(0, 0)
    sol[1] = Coordinate(1, 0)
    sol[2] = Coordinate(3, 2)
    sol[3] = Coordinate(3, 3)

    plot_handler = PlotHandler(instance, sol)
    results_filepath = plot_handler.save_to_file('test2_plt.png')

    print(f'Done! You may look at the results in {results_filepath}')
