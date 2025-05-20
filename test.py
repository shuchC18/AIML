import sys
import numpy as np
lst = [1, 2, 3, 4, 5, 6]  
a = np.array(lst)     # for now, let's assume, we see in next section
print(f'Size of the list :  {sys.getsizeof(5) *len(lst)} Bytes')
print(f'The size of array : {a.itemsize * len(a)} Bytes')