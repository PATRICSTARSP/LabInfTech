def f1(n):
  return n

def f2():
  n = int(input())
  return n+f1(n)

print(f2())
