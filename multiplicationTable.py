for i in range(1,9):
    print("row", i, end = " ")
    for j in range(1,5):
        print("col", j , end=" ")
    print()
    
print("###################################")
for i in range(1,11):
    print(f"row{i}", end = "\t")
    for j in range(1,11):
        print(f"col{i*j}" , end="\t")
    print()    