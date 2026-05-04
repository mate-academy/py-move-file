import os


def move_file(command: str) -> None:
    if command:
        command_splitted = command.split(" ")
    if len(command_splitted) != 3:
        raise Exception("Command should have 3 arguments")
    comm, from_file, to_file = command_splitted
    if comm != "mv":
        raise Exception("Command should start with 'mv'.")
    if from_file[-1] == "/":
        raise Exception("Doesnt support directories.")

    from_file_path = from_file.split("/")
    from_file_name = from_file_path.pop()
    if to_file[-1] == "/":
        to_file += from_file_name
    to_file_path = to_file.split("/")
    to_file_name = to_file_path.pop()

    try:
        counter = 0
        for directory in from_file_path:
            try:
                os.chdir(directory)
                counter += 1
            except FileNotFoundError:
                raise FileNotFoundError
    except FileNotFoundError:
        print("Directory not found")
        return
    else:
        with open(from_file_name, "r") as from_file:
            copy_data = from_file.read()
        os.remove(from_file_name)
    finally:
        for i in range(counter):
            os.chdir("..")

    counter = 0

    try:
        for directory in to_file_path:
            try:
                os.chdir(directory)
                counter += 1
            except FileNotFoundError:
                os.mkdir(directory)
                os.chdir(directory)
                counter += 1
    except Exception as e:
        print(e)
    else:
        with open(to_file_name, "w") as to_file:
            to_file.write(copy_data)
    finally:
        for i in range(counter):
            os.chdir("..")
