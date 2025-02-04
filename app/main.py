import os


def move_file(command: str) -> None:
    try:
        command_mv, source, target_path = command.split(" ")
    except Exception:
        raise ValueError(
            "Must be 3 elements: mv <source_file> <path_to_destination_file>")
    else:
        if not command_mv == "mv":
            raise Exception("'Invalid command, expected 'mv'.")

        target_dict = target_path.split("/")
        current_path = ""
        if len(target_dict) > 0:
            for index in range(len(target_dict) - 1):
                current_path = os.path.join(current_path, target_dict[index])
                os.makedirs(f"{current_path}", exist_ok=True)

        with open(source, "r") as input, open(target_path, "w") as output:
            output.write(input.read())
        os.remove(source)
