import MapReduce
import sys

'''
Created on May 25, 2013
friend count
@author: houston
'''

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: record type - order or line_item
    # value: tuple - entire row
    key = record[0]
    value = record[1]
    
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person
    # value: friends
    
    # print out joined record
    count = 0
    
    for friend in list_of_values:
        count = count + 1
        
    mr.emit((key,count))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
