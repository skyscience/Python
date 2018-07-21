import time
start_time = time.time()


def run():
    i = 0
    while True:
        i += 1
        if i == 100000000:
            print('== ok ==')
            print('I:',i)
            break


run()
print('耗时:',time.time() - start_time)