import time
while True:
    start_time = time.time()
    time.sleep(5)
    current_time = time.time()
    elapsed_time = current_time - start_time
    console.log("{elapsed_time} seconds have passed, starting time {start_time}, current time {current_time}")