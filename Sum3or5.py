#Add all the natural numbers below one thousand that are multiples of 3 or 5.
total = 0
for i in range(1,1000):
    if(i%3==0) or (i%5==0):
            total=total+i
print "Sum of natural numbers below 1000 divisible by 3 or 5:",total
	