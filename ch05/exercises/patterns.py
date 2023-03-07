
times = int(input("How many stars do you want in the pyramid?"))

def star_pyramid(times):
  for i in range(times + 1): 
    print("*" * i)

star_pyramid(times)