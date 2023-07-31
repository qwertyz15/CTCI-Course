# Approach 1
# TC - 0(1)
# SC - 0(1)
def sum_of_n_natural_numbers_1(n):
  sum = (n * (n + 1)) // 2
  return sum


# Approach 2
# TC - 0(n)
# SC - 0(1)
def sum_of_n_natural_numbers_2(n):
  sum = 0
  for i in range(n + 1):
    sum += i
  return sum


if __name__ == '__main__':
  N = int(input())
  sum1 = sum_of_n_natural_numbers_1(N)
  sum2 = sum_of_n_natural_numbers_2(N)
  print(sum1)
  print(sum2)
