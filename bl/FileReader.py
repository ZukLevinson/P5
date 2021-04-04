import os
import pathlib
import h5py

for path, subdirs, files in os.walk("MillionSongSubset"):
    for name in files:
        current_file_path = os.path.join(path, name)

        with h5py.File(current_file_path, 'r') as f:
            print(f.keys())
            data = f['analysis']
            print(data.keys())
            print(data.items())
