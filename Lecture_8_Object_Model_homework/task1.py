import builtins


class KeyValueStorage:
    d = {}

    def __init__(self, filename: str):
        with open(filename) as pairs:
            for pair in pairs:
                key, value = pair.split("=")
                self.d[key] = value
                if key.isidentifier():
                    if key not in dir(builtins):
                        setattr(self, key, value)
                else:
                    raise ValueError(f"{key} is incorrect identifier!")

    def __setitem__(self, key, item):
        self.d[key] = item

    def __getitem__(self, item):
        if isinstance(self.d[item], int):
            return int(self.d[item])
        return self.d[item]


if __name__ == '__main__':
    storage = KeyValueStorage('task1.txt')
    print(storage['name'])  # will be string 'kek'
    print(storage.song)   # will be 'shadilay'
    print(storage.power)  # will be integer 9001
