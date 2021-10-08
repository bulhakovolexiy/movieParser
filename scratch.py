# def preparePeaks(wave):
#     wave = np.array(wave[:, 0], dtype='int16')
#     wave = abs(wave)
#     maxValue = np.amax(wave)
#     return np.where(wave == maxValue)[0].tolist()
#
#
# def count_peaks(peaks_coords, samp_frequency):
#     starting_peak = peaks_coords.pop(0)
#     result_list = [starting_peak]
#     for peak in peaks_coords:
#         if peak < (starting_peak + 0.2 * samp_frequency):
#             starting_peak = peak
#             continue
#         starting_peak = peak
#         result_list.append(peak)
# #     return result_list
# prepared_peaks = preparePeaks(source)
#
# conted = count_peaks(prepared_peaks, sampFreq)
#
# print(len(conted))