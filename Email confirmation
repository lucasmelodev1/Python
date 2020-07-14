import re

text="joao@.. jose@gmail. jeremias@gmail.com @gmail. @gmail.com @gmail jeremias@gmail jonathan@ @"
compiler = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
if compiler.search(text):
    print("The correct email is\n ", compiler.search(text))
