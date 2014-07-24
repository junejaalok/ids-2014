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
    key = record[1]
    value=record
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    val={}
    for value in list_of_values:
      if value[0] == 'order':
        val[value[1]]=value
      else:
        mr.emit(val[value[1]]+value)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
