import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

rowa=5
cola=5
rowb=5
colb=5
def mapper(record):
    # key: document identifier
    # value: document contents
    mat = record[0]
    val = record
    if mat == 'a':
      #for i in range(rowa):
      i=record[1]
      for k in range(colb):
        #print ((i,k), val)
        mr.emit_intermediate((i,k), val)
      

    if mat == 'b':
        k=record[2]
        for i in range(rowa):
          #print ((i,k), val)
          mr.emit_intermediate((i,k), val)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
#    print key,list_of_values
    total=0
    ans={}
    for v1 in list_of_values:
      #total=0
      if v1[0] == 'a':
        for v2 in list_of_values:
          if v2[0] == 'b':
            if v1[2] == v2[1]:
 #             print v1[3],v2[3]
 #             print v1[1],v2[2],v1[3]*v2[3]
              if (v1[1],v2[2]) not in ans:
                ans[(v1[1],v2[2])] = v1[3]*v2[3]
              else:
                ans[(v1[1],v2[2])] += v1[3]*v2[3]
              #print total
              #print v1[1],v2[2],total  

              

    for key in ans:
      f,s=key
      mr.emit((f,s,ans[key]))
#      print i, ans[i]
#      total += v
#    if total == 1 or total == -1:
#      mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
