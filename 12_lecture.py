# function 
# def scope_test():
#     x = 123
# scope_test()
# print(x) /


# def my_function():
#     print("Do I Know that variable?",  var)

# var = 1
# my_function()
# print(var)


# def mult (x):
#     var = 7 
#     return x*var 
# var = 3
# print(mult(7))
2

# def my_function():
#     global var 
#     var = 2
#     print("Do I Know that variable?", var)

# var = 1
# my_function()
# print(var)    


# var = 2 
# print(var) # outputs : 2

# def return_var():
#     global var 
#     var = 5
#     return var 

# print(return_var()) #outputs: 5
# print(var)


# def my_function(n):
#     print("I got", n)
#     n += 1 
#     print("I have", n)

# var = 1
# my_function(var)
# print(var)    


# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)

# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2 )


# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     del my_list_1[0]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)

# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2 )


# recursion

# def CountDown(number):
#     print(number)
#     if number == 0:
#         return 
#     else:
#         print("Going in rec:", number)
#         CountDown(number -1)
#         print("Out of rec:",  number)

# print("Starting Recursion")
# CountDown(5)
# print("Completed Recursion")        


# def fact(number):
#     if number <= 0:
#         return 1
#     else:
#         return number * fact(number - 1)
    
# print(fact(5))    


# my_tuple = (1, 10, 100)

# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3
# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)