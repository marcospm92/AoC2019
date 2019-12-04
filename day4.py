start = 246540
stop = 787419
solutions_part1 = []
solutions_part2 = []

# PART 1
for number in range(start, stop+1):
    current = list(map(int, str(number)))
    fail_decrease = 0
    pass_consecutive = 0
    fail_distinct = 0
    pass_distinct_consecutives = 0
    reps = []
    for i in range(5):  # 0, 1, 2, 3, 4
        # Two adjacent digits are the same
        if current[i] == current[i+1]:
            pass_consecutive += 1
            if current[i] not in reps:
                reps.append(current[i])

        # Going from left to right, the digits never decrease
        if current[i] > current[i+1]:
            fail_decrease = 1

    # If there is more than one repetition, I have to check if I have a valid
    #  iteration, for example 777889 is valid because of the 88.
    # What I do is counting each digit and if it the count of all the digits
    #  repeated is > 2 then it is a fail. Otherwise it is ok
    if pass_consecutive > 1:
        for j in reps:
            if current.count(j) > 2:
                fail_distinct += 1
        if fail_distinct < len(reps):
            pass_distinct_consecutives = 1

    # If there is only one digit repeated twice, it is ok
    elif pass_consecutive == 1:
        pass_distinct_consecutives = 1

    # PART 1
    if pass_consecutive >= 1 and fail_decrease == 0:
        solutions_part1.append(number)
    # PART 2
    if (pass_consecutive >= 1 and pass_distinct_consecutives == 1 and
            fail_decrease == 0):
        solutions_part2.append(number)

print("Number of solutions of Part 1: " + str(len(solutions_part1)))
print("Number of solutions of Part 2: " + str(len(solutions_part2)))
