import MapReduce
import sys

'''
Created on May 25, 2013
asymetric friends
@author: houston
'''

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: friend
    person = record[0]
    friend = record[1]
    
    # generate keys that should match up
    # if friendship goes both ways
    matchKey = person+friend
    # user friend as key
    mr.emit_intermediate(matchKey, (person,friend))
    
    # and flip of relationship
    matchKey = friend+person
    mr.emit_intermediate(matchKey, (friend,person))

def reducer(key, list_of_values):
    # key: person+friend
    # value: friends
    
    # emit friend,person tuple
    # if there is only one value, friendship is not symetric
    
    if len(list_of_values) == 1:
        mr.emit(list_of_values[0])
        
    #mr.emit((key,list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
