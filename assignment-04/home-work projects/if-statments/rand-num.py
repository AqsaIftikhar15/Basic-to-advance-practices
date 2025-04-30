import random

def print_random_numbers():
    for count in range(10):
        random_number = random.randint(1, 100)
        print(random_number, end=' ')
    print()

if __name__ == '__main__':
    print_random_numbers()
