


def load(name: str) -> str:
    _file = open(f"./res/stylesheets/{name}.qss", "r")

    data = _file.read()

    _file.close()

    return data