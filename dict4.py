fruits = {
    1 : "apple",
    2 : "mango",
    3 : "banana",
    4 : "kiwi",
    5 : "cherry"
}

# keys are the output
for x in fruits:
    print(x)

# values are the output
for x in fruits:
    print(fruits[x])  

# both keys and values 
for x,y in fruits.items():
    print(x, ":",y)      