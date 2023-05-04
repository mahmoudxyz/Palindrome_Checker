def palindrome_checker(word):

    # Convert to lowercase
    word = word.lower()

    # Remove all non-alphanumeric characters
    word = ''.join(c for c in word if c.isalnum())

    # Check if the word is a palindrome
    reverse_word = word[::-1]
    is_palindrome = word == reverse_word

    # Return the appropriate message
    if is_palindrome:
        message = f"{word} is a palindrome!"
    else:
        message = f"{word} is not a palindrome."

    return message
