#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod


# ----- interface definition / abc / blueprint

class IOMeta(metaclass=ABCMeta):

    @abstractmethod
    def read(self, size: int = -1) -> bytes:
        pass

    @abstractmethod
    def write(self, data: bytes) -> int:
        pass


# ----- implementation

class IOImplementation(IOMeta):

    def read(self, size: int = -1) -> bytes:
        print("Reading {} bytes ...".format(size))

    def write(self, data: bytes) -> int:
        print("Wrote {} bytes.".format(len(data)))


if __name__ == "__main__":
    i = TestIO()
    i.read(5)
    i.write(b'ZZ')
