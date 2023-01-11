'''
An iterable is any Python object capable of returning its members one at a time, permitting it to be 
iterated over in a for-loop. Familiar examples of iterables include lists, tuples, and strings.


map is a fn in python that takes input pameters of function  and iterators
map(fn_name,iterator1,iterator2,...)
it basically calls the fn n times where n is the number of elements in the iteratoe passed as parameter
i.e. it can be replaced by:-
fn_name(1st element of iterator1,1st element of iterator2...)
fn_name(2nd element of iterator1,2nd element of iterator2...)
fn_name(3rd element of iterator1,3rd element of iterator2...)
____
____
'''

a=['abc','d','ef']
print(list(map(lambda x:x.upper(),a)))#used lambda to def the fn there it self
print(list(map(len,a)))#all elements in list a are mapped to the fn len()
#=====================================================
n=3#int(input("enter a number"))
def f1(i):
	n=3
	prod=n*i
	return (str(n)+'x'+str(i)+'='+str(prod))
print (list(map(f1,list(range(1,11)) )))
#=========================================================

def f2(a,b):
	return (a+b)
print (list(map(f2,list(range(1,11)),list(range(16,6,-1)))))