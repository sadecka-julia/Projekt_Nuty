import pyaudio
import wave

# ******** na podstawie dokumentacji pyaudio ********
ilosc = 1024
format = pyaudio.paInt32
kanaly = 2
sampling = 44100
czas_nagrania = 10
audio = "dzwiek_f4.wav"

p = pyaudio.PyAudio()

stream = p.open(format=format, channels=kanaly, rate=sampling,
                input=True, frames_per_buffer=ilosc)

print("* trwa nagranie")

frames = []

for i in range(0, int(sampling / ilosc * czas_nagrania)):
    data = stream.read(ilosc)
    frames.append(data)

print("* nagranie zakończone")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(audio, 'wb')
wf.setnchannels(kanaly)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(sampling)
wf.writeframes(b''.join(frames))
wf.close()
