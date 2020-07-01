num = int(input(""))
lst = []
thisdict = {}

for i in range(num):
    name = input("")
    maths = float(input(""))
    physics = float(input(""))
    chem = float(input(""))
    # thisdict['name','maths','physics','chem'] = name,maths,physics,chem
    lst.append((name,maths,physics,chem))

alt_name = input("")
for j in range(num):
    if alt_name == lst[j][0]:
        sum = (lst[j][1] + lst[j][2] + lst[j][3])/3
        new = "{:.2f}".format(sum)
        print(new)