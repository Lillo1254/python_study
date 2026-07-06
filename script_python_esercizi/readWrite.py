""" with open("test_python.txt", "w") as file:
    file.write("test prova di scrittura file nuovo \n")
    file.write("seconda riga di test per scrittura su file nuovo") """

with open("test_python.txt", "r") as file:
    contenuto_file = file.read()
    print(contenuto_file)