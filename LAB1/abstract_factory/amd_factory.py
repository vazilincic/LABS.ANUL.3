from lab2.abstract_factory.amd_gpu_new import AmdGPUNew
from lab2.abstract_factory.amd_gpu_old import AmdGPUOld


class AmdFactory:
    def get_gpu(self, gpu_type):
        if gpu_type == "old":
            return AmdGPUOld()
        if gpu_type == "new":
            return AmdGPUNew()
