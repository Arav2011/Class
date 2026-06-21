class fruits:
    # class variable
    taste = 'Sweet'

    # instance variable
    def __init__(self, name, color):
        self.name = name
        self.color = color

#object Creation
apple = fruits('Apple', 'Red')
banana = fruits('Banana', 'Yellow')

print(apple.taste)
print(banana.taste)
print(banana.name, banana.color)


