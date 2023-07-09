import os


def move_file(command: str) -> None:
    conditions = command.split()
    source_file = conditions[1]
    final_file = conditions[2]
    final_file_directories = final_file.split("/")[:-1]

    if len(final_file_directories) > 0:
        os.makedirs("/".join(final_file_directories), exist_ok=True)
    with (
        open(source_file, "r") as start_file,
        open(final_file, "w") as final_file
    ):
        final_file.write(start_file.read())
    os.remove(source_file)
