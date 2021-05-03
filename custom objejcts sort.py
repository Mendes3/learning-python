from operator import attrgetter


class User:
    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + " :" + str(self.user_id)


users = [
    User('bucky', 12),
    User('tune', 21),
    User('roberts', 51),
    User('tom', 45),
    User('roberts', 50)
]
for x in users:
    print(x)
print("-----")
for x in sorted(users, key=attrgetter('name')):
    print(x)
print("-----")
for x in sorted(users,key=attrgetter('user_id')):
    print(x)

