import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Invalid move command")
    elif len(parts[2].split("/")) >= 3:
        source_file = parts[1]
        n_split = len(parts[2].split("/"))
        destination_file = parts[2].split("/")[n_split - 1]
        destination_folder = ""

        for destination_fol in range(n_split - 1):
            if destination_folder == "":
                destination_folder = parts[2].split("/")[destination_fol]
            else:
                destination_folder = (
                    destination_folder
                    + "\\"
                    + parts[2].split("/")[destination_fol]
                )
        os.makedirs(destination_folder, exist_ok=True)
        source_file1 = f"C:\\Olexandr\\py-move-file\\tests\\{source_file}"

        shutil.move(
            source_file1,
            os.path.join(
                "C:\\Olexandr\\py-move-file\\tests",
                destination_folder,
                destination_file
            )
        )

    else:
        source_file = parts[1]
        destination_file = parts[2]
        shutil.move(source_file, destination_file)
