#10 minutes
def makeMarkovDict(filename):
  m = {}
  filename = filename.split()
  for i in range(len(filename)-2):
      temp = filename[i] + ' ' + filename[i+1]
      if temp not in m:
        m[temp] = [filename[i+2]]
      else:
        m[temp] += [filename[i+2]]
  return m
