def modify_content(content, choice):
    """Modify file content based on user selection."""
    if choice == "1":
        return [line.upper() for line in content]  # Convert to uppercase
    elif choice == "2":
        return [line.lower() for line in content]  # Convert to lowercase
    elif choice == "3":
        return [line[::-1] for line in content]  # Reverse text
    elif choice == "4":
        return [line.capitalize() for line in content]  # Capitalize first letter
    elif choice == "5":
        old_word = input("Enter the word to replace: ")
        new_word = input("Enter the new word: ")
        return [line.replace(old_word, new_word) for line in content]  # Replace words
    else:
        print("Invalid choice. No modifications applied.")
        return content

def read_and_modify_file():
    try:
        filename = input("Enter the filename to read: ")

        with open(filename, "r") as file:
            content = file.readlines()

        # User chooses modification type
        print("\nChoose a modification:")
        print("1: Convert text to UPPERCASE")
        print("2: Convert text to lowercase")
        print("3: Reverse text")
        print("4: Capitalize first letter of each line")
        print("5: Find and replace a word")

        choice = input("Enter your choice (1-5): ")
        modified_content = modify_content(content, choice)

        # Save to a new file
        new_filename = f"modified_{filename}"
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"\n✅ Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()