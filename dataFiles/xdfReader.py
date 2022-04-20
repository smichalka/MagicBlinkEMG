import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import mne

streams, header = pyxdf.load_xdf("dataFiles/handSignals.xdf")
print(streams)
for stream in streams:
    y = stream['time_series']
    blah = []
    if stream['info']['name'] == ['MarkersForBooks']:
        # y = y[0::2][1:]
        # stream['time_stamps'] = stream['time_stamps'][0::2][1:]
        # print(y)
        # for i in y:
        #     blah.append(y)
        # print(blah)
        # input("blah: ")
        # y = blah
        continue
    # if stream['info']['name'] == ['obci_eeg2']:
    #     continue
    if stream['info']['name'] == ['obci_eeg3']:
        continue
    if stream['info']['name'] == ['obci_eeg1']:
        continue
    print(stream['info']['name'])
    print(np.shape(stream['time_series']))

    if isinstance(y, list):
        # list of strings, draw one vertical line for each marker
        for timestamp, marker in zip(stream['time_stamps'], y):
            plt.axvline(x=timestamp)
            #print(f'Marker "{marker[0]}" @ {timestamp:.2f}s')
        
    elif isinstance(y, np.ndarray):
        # numeric data, draw as lines
        plt.plot(stream['time_stamps'], y, 'o')
        print("here")
        # if multiple options for data, need to expand this to include selection by name
        if stream["info"]["type"]==['EEG']:
          data = stream["time_series"].T
          sfreq = float(stream["info"]["nominal_srate"][0])
          info = mne.create_info(int(stream["info"]['channel_count'][0]),sfreq,"eeg")
          first_samp = stream["time_stamps"][0]
    else:
        raise RuntimeError('Unknown stream format')
# plt.axis([2210, 2280, 0, 10])
plt.show()
