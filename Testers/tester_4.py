import os
[('Resources', 'Resources'), ('DataBase', 'DataBase')],
for var in os.environ:
    print(var , ' = ', os.environ[var])