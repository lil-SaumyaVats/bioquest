dna = input("Enter a DNA sequence: ")
dna = dna.upper()

print("You entered: ", dna )

print("Length: ", len(dna))

print("A: ", dna.count("A"))
print("T: ", dna.count("T"))
print("G: ", dna.count("G"))
print("C: ", dna.count("C"))

for letter in dna:
    if letter not in "ATGC":
        print("Invalid dna sequence")
        break
else:
    print("Valid dna sequence")    



