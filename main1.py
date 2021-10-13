# Import everything needed to edit video clips
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from moviepy.editor import *


clip = AudioFileClip("D:\movie\stage2.mp4")
sampFreq = clip.fps
source = clip.to_soundarray()
# source1 = np.array(source[:, 0], dtype='float')
source = np.array(source[:, 0], dtype='float')
# max_value = np.amax(wave)
# np.where(wave == max_value)[0].tolist()

x_source = np.arange(0, source.size) / sampFreq


# plt.specgram(source, Fs=sampFreq)

# plt.xlabel('seconds')
# plt.title('source')


# main_beep_freq = 2990
# x_coord, y_coord = find_highest_peak_coord(source, 0.6, 0.1, sampFreq)


# peak_vals, prop = signal.find_peaks(source,
#                   height=highest_peak,
#                   prominence=0,
#                   width=[0.3*sampFreq, 0.6*sampFreq]
#                   )

plt.plot(x_source, source, 'b')


# plt.plot(x_coord/sampFreq, y_coord, 'or')
# plt.plot(x_source, source1, 'r')
# plt.axvline(x=x_source[prop['left_bases']], color='red')
# plt.axvline(x=x_source[prop['right_bases']], color='red')


fft_spectrum = np.fft.rfft(source)

freq = np.fft.rfftfreq(source.size, d=1. / sampFreq)

freq_coords = [int(x) for x in range(0, len(freq)) if 1000 <= freq[x] <= 2000]
fft_spectrum = fft_spectrum[freq_coords]

fft_spectrum_abs = np.abs(fft_spectrum)
# plt.plot(freq[freq_coords], fft_spectrum_abs)

max_amplitude = max(fft_spectrum_abs)
max_amplitude_coord = fft_spectrum_abs.tolist().index(max_amplitude)
main_beep_freq = freq[freq_coords[max_amplitude_coord]]
main_beep_freq = 1500
print(main_beep_freq)

butter_filter = signal.butter(10, [main_beep_freq - 90, main_beep_freq + 90], btype='bandpass', output='sos', fs=sampFreq)

source = signal.sosfilt(butter_filter, source)

highest_peak = source.tolist().index(max(source))

# plt.xlabel("frequency, Hz")
# plt.ylabel("Amplitude, units")


plt.plot(highest_peak/sampFreq, source[highest_peak], 'or')
plt.plot(x_source, source, color='red')
plt.show()

# peaks_idxs = peaks[0]

# plt.plot(x_source[peaks_idxs], source[peaks_idxs], 'or')
