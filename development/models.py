# models.py
class Book:
    def __init__(self, title, author, price, stock_quantity):
        self.title = title
        self.author = author
        self.price = price
        self.stock_quantity = stock_quantity
