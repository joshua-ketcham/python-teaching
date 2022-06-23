def my_function():
    print("This is my function")
    print("Functions are very cool")

# my_function()
# my_function()

def my_function_with_arguements(parameter_one, parameter_two):
    print(parameter_one)
    print(parameter_two)

# my_function_with_arguements("hello", "there")
# my_function_with_arguements("general", "kenobi")


def sum(a, b):
    print(a+b)

# sum(1,3)
# Write a funciton called average that takes in two integers or floats and prints their average

# average(3,7) #### This would print 5
# average(10,20) #### This would print 15


# Return
def add_two(my_num):
    # print(my_num+2)
    return my_num+2
# result = add_two(5) # equal to 7. not print(7)
# print(result)
# print(add_two(5))


def can_i_sleep_in(weekend, morning_plans):
    # can_i_sleep_in(True, False) pretend i sent this into the function
    # return True and (not False)
    # return True and True
    # return True

    return weekend and (not morning_plans)
    
# print(can_i_sleep_in(weekend = True, morning_plans = False))
# print(can_i_sleep_in(morning_plans = False, weekend = True))

# print(can_i_sleep_in(False, False))


# print(not True) # False
# print(True and False) # False
# print(True and True) # True
# print(False and False) # False
# print(False and True) # False

# print(True or False) # True
# print(True or True) # True
# print(False or False) # False
# print(False or True) # True


# def can_i_go_to_the_beach(sunny, temp_over_80, windy):
#     # Fill out the function! 


# print(can_i_go_to_the_beach(True, True, False), "should be True")
# print(can_i_go_to_the_beach(False, True, False), "should be False")
# print(can_i_go_to_the_beach(True, True, True), "should be False")
# print(can_i_go_to_the_beach(True, False, False), "should be False")


# print("hello"==43567)
# print("hello"=="hello")
# print(43567==43567)

# print(43567!=43567)
# print(10>11)
# print(10<11)
# print(10<=11)
# print(10>=11)


def should_i_go_outside(temp):
    # return true if temp>=80
    return temp>=80 and temp<=105

    # if (temp>=80 and temp<=105):
    #     return True
    # else:
    #     return False

# print(should_i_go_outside(80))
# print(should_i_go_outside(106))





def has_teen(a, b, c):
    # Return true if one of these numbers is a teen
    # if any of them are not, return false
    return True


# print(has_teen(10,13,19)==True)
# print(has_teen(16,13,19)==True)
# print(has_teen(15,13,20)==True)
# print(has_teen(16,13,19)==True)
# print(has_teen(20,20,16)==True)
# print(has_teen(9,10,20)==False)
# print(has_teen(45,99,2)==False)





# Write me a function named round_fun that takes in a float and returns the rounded value.

# round_fun(10) ## return 10.0
# round_fun(1.1) #  


# 0
    
    
    #return ...

# print(fround(1.5)==2)
# print(fround(-1.5)==-2)
# print(fround(-1.4)==-1)
# print(fround(1.4)==1)
# print(fround(0)==0)



# def hello(name):
#     # returns "Hello <name>!" as a string
#     # returns an empty string if the name is jacob



# print(hello('bob')=='Hello bob!')
# print(hello('ben')=='Hello ben!')
# print(hello('joshua')=='Hello joshua!')
# print(hello('jacob')=='')



# number = 0

# # if example
# if number>1:
#     print("Im in the first if")

# if number>2:
#     print("Im in the second if")
# else:
#     print("Im in the else (Jackson)")


# number = 2

# # elif example
# if number==1:
#     print("Im in the first if")
# elif number==2:
#     print("Im in the second? elif")
# elif number<3:
#     print("im in the third? elif")
# else:
#     print("Im in the else (Jackson)")
