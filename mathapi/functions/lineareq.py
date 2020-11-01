from random import randint
import re


def make_lineareq(level):
    left_coeffs = [0, 1]
    left_add_coeffs = [0, 0, 0]
    right_add_coeffs = [0, 0, 0]
    left_expr = ""
    right_expr = ""

    if level == 1 or level == 2:
        if level == 1:
            ans = randint(1, 10)
        else:
            ans = randint(-10, -1)

        right_coeffs = [ans, 0]
        k = randint(2, 10)

        if level == 2:
            k *= (-1) ** randint(0, 1)

        for i in range(0, 2):
            left_coeffs[i] *= k
            right_coeffs[i] *= k

    elif 3 <= level <= 6:
        ans = randint(3, 12)
        ans *= (-1) ** randint(0, 1)
        right_coeffs = [ans, 0]
        k = randint(2, 9)
        k *= (-1) ** randint(0, 1)
        for i in range(0, 2):
            left_coeffs[i] *= k
            right_coeffs[i] *= k
        k = randint(1, 15)
        k *= (-1) ** randint(0, 1)
        left_coeffs[0] += k
        right_coeffs[0] += k
        if level >= 4:
            k = randint(1, 9)
            k *= (-1) ** randint(0, 1)
            left_coeffs[1] += k
            right_coeffs[1] += k
        if level >= 5:
            tmp = randint(2, 5)
            if randint(0, 1):
                right_add_coeffs[2] += tmp
            else:
                right_add_coeffs[2] -= tmp
            tmp = randint(1, 6)
            if randint(0, 1):
                right_add_coeffs[1] += tmp
            else:
                right_add_coeffs[1] -= tmp
            tmp = randint(1, 7)
            if randint(0, 1):
                right_add_coeffs[0] += tmp
            else:
                right_add_coeffs[0] -= tmp
            right_coeffs[0] -= right_add_coeffs[2] * right_add_coeffs[0]
            right_coeffs[1] -= right_add_coeffs[2] * right_add_coeffs[1]
            if level == 6:
                tmp = randint(2, 5)
                if randint(0, 1):
                    left_add_coeffs[2] += tmp
                else:
                    left_add_coeffs[2] -= tmp
                tmp = randint(1, 6)
                if randint(0, 1):
                    left_add_coeffs[1] += tmp
                else:
                    left_add_coeffs[1] -= tmp
                tmp = randint(1, 7)
                if randint(0, 1):
                    left_add_coeffs[0] += tmp
                else:
                    left_add_coeffs[0] -= tmp
                left_coeffs[0] -= left_add_coeffs[2] * left_add_coeffs[0]
                left_coeffs[1] -= left_add_coeffs[2] * left_add_coeffs[1]
    if level >= 5:
        if right_add_coeffs[2] > 0:
            right_add_expr = " + "
        else:
            right_add_expr = ""
        right_add_expr += f"{right_add_coeffs[2]} ( {right_add_coeffs[1]} x"
        if right_add_coeffs[0] > 0:
            right_add_expr += " + "
        right_add_expr += f"{right_add_coeffs[0]} )"
        right_add_expr = re.sub(r" 1 x ", " x ", right_add_expr)
        right_add_expr = re.sub(r" -1 x ", " -x ", right_add_expr)
        if level == 6:
            if left_add_coeffs[2] > 0:
                left_add_expr = " + "
            else:
                left_add_expr = ""
            left_add_expr += f"{left_add_coeffs[2]} ( {left_add_coeffs[1]} x"
            if left_add_coeffs[0] > 0:
                left_add_expr += " + "
            left_add_expr += f"{left_add_coeffs[0]} )"
            left_add_expr = re.sub(r" 1 x ", " x ", left_add_expr)
            left_add_expr = re.sub(r" -1 x ", " -x ", left_add_expr)

    if left_coeffs[1]:
        left_expr += f" {left_coeffs[1]} x"

    if left_coeffs[0] > 0:
        left_expr += f"+ {left_coeffs[0]}"
    elif left_coeffs[0] < 0:
        left_expr += str(left_coeffs[0])

    if right_coeffs[1]:
        right_expr += f" {right_coeffs[1]} x"

    if right_coeffs[0] > 0:
        right_expr += f"+ {right_coeffs[0]}"
    elif right_coeffs[0] < 0:
        right_expr += str(right_coeffs[0])

    left_expr = re.sub(r" 1 x", " x ", left_expr)
    left_expr = re.sub(r" -1 x", " -x ", left_expr)
    right_expr = re.sub(r" 1 x", " x ", right_expr)
    right_expr = re.sub(r" -1 x", " -x ", right_expr)
    left_expr = re.sub(r"^\+ ", "", left_expr)
    right_expr = re.sub(r"^\+ ", "", right_expr)

    if level >= 5:
        right_expr += right_add_expr
        if level == 6:
            left_expr += left_add_expr

    if level < 5:
        problem_text = f"{left_expr} = {right_expr}".strip()
    else:
        problem_text = f"{left_expr} = \\\\ {right_expr}".strip()

    return problem_text, ans
