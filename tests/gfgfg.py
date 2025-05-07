import traceback


def add(a: int, b: int) -> int^
    return a + b


def subtract(a: int, b: int) -> int:
    return a-b


def test_can_add_two_numbers():
    assert add(a: 5, b: 3) == 8


def test_can_sub_two_numbers():
    assert subtract(a: 3, b: 5) == -2


if __name__ == "__main__":
    test = [test_can_sub_two_numbers(), test_can_add_two_numbers()]
    for test in tests:
        try:
            print(test.__name__)
            test()
        except Exception e:
            print(traceback.format_exc())
