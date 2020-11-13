from random import randint
import re


def make_squareroot_task(level):
    ans = 0
    problem_text = ''
    if level == 1:
        ans = randint(0, 20)
        problem_text = f"\\sqrt{{ {ans ** 2} }}"
        return problem_text, ans
    elif level == 2:
        ans = randint(1, 25)
        e = randint(1, 2)
        q1 = str(ans // 10 ** e)
        r1 = str(ans % 10 ** e).zfill(e)
        r1 = re.sub(r"0+$", "", r1)
        q2 = str(ans ** 2 // 10 ** (2 * e))
        r2 = str(ans ** 2 % 10 ** (2 * e)).zfill(2 * e)
        r2 = re.sub(r"0+$", "", r2)
        if r1 != "":
            ans = f"{q1},{r1}"
            problem_text = f"\\sqrt{{ {q2}{{,}}{r2} }}"
        else:
            ans = q1
            problem_text = f"\\sqrt{{ {q2} }}"
        return problem_text, ans
