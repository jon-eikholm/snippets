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


# data: https://drive.google.com/uc?export=download&id=15bvblqRi-6qTpWD3Mft7ZIvfQtXU3uBE

# EKSTRA kode, som optæller alle ord og unikke ord:
from collections import Counter

all_tokens = [token for sentence in text_data for token in sentence.lower().split()] # alle ordene i hele sættet
wordSet = set(all_tokens)
print("antal unikke ord: " + str(len(wordSet)))

token_freqs = Counter(all_tokens) # dictionary, som ved hvor mange gange alle ordene forekommer
token_freqs['wine'] # viser antal gange det givne ord forekommer.
print("antal ord tilsammen: " + str(len(all_tokens)))
