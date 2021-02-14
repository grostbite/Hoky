# Development by wencms@gmail.com (AmazetNT)
# HVM on Python

import sys

content = ""

defs = 0

script = sys.argv[1]

with open(script, 'r') as f:

    for line in f:

        lexer = line.split(" ")

        count = len(lexer)

        if lexer[0] == "output":
            if defs == 2:
                content += "        return " + lexer[1] + "\n"
            else:
                content += "return " + lexer[1] + "\n"

        if lexer[0] == "def":
            if defs == 2:
                content += "    def " + lexer[1].replace("()","(self)") + ""+ lexer[2].replace("{", ":") + "\n"
            else:
                defs = 1
                content += "def " + lexer[1] + "" + lexer[2].replace("{", ":") + "\n"

        if lexer[0] == lexer[0]:
            if lexer[0].find('(') != -1:
                content += lexer[0]
            if lexer[0].find('}') != -1:
                defs = 0
                if defs == 2:
                    content += "    pass"

        if count > 1:
            if lexer[1] == "=":
                string = ""
                for x in range(count):
                    string += lexer[x]+" ";
                if defs == 2:
                    content += "        "+string.replace(";", "")+"\n"
                if defs == 1:
                    content += "    "+string.replace(";", "")+"\n"
                if defs == 0:
                    content += string.replace(";", "") + "\n"

        if lexer[0] == "print":
            if defs == 2:
                content += "        print(" + lexer[1].replace("\n", "") + ")\n"
            if defs == 1:
                content += "    print(" + lexer[1].replace("\n", "") + ")\n"
            if defs == 0:
                content += "print(" + lexer[1].replace("\n", "") + ")\n"

        if lexer[0] == "pclass":
            defs = 2
            content += "class " + lexer[1].replace("\n", "") + ""+ lexer[2].replace("{", ":") + "\n"

        if lexer[0] == "input":
            if defs == 2:
                content += "        " + lexer[1].replace("\n", "") + " = input()\n"
            if defs == 1:
                content += "    " + lexer[1].replace("\n", "") + " = input()\n"
            if defs == 0:
                content += "" + lexer[1].replace("\n", "") + " = input()\n"

        if lexer[0] == "if":
            if defs == 2:
                content += "        if " + lexer[1] + " " + lexer[2] + " " + lexer[3] + ""+ lexer[4].replace("{", ":") + "\n"
            if defs == 1:
                defs = 2
                content += "    if " + lexer[1] + " " + lexer[2] + " " + lexer[3] + ""+ lexer[4].replace("{", ":") + "\n"
            if defs == 0:
                defs = 1
                content += "if " + lexer[1] + " " + lexer[2] + " " + lexer[3] + ""+ lexer[4].replace("{", ":") + "\n"

        if lexer[0] == "for":
            if defs == 2:
                content += "        for " + lexer[5] + " in range(" + lexer[3] + ")"+ lexer[6].replace("{", ":") + "\n"
            if defs == 1:
                defs = 2
                content += "    for " + lexer[5] + " in range(" + lexer[3] + ")"+ lexer[6].replace("{", ":") + "\n"
            else:
                defs = 1
                content += "for " + lexer[5] + " in range(" + lexer[3] + ")"+ lexer[6].replace("{", ":") + "\n"

    file = open("rutime.py", "w")
    file.write(content)
    file.close()

    import rutime