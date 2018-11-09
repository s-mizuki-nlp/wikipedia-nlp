#!/usr/bin/env python
# -*- coding:utf-8 -*-
# requirements: spacy and english model. installation procedure is as follows.
# pip install spacy
# python -m spacy download en_core_web_sm

import os, sys, io
import spacy

# model = spacy.load("en_core_web_sm")
model = spacy.load("en_core_web_sm", disable=["tagger","parser","ner"])
model.add_pipe(model.create_pipe('sentencizer'))

with io.open(sys.argv[1]) as ifs:
    for line in ifs:
        doc = model(line.strip())
        for sent in doc.sents:
            print(sent.text)