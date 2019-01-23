def read_data_from_file(file_name, n_ch):
    n_data = 0
    # Count the total number of data point
    with open(file_name, 'r') as f:
        for _ in f:
            n_data += 1

    print('n_data', n_data)
    # Create the data structure as a deque
    data = [deque(np.zeros(n_data),
                  maxlen=n_data) for _ in range(n_ch)]

    # Read all the lines in the file and add them to the data deque
    with open(file_name, 'r') as f:
        for all_ch_line in f:
            all_ch_line = all_ch_line.strip().split(',')
            for ch_no, ch in enumerate(all_ch_line):
                data[ch_no].append(float(ch))
    return data

#%%
import numpy as np
x = np.zeros(10)
x[4] = 10
x[6] = 3
print(np.nonzero(x))