def modify_content(content, choice, old_word=None, new_word=None):
    """Modify file content based on user selection."""
    if choice == "1":
        return [line.upper() for line in content]  # Convert to uppercase
    elif choice == "2":
        return [line.lower() for line in content]  # Convert to lowercase
    elif choice == "3":
        return [line[::-1] for line in content]  # Reverse text
    elif choice == "4":
        return [line.capitalize() for line in content]  # Capitalize first letter
    elif choice == "5" and old_word is not None and new_word is not None:
        return [line.replace(old_word, new_word) for line in content]  # Replace words
    else:
        print("Invalid choice. No modifications applied.")
        return content

def read_and_modify_file():
    filename = input("Enter the filename to read: ").strip()

    try:
        with open(filename, "r") as file:
            content = file.readlines()

        if not content:
            print("❌ Error: The file is empty. Nothing to modify.")
            return

        # User chooses modification type
        print("\nChoose a modification:")
        options = {
            "1": "Convert text to UPPERCASE",
            "2": "Convert text to lowercase",
            "3": "Reverse text",
            "4": "Capitalize first letter of each line",
            "5": "Find and replace a word"
        }
        for key, value in options.items():
            print(f"{key}: {value}")

        choice = input("Enter your choice (1-5) or 'q' to quit: ").strip()

        if choice.lower() == 'q':
            print("Operation canceled.")
            return

        old_word, new_word = None, None
        if choice == "5":
            old_word = input("Enter the word to replace: ").strip()
            new_word = input("Enter the new word: ").strip()

        modified_content = modify_content(content, choice, old_word, new_word)

        # Debug: Check if modifications are applied
        print("\n🔍 Debug: Modified Content Preview:")
        print("".join(modified_content))  # Prints output before saving

        if not modified_content:
            print("❌ Error: Modification resulted in empty content. No changes saved.")
            return

        # Ensure new lines are retained
        modified_content = [line if line.endswith('\n') else line + '\n' for line in modified_content]

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
if __name__ == "__main__":
    read_and_modify_file()
