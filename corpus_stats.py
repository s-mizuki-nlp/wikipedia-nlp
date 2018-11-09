#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys, io
import numpy as np

with io.open(sys.argv[1]) as ifs:

    lst_word = [line.count(" ") + 1 for line in ifs]

    n_word = np.sum(lst_word)
    n_sentence = len(lst_word)

    print(f"number of words: {n_word}")
    print(f"number of sentences: {n_sentence}")
    print(f"avg sentence length: {n_word / n_sentence}")

    # quantile
    vec_q = np.sort(np.unique(np.concatenate([np.linspace(0,100, 21), np.linspace(95,100, 11)])))
    vec_p = np.percentile(lst_word, vec_q)

    print("quantiles are as follows.")
    for q, p in zip(vec_q, vec_p):
        print(f"{q:3.1f}: {p:4.2f}")
