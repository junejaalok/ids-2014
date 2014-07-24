import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    mat = record[0]
    val = record
    if mat == 'a':
      mr.emit_intermediate(record[2], val)
    if mat == 'b':
      mr.emit_intermediate(record[1], val)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    print key,list_of_values
#    total=0
    for v in list_of_values:
      for i in v[0]:
        print i 
#      total += v
#    if total == 1 or total == -1:
#      mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
