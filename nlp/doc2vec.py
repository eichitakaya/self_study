# -*- coding: utf-8 -*-
import sys
import os
import codecs
from os import listdir, path
from pyknp import Jumanpp
from gensim import models
from gensim.models.doc2vec import LabeledSentence

title = "hamlet"
address = "/Users/yuki/Library/Mobile Documents/com~apple~CloudDocs/Documents/Word2Vec/"

def corpus_files():
    paragraph_address = address + "sentence/" + title
    docs = [path.join(paragraph_address, x)
            for x in listdir(paragraph_address) if x.endswith(".txt")]
    return docs

def read_document(path):
    with codecs.open(path, 'r', 'utf-8', 'ignore') as f:
        return f.read()

def split_into_words(text):
    result = Jumanpp().analysis(text)
    return [mrph.midasi for mrph in result.mrph_list()]

def doc_to_sentence(doc, name):
    words = split_into_words(doc)
    return LabeledSentence(words=words, tags=[name])

def corpus_to_sentences(corpus):
    docs = [read_document(x) for x in corpus]
    for idx, (doc, name) in enumerate(zip(docs, corpus)):
        sys.stdout.write('\r前処理中 {}/{}'.format(idx, len(corpus)))
        yield doc_to_sentence(doc, name)

def make_directories():
    if not os.path.exists(address + "sentence"):
        os.mkdir(address + "sentence")
    if not os.path.exists(address + "sentence/" + title):
        os.mkdir(address + "sentence/" + title)
    if not os.path.exists(address + "model"):
        os.mkdir(address + "model")
    if not os.path.exists(address + "model/" + title):
        os.mkdir(address + "model/" + title)
    if not os.path.exists(address + "model/" + title + "/doc2vec.model"):
        with open(address + "model/" + title + "/doc2vec.model", mode="w") as f:    #空のファイル作成
            pass
            

def read_sentence():  # 読み込んだ文章からスペースと改行記号を削除
    with open(address + title + ".txt") as f:
        s1 = f.read()
    #s2 = s1.replace("\n", "")      #改行は残す
    s3 = s1.replace("\u3000", "")
    result = ""
    parenthesis = 0
    double_angle_bracket = 0
    bracket = 0
    for i in range(len(s3)):
        if s3[i] == "(":
            parenthesis = 1
        if s3[i] == "《":
            double_angle_bracket = 1
        if s3[i] == "［":
            bracket = 1
        if parenthesis == 0 and double_angle_bracket == 0 and bracket == 0:
            result += s3[i]
        if s3[i] == ")":
            parenthesis = 0
        if s3[i] == "》":
            double_angle_bracket = 0
        if s3[i] == "］":
            bracket = 0
    return result

def paragraph_division(sentence):
    result = sentence.split("\n　")
    for i in range(len(result)):
        result[i].replace("\n", "")
    return result

def write_paragraphs(paragraphs):
    for i in range(len(paragraphs)):
        with open(address + "sentence/" + title + "/paragraph" + str(i+1) + ".txt", mode="w") as f:
            f.write(paragraphs[i])

make_directories()      #無ければディレクトリを作成
sentence = read_sentence()          #文章を読み込む
paragraphs = paragraph_division(sentence)  # 形式段落で分割
write_paragraphs(paragraphs)        #段落ごとにtxtファイルとして保存

corpus = corpus_files()
sentences = corpus_to_sentences(corpus)

model = models.Doc2Vec(sentences, dm=0, size=300, window=15, alpha=.025, min_alpha=.025, min_count=1, sample=1e-6)

print('\n訓練開始')
for epoch in range(20):
    print('Epoch: {}'.format(epoch + 1))
    model.train(sentences)
    model.alpha -= (0.025 - 0.0001) / 19
    model.min_alpha = model.alpha

model.save(address + "model/" + title + "/doc2vec.model")
