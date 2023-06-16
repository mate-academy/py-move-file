import os


def move_file(command: str) -> None:
    words = command.split()
    if len(words) != 3:
        raise ValueError(
            "Invalid command. "
            "Expected three parts: mode, source file, destination file."
        )
    mode = words[0]
    source_file = words[1]
    destination_file = words[2]
    if mode == "mv":
        destination_dir = os.path.dirname(destination_file)
        os.makedirs(destination_dir, exist_ok=True)
        os.remove(source_file)
    else:
        raise ValueError(f"Invalid mode: {mode}")
