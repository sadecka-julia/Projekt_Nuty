import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from scipy.io import wavfile

audio = "dzwiek_c4.wav"

# Odczytaj sampling (44100), a także data czyli naszego dźwięku
sampling, data = wavfile.read('output.wav')

print(sampling)
print(data)

samplePoints = float(data.shape[0])


print(samplePoints)
one_channel = data[:, 0]
timeArray = np.arange(0, samplePoints, 1)
timeArray = timeArray / sampling
# milisekundy
timeArray = timeArray * 1000
# rysowanie wykresu
plt.plot(timeArray, data)
plt.xlabel('Czas (ms)')
plt.ylabel('Amplituda')
plt.show()

# Wyświetlenie częstotliwości do czasu:
f, t, sxx = scipy.signal.spectrogram(one_channel, fs=sampling)
plt.pcolormesh(t, f, sxx)
plt.ylim([0, 5000])
plt.ylabel('Częstotliwość [Hz]')
plt.xlabel('Czas [sekundy]')
plt.show()

# Oblicz spektrogram za pomocą funkcji specgram
plt.specgram(one_channel, Fs=sampling)
plt.ylim([0, 8000])

# Wyświetl spektrogram
plt.show()
