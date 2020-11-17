import random
import time

def compute():
    return random.random() + random.random()

while True:
    nb_of_computation = random.randint(10000, 10000000)
    time_to_sleep = random.random()

    print('compute')
    for _ in range(nb_of_computation):
        compute()
    print('sleep')
    time.sleep(time_to_sleep)
