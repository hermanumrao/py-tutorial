class student :
	#constructor

	def get_data(self):
		self.__rono=input("roll number")
		self.name=input("name")
		self.marks1=int(input("marks sub1 "))
		self.marks2=int(input("marks sub2 "))
		self.marks3=int(input("marks sub3"))
	def total(self):
		self.sum=self.marks1+self.marks2+self.marks3
	def show_data(self):
		print(self.name)
		print(self.sum)
		print(self.rono)
obj1=student()
obj1.get_data()
obj1.total()
obj1.show_data()
