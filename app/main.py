import os


def move_file(command: str) -> None:
    command_list = command.split()
    first_file = command_list[1]
    if "/" in command:
        file_path = "/".join(command_list[-1].split("/")[:-1])
        os.makedirs(file_path, exist_ok=True)
        destination_file = f"{file_path}/{command_list[-1].split("/")[-1]}"
        try:
            with (open(destination_file, "w") as f, open(
                    first_file, "r") as src_file):
                f.write(src_file.read())
            os.remove(first_file)
        except FileNotFoundError:
            print(f"Error: File {first_file} not found.")
        except OSError as e:
            print(f"Error while working with files: {e}")
    else:
        second_file = command_list[2]
        try:
            os.rename(first_file, second_file)
        except FileNotFoundError:
            print(f"Error: File {first_file} not found.")
        except OSError as e:
            print(f"Error while working with files: {e}")
