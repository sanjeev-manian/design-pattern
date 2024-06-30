# Mediator Interface
class ChatRoom:
    def display_message(self, message, user):
        raise NotImplementedError("Subclasses should implement this method.")


# Concrete Mediator
class ChatRoomImpl(ChatRoom):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def display_message(self, message, user):
        for u in self.users:
            # Send the message to all users except the sender
            if u != user:
                u.receive_message(message)


# Colleague Interface
class User:
    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room

    def send_message(self, message):
        self.chat_room.display_message(message, self)

    def receive_message(self, message):
        print(f"{self.name} received: {message}")


# Concrete Colleague
class ChatUser(User):
    def __init__(self, name, chat_room):
        super().__init__(name, chat_room)


# Usage
if __name__ == "__main__":
    chat_room = ChatRoomImpl()

    user1 = ChatUser("Alice", chat_room)
    user2 = ChatUser("Bob", chat_room)
    user3 = ChatUser("Charlie", chat_room)

    chat_room.add_user(user1)
    chat_room.add_user(user2)
    chat_room.add_user(user3)

    user1.send_message("Hello everyone!")
