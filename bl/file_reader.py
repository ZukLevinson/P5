import os
import hdf5_getters
import matplotlib.pyplot as plt

dictionary = {}

for path, subdirs, files in os.walk("MillionSongSubset"):
    for name in files:
        current_file_path = os.path.join(path, name)

        h5 = hdf5_getters.open_h5_file_read(current_file_path)

        artist = hdf5_getters.get_artist_name(h5).decode('UTF-8')

        if artist in dictionary:
            dictionary[artist] += 1
        else:
            dictionary[artist] = 1

        h5.close()

plt.bar(range(len(dictionary)), list(map(lambda x: r"{}".format(x), list(dictionary.values()))), align='center')
plt.xticks(range(len(dictionary)))

plt.show()
