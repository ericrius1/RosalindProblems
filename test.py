f = open('text.txt', 'r')
bases = [0, 0, 0, 0]
for line in f:
  for char in line:
    if char == 'A':
      bases[0]+=1
    if char == 'C':
      bases[1]+=1
    if char == 'G':
      bases[2]+=1
    if char == 'T':
      bases[3]+=1

print bases


