import os


def move_file(command: str) -> None:
    try:
        command, source_path, destination_path = command.split()
    except ValueError:
        print("Wrong command format")
    else:
        if command == "mv" and source_path != destination_path:
            if os.path.split(destination_path)[0]:
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)

            try:
                with (
                    open(source_path) as source,
                    open(destination_path, "w") as destination
                ):
                    destination.write(source.read())

                os.remove(source_path)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
