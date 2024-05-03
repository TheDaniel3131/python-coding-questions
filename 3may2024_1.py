class MyClass:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x * y


p1 = MyClass(2)

print(p1(3))


# Explanation from online

# The code defines a class named MyClass with two methods: __init__ and __call__.
# The __init__ method is the constructor for the class and it takes one argument, x.
# It assigns the value of x to the instance attribute self.x.

# The __call__ method is a special method that allows an instance of the class to be called like a function.
# It takes one argument, y, and returns the product of self.x and y.

# In the code, an instance of the class MyClass is created with the value 2 passed to the constructor.
# This creates an object with the attribute self.x set to 2.

# When the instance is called with the value 3 (p1(3)), the __call__ method is executed.
# The method multiplies self.x (which is 2) by y (which is 3) and returns the result, which is 6.


# Therefore, the output of the code is 6.