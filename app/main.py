import os


def move_file(command: str):
    words_of_command = command.split(" ")
    if (len(words_of_command) == 3 and
        words_of_command[0] == "mv" and
        words_of_command[1] != words_of_command[2]):
        if words_of_command[2].count("/") == 0:
            os.rename(words_of_command[1], words_of_command[2])
        else:
            create_directory = words_of_command[2].split("/")
            new_directory = create_directory[0]
            for i in range(len(create_directory) - 1):
                if os.path.exists(new_directory) is False:
                    os.mkdir(new_directory)
                new_directory += f"/{create_directory[i + 1]}"
            with (open(words_of_command[1], "r") as data_file,
                  open(words_of_command[2], "w") as new_data_file):
                new_data_file.write(data_file.read())
            os.remove(words_of_command[1])
