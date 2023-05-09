import random
# Part A
weeks = 16
print(weeks, type(weeks))
classes = 4 
print(classes, type(classes))
tuition = 32000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))
classes_per_week = 3
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class))


# Part B
var1= "hi"
var2 = "bye"
var3 = "no"
var4 = "yeah" 
var5 = '4?'
mylist = [var1, var2, var3, var4, var5]
answer = random.choice(mylist)
print(answer)