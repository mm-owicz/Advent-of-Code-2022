def add_to_sum(cal_sum, l):
    if(l != ''):
        cal_sum += int(l)
    else:
        cal_sum = 0

    return cal_sum


def part1():
    # Find the elf carrying the most calories

    max_cal = 0
    cal_sum = 0

    with open("input.txt", 'r') as f:
        for l in f.readlines():
            cal_sum = add_to_sum(cal_sum, l[:-1])
            max_cal = cal_sum if cal_sum > max_cal else max_cal

    return max_cal

def part2():
    # Find the 3 elves carrying the most calories

    max_cal = [0, 0, 0]
    cal_sum = 0

    with open("input.txt", 'r') as f:
        for l in f.readlines():

            cal_sum = add_to_sum(cal_sum, l[:-1])

            if cal_sum > min(max_cal):
                max_cal.append(cal_sum)
                max_cal.remove(min(max_cal))

    return sum(max_cal)


if __name__ == "__main__":

    print(part1())

    print(part2())
