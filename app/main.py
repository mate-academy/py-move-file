from pathlib import Path
import os


def move_file(command: str) -> None:
    text = command.split(" ")
    error = "Invalid file name"
    if len(text) != 3:
        print(error)
        return
    if text[0] != "mv":
        print(error)
        return

    file_in = text[1]
    file_out = text[2]
    file_path = Path(file_in)
    if not file_path.exists():
        print(f"The file {file_in} does not exist!!!")
        return

    stroka2 = file_out.split("/")
    print(stroka2)
    quantity_folders = len(stroka2) - 1
    number_folder = 0
    folder = ""
    if quantity_folders > 0:
        for _ in range(quantity_folders):
            folder += stroka2[number_folder]
            if not Path(folder).exists() or not Path(folder).is_dir():
                os.makedirs(folder, exist_ok=True)
            folder += "/"
            number_folder += 1

    with open(file_in, "rb") as file1, open(file_out, "wb") as file2:
        lines = file1.readlines()
        file2.writelines(lines)
    os.remove(file_in)
    print(f"File {file_in} moved in {file_out} successfully!")
