################### Here we have to explicitly put global ###############
health = 10
print(health) # = 10

def decreaseHealth():
    global health
    health -= 1

decreaseHealth()
print(health) # = 9

################ For a list we don't need to ########################
lst = [1,2,3,4,5]
print(lst)

def decreaseList():
    lst.pop()

decreaseList()
print(lst)