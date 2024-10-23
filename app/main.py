import os
import shutil


def move_file(command: str) -> None:
    parts: list[str] = command.split(" ")
    if parts[0] == "mv" and len(parts) == 3:
        source_file: str = parts[1]
        destination: str = parts[2]

        if not os.path.exists(source_file):
            raise FileNotFoundError(f"The source file {source_file} "
                                    f"does not exist.")

        if destination.endswith("/"):
            if not os.path.exists(destination):
                os.makedirs(destination, exist_ok=True)
            destination = os.path.join(destination,
                                       os.path.basename(source_file))
        else:
            destination_dir: str = os.path.dirname(destination)
            if destination_dir:
                os.makedirs(destination_dir, exist_ok=True)

        shutil.move(source_file, destination)
