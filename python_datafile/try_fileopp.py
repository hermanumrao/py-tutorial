
print(max(open("poem2.txt").read().split(),key=len))
#perfect square
#wap to find all the number btw 1 and n which are both perfect sqare and even

def sq(numb):
	if (numb**(1/2)==int(numb**(1/2))):
		return True
	else:
		return False
