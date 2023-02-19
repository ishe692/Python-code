

# list can hold different objects
camping_list = ["oranges","apples","bannana","your mum","water","volley ball", "fishing rod"] 

# address| street number | temperature | is it dangerous?
camp_site = ["your mums place", 404, 25.3, True]

me = camping_list[-1]

print(me)
#print(type(camping_list))

# a meathod is a function for a specific object
camping_list.append("tp")
camping_list.insert(0,"ice")
me = camping_list[-1]
print(me)
# add 2 lists can also use .extend
camping_list += ["juice","chocolate"]
# removes and returns item at index
print(camping_list.pop(0))
camping_list.remove("fishing rod")
print(camping_list)

