FILEPATH = "todos.txt"

def get_ToDos(filePath=FILEPATH):
    """ Devuelve una lista con todos los que haceres pendientes"""
    with open(filePath, "r") as fileLocal:
        ToDosLocal = fileLocal.readlines()
    return ToDosLocal
# print(help(get_ToDos))

def post_ToDos(ToDosLocal, filePath=FILEPATH):
    """ guarda la lista en un archivo de texto"""
    with open(filePath, "w") as file:
        file.writelines(ToDosLocal)

print(__name__)

if __name__ == "__main__":
    print("hello form functions")
    print(get_ToDos("../todos.txt"))
