#!/usr/bin/env python3

from implements import implements, Interface


# ----- interface definition / abc / blueprint

class IOInterface(Interface):

    def read(self, size: int = -1) -> bytes:
        pass

    def write(self, data: bytes) -> int:
        pass


# ----- implementation

@implements(IOInterface)
class IOImplementation:

    def read(self, size: int = -1) -> bytes:
        print("Reading {} bytes ...".format(size))

    def write(self, data: bytes) -> int:
        print("Wrote {} bytes.".format(len(data)))


if __name__ == "__main__":
    i = TestIO()
    i.read(5)
    i.write(b'ZZ')
