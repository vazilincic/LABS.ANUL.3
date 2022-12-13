from lab2.factory.hdd import HDD
from lab2.factory.ssd import SSD


class StorageFactory:
    def get_storage(self, storage_type):
        if storage_type == "fast":
            return SSD()
        if storage_type == "big":
            return HDD()


if __name__ == "__main__":
    factory = StorageFactory()

    a = factory.get_storage("fast")
    print(a.model())
    b = factory.get_storage("big")
    print(b.model())
