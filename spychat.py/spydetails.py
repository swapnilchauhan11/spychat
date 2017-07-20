from datetime import datetime   #Import Datetime

class spy:              #Class named spy consisting of spy data

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me



spy = spy('Swapnil', 'Ms.', 20, 4)    #Already existing spy details

#friends details
friend_one = spy('Sabha', 'Ms.', 21, 4.7)
friend_two = spy('Chanchal', 'Mr.', 33, 4.2)
friend_three = spy('Sakshi', 'Ms.', 35, 3.8)
friend_four = spy('Kavin', 'Mr.', 40, 4)


#friends list
friends = [friend_one, friend_two, friend_three, friend_four]
