import inspect

# TODO: Implement function
# some additional notes
def my_func(a: "mandatory positional",
            b: "optional positional" = 1,
            c=2,
            *args: "additional positional arguments",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: 'additional keyword-only arguments') -> "does something":
    """does something
       or other.
       
    """
    i = 10
    j = 20

my_func.short_description = "this is a function that does something"

print(my_func.__doc__)

print(dir(my_func))


def func(): # this function is not bound to anything. It is a function.
    pass

class MyClass():
    def f(self): # this function is bound to an instance of the class. So it is a method and not a function.
        pass

my_object = MyClass()

inspect.isfunction(func) # True
inspect.ismethod(func) # False
inspect.isfunction(f) # False
inspect.ismethod(f) # True

inspect.isfunction(my_object.f) # False
inspect.ismethod(my_object.f) # True

inspect.isroutine(my_func) # True
inspect.isroutine(f) # True
inspect.isroutine(my_object.f) # True