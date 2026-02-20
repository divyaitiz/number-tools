while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

def is_palindrome(n):
    return n == reverse_number(n)

reversed_num = reverse_number(num)
print("Reversed number:", reversed_num)
print("Is palindrome:", is_palindrome(num))

