class MyException:
	def __init__(self, str):
		self.str = str
	def __str__(self):
		return self.str
n = int(input("enter a number:"))
try:
	if not 1 <= n <= 100 :
		raise MyException("number not in range")
		print("number is fine : ", n)
except MyException as e:
	print(e)
	print("thats all")
else:
	print("in range")