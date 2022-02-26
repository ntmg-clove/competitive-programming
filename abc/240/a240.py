from pprint import pprint


PRINT_DEB = True
# PRINT_DEB = False


def debug_(msg: str, ppr: str = None) -> None:
    if not PRINT_DEB:
        return
    print(msg)
    if ppr:
        pprint(ppr)

    return


a, b = map(int, input().split())
# a -= 1
# b -= 1
if abs(a - b) in (1, 9):
    print("Yes")
else:
    print("No")
