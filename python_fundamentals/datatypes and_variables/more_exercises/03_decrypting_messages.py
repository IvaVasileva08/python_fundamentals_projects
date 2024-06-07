key = int(input())
n = int(input())
characters = []
for _ in range(n):
    char = input()
    characters.append(char)
message = ""
for char in characters:
    new_char = chr(ord(char) + key)
    message += new_char
print(message)
