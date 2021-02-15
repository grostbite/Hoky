# Development by wencms@gmail.com (AmazetNT)
# HVM on Python

import sys

__script__ = sys.argv[1]

def hk_lexer(__script__):

    comnd = "output|def|print|pclass|input|if|for".split("|")

    pycmnd = "return|def|print|class|input()|if|for".split("|")

    content = ""

    defs = 0

    with open(__script__, 'r') as f:

        for line in f:

            lexer = line.split(" ")

            count = len(lexer)

            if lexer[0] == comnd[0]:
                if defs == 5:
                    content += "                    "+pycmnd[0]+" " + lexer[1] + "\n"
                if defs == 4:
                    content += "                "+pycmnd[0]+" " + lexer[1] + "\n"
                if defs == 3:
                    content += "            "+pycmnd[0]+" " + lexer[1] + "\n"
                if defs == 2:
                    content += "        "+pycmnd[0]+" " + lexer[1] + "\n"
                if defs == 1:
                    content += "    "+pycmnd[0]+" " + lexer[1] + "\n"
                if defs == 0:
                    content += pycmnd[0]+" " + lexer[1] + "\n"

            if lexer[0] == comnd[1]:
                if defs == 5:
                    content += "                    "+pycmnd[1]+" " + lexer[1].replace("()","(self)") + ""+ lexer[2].replace("{", ":") + "\n"
                if defs == 4:
                    defs = 5
                    content += "                "+pycmnd[1]+" " + lexer[1].replace("()","(self)") + ""+ lexer[2].replace("{", ":") + "\n"
                if defs == 3:
                    defs = 4
                    content += "            "+pycmnd[1]+" " + lexer[1].replace("()","(self)") + ""+ lexer[2].replace("{", ":") + "\n"
                if defs == 2:
                    defs =3
                    content += "        "+pycmnd[1]+" " + lexer[1].replace("()","(self)") + ""+ lexer[2].replace("{", ":") + "\n"
                if defs == 1:
                    defs = 2
                    content += "    "+pycmnd[1]+" " + lexer[1].replace("()","(self)") + ""+ lexer[2].replace("{", ":") + "\n"
                if defs == 0:
                    defs = 1
                    content += pycmnd[1]+" " + lexer[1] + "" + lexer[2].replace("{", ":") + "\n"

            if lexer[0] == lexer[0]:
                if lexer[0].find('(') != -1:
                    content += lexer[0]
                if lexer[0].find('}') != -1:
                    if defs == 0:
                        defs = 0
                    if defs == 1:
                        defs = 0
                    if defs == 2:
                        defs = 1
                    if defs == 3:
                        defs = 2
                    if defs == 4:
                        defs = 3
                    if defs == 5:
                        defs = 4

            if count > 1:
                if lexer[1] == "=":
                    string = ""
                    for x in range(count):
                        string += lexer[x]+" ";
                    if defs == 5:
                        content += "                    "+string.replace(";", "")+"\n"
                    if defs == 4:
                        content += "                "+string.replace(";", "")+"\n"
                    if defs == 3:
                        content += "            "+string.replace(";", "")+"\n"
                    if defs == 2:
                        content += "        "+string.replace(";", "")+"\n"
                    if defs == 1:
                        content += "    "+string.replace(";", "")+"\n"
                    if defs == 0:
                        content += string.replace(";", "") + "\n"

            if lexer[0] == comnd[2]:
                if defs == 5:
                    content += "                    "+pycmnd[2]+"(" + lexer[1].replace("\n", "") + ")\n"
                if defs == 4:
                    content += "                "+pycmnd[2]+"(" + lexer[1].replace("\n", "") + ")\n"
                if defs == 3:
                    content += "            "+pycmnd[2]+"(" + lexer[1].replace("\n", "") + ")\n"
                if defs == 2:
                    content += "        "+pycmnd[2]+"(" + lexer[1].replace("\n", "") + ")\n"
                if defs == 1:
                    content += "    "+pycmnd[2]+"(" + lexer[1].replace("\n", "") + ")\n"
                if defs == 0:
                    content += pycmnd[2]+"(" + lexer[1].replace("\n", "") + ")\n"

            if lexer[0] == comnd[3]:
                defs = 1
                content += pycmnd[3]+" " + lexer[1].replace("\n", "") + ""+ lexer[2].replace("{", ":") + "\n"

            if lexer[0] == comnd[4]:
                if defs == 5:
                    content += "                    " + lexer[1].replace("\n", "") + " = "+pycmnd[4]+"\n"
                if defs == 4:
                    content += "                " + lexer[1].replace("\n", "") + " = "+pycmnd[4]+"\n"
                if defs == 3:
                    content += "            " + lexer[1].replace("\n", "") + " = "+pycmnd[4]+"\n"
                if defs == 2:
                    content += "        " + lexer[1].replace("\n", "") + " = "+pycmnd[4]+"\n"
                if defs == 1:
                    content += "    " + lexer[1].replace("\n", "") + " = "+pycmnd[4]+"\n"
                if defs == 0:
                    content += "" + lexer[1].replace("\n", "") + " = "+pycmnd[4]+"\n"

            if lexer[0] == comnd[5]:
                if defs == 5:
                    content += "                    "+pycmnd[5]+" " + lexer[1] + " " + lexer[2] + " " + lexer[3] + ""+ lexer[4].replace("{", ":") + "\n"
                if defs == 4:
                    content += "                "+pycmnd[5]+" " + lexer[1] + " " + lexer[2] + " " + lexer[3] + ""+ lexer[4].replace("{", ":") + "\n"
                if defs == 3:
                    defs = 4
                    content += "            "+pycmnd[5]+" " + lexer[1] + " " + lexer[2] + " " + lexer[3] + ""+ lexer[4].replace("{", ":") + "\n"
                if defs == 2:
                    defs = 3
                    content += "        "+pycmnd[5]+" " + lexer[1] + " " + lexer[2] + " " + lexer[3] + ""+ lexer[4].replace("{", ":") + "\n"
                if defs == 1:
                    defs = 2
                    content += "    "+pycmnd[5]+" " + lexer[1] + " " + lexer[2] + " " + lexer[3] + ""+ lexer[4].replace("{", ":") + "\n"
                if defs == 0:
                    defs = 1
                    content += pycmnd[5]+" " + lexer[1] + " " + lexer[2] + " " + lexer[3] + ""+ lexer[4].replace("{", ":") + "\n"

            if lexer[0] == comnd[6]:
                if defs == 4:
                    defs = 5
                    content += "                "+pycmnd[6]+" " + lexer[5] + " in range(" + lexer[3] + ")"+ lexer[6].replace("{", ":") + "\n"
                if defs == 3:
                    defs = 4
                    content += "            "+pycmnd[6]+" " + lexer[5] + " in range(" + lexer[3] + ")"+ lexer[6].replace("{", ":") + "\n"
                if defs == 2:
                    defs = 3
                    content += "        "+pycmnd[6]+" " + lexer[5] + " in range(" + lexer[3] + ")"+ lexer[6].replace("{", ":") + "\n"
                if defs == 1:
                    defs = 2
                    content += "    "+pycmnd[6]+" " + lexer[5] + " in range(" + lexer[3] + ")"+ lexer[6].replace("{", ":") + "\n"
                if defs == 0:
                    defs = 1
                    content += pycmnd[6]+" " + lexer[5] + " in range(" + lexer[3] + ")"+ lexer[6].replace("{", ":") + "\n"

        file = open("rutime.py", "w")
        file.write(content)
        file.close()

        import rutime

hk_lexer(__script__)