### 2 types of loop controls 1.break 2.continue ###
### break - will terminate the loop when the condition met ###

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)    


### continue - it will skip the current iteration of the loop and proceed to the next one ###
fruits = ['apple','banana','mango',7]
for x in fruits:
    if x == 'mango':
        continue
    print(x)   