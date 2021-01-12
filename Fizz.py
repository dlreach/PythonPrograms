
	
def GetNumber():
	global number
	number = input('Enter a number and I will FizzBuzz that mf!')
	number = int(number)

def Fizzle(number):
	for i in range(number + 1):
		if i % 15 == 0:
			print("FizzBuzz!")
		elif i %3 == 0:
			print("Fizz!")
		elif i %5 == 0:
			print("Buzz") 
		else:
			print(i)

GetNumber()
Fizzle(number)