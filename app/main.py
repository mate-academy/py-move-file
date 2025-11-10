import os


def move_file(command: str) -> None:
    split_command = command.split(" ")

    if len(split_command) != 3:
        print("Invalid command")
        return

    first_word, source_file_name, destination_file_path = split_command

    if first_word != "mv":
        print("Invalid command")
        return

    if source_file_name == destination_file_path:
        print("Source and destination file cannot be the same")
        return

    if destination_file_path.endswith("/"):
        destination_file_path = os.path.join(
            destination_file_path, os.path.basename(source_file_name)
        )

    try:
        os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
    except PermissionError:
        print(f"Permission denied: "
              f"Unable to create '{destination_file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with (open(source_file_name, "r") as source_file_object,
              open(destination_file_path, "w") as destination_file_object):
            for line in source_file_object:
                destination_file_object.write(line)
        os.remove(source_file_name)
    except FileNotFoundError:
        print("Source file not found")
        return
