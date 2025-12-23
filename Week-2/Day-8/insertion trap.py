import time

dataset = list(range(10000000))

start_time = time.time()

dataset.append(99)

end_time = time.time()

print(f'Append (End) Time: {end_time - start_time: .5f} seconds')

start_time = time.time()

dataset.insert(0,99)

end_time = time.time()
print (f'Insert (Start) Time: {end_time - start_time: .5f} seconds')