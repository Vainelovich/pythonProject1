class User:
    def __init__(self, name):
        self.name = name

class Client(User):
    def __init__(self, name="", balance = 0):
        self.balance = balance

        User.__init__(self, name)

    def check_balance(self):
        print('Client "' + self.name + '". Balance: ' + str(self.balance) + ' usd.\n')



if __name__ == '__main__':
    user1 = Client('Vlad B', 50)
    user2 = Client('Anna V', 130)
    user3 = Client('Dan P', 250)
    users = [user1, user2, user3]

for user in users:
    Client.check_balance(user)