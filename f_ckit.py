# just another brainfuck interpreter written in python


def f_ckit(code, inputIntList=[]):
    instructions = list(
        filter(lambda x: x in '[]<>.,+-', code)
    )
    instructionCursor = 0
    data = [0]
    dataCursor = 0
    inputCopy = inputIntList[:]
    output = []

    while instructionCursor < len(instructions):
        instruction = instructions[instructionCursor]
        if instruction == ',':
            data[dataCursor] = inputCopy.pop(
            ) if input else float('nan')
            instructionCursor += 1
        elif instruction == '.':
            output.append(data[dataCursor])
            instructionCursor += 1
        elif instruction == '[':
            if data[dataCursor] != 0:
                instructionCursor += 1
            else:
                skipCounter = 0
                for i, instruction in enumerate(
                        instructions[instructionCursor:]):
                    if instruction == '[':
                        skipCounter -= 1
                    elif instruction == ']':
                        skipCounter += 1

                    if skipCounter == 0:
                        instructionCursor = instructionCursor + i
                        break
        elif instruction == ']':
            if data[dataCursor] == 0:
                instructionCursor += 1
            else:
                skipCounter = 0
                for i, instruction in enumerate(
                        reversed(instructions[:instructionCursor + 1])):
                    if instruction == '[':
                        skipCounter += 1
                    elif instruction == ']':
                        skipCounter -= 1

                    if skipCounter == 0:
                        instructionCursor = instructionCursor - i
                        break
        elif instruction == '>':
            data.append(0)
            dataCursor += 1
            instructionCursor += 1
        elif instruction == '<':
            dataCursor = max(dataCursor - 1, 0)
            instructionCursor += 1
        elif instruction == '+':
            data[dataCursor] += 1
            instructionCursor += 1
        elif instruction == '-':
            data[dataCursor] -= 1
            instructionCursor += 1

    print(''.join(map(chr, output)).rstrip('\n'))


f_ckit('''
\o/

this code prints "beynisikik" which translates to "brainfucked"
it was generated with this:
https://andrew.hedges.name/experiments/brainf_cker/

++++++++
[
    >+>++>+++>++++>+++++>++++++>+++++++>
    ++++++++>+++++++++>++++++++++>++++++
    +++++>++++++++++++>+++++++++++++>+++
    +++++++++++>+++++++++++++++>++++++++
    ++++++++<<<<<<<<<<<<<<<<-
]
>>>>>>>>>>>>++.
--<<<<<<<<<<<<>>>>>>>>>>>>>---.
+++<<<<<<<<<<<<<>>>>>>>>>>>>>>>+.
-<<<<<<<<<<<<<<<>>>>>>>>>>>>>>--.
++<<<<<<<<<<<<<<>>>>>>>>>>>>>+.
-<<<<<<<<<<<<<>>>>>>>>>>>>>>+++.
---<<<<<<<<<<<<<<>>>>>>>>>>>>>+.
-<<<<<<<<<<<<<>>>>>>>>>>>>>+++.
---<<<<<<<<<<<<<>>>>>>>>>>>>>+.
-<<<<<<<<<<<<<>>>>>>>>>>>>>+++.
---<<<<<<<<<<<<<.

\o/
''')
