# def show_value():
#     x = 7 #local variable
#     print(x)

# show_value()
# x = 78 
# show_value()

x = 78 #global variable
def show_value():
    global x
    x = 99
    print(x)

show_value()
show_value()
print(x)