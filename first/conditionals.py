
print("Hello and welcome to countup.")

name = input("What is your name?\n")

if name == "john" or name == "dave" or name == "steven":
    bear_status = input("Are u a bear?\n")

    if bear_status.startswith("y") and int(input("how many people have you eaten today?")) > 4:
        print("You are not welcome here "+name+" the bear, ") 
        print("you do not have the right to bear arms\n *rips off arms")
    else:
        print("Hello "+name+", thank you for coming in today.\n\n")

else:
    print("Hello "+name+", thank you for coming in today.\n\n")
