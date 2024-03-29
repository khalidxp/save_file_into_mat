import numpy as np
import scipy.io

# Some test data
x = np.arange(200).reshape((4,5,10))
# file name
matfile = 'saved_3D.mat'
# save the file
scipy.io.savemat(matfile, mdict={'saved_x': x}, oned_as='row')

# load the file
matdata = scipy.io.loadmat(matfile)
# read x
my_x = matdata["saved_x"]
# compare 
print(my_x-x)