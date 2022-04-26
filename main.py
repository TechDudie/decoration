def foo(function):
    def whapper():
      print("Hello World!")
      function()
    return whapper
    
@foo
def bar():
    print("Would you like some Foo Bars?")

bar()
