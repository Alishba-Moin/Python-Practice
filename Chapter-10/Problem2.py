import random

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def booked(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {random.randint(222, 5555)}")

train = Train(98765)
train.booked("Lahore", "Multan")
train.getStatus()
train.getFare("Lahore", "Multan")