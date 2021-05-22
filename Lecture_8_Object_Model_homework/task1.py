import builtins


class KeyValueStorage:
    d = {}

    def __init__(self, filename: str):
        with open(filename) as pairs:
            for pair in pairs:
                pair = pair.strip("\n")
                key, value = pair.split("=")
                try:
                    self.d[key] = int(value)
                except ValueError:
                    self.d[key] = value
                if key.isidentifier():
                    if key not in dir(builtins):
                        setattr(self, key, self.d[key])
                else:
                    raise ValueError(f"{key} is incorrect identifier!")

    def __setitem__(self, key, item):
        self.d[key] = item

    def __getitem__(self, item):
        return self.d[item]

