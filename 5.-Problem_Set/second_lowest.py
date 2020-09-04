if __name__ == '__main__':
    lowest = 100
    second_lowest = 100
    secondLowests = []
    student = {}

    for _ in range(int(input())):
        name = str(input())
        score = float(input())
        student[name] = score

        if score < lowest:
            second_lowest = lowest
            lowest = score
        elif score < second_lowest and score > lowest:
            second_lowest = score

    for key, value in student.items():
        if(value == second_lowest):
            secondLowests.append(key)

    secondLowests.sort()
    print ('\n'.join(secondLowests))
