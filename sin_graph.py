import matplotlib.pyplot as plt
import numpy
from settings import Settings

class SinGraph:

    def __init__(self):
        # Grab settings
        settings = Settings()
        cycles = settings.cycles
        plot_count = settings.plot_count

        end = 2 * numpy.pi * cycles
        ind_var, dep_var = self.get_vars(end, plot_count)

        plt.style.use('dark_background')
        _, graph = plt.subplots()
        graph.plot(ind_var, dep_var)
        graph.set_title('Sine Wave', fontsize=settings.title_fontsize)
        graph.set_xlabel('Radians', fontsize=settings.xlabel_fontsize)
        graph.set_ylabel('Sin(Radians)', fontsize=settings.ylabel_fontsize)

        graph.tick_params(labelsize=14)
        graph.axis([0, end, -1.1, 1.1])
        graph.ticklabel_format(axis='y', style='plain')
        plt.show()

    def get_vars(self, end, plot_count):
        ind_var = numpy.linspace(0, end, plot_count)
        dep_var = numpy.sin(ind_var)
        return ind_var, dep_var

if __name__ == "__main__":
    SinGraph()
