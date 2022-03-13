# Create a function, which takes strings list and returns only those strings which start from letter "b".
# - Check this function on file three_rings.txt.


# put your code here


path = "G:\\QA\\Nokia\Robot\\NA_Python\\exercises\\three_rings.txt"
file = open(path, "r")
content = file.readlines()
lista = []
def find(txt):
    for i in content:
     content2 = i.split(" ")
     for x in content2:
         if x[0] == "b":
             lista.append(x)
    return(lista)



print(find(content))
