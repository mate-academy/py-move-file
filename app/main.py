import os


def move_file(command: str) -> None:
    parts = command.split()
    source_path = parts[1]
    destination_path = parts[2]
    if destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        dst_file = os.path.join(
            destination_path, os.path.basename(source_path)
        )
    else:
        dst_file = destination_path
    os.replace(source_path, dst_file)


with open("file.txt", "w") as source:
    source.write("Some\nText\n")
move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
with open("first_dir/second_dir/third_dir/file2.txt", "r") as new_files:
    print(new_files.read())
os.remove("first_dir/second_dir/third_dir/file2.txt")
