import time

dataset = list(range(10000000))

start_time = time.time()

if -5 in dataset:
    print('Found it!')
else:
    print('Not found!')

end_time = time.time()

print(f'Time take: {end_time - start_time: .5f} seconds')