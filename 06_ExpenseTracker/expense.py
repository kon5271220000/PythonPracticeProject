class expense():
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"name: {self.name}\ncategorie: {self.category}\namount: {self.amount}"