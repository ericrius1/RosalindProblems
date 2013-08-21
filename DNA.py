f = open("dna.txt","r")
dna = f.read()
counts = [dna.count(l) for l in "ACGT"]
print " ".join(str(l) for l in counts)