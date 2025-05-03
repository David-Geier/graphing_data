


import matplotlib.pyplot as plt
import numpy as np
from settings import Settings

class SinGraph:

    def __init__(self):

        settings = Settings()

        # Calculate end with number of desired cycles, grab variables for the graph
        end = self._calc_end(settings)
        ind_var, dep_var = self._get_vars(end, settings.plot_count)

        # Setup sin graph visually
        plt.style.use(settings.style)
        _, graph = plt.subplots()
        graph.plot(ind_var, dep_var, color=settings.line_color)
        graph.set_title('Sine Wave', fontsize=settings.title_fontsize)
        graph.set_xlabel('Radians', fontsize=settings.xlabel_fontsize)
        graph.set_ylabel('Sin(Radians)', fontsize=settings.ylabel_fontsize)
        graph.tick_params(labelsize=14)
        graph.axis(settings.axis_limits)
        graph.ticklabel_format(axis='y', style='plain')

        # If grid is desired from settings, calls grid setup
        if settings.show_grid:
            self._setup_pi_grid(graph, settings)

        plt.show()

    def _calc_end(self, settings):
        """Determines end of graph with 2*pi*r and the set number of cycles"""

        end = 2 * np.pi * settings.cycles
        return end

    def _get_vars(self, end, plot_count):
        """Calculates variables based on end and plot count"""

        ind_var = np.linspace(0, end, plot_count)
        dep_var = np.sin(ind_var)
        return ind_var, dep_var

    def _setup_pi_grid(self, graph, settings):
        """Calculates grid and tick locations for each quarter pi cycle"""

        # Ultimately calculate list of tick positions
        step = settings.grid_step_pi * np.pi
        num_ticks = int((settings.cycles * 2 * np.pi) // step) + 1
        tick_positions = [i * step for i in range(num_ticks)]

        # Set ticks and labels for each tick
        graph.set_xticks(tick_positions)
        # This is a different application for someone else's elegant solution to a coding challenge I found a while back
        graph.set_xticklabels(
            [f'{round(x/np.pi, 1)}π' if x != 0 else '0' for x in tick_positions] # Said elegant solution (Always cool to see code condensed to a single line)
        )
        graph.grid(True, which='both', axis='x', linestyle='--', alpha=0.5)

if __name__ == "__main__":
    SinGraph()
