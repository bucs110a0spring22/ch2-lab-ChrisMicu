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
print("Classes Per Week:" , classes_per_week)
cost_per_class = (cost_per_week / classes_per_week)
print("Cheap Cost Per Class:" , cost_per_class)

#Part B
list = ["Health" , "Time" , "Money" , "Power" , "Knowledge"]
rando = random.choice(list)
print(rando)