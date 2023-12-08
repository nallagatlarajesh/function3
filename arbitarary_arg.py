#foir vertival alignment
#for arbitarary arfuments we are given 2 artistrts..


def people(**data):
    for k,v in data.items():
        if k=="fname" or k=="sname":
            print(k, " :", v)
        elif k=="age":
            print(k, "   :", v)
        else:
            print(k, "   :", v)
people(fname="rajesh", sname="n", age=30, num=8179123)
