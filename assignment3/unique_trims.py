import MapReduce
import sys

'''
Created on May 27, 2013
unique_trims
@author: houston
'''

# Problem 5
# The output from the reduce function should be the 
# unique trimmed nucleotide strings.

# Consider a set of key-value pairs where each key is sequence id 
# and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....
# Write a MapReduce query to remove the last 10 characters from each string of nucleotides,
# then remove any duplicates generated.

# You can test your solution to this problem using dna.json:
# python unique_trims.py dna.json
# You can verify your solution against unique_trims.json.

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: friend
    sequence = record[0]
    nucleotides = record[1]
    
    # remove late 10 characters
    trimmed_nucleotides = nucleotides[0:len(nucleotides)-10]
    
    # Send to reducer... use unique key to limit results
    mr.emit_intermediate(trimmed_nucleotides,sequence)
    

def reducer(key, list_of_values): 
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
    