class ChatRoomMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message)

class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom

    def send(self, message):
        self.chatroom.send_message(message, self)

    def receive(self, message):
        print(f"{self.name} received: {message}")

chatroom = ChatRoomMediator()

carol = User("Carol", chatroom)
thomas = User("Thomas", chatroom)
matthew = User("Matthew", chatroom)

chatroom.add_user(carol)
chatroom.add_user(thomas)
chatroom.add_user(matthew)

carol.send("Hello, everyone!")
thomas.send("Hi, Carol!")
matthew.send("Hey there!")
