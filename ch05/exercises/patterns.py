
times = int(input("How many stars do you want in the pyramid?"))

def star_pyramid(times):
  for i in range(times + 1): 
    print("*" * i)

# range(start, stop, step)
def rstar_pyramid(rows):
  for i in range(rows, 0, -1):
    print("*" * i)

star_pyramid(times)
rstar_pyramid(times)