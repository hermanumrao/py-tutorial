'''As observed from previous example code, closures help to
invoke function outside their scope'''
def outer(msg): # This is the outer enclosing function
	def inner(): # This is the nested function
		print(msg)
	return inner # returns the nested function
# Now let's try calling this function.
different = outer("this is an example of closure")
different () #refers to inner()
'''Decorators allow us to wrap another function in order to
extend the behavior of wrapped function, without
permanently modifying it
Using decorators, we can extend the features of different
functions in a common way'''