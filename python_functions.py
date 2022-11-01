def sum_to(n):
  return sum(range(n+1))

print(sum_to(6))
print(sum_to(10))



def largest(nums):
  big = nums[0]
  for x in nums:
    if x > big:
      big = x
  return big

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))



def occurrences(str1, str2):
  return str1.count(str2)

print(occurrences('fleep floop', 'e'))
print(occurrences('fleep floop', 'p'))
print(occurrences('fleep floop', 'ee'))
print(occurrences('fleep floop', 'fe'))



def product(*args):
  total = 1
  for arg in args:
    total *= arg
  return total

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))

