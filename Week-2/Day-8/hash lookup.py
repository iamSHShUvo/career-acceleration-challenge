import time

dataset = list (range(10000000))

print ('Converting list to set:')

data_set = set (dataset)

start_time = time.time()

if -5 in data_set:
    print('Found it!')
else:
    print('Not Found!')

end_time = time.time()

print (f'Time taken: {end_time - start_time: .5f} seconds')