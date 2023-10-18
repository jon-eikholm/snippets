import numpy as np
import pandas as pd
import re
import string
import tensorflow as tf
from tensorflow.keras import layers, models, losses, callbacks

# parameters
VOCAB_SIZE = 10000
MAX_LEN = 80
EMBEDDING_DIM = 256
KEY_DIM = 256
N_HEADS = 2
FEED_FORWARD_DIM = 256
VALIDATION_SPLIT = 0.2
SEED = 42
LOAD_MODEL = True
BATCH_SIZE = 32
EPOCHS = 1


# data: https://drive.google.com/file/d/15bvblqRi-6qTpWD3Mft7ZIvfQtXU3uBE/view?usp=sharing
