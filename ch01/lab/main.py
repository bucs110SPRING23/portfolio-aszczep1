import random
# Part A
weeks = 16
print(weeks, type(weeks))
classes = 4 
print(classes, type(classes))
tuition = 32000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print(type(cost_per_week))
print("Whats the opportunity cost of my class?:", cost_per_week)

# Part B
var1= "hi"
var2 = "bye"
var3 = "no"
var4 = "yeah" 
var5 = '4?'
mylist = [var1, var2, var3, var4, var5]
answer = random.choice(mylist)
print(answer)