#!/bin/sh

python ./wordpiece_tokenizer.py \
--bert_dir /home/sakae/Windows/public_model/BERT/bert/ \
--vocab_file /home/sakae/Windows/public_model/BERT/cased_L-12_H-768_A-12/vocab.txt \
--corpus ../corpus_sentence.txt \
> ../corpus_sentence_wordpiece.txt