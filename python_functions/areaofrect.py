class student :
	#constructor

	def get_data(rectangle):
		rectangle.length=input("length")
		rectangle.breadth=input("breadth")
	def show_data(rectangle):
		print(rectangle.length*rectangle.breadth)
obj1=student()
obj1.get_data()
obj1.show_data()
