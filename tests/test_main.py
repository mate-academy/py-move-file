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
