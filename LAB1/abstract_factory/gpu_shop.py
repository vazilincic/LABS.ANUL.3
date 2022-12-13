from lab2.abstract_factory.nvidia_factory import NvidiaFactory
from lab2.abstract_factory.amd_factory import AmdFactory


class GPUShop:
    def __init__(self, gpu_factory):
        self._gpu_factory = gpu_factory

    def buy_gpu(self, gpu_type):
        gpu = self._gpu_factory.get_gpu(gpu_type)
        return gpu


if __name__ == "__main__":

    nvidia_factory = NvidiaFactory()
    gpu_shop = GPUShop(nvidia_factory)
    gpu_shop.buy_gpu('new')

    amd_factory = AmdFactory()
    cable_shop = GPUShop(amd_factory)
    cable_shop.buy_gpu('old')
