import os


def move_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) != 3 or split_command[0] != "mv":
        print("Invalid command")
        return

    file_to_move = split_command[1]
    new_file_name = split_command[2]

    if file_to_move == new_file_name:
        print("Source and destination file names are the same.")
        return

    new_file_dir = os.path.dirname(new_file_name)
    if new_file_dir:
        if os.path.isfile(new_file_dir):
            print(f"Error: A file with the name '"
                  f"{new_file_dir}' already exists.")
            return
        try:
            os.makedirs(new_file_dir, exist_ok=True)
        except Exception as e:
            print(f"An error occurred while creating directory '"
                  f"{new_file_dir}': {e}")
            return

    try:
        os.rename(file_to_move, new_file_name)
        print(f"Moved {file_to_move} to {new_file_name}")
    except FileNotFoundError:
        print(f"File {file_to_move} not found.")
    except FileExistsError:
        print(f"File {new_file_name} already exists.")
    except PermissionError:
        print(f"Permission denied while accessing "
              f"{file_to_move} or {new_file_name}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
