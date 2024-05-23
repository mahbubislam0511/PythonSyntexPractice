class Base(object):
    pass  # Empty Class


class Child(Base):
    pass  # Empty Class


# Test Code:

print(issubclass(Child, Base))
print(issubclass(Base, Child))


c = Child()
b = Base()

print(isinstance(b, Child))
print(isinstance(c, Child))
print(isinstance(b, Base))
print(isinstance(c, Base))
