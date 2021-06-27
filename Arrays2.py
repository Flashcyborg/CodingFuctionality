b = [["A0001","Vishanth","1000000"],
    ["A0002","Alex","23400"],
    ["A0003","Sidharth","34000"],
    ["A0004","Trilochan","500000"],
    ["A0005","Rakesh","23500"]]

def names():
    for x in b:
        print (x[1])

v = []
for x in b:
    v.append(x[1])
    
i = []
for t in b:
    i.append(t[0])

r = []
for e in b:
    r.append(e[2])