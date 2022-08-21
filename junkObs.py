import random
import string


def junkPy_List():

    randVarList = ["".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15))) for i in range(30)]

    mathProblems = [f'{random.randint(3, 20)} / math.tan({random.randint(5, 15)})',
                    f'math.ceil({random.randint(3, 20)})',
                    f'math.floor({random.randint(5, 15)})',
                    f'math.fabs({random.randint(5, 15)} * {random.randint(3, 20)})',
                    f'math.trunc({random.randint(5, 15)} ** 2) / math.ceil(math.fabs({random.randint(3, 20)}))',
                    f'math.tan({random.randint(3, 20)} + {random.randint(5, 15)}) - {random.randint(3, 20)}',
                    f'math.trunc(math.tan({random.randint(3, 20)}) ** 2)',
                    f'{random.randint(3, 20)} ** 2 / {random.randint(5, 15)} + math.fabs({random.randint(5, 15)} * math.tan({random.randint(5, 15)}))']

    junkList = ['time.sleep(0)\n',

                'time.sleep(0)\n'
                'time.sleep(0)\n',

                'time.sleep(0)\n'
                'time.sleep(0)\n'
                'time.sleep(0)\n'
                'time.sleep(0)\n',

                f'for {random.choice(list(string.ascii_letters))} in {range(random.randint(3, 20))}:\n'
                f'\tif {random.choice(mathProblems)} <= {random.randint(5, 15)}:\n'
                f'\t\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.randint(3, 20)} * {random.randint(5, 15)}\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n'
                f'\telse:\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n'
                f'\t\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.randint(5, 15)} * {random.randint(3, 20)}\n',    

                f'for {random.choice(list(string.ascii_letters))} in {range(random.randint(3, 20))}:\n'
                f'\tif {random.choice(mathProblems)} + {random.choice(mathProblems)} < {random.choice(mathProblems)}:\n'
                f'\t\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.choice(mathProblems)} * {random.choice(mathProblems)}\n'
                f'\telse:\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n',     

                f'for {random.choice(list(string.ascii_letters))} in {randVarList}:\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = "{"".join(random.choices(string.hexdigits, k = random.randint(5, 16)))}"\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = "{"".join(random.choices(string.hexdigits, k = random.randint(5, 16)))}"\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = "{"".join(random.choices(string.hexdigits, k = random.randint(5, 16)))}"\n',

                f'def {"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))}():\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = str({random.randint(3, 20)} * {random.randint(5, 15)})\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                f'\tif {random.choice(mathProblems)} <= {random.randint(5, 15)}:\n'
                f'\t\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.randint(3, 20)} * {random.randint(5, 15)}\n',       

                f'def {"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))}():\n'
                '\ttime.sleep(0)\n'
                f'\tfor {random.choice(list(string.ascii_letters))} in {range(random.randint(3, 20))}:\n'
                f'\t\tif {random.choice(mathProblems)} + {random.choice(mathProblems)} < {random.choice(mathProblems)}:\n'
                f'\t\t\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.choice(mathProblems)} * {random.choice(mathProblems)}\n'
                f'\t\telse:\n'
                '\t\t\ttime.sleep(0)\n'
                '\t\t\ttime.sleep(0)\n',
                
                f'def {"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))}():\n'
                f'\tif {random.choice(mathProblems)} != {random.choice(mathProblems)}:\n'
                '\t\ttime.sleep(0)\n'
                f'\t\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.choice(mathProblems)}\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n',

                f'if {random.choice(mathProblems)} != {random.choice(mathProblems)}:\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.randint(3, 20)}\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.randint(3, 20)}\n',

                f'if {random.choice(mathProblems)} <= {random.choice(mathProblems)}:\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.randint(3, 20)}\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.randint(3, 20)}\n',

                f'if {random.choice(mathProblems)} > {random.choice(mathProblems)}:\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.randint(3, 20)}\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} = {random.randint(3, 20)}\n']

    return junkList

def junkVBS_List():

    mathProblems = [f'{random.randint(5,30)} - {random.randint(5,30)}',
                    f'{random.randint(5,30)} * {random.randint(5,30)}/Tan({random.randint(5,30)})',
                    f'{random.randint(5,30)} * {random.randint(5,30)} * {random.randint(5,30)}',
                    f'Tan({random.randint(5,30)})',
                    f'sqr({random.randint(50,100)})']
        
    junkList = ['WScript.Sleep(0)\n',

                'WScript.Sleep(0)\n'
                'WScript.Sleep(0)\n',

                'WScript.Sleep(0)\n'
                'WScript.Sleep(0)\n'
                'WScript.Sleep(0)\n'
                'WScript.Sleep(0)\n',

                f'for each {"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))} in Array({"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))}, {"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))}, {"".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))})\n'
                f'\tif {random.choice(mathProblems)} <> {random.choice(mathProblems)} then\n'
                'WScript.Sleep(0)\n'
                'WScript.Sleep(0)\n'
                f'\t\t{"".join(random.choices(list(string.ascii_letters), k = random.randint(5,12)))} = {random.randint(5, 450)}\n'
                '\tend if\n'
                'next\n',

                f'for {random.choice(list(string.ascii_letters))} = 1 to {random.randint(5, 10)}\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k = random.randint(5,12)))} = {random.choice(mathProblems)}\n'
                f'\tWScript.Sleep(0)\n'
                f'\t{random.choice(list(string.ascii_letters))} = cstr({random.randint(50, 500)}) & {"".join(random.choices(list(string.ascii_letters), k = random.randint(5,10)))}\n'
                'next\n',

                f'sub {"".join(random.choices(list(string.ascii_letters), k = random.randint(10, 20)))}()\n'
                f'\t{"".join(random.choices(list(string.ascii_letters), k = random.randint(5,12)))} = {random.choice(mathProblems)}\n'
                '\tWScript.Sleep(0)\n'
                f'\t{random.choice(list(string.ascii_letters))} = {random.choice(mathProblems)}\n'
                '\tWScript.Sleep(0)\n'
                '\tWScript.Sleep(0)\n'
                'end sub\n']

    return junkList

def junkPy():
    junk = [random.choice(junkPy_List()) for x in range(random.randint(1000, 5000))]
    return junk

def junkVBS():
    junk = [random.choice(junkVBS_List()) for x in range(random.randint(1000, 5000))]
    return junk
