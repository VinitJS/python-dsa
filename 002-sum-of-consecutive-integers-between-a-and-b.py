# Sum of consecutive integers between a and b

def solution(a, b):
  return int(((b * (b + 1)) / 2) - ((a * (a - 1)) / 2))

# Time O(1)
# Space O(1)
