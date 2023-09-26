import logging
import time
import json
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__)) # parallel import is weird
parent_dir = os.path.dirname(current_dir) # I know what I am doing, I swear
sys.path.append(parent_dir)
from api import binsize

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
<<<<<<< HEAD
        test_problem = binsize.new_problem() # creating a new problem for testing purposes
=======
        test_problem = bin_size.new_problem(12501) # creating a new problem for testing purposes
>>>>>>> 50d6c83ea0761ecc2474a951e45ae43db41eeca4
        test_id = json.loads(test_problem)["ID"]
        sizes = range(0, 12501) # bin sizes we will test
        total = 0 # total time to be returned
        for size in sizes:
            start_time = time.time() # testing each placement size
            response = binsize.place_item(test_id, str(size))
            end_time = time.time()
            if not size % 1000:
                self.logger.info(f"Execution time for place_item up to size {size}: {total} seconds")
            total += end_time-start_time
        response = binsize.end_problem(test_id)
        return total
    
    def measure_newend(self):
        """
        Measures the average time needed to create and delete problems
        """
        times = [0, 1, 10, 100, 1000, 10000] # how many bins we will be creating as a part of the test
        total = 0 # total time to be returned
        for t_time in times:
            start_time = time.time() # testing each creation size
            for i in range(0, t_time):
<<<<<<< HEAD
                response = binsize.new_problem() # create n problems
=======
                response = bin_size.new_problem(t_time) # create n problems
>>>>>>> 50d6c83ea0761ecc2474a951e45ae43db41eeca4
            end_time = time.time()
            self.logger.info(f"Execution time for new_problem up to {t_time} times: {total} seconds")
            total += end_time-start_time # save the info
        start_time = time.time() # testing deletion time
        for instanceId in binsize.binPackingInstances.keys():
            response = binsize.end_problem(instanceId)
        end_time = time.time()
        self.logger.info(f"Execution time for deleting all problems: {end_time-start_time} seconds, last response: {response}")
        total += end_time-start_time # save the info
        return total
    
    def main(self):
        """
        Runs the program and measures its performance in all tasks
        """
        total = self.measure_newend()
        total += self.measure_place()
        self.logger.info(f"Total running time for {self.algo_name} evaluation is {total}")
        return total
    
if __name__ == "__main__":
    evaluate = Evaluation() # skeleton code to be changed
    evaluate.main()
