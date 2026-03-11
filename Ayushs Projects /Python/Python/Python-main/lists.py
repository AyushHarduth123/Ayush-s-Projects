# lists = used to store multiple items in a single variable

food = ["pizza","burger","hotdog","spaghetti","pudding"]
print(food[0])
print(food[1])
print(food[2])
print(food)

food.append("banana")
food.insert(1, "apple") # moves other indexes up to fit in new item
print(food[3])

food.remove("apple")
food.sort()
food.reverse()
food.pop(0)
food.clear()


print(food)