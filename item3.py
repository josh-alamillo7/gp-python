def square_if_even(x):
  if x%2 == 0:
    return x**2
  else:
    return x

squared_list = list(square_if_even(n) for n in range(1, 11))

print squared_list