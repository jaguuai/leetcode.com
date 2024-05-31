def is_palindrome(x: int) -> bool:
    # Negative numbers are not palindromes
    if x < 0:
        return False

    # Convert the number to a string
    str_x = str(x)

    # Reverse the string
    reversed_str_x = str_x[::-1]

    # Check if the original string is equal to the reversed string
    return str_x == reversed_str_x

# Example usages
print(is_palindrome(121))   # Output: True
print(is_palindrome(-121))  # Output: False
print(is_palindrome(10))    # Output: False
