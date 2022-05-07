class Person:
    """
    class for declaring some person method
    """
    def __init__(self, name):
        """
        Constructor to initialize variables
        :param name: to access name of a person
        """
        self.name = name

    def my_func(self):
        """
        Function for printing name and age of a person
        :return: name of a person
        """
        print("Hello, my name is "+self.name)


if __name__ == "__main__":
    # creating an object of Person class
    p1 = Person("Abhi")
    # calling my_func method by object
    p1.my_func()