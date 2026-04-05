import os


def move_file(command: str) -> None:
    input_tokens = command.split()

    if len(input_tokens) != 3:
        return

    command_name, source, destination = input_tokens

    if command_name != "mv":
        return

    # получили путь файла
    input_file_path = os.path.dirname(source)
    # получили имя файла
    input_file_name = os.path.basename(source)

    if not input_file_path:
        print("Входящий файл в корне")
    else:
        print("Входящий файл лежит в: ", input_file_path)

    print("Имя входящего файла: ", input_file_name)

    # если нет такого пути и нет файла по такому пути - стопать программу
    if not os.path.exists(source) and not os.path.isfile(source):
        print("Не вижу файл")
        return

    content = None

    with open(source, "rb") as file:
        content = file.read()



    out_file_path = os.path.dirname(destination)
    out_file_name = os.path.basename(destination)
    print("Путь для исходящего файла", out_file_path)
    print("Имя исходящего файла", out_file_name)

    # если имя файла в третем параметре не указано, беру имя фиайла из второго параметра
    if not out_file_name:
        out_file_name = input_file_name

    print("Новый файл будет засунут в: ", out_file_path)
    print("Есть папки куда пихать новый файл: ", os.path.exists(out_file_path))

    # если нет папки которая указана в третем параметре то создаю папки
    if out_file_path and not os.path.exists(out_file_path):
        os.makedirs(out_file_path, exist_ok=True)

    # создаю то, что попадет в метод создания исходязего файла
    if out_file_path == "/":
        out_file_path = ""
    out = os.path.join(out_file_path, out_file_name)
    print("В метод по созданию файла попадет: ", out)


    with open(out, "wb") as file:
        file.write(content)

    os.remove(source)

move_file("mv my_copy_file.txt /copy.txt")
