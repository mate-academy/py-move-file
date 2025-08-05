import os


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) < 3:
        print("Error: can't work with that command")
        return
    if commands[0] != "mv":
        print(f"Error: '{commands[0]}' should be 'mv'")
        return
    source_file = commands[1]
    if not os.path.exists(source_file):
        print(f"Error: file with name '{source_file}' does not exist")
        return
    path = "/".join(commands[2].split("/")[0:-1])
    if path != "":
        try:
            os.makedirs(path)
            print(f"Directory '{path}' created successfully.")
        except FileExistsError:
            print(f"Directory '{path}' already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")

    try:
        with open(commands[2], "w") as file, open(source_file, "r") as source:
            file.write(source.read())
        os.remove(source_file)
    except FileNotFoundError:
        print("Error: source file was not found during file operations.")
    except PermissionError:
        print("Error: insufficient permissions to read/write/delete the file.")
    except Exception as e:
        print(f"Error during file operation: {e}")
