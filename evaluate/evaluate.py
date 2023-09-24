import logging
from ..api import bin_size

class Evaluation(object):
    """
    A single class for measuring and evaluating the performance of different bin-packing algorithms
    """
    def __init__(self, algo_name="Alex"):
        self.algo_name = algo_name # Alex or Clara
        logging.basicConfig( # keeping track of what's going on
            level=logging.INFO,  # setting the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            filename="evaluate-" + algo_name + ".log",  # specifying the log file name
            filemode='w'  # use 'w' for overwriting, 'a' for appending
        )
        self.logger = logging.getLogger(__name__)

    def measure_place(self):
        """
        Measures the average bin placement time
        """
        return
    
    def measure_newend(self):
        """
        Measures the average time needed to create and delete problems
        """
        return
    
    def main(self):
        """
        Runs the program and measures its performance in all tasks
        """
        return