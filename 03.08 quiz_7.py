""" Calculate the Collatz conjecture """
def collatz(n):
	''' For positive integer n, return value based on odd or even integer'''
	if n%2==0:
		return n/2
	if n%2==1:
		return 3*n+1

num1=12	
num2 = 1071


f9= collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(num1)))))))))
f14= collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(collatz(num2))))))))))))))

print(f9, f14)
