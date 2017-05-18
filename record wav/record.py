# Borrowed from https://gist.github.com/mabdrabo/8678538

import pyaudio
import wave
from datetime import datetime
from sys import argv
from os.path import dirname, abspath

BITS = 1024
SAMPLE_FORMAT = pyaudio.paInt16
CHANNELS = 2
SAMPLE_RATE = 44100
RECORD_SECONDS = int(argv[1])

ts = datetime.today().now().time()
FILENAME = "/{lvl_back}/pi_project/test/{timestamp}_transcription.wav"\
            .format(lvl_back=dirname(dirname(abspath(__file__))),\
            timestamp=ts)

p = pyaudio.PyAudio()

mic = p.open(format=SAMPLE_FORMAT, channels=CHANNELS,\
		rate=SAMPLE_RATE, input=True,\
		frames_per_buffer=BITS)

print("start record")

soundArray = []

for i in range(0, int(SAMPLE_RATE / BITS * RECORD_SECONDS)):
    data = mic.read(BITS)
    soundArray.append(data)

print("end record")

mic.stop_stream()
mic.close()
p.terminate()

waveFile = wave.open(FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(p.get_sample_size(SAMPLE_FORMAT))
waveFile.setframerate(SAMPLE_RATE)
waveFile.writeframes(b''.join(soundArray))
waveFile.close()
