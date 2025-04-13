import numpy as np
numbers=[1,2,3,4,5]

# list=list(map(lambda a:a**2,numbers))
# print(list)
list2=list(filter(lambda a:a%2==0,numbers))
print(list2)