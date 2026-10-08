arr=[-1,100, 400, 500, -300]

total=0
for i in arr:
    if i<0:
        continue
    total+=i
print("total marks", total)
print("total students:", len(arr))