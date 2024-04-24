def find_factors(num):
  f = []

  for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
      f.append(i)
      # If i is a factor, its corresponding pair (num // i) must also be a factor
      # Only append the pair if it's not already included (avoids duplicates for perfect squares)
      if i != num // i:
        f.append(num // i)
  return f

# Get user input
while True:
  try:
    number = int(input("Enter an integer: "))
    if number < 0:
      print("Please enter a non-negative integer.")
      continue
    break
  except ValueError:
    print("Invalid input. Please enter an integer.")

# Find factors and print the result
factors_list = find_factors(number)
print(f"The factors of {number} are: {factors_list}")
