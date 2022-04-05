def say(func):
  print("Hello World!")
  func()

@say
def foo():
  print("Would you like some Foo Bars?")

print("Yes please!")
