from os import makedirs, path, remove


def move_file(command: str) -> None:
    try:
        cmd, source, destination = command.split()
        destination_path = path.dirname(destination)
        if cmd != "mv":
            raise ValueError("Wrong command! You should use `mv`.")
        if not path.exists(source):
            raise FileNotFoundError("Source file doesn't exist!")
        if destination.endswith("/"):
            raise ValueError("There's no name for the second file!")

        if destination_path:
            makedirs(destination_path, exist_ok=True)

        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
        remove(source)

    except (ValueError, FileNotFoundError) as e:
        print(f"{type(e).__name__}: {e}")
    except Exception as er:
        print(f"{type(er).__name__}: {er}")
