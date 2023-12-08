def getsum(*x):
    #*is passed as tuple
    result=0
    for a in x:
        result +=a
    print("result:",result)

getsum(25,5,33,15,22)
