import os

def move_file(command: str) -> None:
    # Split the command string into its components
    parts = command.split()

    # Check if the command is formatted correctly
    if len(parts) != 3 or parts[0] != 'mv':
        print("Invalid command format. Please use 'mv source_file destination_path'.")
        return

    source_file, destination_path = parts[1], parts[2]

    # Check if the destination path ends with '/'
    if destination_path.endswith('/'):
        # If it does, consider it as a directory
        destination_file = os.path.join(destination_path, os.path.basename(source_file))
    else:
        destination_file = destination_path

    # Create the parent directories if they don't exist
    destination_directory = os.path.dirname(destination_file)
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory, exist_ok=True)

    # Move the file
    os.rename(source_file, destination_file)

    print(f"File '{source_file}' moved to '{destination_file}' successfully.")
import os
import shutil

import pytest

from app.main import move_file


@pytest.fixture
def create_file(filename: str = "file.txt") -> str:
    content = "This is some\n content for\n the file."

    with open(filename, "w") as created_file:
        created_file.write(content)

    return filename


def test_file_renamed(create_file: callable) -> None:
    move_file("mv file.txt file1.txt")

    assert os.path.exists("file.txt") is False
    with open("file1.txt", "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    os.remove("file1.txt")


def test_should_work_when_directory_exists(create_file: callable) -> None:
    os.makedirs("dir")
    move_file(f"mv file.txt dir/file2.txt")

    with open("dir/file2.txt", "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    assert os.path.exists("file.txt") is False

    shutil.rmtree("dir")


def test_should_create_multiple_directories(create_file: callable) -> None:
    move_file(f"mv file.txt first_dir/second_dir/file2.txt")

    assert os.path.exists("first_dir/second_dir/file2.txt") is True
    assert os.path.exists("file.txt") is False

    with open("first_dir/second_dir/file2.txt", "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    shutil.rmtree("first_dir")


def test_should_create_multiple_directories_when_they_exist(create_file: callable) -> None:
    os.makedirs("first_dir/second_dir")
    move_file(f"mv file.txt first_dir/second_dir/third_dir/file2.txt")

    with open("first_dir/second_dir/third_dir/file2.txt", "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    assert os.path.exists("file.txt") is False

    shutil.rmtree("first_dir")