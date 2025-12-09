# Write a program to merge two dictionaries

d1={1:"a",2:"b",3:"c"}
d2={4:"d",5:"e",6:"f"}
m = {}
for i in (d1, d2):
    for key, value in i.items():
        m[key] = value

print("Merged Dictionary:", m)