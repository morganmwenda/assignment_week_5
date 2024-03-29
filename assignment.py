def create_and_modify_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Hello, this is line 1.\n")
            file.write("12345 is a number.\n")
            file.write("This is the third line.\n")
        print("File 'my_file.txt' created successfully.")

        # Read the contents of "my_file.txt" and display them on the console
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nContents of 'my_file.txt':\n")
            print(content)

        # Modify the script to open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("\nAppending line 1.\n")
            file.write("Appending line 2.\n")
            file.write("Appending line 3.\n")
        print("\nFile 'my_file.txt' modified successfully.")

    except FileNotFoundError:
        print("Error: File 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied. Check file permissions.")
    finally:
        print("\nFile handling completed.")

# Call the function to create, read, and modify the file
create_and_modify_file()