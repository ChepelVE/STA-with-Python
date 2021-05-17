import sqlite3


class TableData:

    def __init__(self, database_name=None, table_name=None):
        self.database_name = database_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()
        # self.row = self.cursor.execute(f'SELECT * from {self.table_name} order by name asc limit 1').fetchone()
        self.name = "0"

    def __len__(self):
        return self.cursor.execute(f'SELECT count(*) FROM {self.table_name}').fetchone()[0]

    def __iter__(self):
        return self

    def __next__(self):
        self.row = self.cursor.execute(f"SELECT * from presidents where name > '{self.name}' order by name limit 1") \
            .fetchone()
        if self.row is not None:
            self.name = self.row[0]
            return dict(zip(['name', 'code', 'country'], self.row))
        raise StopIteration

    def __contains__(self, item):
        return self.cursor.execute(f"SELECT * FROM {self.table_name} where name='{item}'").fetchone() is not None

    def __getitem__(self, item):
        return self.cursor.execute(f"SELECT * FROM {self.table_name} where name='{item}'").fetchone()


if __name__ == '__main__':
    presidents = TableData(database_name='example.sqlite', table_name='presidents')
    print(len(presidents))
    print(presidents['Yeltsin'])
    print('Yeltsin' in presidents)
    for president in presidents:
        print(president['name'])
