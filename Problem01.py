i = 1
list = []

# Create loop to go through natural numbers below 1000
while i < 4000000:
    if i % 3 == 0: # Make sure it is multiple of 3
        print(i)
        list.append(i) # Store in list then get the sum
    elif i % 5 == 0:
        print(i)
        list.append(i) # Make sure it is multiple of 5
    i += 1

answer = sum(list) # Grab the total
print(answer)