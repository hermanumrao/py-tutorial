from functools import reduce 
'''reduce format=reduce(fn_name,iterator1,iterator2,iterator3,iterator4....)
reduce applies the fuction which has only 2 parameters
such that only 2 members of the iterator are taken at a time and executed
in simple terms it is like doing this:

print(sum1(1,sum1(2,sum1(3,4))))
nn number of times
'''
l=[1,2,3,4]
def sum1(a,b):
	return a+b
print(reduce(sum1,l))