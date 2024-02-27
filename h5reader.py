import h5py


hdf5_file_path = '/datasets/public/eth-xgaze/preprocessed_224/xgaze_224/train/subject0000.h5'

with h5py.File(hdf5_file_path, 'r') as file:
    # 列出文件中的顶级组/数据集
    print("Keys: %s" % list(file.keys()))