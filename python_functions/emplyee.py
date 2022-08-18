class student :
	class_var=0
	#constructor
	def __init__(self,name,des,sal):
		student.class_var+=1
		self.name=name
		self.des=des
		self.sal=sal
	def show_data(self):
		print(self.name)
		print(self.des)
	def __del__(self):
		print('obj deleted')
obj1=student("asd",'boss',12)
obj2=student('dde','worker',13)
obj3=student('dafd','ceo',1003)
#obj4=student('ewfire','worker',130)
obj1.show_data()
obj2.show_data()
obj3.show_data()
#obj4.show_data()
del obj1
obj4=student('ewfire','worker',130)
obj1.show_data()
obj2.show_data()
obj3.show_data()
obj4.show_data()