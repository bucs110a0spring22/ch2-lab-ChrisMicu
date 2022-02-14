import random

#Part A
weeks = 16
print("Weeks:" , weeks)
classes = 5
print("Classes:", classes)
tuition = 6000
print("Tuition:" , tuition)
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 5
print(classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print(cost_per_class , type(cost_per_class))


#Part B
liist = ["Health" , "Time" , "Wealth" , "Power" , "Knowledge"]
rando = random.choice(liist)
print("Random goal to achieve:" , rando)