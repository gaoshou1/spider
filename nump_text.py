import numpy as np


t1 = np.arange(24).reshape((4,6)).astype("float")
t1[1,2:] = np.nan
for i in range(t1.shape[1]):
    temp_col = t1[:,i]
    nan_num = np.count_nonzero(temp_col!=temp_col)
    if nan_num !=0:
        temp_col_nan_col = temp_col[temp_col==temp_col]

        temp_col[np.isnan(temp_col)] = np.mean(temp_col_nan_col)



print(t1)