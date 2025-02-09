# for loop and while loop

# for loop
for i in range(10): # the rang returns a list of n-1 in this case n is 6
    if i == 5:
        break # stops a loop
    if i == 2:
        continue # skips an iteration
    print(i)
    
# while 
# this will run as long as a certain condition is true
x = 1

while x <= 5:
    print(x)
    x = x + 1
