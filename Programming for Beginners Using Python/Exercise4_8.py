#For Loops
furnitures = ["table","chair","cabinet","desk","couch"]
for x in furnitures:
    if x == "cabinet":
        continue
    print(x)

#For While Loops
i = 1
while i < 15:
    print(i)
    i += 1
else:
    print("i is no longer less than 15")