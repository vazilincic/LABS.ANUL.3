from lab2.builder.computer import Computer
from lab2.factory.storage_factory import StorageFactory
from lab2.abstract_factory.gpu_shop import GPUShop
from lab2.abstract_factory.nvidia_factory import NvidiaFactory
from lab2.abstract_factory.amd_factory import AmdFactory


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_ram(self, amount):
        self.computer.ram = amount
        self.computer.ram_price = 10 * amount

    def configure_storage(self, type):
        factory = StorageFactory()
        self.computer.storage = factory.get_storage(type)

    def configure_gpu(self, gpu_model):
        if gpu_model.startswith('Nvidia'):
            factory = NvidiaFactory()

        else:
            factory = AmdFactory()

        gpu_shop = GPUShop(factory)
        self.computer.gpu = gpu_shop.buy_gpu(gpu_model.split()[1])
