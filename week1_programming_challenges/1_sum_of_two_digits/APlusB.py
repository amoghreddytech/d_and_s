# python3

"""This was provided in the starter files and its a great solution, I'm not really sure what I need to do for the first assignment. My guess is that this is just a test to see how the submission works. So I'm submitting it as is"""

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
