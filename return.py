def add(*nums):
    result=0
    val=99
    for x in nums:
        result +=x
    return result,val
#function calling
numsum,z=add(20,30,40,50,60)
print(numsum,z)
print(z)
print(numsum)
