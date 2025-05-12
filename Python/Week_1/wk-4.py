def modify_and_write_file(input_filename, output_filename, modification_func):
    try:
        with open(input_filename, 'r') as infile:
            with open(output_filename, 'w') as outfile:
                for line in infile:
                    modified_line = modification_func(line)
                    outfile.write(modified_line)

        print(f"Successfully read from '{input_filename}', modified content,")
        print(f"and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        print(f"Error reading or writing file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example modification function: Convert line to uppercase and add a prefix
def uppercase_and_prefix(line):
    
    return "MODIFIED: " + line.upper()
input_file = 'input.txt'
output_file = 'output_modified.txt'

# Run the file modification program
print("--- Running File Read, Modify, Write Program ---")
modify_and_write_file(input_file, output_file, uppercase_and_prefix)
print("-" * 40) # Separator


# --- Program 2: Error Handling Lab (File Existence and Readability) ---

def read_file_with_error_handling():
    while True: # Loop to allow retries if input is invalid
        filename = input("Enter the name of the file you want to read: ")

        try:
            # Attempt to open and read the file
            with open(filename, 'r') as f:
                content = f.read()
                print(f"\n--- Content of '{filename}' ---")
                print(content)
                print("------------------------------")
            break # Exit the loop if file reading was successful

        except FileNotFoundError:
            # Handle the case where the file does not exist
            print(f"Error: The file '{filename}' was not found.")
            print("Please check the filename and try again.")
        except IOError as e:
            # Handle other potential input/output errors (e.g., permission issues)
            print(f"Error reading file '{filename}': {e}")
            print("Please check file permissions or if the file is accessible.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

# --- How to use Program 2 ---
print("--- Running Error Handling Lab ---")
read_file_with_error_handling()
print("-" * 40) # Separator
