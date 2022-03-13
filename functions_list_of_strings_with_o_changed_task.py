# Create a function, which takes list of strings and exchanges any letter "o" into "."
# - Check this function on file three_rings.txt.

# put your code here

path = "G:\\QA\\Nokia\Robot\\NA_Python\\exercises\\three_rings.txt"
with open(path, "r") as file:
    content = file.read()
print(content)

def change(txt):
    for x in txt:
        x = txt.replace("o", ".")
        return (x)

print(change(content))


