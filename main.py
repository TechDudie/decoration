def say(func):
  print("Hello World!")
  func()

def foo():
  print("Would you like some Foo Bars?")

@say(foo)
print("Yes please!")
