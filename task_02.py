from collections import deque

def is_palindrome(string_input: str) -> bool:
    string_input = string_input.lower()
    string_input = ''.join(e for e in string_input if e.isalnum())
    queue = deque()
    for char in string_input:
        queue.append(char)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True



def main():
    string_input = input("Enter a string: ")
    if is_palindrome(string_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()