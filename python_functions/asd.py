class student :
	#constructor

	def get_data(self):
		self.name=input("name")
		self.marks=input("marks")
	def __init__(self):
		self.name='null'
		self.marks=0
	def show_data(self):
		print(self.name)
		print(self.marks)
	def __init__(self):
		self.name='null'
		self.marks=0
obj1=student()
obj1.get_data()
obj1.show_data()
