import os


def move_file(command: str) -> None:
    lcommand = command.split()

    if len(lcommand) != 3 or lcommand[0] != "mv":
        raise ValueError(
            "Invalid command format! Use: mv <source_file> <destination_path>"
        )

    _, source_file, destination_file = lcommand

    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"File {source_file} does not exist!")

    destination_file_dir = os.path.dirname(destination_file)
    if destination_file_dir:
        os.makedirs(destination_file_dir, exist_ok=True)

    with open(source_file, "r") as src_file:
        with open(destination_file, "w") as dst_file:
            dst_file.write(src_file.read())

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
