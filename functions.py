#damn you, useless function
def beef():
    print("hey granny, you like beef?")

beef()

#lets make one useful function
def bitcoin(btc):
    amount = btc * 527
    print("The amount in dollars of bitcoin", btc ,"is" , amount)

bitcoin(2)

#return values
def allowed_dating_age(my_age):
    girls_age = my_age/2 +7
    return girls_age

dating_limit = allowed_dating_age(22)
print("bucky can date girls of age",dating_limit,"or older")

#appropriate to drink or not
def drink_or_not(age):
    if age >=18:
        print("you can drink")
    else:
        print("you cannot drink, u are a kid")

drink_or_not(12)
drink_or_not(19)

#guys age between 15 to 60 and their dating age, print in a row of a guy

def allowed_dating_age(my_age):
    girls_age = my_age /2 + 7
    return girls_age

for p in range(15, 61):
    dating_age_limit = allowed_dating_age(p)
    print("A guy of age",p,"can date a girl of age",dating_age_limit)

#default values and arguments
def get_sex(sex="Unknown"):
    if sex == 'm':
        sex= "male"
    elif sex == 'f':
        sex="female"
    print(sex)
get_sex('m')
get_sex('f')
get_sex()

#passing an argument
def dumb_statement(name="messi", action="plays", sports="football"):
    print(name, action, sports)

dumb_statement()
dumb_statement("nadal", "plays", "tennis")
dumb_statement(name="lee chowg wei",sports="badminton")
dumb_statement("ronaldo")
dumb_statement("","" ,"tennis")

#functions that can take any number of arguments
def add_numbers(*args):
    total=0;
    for a in args:
        total += a
    print(total)

add_numbers(2)
add_numbers(2,5)
add_numbers(1,2,3,4,5)
add_numbers(2,3,4,5,44)

#unpacking an argument
def health_calculator(age,apples_ate,cigg_smoked):
    answer=(100-age)+(apples_ate * 3.5)-(cigg_smoked*2.5)
    print("Your health calulator answer is", answer)

buckys_data=[27,20,0]
health_calculator(buckys_data[0],buckys_data[1],buckys_data[2])
health_calculator(*buckys_data)          #this is called argument unpacking



