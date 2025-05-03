class Settings:
    """A class to control settings for the graphs, so they can be easily adjusted"""

    def __init__(self):
        """Initialize graph settings"""

        # Settings for sin_graph's calculation
        self.cycles = 5
        self.plot_count = 1000

        # Settings for sin_graph's visuals
        self.title_fontsize = 24
        self.xlabel_fontsize = 14
        self.ylabel_fontsize = 14
