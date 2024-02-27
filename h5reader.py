import cv2
import h5py


hdf5_file_path = '/datasets/public/eth-xgaze/preprocessed_224/xgaze_224/train/subject0010.h5'

with h5py.File(hdf5_file_path, 'r') as file:

    print("Keys: %s" % list(file.keys()))
    #  Keys: ['cam_index', 'face_gaze', 'face_head_pose', 'face_mat_norm', 'face_patch', 'frame_index']
    cam_index = file['cam_index'][1]
    face_gaze = file['face_gaze'][1]
    face_head_pose = file['face_head_pose'][1]
    face_mat_norm = file['face_mat_norm'][1]
    face_patch = file['face_patch'][1]
    frame_index = file['frame_index'][1]

    # 打印数据以检查
    print("Camera Index:", cam_index)
    print("Face Gaze:", face_gaze)
    print("Face Head Pose:", face_head_pose)
    print("Face Matrix Normalized:", face_mat_norm)
    print("Face Patch:", face_patch)
    print("Frame Index:", frame_index)
    output_path = 'example/output/image1.jpg'
    print('save output image to: ', output_path)
    cv2.imwrite(output_path, face_patch)