import MapReduce
import sys

'''
Created on May 25, 2013
inverted index
@author: houston
'''

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: documents
    
    # need to make doc a unique set
    docSet = list(set(list_of_values))
    
    mr.emit((key, docSet))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
