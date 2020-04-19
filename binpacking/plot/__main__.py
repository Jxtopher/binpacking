from binpacking.plot.plot_handler import PlotHandler


if __name__ == '__main__':
    print('Processing and printing to file...')

    # TODO: needs to be based on JSON input, processed by solver,
    # and properly given to the PlotHandler

    capacity = (42.0, 42.0)
    items_to_plot = [
        (0.0, 0.0, 20.0, 20.0),
        (20.0, 0.0, 42.0, 20.0),
        (0.0, 20.0, 20.0, 42.0),
        (20.0, 20.0, 42.0, 42.0),
    ]

    plot_handler = PlotHandler(capacity, items_to_plot)
    results_filepath = plot_handler.save_to_file('cool_plot.png')

    print(f'Done! You may look at the results in {results_filepath}')
