#libraries
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import subprocess
import sys
import os
def install(package):
    subprocess.check_call(["pip3", "install", package])
#check if Gpu is activated
print('tensorflow version',tf.__version__)
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
print(tf.test.is_built_with_cuda())
print(tf.test.is_gpu_available(
    cuda_only=False,
    min_cuda_compute_capability=None
))
#Install Pillow (Ex.)
try:
    from PIL import Image
    print("Pillow already installed")
except:
    print("installing Pillow")
    install("Pillow")
print("Pillow installed")