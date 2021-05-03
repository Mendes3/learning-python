# map function is an easier way to modify a list
income = [34, 55, 66]
def double(dollars):
    return(dollars*2)

new_list = map(double,income)

print(list(new_list))

