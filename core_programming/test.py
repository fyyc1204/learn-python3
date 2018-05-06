import numpy as np


gl_set = np.array([False, False, True, True, True])

print(len(gl_set))
print("********")
print(gl_set)

rfl_init_mode = gl_set * (-1)

print(rfl_init_mode)

print((2-1)%3)
print((2+1)%3)
for i in range(299, 350):
    print(i)