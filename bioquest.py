dna = input("Enter a DNA sequence: ")
dna = dna.upper()

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



