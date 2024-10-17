class User():
    def __init__(self, name, id, booking_cost):
        self.name = name
        self.id = id
        self.booking_cost = booking_cost

    def __str__(self):
        return f"name: {self.name}, id: {self.id}, booking cost: {self.booking_cost}"
        