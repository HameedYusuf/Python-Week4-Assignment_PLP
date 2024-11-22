def read_and_modify_file(filename):
    """Reads a file, modifies its content, and writes it to a new file.

    Args:
        filename (str): The name of the file to read.

    Raises:
        FileNotFoundError: If the file is not found.
        IOError: If there's an error reading or writing the file.
    """

    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (example: add a line)
        modified_content = content + "\nThis line was added."

        with open('modified_' + filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"File '{filename}' modified successfully. New file: 'modified_{filename}'")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"Error reading or writing file: {e}")

# Get filename from user
filename = input("Enter the filename: ")

# Call the function to read, modify, and write the file
read_and_modify_file(filename)
