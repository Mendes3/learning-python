items = ['o1 may 21', 'bread gloves', '99']
print(items[0])
# we can store each item in a variable using a single line of code
date, name, number = ['o1 may 21', 'bread gloves', '99']
print(name)
print(name)
print(number)
# we can use a function and utilize concept of aestirk to unpack a list in three variables
# three variables first, *middle and last can store items of lists of any lenght


def unpack_a_list(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


unpack_a_list([1,2,3,4,1])
unpack_a_list([34,323,434,2,232,23,556])
