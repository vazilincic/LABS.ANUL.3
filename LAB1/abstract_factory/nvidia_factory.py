from lab2.abstract_factory.nvidia_gpu_new import NvidiaGPUNew
from lab2.abstract_factory.nvidia_gpu_old import NvidiaGPUOld


class NvidiaFactory:
    def get_gpu(self, gpu_type):
        if gpu_type == "old":
            return NvidiaGPUOld()
        if gpu_type == "new":
            return NvidiaGPUNew()
