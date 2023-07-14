from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import FakeEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
import os
import sys
from sentence_transformers import SentenceTransformer, util
from CSVhandler import *
from googletranslatepy import Translator
translator = Translator(target='en')


def get_similar(image_desc, count):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    sentences = get_csv()
    embeddings = model.encode(sentences)
    em1 = model.encode(image_desc)
    cos_sim = util.cos_sim(em1, embeddings)

    if len(sentences) < count:
        count = len(sentences)
    top_k_vals, top_k_indices = cos_sim.topk(k=count, dim=1)
    images_name = []
    for i in range(count):
        image_name = get_image_from_index(top_k_indices[0][i].item())
        images_name.append(image_name)
    return images_name


def main(desc):
    text = translator.translate(desc)
    res = get_similar(text, 1)
    return res


# if __name__ == '__main__':
#     main('')
