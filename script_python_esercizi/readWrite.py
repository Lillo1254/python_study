""" with open("test_python.txt", "w") as file:
    file.write("test prova di scrittura file nuovo \n")
    file.write("seconda riga di test per scrittura su file nuovo\n") """

""" with open("test_python.txt", "r") as file:
    contenuto_file = file.read()
    print(contenuto_file) """

with open("test_python.txt" , "a") as file:
    file.write("terza riga di test per scrittura su file nuovo con append \n")