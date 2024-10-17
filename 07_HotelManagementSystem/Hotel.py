class Hotel():
    def __init__(self, name, room, location, rating, pricePerRoom):
        self.name = name
        self.room = room
        self.location = location
        self.rating = rating
        self.pricePerRoom = pricePerRoom

    def __str__(self):
        return f"name: {self.name}, room available: {self.room}, location: {self.location}, rating: {self.rating}, price per room: {self.pricePerRoom}"
    
    def get_name(self):
        return self.name
    
    def get_room(self):
        return self.room
    
    def get_location(self):
        return self.location
    
    def get_rating(self):
        return self.rating