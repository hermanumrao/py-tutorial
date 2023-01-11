'''filter() allows you to select or filter items from an iterable based on
evaluation of the given function. 
filter(<f>, <iterable>)'''
def gret4(a):# fn to return numbers greater than 4
	if (a>4):
		return True
	else:
		return False
l=[1,2,6,3,5,3,7]
print(list(filter(gret4,l)))
# for use with lambda-------------
print(list(filter(lambda a:a>4,l)))