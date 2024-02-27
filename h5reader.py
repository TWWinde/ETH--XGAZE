import h5py


hdf5_file_path = '/datasets/public/eth-xgaze/preprocessed_224/xgaze_224/train/subject0010.h5'

with h5py.File(hdf5_file_path, 'r') as file:

    print("Keys: %s" % list(file.keys()))