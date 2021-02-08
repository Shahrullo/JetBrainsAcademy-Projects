import re


def input_shape(inp):
    if "**" in inp or "//" in inp:
        return 0

    val = inp.replace(" ", "")

    val = re.sub(r"\++", "+", val)

    val = re.split("(-+)", val)
    for i in range(len(val)):
        if "-" in val[i]:
            if len(val[i]) % 2 == 0:
                val[i] = "+"
            else:
                val[i] = "-"
    val = "".join(val)

    val = re.split("([+\\-*/()])", val)

    while "" in val:
        val.remove("")

    return val


variables = {}


def get_var(x):
    inp = x.replace(" ", "").split("=")

    if len(inp) > 2:
        return "Invalid assignment"

    for sign in inp[0]:
        if sign.isalpha():
            continue
        else:
            return "Invalid identifier"

    if len(inp) == 1:
        return 0

    try:
        float(inp[1])
    except (ValueError, IndexError):
        if inp[1] not in variables.keys():
            return "Invalid assignment"

    variables[inp[0]] = variables[inp[1]] if inp[1] in variables.keys() else inp[1]
    return 0


def postfix(val):
    result = []
    operators = []
    signs = "+-/*"

    for i in val:
        if i == "(":
            operators.append(i)
        elif i == ")":
            left_missing = True
            while operators:
                if operators[-1] != "(":
                    result.append(operators.pop())
                else:
                    operators.pop()
                    left_missing = False
                    break
            if left_missing:
                return 0
        elif i in signs:
            if not operators or operators[-1] == "(" or \
                    i in signs[2:] and operators[-1] in signs[:2]:
                operators.append(i)
            else:
                while operators:
                    if operators[-1] in signs[:2] and i in signs[2:] or operators[-1] == "(":
                        break
                    else:
                        result.append(operators.pop())
                operators.append(i)
        else:
            result.append(i)

    while operators:
        result.append(operators.pop())

    if "(" in result or ")" in result:
        return 0

    return result


def compute(x):
    result = []
    for i in x:
        if i.isdigit():
            result.append(i)
        elif i in variables:
            result.append(variables[i])
        elif len(result) > 1:
            if i == '+':
                a = int(result.pop())
                b = int(result.pop())
                result.append(a + b)
            elif i == '-':
                a = int(result.pop())
                b = int(result.pop())
                result.append(b - a)
            elif i == '*':
                a = int(result.pop())
                b = int(result.pop())
                result.append(a * b)
            elif i == '/':
                a = int(result.pop())
                b = int(result.pop())
                result.append(b // a)
    return result[0]


def main():
    while True:
        nums = input()
        if not nums:
            pass
        elif nums == "/help":
            print("The program calculates the sum of numbers")
        elif nums == "/exit":
            print("Bye!")
            break
        elif "=" in nums:
            var = get_var(nums)
            if var:
                print(var)
            continue
        elif nums[0] == "/" and nums[1:len(nums) + 1] not in ["help", "exit"]:
            print("Unknown command")
        elif nums in variables.keys():
            print(variables[nums])
        else:
            infix_ = input_shape(nums)
            if not infix_:
                print('Invalid expression')
                continue
            if len(infix_) == 1:
                try:
                    print(int(nums))
                except ValueError:
                    print('Invalid expression' if get_var(nums) else 'Unknown variable')
            else:
                postfix_ = postfix(infix_)
                if postfix_ == 0:
                    print('Invalid expression')
                    continue
                try:
                    print(compute(postfix_))
                except (TypeError, ValueError):
                    print('Invalid expression')


if __name__ == '__main__':
    main()