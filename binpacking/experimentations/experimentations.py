from abc import ABCMeta, abstractmethod


class Experimentations:

    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self) -> None:
        pass
