class Stack:
  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if len(self.stack) < 1:
      return None
    return self.stack.pop()

  def is_empty(self):
    return len(self.stack) == 0

  def peek(self):
    if not self.is_empty():
      return self.stack[-1]

def is_balanced(string: str) -> bool:
    stack = Stack()
    for char in string:
        if char in ['(', '{', '[']:
            stack.push(char)
        else:
            if stack.is_empty() and char in [')', '}', ']']:
                return False
            if char == ')' and stack.peek() == '(':
                stack.pop()
            elif char == '}' and stack.peek() == '{':
                stack.pop()
            elif char == ']' and stack.peek() == '[':
                stack.pop()
            else:
                continue
    return stack.is_empty()

def main():
    string = input("Enter a string: ")
    if is_balanced(string):
        print("The string is balanced.")
    else:
        print("The string is not balanced.")

if __name__ == "__main__":
    main()