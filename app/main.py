import os


def move_file(command: str) -> None:
    words_of_command = command.split(" ")
    if (len(words_of_command) == 3
        and words_of_command[0] == "mv"
            and words_of_command[1] != words_of_command[2]):
        if words_of_command[2].count("/") == 0:
            os.rename(words_of_command[1], words_of_command[2])
        else:
            create_directory = os.path.split(words_of_command[2])
            if os.path.exists(create_directory[0]) is False:
                os.makedirs(create_directory[0])
            with (open(words_of_command[1], "r") as data_file,
                  open(words_of_command[2], "w") as new_data_file):
                new_data_file.write(data_file.read())
            os.remove(words_of_command[1])
