import os


def move_file(command: str) -> None:
    list_of_command = command.split(" ")
    if len(list_of_command) == 3:
        if os.path.dirname(list_of_command[2]) != "":
            os.makedirs(os.path.dirname(list_of_command[2]), exist_ok=True)
            try:
                with open(list_of_command[2], "w",
                          encoding="utf-8") as file_to:
                    with open(list_of_command[1], "r",
                              encoding="utf-8") as file_from:
                        file_to.write(file_from.read())
            except FileNotFoundError as e:
                print(f"Файл не найден: {e}")
            except IOError as e:
                print(f"Ошибка ввода-вывода: {e}")
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        else:
            try:
                with open(list_of_command[2], "w",
                          encoding="utf-8") as file_to:
                    with open(list_of_command[1], "r",
                              encoding="utf-8") as file_from:
                        file_to.write(file_from.read())
            except FileNotFoundError as e:
                print(f"Файл не найден: {e}")
            except IOError as e:
                print(f"Ошибка ввода-вывода: {e}")
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        try:
            os.remove(list_of_command[1])
        except FileNotFoundError as e:
            print(f"Файл не найден: {e}")
        except IOError as e:
            print(f"Ошибка ввода-вывода: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
