dna = input("Enter a DNA sequence: ")
dna = dna.upper()
dna = dna.replace(" ", "")

print("You entered: ", dna )

print(f"Length : {len(dna)}")

print("A: ", dna.count("A"))
print("T: ", dna.count("T"))
print("G: ", dna.count("G"))
print("C: ", dna.count("C"))

for letter in dna:
    if letter not in "ATGC":
        print("Invalid dna sequence. Try again")
        break
else:
    print("Valid dna sequence")    

counts = {}
counts["A"] = dna.count("A")
counts["T"] = dna.count("T")
counts["G"] = dna.count("G")
counts["C"] = dna.count("C")

print(counts)

gc_percent = (counts["G"] + counts["C"]) / len(dna) * 100
print(f"GC%: {gc_percent:.2f}%")

at_percent = (counts["A"] + counts["T"]) / len(dna) * 100
print(f"AT%: {at_percent:.2f}%")

most_common = max(counts, key= counts.get)
print(f"Most_common: {most_common}")

least_common = min(counts, key= counts.get)
print(f"Least_common: {least_common}")

dna_reversed = dna[::-1]
print(f"reversed : {dna_reversed}" )

pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}
dna_complement = ""
for letter in dna:
   dna_complement += pairs[letter]
print(f"complement : {dna_complement}")

dna_reversed_complement = dna_complement[::-1]
print(f"reversed complement : {dna_reversed_complement}")

rna = dna.replace("T", "U")
print(f"RNA : {rna}")

motif = input("Enter motif : ")
motif = motif.upper()
if motif in dna:
    print("Motif :", "Found it!")
else:
    print("Motif :", "Not found")

motif_count = dna.count(motif)
print(f"Motif count : {motif_count}")

restriction_site = "GAATTC"
if restriction_site in dna:
    print("Restriction site :", "Found!")
else:
    print("Restriction site :","Not found!")    

start_codon = "ATG"
position = dna.find(start_codon)
print(f"Codon position : {position}")


   





