class Settings:
    """A class to control settings for the graphs, so they can be easily adjusted"""

    def __init__(self):
        # Calculation settings
        self.cycles = 5
        self.plot_count = 1000

        # Font size settings
        self.title_fontsize = 24
        self.xlabel_fontsize = 14
        self.ylabel_fontsize = 14

        # Visual styling
        self.style = 'seaborn-v0_8-whitegrid'
        self.line_color = 'cyan'
        self.axis_limits = [0, 2 * 3.14159 * self.cycles, -1.1, 1.1]

        # Grid settings
        self.show_grid = True
        self.grid_step_pi = 0.5
