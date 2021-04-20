import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit


lengths = [10 ** 7 * x for x in range(1, 5)]
times_py = []
times_np = []
speed_up_rotation = []
trials = 100

for l in lengths:
    numbers_np = np.random.randint(0, 100, size=l)
    numbers_py = numbers_np.tolist()
    
    times_sum_py = timeit(lambda: sum(numbers_py), number=trials)
    times_sum_np = timeit(lambda: np.sum(numbers_np), number=trials)
    
    times_py.append(times_sum_py)
    times_np.append(times_sum_np)
    speed_up_rotation.append(times_sum_np / times_sum_py)
    

plt.gca()
plt.plot(list(range(len(lengths))), times_py, color = "blue")
plt.plot(list(range(len(lengths))), times_np, color = "red")
# plt.xticks(list(range(len(lengths))), lengths)
plt.legend(["py", "np"])
plt.xlabel("elements") 
plt.ylabel("average time [ms]")
plt.show()

plt.plot(list(range(len(lengths))), speed_up_rotation, color="orange")
plt.show()
# lens = [x for x in range(10)]
# plt.plot(lengths, times_np, c="blue")
# plt.plot(lengths, times_py, c="red")


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.transforms import Affine2D
# import time

# lengths = [10 ** 7 * i for i in range(10)]
# times_py = []
# times_np = []

# for l in lengths:
#     numbers_to_sum_np = np.random.uniform(0, 100, size=1)
#     numbers_to_sum_py = numbers_to_sum_np.tolist()

#     times = []
#     for trial in range(10):
#         start = time.time()
#         sum = 0
#         for i in range(len(numbers_to_sum_py)):
#             sum += numbers_to_sum_py[i]
#         times.append(time.time() - start)
#     mean_time_py = np.mean(times)
#     times_py.append(mean_time_py)

#     times = []
#     for trial in range(10):
#         start = time.time()
#         np.sum(numbers_to_sum_np)
#         times.append(time.time() - start)
#     mean_time_np = np.mean(times)
#     times_np.append(mean_time_np)

# plt.gca()
# lens = [_ for _ in range(10)]
# plt.plot(lens, times_np, c="blue")
# plt.plot(lens, times_py, c="red")
# plt.gca().set_aspect("equal")
# plt.show()
