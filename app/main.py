import shutil
import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Invalid move command")
    elif len(parts[2].split("/")) == 2:
        source_file = parts[1]
        destination_file = parts[2].split("/")[1]
        destination_folder = parts[2].split("/")[0]
        shutil.move(
            source_file, f"C:\\Olexandr\\py-move-file\\"
                         f"tests\\{destination_folder}\\"
                         f"{destination_file}"
        )
    elif len(parts[2].split("/")) == 3:
        source_file = parts[1]
        destination_file = parts[2].split("/")[2]
        destination_folder1 = parts[2].split("/")[0]
        destination_folder2 = parts[2].split("/")[1]
        destination_folder = f"{destination_folder1}\\{destination_folder2}"
        os.makedirs(destination_folder)
        shutil.move(
            source_file, f"C:\\Olexandr\\py-move-file\\tests\\"
                         f"{destination_folder}\\{destination_file}"
        )
    elif len(parts[2].split("/")) == 4:
        source_file = parts[1]
        destination_file = parts[2].split("/")[3]
        destination_folder1 = parts[2].split("/")[0]
        destination_folder2 = parts[2].split("/")[1]
        destination_folder3 = parts[2].split("/")[2]
        destination_folder4 = (
            f"{destination_folder1}\\"
            f"{destination_folder2}\\"
            f"{destination_folder3}"
        )
        os.makedirs(destination_folder4)
        shutil.move(
            source_file, f"C:\\Olexandr\\py-move-file\\tests\\"
                         f"{destination_folder4}\\"
                         f"{destination_file}"
        )
    else:
        source_file = parts[1]
        destination_file = parts[2]
        shutil.move(source_file, destination_file)
