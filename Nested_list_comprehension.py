
#Nested list comprehension using loop
lst = []
for i in range(5):
    lst.append([])
    for j in range(5):
        lst[i].append(j)
print(lst)