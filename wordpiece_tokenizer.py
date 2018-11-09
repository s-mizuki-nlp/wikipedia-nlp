#!/usr/bin/env python
# -*- coding:utf-8 -*-
# you need a tokenizer script that is included in the Google's bert repository.
# git clone https://github.com/google-research/bert.git

import os, sys, io
import argparse
# import progressbar

parser = argparse.ArgumentParser(description="WordPiece tokenizer: BERT's tokenization methodology.")
parser.add_argument("--bert_dir", "-b", required=True, type = str, help = "relative path to the BERT script directory.")
parser.add_argument("--vocab_file", "-v", required=True, type = str, help = "WordPiece vocabulary file. You can use the one distributed along with pre-trained bert model.")
parser.add_argument("--corpus", "-c", required=True, type = str, help = "relative path to the raw text corpus to be processed.")
parser.add_argument("--separator", required=False, type=str, default=" ", help="token separator. DEFAULT:whitespace")
parser.add_argument("--case_sensitive", action="store_true", help="case sensitive tokenizatoin. DEFAULT:False")
parser.add_argument("--eos", required=False, type=str, default="", help="end-of-sentence characters. DEFAULT:empty")
args = parser.parse_args()

sys.path.append(args.bert_dir)

from tokenization import FullTokenizer

tokenizer = FullTokenizer(vocab_file=args.vocab_file, do_lower_case=not args.case_sensitive)

separator = args.separator
eos = args.eos
with io.open(args.corpus, mode="r") as ifs:
    for sentence in ifs:
        sentence = sentence.strip()
        if len(sentence) == 0:
            continue
        lst_token = tokenizer.tokenize(sentence)
        print(separator.join(lst_token)+eos)