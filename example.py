def once(f):
    called = False

    def inner(*args, **kwargs):
        nonlocal called
        if not called:
            called = True
            res = f(*args, **kwargs)
            assert res is None

    return inner


def init_logger():
    print("Initializing logger")


@once
def foo():
    init_logger()


if __name__ == "__main__":
    foo()
    foo()
