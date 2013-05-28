import MapReduce
import sys

'''
Created on May 27, 2013
multiply - This one really sucked btw...
@author: houston
'''

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: friend
    matrixName = record[0]
    
    i = 0
    j = 0
    k = 0
    value = 0
    
    if matrixName == 'a':
        i = record[1]
        j = record[2]
        value = record[3]
    else:
        j = record[1]
        k = record[2]
        value = record[3]
    
    # guess we know the dimensions already?
    N = 5
    L = 5
    
    # traverse matrix
    # emit a key that matches for each row / column combo we want to multiply
    # and then sum the results
    
    # C = A X B
    # A has dimensions L,M
    # B has dimensions M,N
    # 
    # for each elem (i,j) of A, emit ((i,k), A[i,j]) for k in 1..N
    # for each elem (j,k) of B, emit ((i,k), B[j,k])) for i in 1..L
    
    if matrixName == 'a':
        for k in range(0,N):
            mr.emit_intermediate((i,k),(matrixName,i,j,value))
    else:
        for i in range(0,L):
            mr.emit_intermediate((i,k),(matrixName,j,k,value))


def reducer(key, list_of_values):
    # key is column / row tuple
    # list of values are values to multiply
    
    # convert list to dict
    mA = {}
    mB = {}
    for record in list_of_values:
        if record[0] == 'a':
            mA[(record[1],record[2])] = record[3]
        else:
            mB[(record[1],record[2])] = record[3]
    
    # from lecture notes... which do not make any sense...
    # key = (i,k)
    # value = Sum j ( A[i,j] * B[j,k] )
    
    # find pairs to multiply
    mSum = 0
    for j in range(0,5):
        
        # default to 1 or 0? 0
        aVal = 0
        bVal = 0
        if (key[0],j) in mA:
            aVal = mA[(key[0],j)]
        if (j,key[1]) in mB:
            bVal = mB[(j,key[1])]
        
        multi = aVal * bVal
        mSum = mSum + multi
           
    mr.emit((key[0],key[1],mSum))
    
        

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
