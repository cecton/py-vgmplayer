from ctypes import CDLL
import threading

from . import _libvgm

__version__ = "0.1.4"


lib = CDLL(_libvgm.__file__)


def play(filepath, fd, sample_rate=44100, loop=2):
    return lib.play(filepath.encode(), fd, sample_rate, loop)


class PlayThread(threading.Thread):
    def __init__(self, filepath, fd, sample_rate=44100, loop=2):
        super(PlayThread, self).__init__(
            daemon=True,
            target=play,
            args=(filepath, fd, loop))
