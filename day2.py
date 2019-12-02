opcode = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 6,
          19, 23, 1, 23, 13, 27, 2, 6, 27, 31, 1, 5, 31, 35, 2, 10, 35, 39, 1,
          6, 39, 43, 1, 13, 43, 47, 2, 47, 6, 51, 1, 51, 5, 55, 1, 55, 6, 59,
          2, 59, 10, 63, 1, 63, 6, 67, 2, 67, 10, 71, 1, 71, 9, 75, 2, 75, 10,
          79, 1, 79, 5, 83, 2, 10, 83, 87, 1, 87, 6, 91, 2, 9, 91, 95, 1, 95,
          5, 99, 1, 5, 99, 103, 1, 103, 10, 107, 1, 9, 107, 111, 1, 6, 111,
          115, 1, 115, 5, 119, 1, 10, 119, 123, 2, 6, 123, 127, 2, 127, 6,
          131, 1, 131, 2, 135, 1, 10, 135, 0, 99, 2, 0, 14, 0]
orig_opcode = opcode[:]


def run(index, opcode):
    while 1:
        print("Index: " + str(index))
        print("OpCode: " + str(opcode[index]))
        if opcode[index] == 1:
            # print("Sum pos '" + str(index+1) +
            #      "' (opcode[" + str(opcode[index + 1]) + "]: " +
            #      str(opcode[opcode[index + 1]]) +
            #      ") and pos '" + str(index+2) +
            #      "' (opcode[" + str(opcode[index + 2]) + "]: " +
            #      str(opcode[opcode[index + 2]]) +
            #      "). Store the result (" +
            #      str(opcode[opcode[index + 1]] + opcode[opcode[index + 2]]) +
            #      ") in pos '" + str(index+3) +
            #      "' (opcode[" + str(opcode[index + 3]) + "])")
            opcode[opcode[index + 3]] = (opcode[opcode[index + 1]] +
                                         opcode[opcode[index + 2]])

        elif opcode[index] == 2:
            # print("Multiply pos '" + str(index+1) +
            #      "' (opcode[" + str(opcode[index + 1]) + "]: " +
            #      str(opcode[opcode[index + 1]]) +
            #      ") and pos '" + str(index+2) +
            #      "' (opcode[" + str(opcode[index + 2]) + "]: " +
            #      str(opcode[opcode[index + 2]]) +
            #      "). Store the result (" +
            #      str(opcode[opcode[index + 1]] * opcode[opcode[index + 2]]) +
            #      ") in pos '" + str(index+3) +
            #      "' (opcode[" + str(opcode[index + 3]) + "])")
            opcode[opcode[index + 3]] = (opcode[opcode[index + 1]] *
                                         opcode[opcode[index + 2]])
        elif opcode[index] == 99:
            print("End program")
            break
        else:
            print("Wrong OpCode")
        index = index + 4


print("PART 1")
index = 0
noun = 12
verb = 2
opcode[1] = noun
opcode[2] = verb
print(opcode)
run(index, opcode)
print(opcode)


print("\nPART 2")
index = 0
new_opcode = orig_opcode[:]
for number in range(100):
    noun = number
    new_opcode[1] = noun
    for number in range(100):
        verb = number
        new_opcode[2] = verb
        print(new_opcode)
        print("Noun: " + str(noun) + ". Verb: " + str(verb))
        run(index, new_opcode)
        print(new_opcode)
        if new_opcode[0] == 19690720:
            final_noun = noun
            final_verb = verb
        new_opcode = orig_opcode[:]
        new_opcode[1] = noun

print("Noun: " + str(final_noun))
print("Verb: " + str(final_verb))
print("Answer: " + str(100*final_noun + final_verb))
