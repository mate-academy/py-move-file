import os


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3:
        raise ValueError("Неправильний формат команди."
                         " Використовуйте: mv <input_path> <output_path>")
    action, file_in_path, file_out_path = commands
    if action != "mv":
        raise ValueError("Помилка: Команда повинна бути 'mv'.")

    if file_in_path == file_out_path:
        raise ValueError("Помилка: Вхідний та вихідний файли "
                         "не можуть бути однаковими.")

    try:
        if "/" not in file_out_path:
            if os.path.exists(file_out_path):
                os.remove(file_out_path)
            os.rename(file_in_path, file_out_path)
        else:
            file_out_list = file_out_path.split("/")
            file_out_list.pop()
            file_out_direct = "/".join(
                file_out_list
            )
            if not os.path.exists(file_out_direct):
                os.makedirs(file_out_direct, exist_ok=True)
            with (open(file_in_path, "rb") as file_in,
                  open(file_out_path, "wb") as file_out):
                file_out.write(file_in.read())
            os.remove(file_in_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{file_in_path}' не знайдено.")
