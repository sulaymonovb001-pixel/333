def find_top_seller(products: dict, sales: dict) -> str:
    a=[]
    b=[]
    y=[]
    for x,i in products.items():
        b.append(x)
        a.append(i)
    for i,x in sales.items():
        y.append(x)

    z,c,v=y
    q,w,e=a

    d=z*q
    f=c*w
    l=v*e
    g=max(d,f,l)
    g=g/v
    for i,x in products.items():
        if x==g:
            return(i)


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))  