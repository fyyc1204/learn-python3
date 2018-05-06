from configparser import ConfigParser

parser=ConfigParser()

parser.read('D:\project\learn-python3\MachineLearn\database.ini')

db = {}
if parser.has_section('postgresql'):
    params = parser.items('postgresql')
    for param in params:
        db[param[0]] = param[1]
else:
    print("error")

print(db)

