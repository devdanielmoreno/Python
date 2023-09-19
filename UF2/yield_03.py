"""
yield03b.py 
20221202
https://www.simplilearn.com/tutorials/python-tutorial/yield-in-python
"""

def generator():
   yield "Welcome"
   yield "to"
   yield "Programming Class"

def generator2():
   phrase = ["Welcome","to","Programming Class"]
   for word in phrase:
       yield word

for i in generator():
   print(i)
print("----")
for paraula in ["Welcome","to","Programming Class"]:
    print(paraula)
print("****")
for paraula in generator2():
    print(paraula)
