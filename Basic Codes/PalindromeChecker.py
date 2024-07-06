def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    input_string = input("Enter a string: ")

    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
