from src.factory import get_scribe
from lib.read import read


def main(*wav_files):
    scribe = get_scribe()
    for text in scribe.transcribe(wav_files):
        read(text)
