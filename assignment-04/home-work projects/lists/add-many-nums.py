def add_nums(numbers)-> int:
  sum = 0
  for num in numbers:
    sum += num
  return sum

def main():
  lists : list[int] = [1,2,3,4,5,6,7]
  total = add_nums(lists)
  print(total)

if __name__ == "__main__":
  main()
