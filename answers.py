# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

file = open("wk_4_python-Assignment/readonly.txt", "r")
data = file.read()
print(data)

file = open("modified.txt", "w")
data = file.write("Hello World, I enjoy coding")

print(data)

# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError: 
    print("File not found. Please check the filename.")
finally:
    file.close()