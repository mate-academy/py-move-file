import os


BUFFER_SIZE = 2048
CHARACTER_SEPARATOR = "/"


class FileInfo:
    def __init__(self, file_name: str) -> None:
        self.path = []
        self.full_path = ""
        self.path_only = False
        self.filename = ""
        self.full_filename = ""

        if file_name[-1] == CHARACTER_SEPARATOR:
            self.path = file_name[:-1].split(CHARACTER_SEPARATOR)
            self.full_path = file_name.rstrip(CHARACTER_SEPARATOR)
            self.path_only = True
        else:
            self.full_filename = file_name
            temp = file_name.split(CHARACTER_SEPARATOR)
            self.filename = temp[-1]
            self.path = temp[:-1]
            self.full_path = CHARACTER_SEPARATOR.join(self.path)

    def path_add_filename(self, filename: str) -> str:
        if self.path and self.path_only:
            return CHARACTER_SEPARATOR.join((self.full_path, filename))
        return self.full_filename


def move_file(user_command: str) -> None:
    command = user_command.split()
    if len(command) != 3 or \
            command[0].lower() != "mv" or \
            command[1] == command[2]:
        return

    source = FileInfo(command[1])
    if not os.path.isfile(source.full_filename) \
            or source.path_only is True:
        return

    destination = FileInfo(command[2])
    if source.full_path == destination.full_path:
        os.rename(source.full_filename, destination.full_filename)
    else:
        path_traverse = ""
        for path in destination.path:
            path_traverse += \
                (CHARACTER_SEPARATOR if path_traverse else "") + path
            if not os.path.isdir(path_traverse):
                os.mkdir(path_traverse)

        destination_filename = destination.path_add_filename(source.filename)
        with open(source.full_filename, "rb") as src_obj, \
                open(destination_filename, "wb") as dest_obj:
            buffer = src_obj.read(BUFFER_SIZE)
            while buffer:
                dest_obj.write(buffer)
                buffer = src_obj.read()

        if os.path.isfile(destination_filename):
            os.remove(source.full_filename)


if __name__ == "__main__":
    move_file("mv file1.txt file2.txt")
    input("file2.txt")
    move_file("mv file2.txt file1.txt")
    input("file1.txt")
    move_file("mv file1.txt first_dir/second_dir/third_dir/")
    input("first_dir/second_dir/third_dir/file1.txt")
    move_file("mv first_dir/second_dir/third_dir/file1.txt "
              "first_dir/second_dir/third_dir/file2.txt")
    input("first_dir/second_dir/third_dir/file2.txt")
    move_file("mv first_dir/second_dir/third_dir/file2.txt file1.txt")
    input("file1.txt")
