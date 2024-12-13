import os


def move_file(command: str) -> None:
    try:
        cmd, source_file, final_file = command.split()
    except ValueError:
        print(f"Invalid command: {command}")
        return

    if cmd == "mv" and source_file != final_file:

        with open(source_file) as source:
            data = source.read()

        final_path, fin_file_name = os.path.split(final_file)

        if final_path:
            os.makedirs(final_path, exist_ok=True)

        with (
            open(final_file, "w") as target_file,
            open(source_file) as source
        ):
            data = source.read()
            target_file.write(data)

        os.remove(source_file)
