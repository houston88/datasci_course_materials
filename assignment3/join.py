import MapReduce
import sys

'''
Created on May 25, 2013
join records
@author: houston
'''

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: record type - order or line_item
    # value: tuple - entire row
    key = record[1]
    value = record
    #words = value.split()
    #for w in words:
    
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: documents
    
    # print out joined record
    orderRecord = []
    lineItemRecords = []
    
    for record in list_of_values:
        if record[0] == 'order':
            orderRecord = record
        else:
            lineItemRecords.append(record)
    
    for lineRecord in lineItemRecords:
        mr.emit(orderRecord + lineRecord)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
