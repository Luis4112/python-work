print ('/n')

# Boolean expressions (True or False)
print("Boolean expressions:")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)

print(type(bool1))

#Relational and Boolean Operators

greater_than = 7 > 5
less_than =  5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and = (7 > 5) and (8 < 7)
test_or =(7 > 5) or (5 < 7)
test_not = not True

print(test_and,test_or,test_not)

#Conditional Statements
print("Conditional statements:")

def soda(money):
    if money >= 2:
            return "You've got a soda"
    else:
            return "No soda here.."

print(soda(2))

def alcohol(age,money):
    if(age >=21) and (money >= 5):
        return "We're getting smashed"
    elif(age >=21) and (money < 5):
        return "Come back with more money"
    elif(age < 21):
        return "You're not old enough man... but i got you." 
print(alcohol(20,5))

