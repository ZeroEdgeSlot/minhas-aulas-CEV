# digite uma frase
f = str(input("digite uma frase: ")).upper().strip()

# quando vezes a letra aparece
print("a letra aparece:", f.count("A"),"vezes")

# quando ela aparece
print("a letra A apareceu na posição", f.find("A")+1)

# quando e a ultima vez que ela aparece
print("quando e a ultima vez que ela aparece", f.rfind("A")+1)
