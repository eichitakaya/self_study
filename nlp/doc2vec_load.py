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

def make_directories():
    if not os.path.exists(address + "result"):
        os.mkdir(address + "result")
    if not os.path.exists(address + "result/" + title):
        os.mkdir(address + "result/" + title)

def text_name():
    result = []
    paragraph_address = address + "sentence/" + title
    docs = [path.join(paragraph_address, x)
            for x in listdir(paragraph_address) if x.endswith(".txt")]
    for i in range(len(docs)):
        result.append(address + "sentence/" + title + "/paragraph" + str(i+1) + ".txt")
    return result

def calcurate_similarity(texts, model):
    result = []
    for i in range(len(texts) - 1):
        result.append(model.docvecs.similarity(texts[i], texts[i+1]))
    return result

def calcurate_abs(similarity):
    result = []
    for i in range(len(similarity)):
        result.append(abs(similarity[i]))
    return result

def make_split_number(abs_similarity):
    result = []
    sort_absim = sorted(abs_similarity)
    for i in range(min(len(sort_absim), 12)):   #可能なら13フェイズに分ける
        result.append(abs_similarity.index(sort_absim[i]) + 1)  #txtファイルの番号が1からなので1加算
    result.sort()
    result.append(len(abs_similarity) + 1)      #最終段落(の次)を最後の区切り用の番号として追加
    for i in range(len(result)-1):      #各フェイズの開始段落番号を各フェイズの段落数に変換
        result[len(result)-i-1] -= result[len(result)-i-2]
    return result

def read_document(path):
    with codecs.open(path, 'r', 'utf-8', 'ignore') as f:
        return f.read()

def read_documents(texts):
    docs = [read_document(x) for x in texts]
    return docs

def make_phases(documents, split_number):
    result = []
    count = 0
    for i in range(min(len(documents),13)):
        candidate = ""
        for j in range(split_number[i]):
            candidate += documents[count]
            count += 1
        result.append(candidate)
    return result

def write_phases(phases):
    for i in range(len(phases)):
        with open(address + "result/" + title + "/phase" + str(i+1) + ".txt", mode="w") as f:
            f.write(phases[i].encode('utf-8'))

make_directories()
model = models.Doc2Vec.load(address + "model/" + title + "/doc2vec.model")
texts = text_name()
similarity = calcurate_similarity(texts, model)
abs_similarity = calcurate_abs(similarity)
split_number = make_split_number(abs_similarity)
documents = read_documents(texts)
phases = make_phases(documents, split_number)
write_phases(phases)
