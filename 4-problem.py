import json 


with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)
    f=[]
    for x in students:
        x=x["grade"]
        f.append(x)
    a=len(f)

    x=min(f)
    d=max(f)

    for i in students:
        if i["grade"] == d:
            print(f"eng baland ball olgan talaba => {i["name"]}")

    for i in students:
        if i["grade"] == x:
            print(f"eng kam ball ogan talaba => {i["name"]}")

    l=0
    for i in f:
        l=l+i
    l=l/a
    print(f"ortacha ball => {l} ")

