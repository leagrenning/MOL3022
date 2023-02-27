import numpy as np

import torch
from torch import nn

import pandas as pd

from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical, pad_sequences


class ML:
    def __init__(self):
        df = pd.read_csv("archive/2018-06-06-ss.cleaned.csv")

        df = df[df["seq"].str.contains("[*]") == False]
        maxlen_seq = 128

        df = df.loc[df["seq"].str.len() < maxlen_seq]

        self.input_seqs, target_seqs = df[['seq', 'sst3']][(df.len <= maxlen_seq) & (~df.has_nonstd_aa)].values.T

        input_grams = self.n_grams(self.input_seqs)

        self.tokenizer_encoder = Tokenizer()
        self.tokenizer_encoder.fit_on_texts(input_grams)

        self.tokenizer_decoder = Tokenizer(char_level=True)
        self.tokenizer_decoder.fit_on_texts(target_seqs)

        self.reverse_decoder_index = {value: key for key, value in self.tokenizer_decoder.word_index.items()}

        n_words, n_tags, self.maxlen_seq = 8421, 4, 128

        self.model = LSTM(n_words, self.maxlen_seq, n_tags)
        self.model.load_state_dict(torch.load('model_1.torch', map_location=torch.device('cpu')))

    def n_grams(self, seqs, n=3):
        return np.array([[seq[i:i + n] for i in range(len(seq))] for seq in seqs], object)

    def n_gram(self, seq, n=3):
        return [seq[i:i + n] for i in range(len(seq))]

    def onehot_to_seq(self, oh_seq, index):
        s = ''
        for o in oh_seq:
            i = np.argmax(o)
            if i != 0:
                s += index[i]
            else:
                break
        return s

    def preprocess(self, x):
        x = self.n_gram(x, n=3)
        x = np.array([x, []], object)

        input_data = self.tokenizer_encoder.texts_to_sequences(x)
        input_data = pad_sequences(input_data, maxlen=self.maxlen_seq, padding='post')

        return input_data

    def predict(self, x):
        x = self.preprocess(x)
        x = torch.tensor(x)
        y = self.model(x).detach().numpy()

        y = self.onehot_to_seq(y[0], self.reverse_decoder_index).upper()

        return y


class LSTM(nn.Module):
    def __init__(self, n_words, maxlen_seq, n_tags, hidden_size=64, dropout=0.1):
        super(LSTM, self).__init__()
        self.embedding = nn.Embedding(n_words, 128, padding_idx=0)
        self.bilstm = nn.LSTM(input_size=128, hidden_size=hidden_size, num_layers=1,
                              batch_first=True, bidirectional=True, dropout=dropout)
        self.dense = nn.Linear(hidden_size * 2, n_tags)

    def forward(self, x):
        return self.dense(self.bilstm(self.embedding(x))[0])














