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
    person = record[0]
    friend = record[1]
    mr.emit_intermediate((person,friend),1)
    mr.emit_intermediate((friend,person),-1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    print key,list_of_values
    total=0
    for v in list_of_values:
      total += v
    if total == 1 or total == -1:
      mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
