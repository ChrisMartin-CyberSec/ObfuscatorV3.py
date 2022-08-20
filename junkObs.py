import random
import string


def junkPy():

    randomList = list(string.ascii_letters)
    randomLetter = random.choice(randomList)

    randVarList = ["".join(random.choices(randomList, k=random.randint(5, 15))) for i in range(30)]

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

                f'for {randomLetter} in {range(random.randint(3, 20))}:\n'
                f'\tif {random.choice(mathProblems)} <= {random.randint(5, 15)}:\n'
                f'\t\t{random.choice(randVarList)} = {random.randint(3, 20)} * {random.randint(5, 15)}\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n'
                f'\telse:\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n'
                f'\t\t{random.choice(randVarList)} = {random.randint(5, 15)} * {random.randint(3, 20)}\n',    

                f'for {randomLetter} in {range(random.randint(3, 20))}:\n'
                f'\tif {random.choice(mathProblems)} + {random.choice(mathProblems)} < {random.choice(mathProblems)}:\n'
                f'\t\t{random.choice(randVarList)} = {random.choice(mathProblems)} * {random.choice(mathProblems)}\n'
                f'\telse:\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n',     

                f'for {randomLetter} in {randVarList}:\n'
                f'\t{random.choice(randVarList)} = "{"".join(random.choices(string.hexdigits, k = random.randint(5, 16)))}"\n'
                f'\t{random.choice(randVarList)} = "{"".join(random.choices(string.hexdigits, k = random.randint(5, 16)))}"\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                f'\t{random.choice(randVarList)} = "{"".join(random.choices(string.hexdigits, k = random.randint(5, 16)))}"\n',

                f'def {"".join(random.choices(randomList, k=random.randint(5, 15)))}():\n'
                f'\t{"".join(random.choices(randomList, k=random.randint(5, 15)))} = str({random.randint(3, 20)} * {random.randint(5, 15)})\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                f'\tif {random.choice(mathProblems)} <= {random.randint(5, 15)}:\n'
                f'\t\t{random.choice(randVarList)} = {random.randint(3, 20)} * {random.randint(5, 15)}\n',       

                f'def {"".join(random.choices(randomList, k=random.randint(5, 15)))}():\n'
                '\ttime.sleep(0)\n'
                f'\tfor {randomLetter} in {range(random.randint(3, 20))}:\n'
                f'\t\tif {random.choice(mathProblems)} + {random.choice(mathProblems)} < {random.choice(mathProblems)}:\n'
                f'\t\t\t{random.choice(randVarList)} = {random.choice(mathProblems)} * {random.choice(mathProblems)}\n'
                f'\t\telse:\n'
                '\t\t\ttime.sleep(0)\n'
                '\t\t\ttime.sleep(0)\n',
                
                f'def {"".join(random.choices(randomList, k=random.randint(5, 15)))}():\n'
                f'\tif {random.choice(mathProblems)} != {random.choice(mathProblems)}:\n'
                '\t\ttime.sleep(0)\n'
                f'\t\t{"".join(random.choices(randomList, k=random.randint(5, 15)))} = {random.choice(mathProblems)}\n'
                '\t\ttime.sleep(0)\n'
                '\t\ttime.sleep(0)\n',

                f'if {random.choice(mathProblems)} != {random.choice(mathProblems)}:\n'
                f'\t{random.choice(randVarList)} = {random.randint(3, 20)}\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                f'\t{random.choice(randVarList)} = {random.randint(3, 20)}\n',

                f'if {random.choice(mathProblems)} <= {random.choice(mathProblems)}:\n'
                f'\t{random.choice(randVarList)} = {random.randint(3, 20)}\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                f'\t{random.choice(randVarList)} = {random.randint(3, 20)}\n',

                f'if {random.choice(mathProblems)} > {random.choice(mathProblems)}:\n'
                f'\t{random.choice(randVarList)} = {random.randint(3, 20)}\n'
                '\ttime.sleep(0)\n'
                '\ttime.sleep(0)\n'
                f'\t{random.choice(randVarList)} = {random.randint(3, 20)}\n']
    
    junk = [random.choice(junkList) for x in range(random.randint(100,200))]

    return junk

def junkVBS():

    randomList = list(string.ascii_letters)
    randomLetter = random.choice(randomList)

    randVarList = ["".join(random.choices(randomList, k = random.randint(5, 15))) for i in range(30)]

    mathProblems = [f'{random.randint(5,30)} - {random.randint(5,30)}',
                    f'{random.randint(5,30)} * {random.randint(5,30)}/Tan({random.randint(5,30)})',
                    f'{random.randint(5,30)} * {random.randint(5,30)} * {random.randint(5,30)}',
                    f'Tan{random.randint(5,30)}',
                    f'sqr({random.randint(50,100)})']
        
    junkList = ['WScript.Sleep(0)\n',

                'WScript.Sleep(0)\n'
                'WScript.Sleep(0)\n',

                'WScript.Sleep(0)\n'
                'WScript.Sleep(0)\n'
                'WScript.Sleep(0)\n'
                'WScript.Sleep(0)\n',

                f'for each {random.choice(randVarList)} in Array({random.choice(randVarList)}, {random.choice(randVarList)}, {random.choice(randVarList)})\n'
                f'\tif {random.choice(mathProblems)} <> {random.choice(mathProblems)} then\n'
                'WScript.Sleep(0)\n'
                'WScript.Sleep(0)\n'
                f'\t\t{"".join(random.choices(randomList, k = random.randint(5,12)))} = {random.randint(5, 450)}\n'
                '\tend if\n'
                'next\n',

                f'for {randomLetter} = 1 to {random.randint(5, 10)}\n'
                f'\t{"".join(random.choices(randomList, k = random.randint(5,12)))} = {random.choice(mathProblems)}\n'
                f'\tWScript.Sleep(0)\n'
                f'\t{randomLetter} = cstr({random.randint(50, 500)}) & {"".join(random.choices(randomList, k = random.randint(5,10)))}\n'
                'next\n',

                f'sub {"".join(random.choices(randomList, k = random.randint(10, 20)))}()\n'
                f'\t{"".join(random.choices(randomList, k = random.randint(5,12)))} = {random.choice(mathProblems)}\n'
                '\tWScript.Sleep(0)\n'
                f'\t{randomLetter} = {random.choice(mathProblems)}\n'
                '\tWScript.Sleep(0)\n'
                '\tWScript.Sleep(0)\n'
                'end sub\n']

    junk = [random.choice(junkList) for x in range(random.randint(100, 200))]

    return junk
