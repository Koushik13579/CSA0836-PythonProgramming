import itertools
n=int(input("Enter a number:"))
n=str(n)
perm=itertools.permutations(n)
permutatednums=[int(''.join(p)) for p in perm]
print(permutatednums)