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
    files = destination_file.split("/")
    dir_files = files[:-1]

    mk_directory = ""
    for directory in dir_files:
        if len(mk_directory) == 0:
            mk_directory += directory
            os.mkdir(mk_directory)
        else:
            mk_directory += "/" + directory
            os.mkdir(mk_directory)

    if mode == "mv":
        os.rename(source_file, destination_file)
    else:
        raise ValueError(f"Invalid mode: {mode}")
