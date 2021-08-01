
def hello(n):
  if n > 0:
    hello(n-1)
    print("Hello world")

hello(5)
