tup = (1,3,5,2,3,5,1,1,3)
print("The original tuple is : " + str(tup))
res = tuple(set(tup))
print("The tuple after removing duplicates : " + str(res))
