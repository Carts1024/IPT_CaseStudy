def get_integer_tuple_list():
  """Gets a list of integer tuples from the user.

  Returns:
    A list of tuples where each tuple contains integers.
  """
  while True:
    try:
      user_input = input("Enter a list of comma-separated integer tuples enclosed in square brackets (e.g. [(1, 2), (3, 4)]): ")
      # Remove any extra spaces from the input
      user_input = user_input.strip()
      # Evaluate the input as a list comprehension to handle tuples correctly
      return eval(user_input)
    except SyntaxError:
      print("Invalid input. Please enter a list of comma-separated integer tuples in square brackets.")

def get_integer_value():
  """Gets an integer value from the user.

  Returns:
    An integer entered by the user.
  """
  while True:
    try:
      k = int(input("Enter an integer value for K: "))
      return k
    except ValueError:
      print("Invalid input. Please enter an integer value.")

def find_divisible_tuples(list_of_tuples, k):
  """Finds tuples in the list that are divisible by K.

  Args:
    list_of_tuples: A list of tuples containing integers.
    k: An integer value.

  Returns:
    A list of tuples that are divisible by K.
  """
  return [x for x in list_of_tuples if all(val % k == 0 for val in x)]

def main():
  """Gets user input, finds divisible tuples, and prints the result."""
  list_of_tuples = get_integer_tuple_list()
  k = get_integer_value()
  divisible_tuples = find_divisible_tuples(list_of_tuples, k)
  print("Tuples divisible by", k, "are:", divisible_tuples)

if __name__ == "__main__":
  main()
