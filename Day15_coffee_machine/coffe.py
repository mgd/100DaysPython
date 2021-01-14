
choices = ["espresso", "latte", "cappuccino"]

resources = {
    "Water": [300, "ml"],
    "Milk": [200, "ml"],
    "Coffee": [100, "g"],
    "Money": ["$", 0.00]
}

money = {
    "Quarters": .25,
    "Dimes": .1,
    "Nickles": .05,
    "Pennies": .01
}

espresso = [50, 0, 18]
latte = [200, 24, 150]
cappuccino = [250, 24, 100]

def getInput():
    return input("What would you like? (espresso/latte/cappuccino):").strip()

def report():
    for key, value in resources.items():
        if key != "money":
            print(f"{key}: {value[0]}{value[1]}")
        else:
            print(f"{key}: {value[1]}{value[0]:.2f}")

def checkResources(bev):
    rVal = True
    bevCounter = 0

    for key, value in resources.items():
        if key != "Money":
            if value[0] - eval(bev)[bevCounter] < 0:
                print(f"Sorry there is not enough enough {key}.")
                rVal = False
        bevCounter += 1
    return True

def removeResources(bev):
    bevCounter = 0
    for key, value in resources.items():
        if key != "Money":
            resources[key] = value[0] - eval(bev)[bevCounter]
        bevCounter += 1

def getMoney(bev):
    total = 0.00
    cost = 0.00
    print("Please insert some coins")
    for key, value in money.items():
         amnt = int(input(f"How many {key}: "))
         total += amnt * value

    if bev == "espresso":
        cost = 1.50
    elif bev == "latte":
        cost = 2.50
    elif bev == "cappuccino":
        cost = 3.00

    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        #Update machine values
        resources["Money"][1] += cost
        resources["Water"][0] = resources["Water"][0] - eval(bev)[0]
        resources["Milk"][0] = resources["Milk"][0] - eval(bev)[1]
        resources["Coffee"][0] = resources["Coffee"][0] - eval(bev)[2]
        print(f"Here is ${(total - cost):.2f} in change.")
    return True

mainFlag = True
while(mainFlag):
    choice = getInput()
    if choice in choices:
        if checkResources(choice):
            if getMoney(choice):
                print(f"Here is your {choice} enjoy!")
    elif "report" == choice:
        report()
    elif "off" == choice:
        mainFlag = False
    else:
        print("Not a valid option")