import pytest
from ..api import api

# pytest functions


##!!!!! if something breaks and it's been fixed, add a test case

#test new problem

#test insert item size 3
#test insert item size 10
#test insert item size 0
#test insert two items into same bin

#test bin number returns properly

#test end problem

#test insert item size 10000
#test 10000 bins with bin of size 1000
problems_dic = {}

def retrieve_id():
    new_bin = api.newProblem()
    problems_dic['ID'] = new_bin['bins']
    return new_bin['ID']


def test_new_problem():
    new_bin = api.newProblem()
    assert new_bin['bins'] == ""

#make a test Class, and make a new object everytime?
#or just one object and reuse it?

#should have a new problem creation
def test_item_size_0():
    id = retrieve_id()
    api.place_item()
