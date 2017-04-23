class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
            return self.side * 4

    def change_size(self, amount):
         self.side += amount

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def print_size(self):
            print (""" I sqaure with a side of {} and my perimeter is {}
                    """.format(self.side, self.calculate_perimeter()))


a_square = Square(20)
a_square.print_size()
a_square.change_size(-1)
a_square.print_size()
a_square.what_am_i()




class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
            return (self.width+ self.length)* 2

    def print_size(self):
        print("""I am a Rectangle that is {} by {} width a perimeter of {}
              """.format(self.width,
                         self.length, self.calculate_perimeter()))

    def what_am_i(self):
        super().what_am_i()
        print("I am a Rectangle.")


my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()
my_rectangle.what_am_i()


class Horse():
    def __init__(self , name, age):
        self.name = name
        self.age = age

class Rider():
    def __init__(self, name, horseName):
        self.name = name
        self.horseName  = horseName

    def printRider(self):
        print ("My name is {} and my horse is {} and he is {} years old".format(self.name, self.horseName.name, self.horseName.age))


horse1 = Horse("pony1",6)
rider1 = Rider("Billy",horse1)
rider1.printRider()       
