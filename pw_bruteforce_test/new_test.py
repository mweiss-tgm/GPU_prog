import numba.cuda
import sys
import random

ELEMENTS = "abcdefghijklmnopqrstuvwxyz0123456789"

def get_pw(le):

    pw_length = le
    mypw = ""

    for i in range(pw_length):
        next_index = random.randrange(len(ELEMENTS))
        mypw += ELEMENTS[next_index]

    print(mypw)
    return mypw


PASSWORD = get_pw(5)
PASSWORD_LENGTH = len(PASSWORD)

@numba.cuda.jit("str(str[:])")
def bruteforce(pw):
    complete_list = []
    for current in range(PASSWORD_LENGTH):
        a = [i for i in ELEMENTS]
        for y in range(current):
            a = [x+i for i in ELEMENTS for x in a]
            if pw in a:
                index = a.index(pw)
                print("Password found! %s" % a[index])
                return a[index]
        complete_list = complete_list+a
    print(len(complete_list))


if __name__ == "__main__":
    bruteforce(PASSWORD)
