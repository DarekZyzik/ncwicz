# Write a program that prints sorted list of words from three_rings.txt
# 
# words should be unique (ignore case-sensitive)
# words should not have any dots
# words should not have any commas

# put your code here
path = "G:\\QA\\Nokia\Robot\\NA_Python\\exercises\\three_rings.txt"
file = open(path, "r")
content = file.readlines()
lines = [line.rstrip() for line in content]
print(lines)

lista = []
for i in lines:
    content2 = i.split(" ")
    for x in content2:
        content2 = x.lower()
        content2 = content2.replace(".", "")
        content2 = content2.replace(",", "")
        if content2 not in lista and content2 != "":
            lista.append(content2)
lista.sort()
print(lista)
