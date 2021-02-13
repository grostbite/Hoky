import sys

content = ""

script = sys.argv[1]

with open(script, 'r') as f:

    for line in f:

        lexer = line.split(" ")

        count = len(lexer)

        if lexer[1] == "=":
            string = ""
            for x in range(count):
                string += lexer[x]+" ";

            content += string.replace(";", "")+"\n"

        if lexer[0] == "print":
            content += "print(" + lexer[1].replace(";", "") + ")\n"

    file = open("rutime.py", "w")
    file.write(content)
    file.close()

    import rutime