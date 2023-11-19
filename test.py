import time

while True:
    current_time_A = time.time()
    print(f"Current time A {current_time_A}")
    time.sleep(1)
    current_time_B = time.time()
    print(f"Current time B: {current_time_B}")

    # calculate how many seconds have elapsed since the start of the program
    elapsed_time = current_time_B - current_time_A
    print(f"Elapsed time: {elapsed_time}")
    # round to the nearest second
    print("Elapsed time (rounded):", round(elapsed_time))