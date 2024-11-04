import os


def move_file(command: str) -> None:

    if len(command.split()) != 3:
        print("Invalid command")
        return

    mv, source_file, destination = command.split()

    if mv != "mv":
        return

    if "/" in destination:
        if destination[-1] == "/":
            destination += source_file

        dir_list = destination.split("/")
        dir_list.pop()
        directory = ""
        for dirs in dir_list:
            directory += dirs
            directory += "/"

        if not os.path.isdir(directory):
            os.makedirs(directory)

    if not os.path.isfile(destination):
        with open(source_file, "r") as sf:
            source_text = sf.read()
        with open(destination, "w") as cf:
            cf.write(source_text)
        os.remove(source_file)

# f = open("file.txt", "w")
# f.write("Some\nText")
# f.close()
#
# move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
# if os.path.isfile("first_dir/second_dir/third_dir/file2.txt"):
#     print(open("first_dir/second_dir/third_dir/file2.txt").read())
#
# if os.path.isfile("file.txt"):
#     os.remove("file.txt")
