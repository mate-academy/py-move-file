import os


def move_file(command):
    main_command, old_file, new_file = command.split()
    if not os.path.exists(old_file):
        with open(old_file, "w") as f:
            f.write("Hello")
    if main_command != "mv" or old_file == new_file:
        exit()
    if len(new_file.split("/")) == 1:
        with open(old_file, "r") as file_read:
            with open(new_file, "w") as file_write:
                file_write.writelines(file_read.readlines())
    else:
        path_list = new_file.split("/")[:-1]
        new_path = ""
        for item in path_list:
            new_path += item
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            new_path += "/"
        with open(old_file, "r") as file_read:
            with open(new_file, "w") as file_write:
                file_write.writelines(file_read.readlines())
    os.remove(old_file)


if __name__ == "__main__":
    move_file(input("Enter command: "))
