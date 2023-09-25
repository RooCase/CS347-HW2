import logging
import time
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

    def time_place(self, problem, size):
        """
        Measures the time it takes to place a bin of specific size
        """
        start_time = time.time() # testing the empty placement
        response = bin_size.place_item(problem, size)
        end_time = time.time()
        self.logger.info(f"Execution time for place_item size {size}: {end_time-start_time} seconds")
        return response

    def measure_place(self):
        """
        Measures the average bin placement time
        """
        test_problem = bin_size.new_problem() # creating a new problem for testing purposes
        times = [-1, 0, 1, 5, 15, 99, 100, 101, 1000, 12500]
        for t_time in times:
            self.time_place(test_problem, t_time)
        return 200
    
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