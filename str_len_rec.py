#wap recursion find len of string
def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
 
a = 60
b = 48
 
# prints 12
print("The gcd of 60 and 48 is : ", end="")
print(hcf(a, b))
st=input("string=")

def st_len(st,i):
	if 