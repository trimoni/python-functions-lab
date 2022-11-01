def sum_to(n):
  return sum(range(n+1))

print(sum_to(6))
print(sum_to(10))

def largest(list):
  max = list[0]
  for x in list:
    if x > max:
      max = x
  return max

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))
