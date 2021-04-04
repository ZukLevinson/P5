import os
import pathlib
import h5py
import hdf5_getters




for path, subdirs, files in os.walk("MillionSongSubset"):
    for name in files:
        current_file_path = os.path.join(path, name)

        h5 = hdf5_getters.open_h5_file_read(current_file_path)
        duration = hdf5_getters.get_duration(h5)
        print(duration)
        h5.close()
