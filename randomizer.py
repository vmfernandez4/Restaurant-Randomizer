import random

restaurant_list = ["rudys", "tonys", "ribhut","pizza", "chicken"]

random.shuffle(restaurant_list)

stack1 = restaurant_list.pop()
stack2 = []
print("You're going to: " + stack1)


print("Remaining places: " + str(restaurant_list))
print("-------------------------------------------------------------")

stack2.append(stack1)
print("Visited places: " + str(stack2[0]))
file = open("visited.txt", "w")
file.write(stack1.append(stack2))
file.close()



