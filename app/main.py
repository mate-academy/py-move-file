import os


def move_file(command: str) -> None:
    command_name, source, destination, *_ = command.split()

    if command_name != "mv":
        return
    try:
        if not os.path.exists(source):
            raise FileNotFoundError(
                f"The source file {source} does not exist."
            )

        destination_dir = os.path.dirname(destination)
        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        os.replace(source, destination)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")
