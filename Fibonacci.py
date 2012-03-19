#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a, n, sum, total = 0, 1, 0, 0
while sum <= 4000000:
	sum = a + n
	a = n
	n = sum
	if sum%2 == 0:
		total = total + sum
print "Sum of even valued fibonacci numbers:",total
