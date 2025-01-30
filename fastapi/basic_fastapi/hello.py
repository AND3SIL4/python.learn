import tomllib


def load() -> dict:
    with open("pyproject.toml", "rb") as f:
        tom_data: dict = tomllib.load(f)
        return tom_data


data: dict = load()
print(data["project"]["name"])
