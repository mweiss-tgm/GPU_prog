import random
import time
from numba import jit


@jit
def brute():
    Password = str(random.randint(0, 999999)) #example password
    print("Example Password", Password)
    #start_time = time.clock()
    for i in range(1000000):    #0-9999
       trial = str(i)
       if trial == Password:
           print('Found password: ' + trial)
           #print("--- %s seconds ---" % (time.clock() - start_time))


if __name__ == "__main__":
    brute()
