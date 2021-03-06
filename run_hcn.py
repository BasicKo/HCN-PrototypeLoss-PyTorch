import sys

import torch
from torch.backends import cudnn

from processor.processor import Processor

torch.backends.cudnn.deterministic = False
cudnn.benchmark = True  # https://discuss.pytorch.org/t/what-does-torch-backends-cudnn-benchmark-do/5936
torch.cuda.empty_cache()  # release cache

if __name__ == '__main__':
    proc = Processor(sys.argv[1:])
    proc.start()
