def cl(r):
    pl = float
    pl = r * r * 3.14
    return pl
def tl(a, h):
    ploshadT = a * h * 0.5
    return ploshadT
def rl(x, y):
    ploshadRL = x * y
    return ploshadRL
S = str(input())
if S == "cl":
    r = int(input())
    print(cl(r))
if S == "tl":
    a = int(input())
    h = int(input())
    print(tl(a, h))
if S == "rl":
    x = int(input())
    y = int(input())
    print(rl(x, y))