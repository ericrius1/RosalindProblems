def comp(char):
  if char == 'A':
    print 'T'
  if char == 'T':
    print 'A'
  if char == 'G':
    print 'C'
  if char == 'C':
    print 'G'

f = open('dna.txt', 'r')
dna = f.read()
dna = dna[::-1]
map(comp, dna)

#BASH : cat rosalind2.txt | tr 'ACGT' 'TGCA' | rev