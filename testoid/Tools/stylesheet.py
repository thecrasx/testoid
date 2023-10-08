


def load(name: str) -> str:
    _file = open(f"./assets/stylesheets/{name}.qss", "r")

    data = _file.read()

    _file.close()

    return data