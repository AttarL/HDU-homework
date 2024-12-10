import re
import os
import jieba
import math
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import csv
import re
import pandas as pd

def read_and_process_txt_file(file_path):
    lines = []
    with open(file_path, 'r', encoding='gbk') as file:
        for line in file:
            lines.append(line[2:])
    return lines

# 加载停用词表
def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f]
    return stopwords


# 预处理文本（包括分词和去除停用词）
def preprocess_text(text):
    stopwords = load_stopwords("baidu_stopwords.txt")  # 加载停用词表
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', ' ', text)  # 只保留中文、字母和数字
    words = jieba.cut(text, cut_all=False)  # jieba分词
    filtered_words = [word for word in words if word not in stopwords]
    processed_text = " ".join(filtered_words)
    return processed_text

# 加载文档文件（同时进行预处理）
def load_and_preprocess_txt_files(folder_path):
    txt_documents = []
    file_names = []  # 保存文件名
    stopwords = load_stopwords("baidu_stopwords.txt")  # 加载停用词表
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'r', encoding='gbk', errors='ignore') as f:
                try:
                    content = f.read()
                    processed_content = preprocess_text(content)  # 预处理文本
                    txt_documents.append(processed_content)
                    file_names.append(file.split('.')[0])  # 获取文件名，去掉后缀
                except UnicodeDecodeError:
                    print(f"UnicodeDecodeError: Could not decode {file_path}")
    return txt_documents, file_names

# 从文本文件中读取数据并转换为列表
def read_list_from_file(file_path):
        with open(file_path, 'r') as f:
            # 读取文件内容
            content = f.read()
            # 将内容按换行符分割为列表
            my_list = content.split('\n')
        return my_list

# 计算词频（TF）
def calculate_term_frequency(document):
    word_count = {}
    total_words = 0
    words = document.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        total_words += 1

    term_frequency = {word: count / total_words for word, count in word_count.items()}
    return term_frequency


# 计算逆文档频率（IDF）
def calculate_inverse_document_frequency(documents):
    document_count = len(documents)
    word_document_count = {}

    for document in documents:
        words = set(document.split())
        for word in words:
            if word in word_document_count:
                word_document_count[word] += 1
            else:
                word_document_count[word] = 1

    inverse_document_frequency = {}
    for word, count in word_document_count.items():
        inverse_document_frequency[word] = math.log(document_count / count)

    return inverse_document_frequency

# 计算TF-IDF并返回向量化矩阵
def calculate_tfidf_matrix(documents):
    term_frequency_list = [calculate_term_frequency(doc) for doc in documents]
    inverse_document_frequency = calculate_inverse_document_frequency(documents)

    vocabulary = set(inverse_document_frequency.keys())
    tfidf_matrix = []

    for term_frequency in term_frequency_list:
        tfidf_vector = [term_frequency[word] * inverse_document_frequency[word] if word in term_frequency else 0.0 for
                        word in vocabulary]
        tfidf_matrix.append(tfidf_vector)

    return tfidf_matrix, list(vocabulary)

# 处理查询词并返回查询向量
def process_query(query, vocabulary):
    query_terms = query.split()
    query_vector = [query_terms.count(word) * (
        math.log(len(vocabulary) / (vocabulary.index(word) + 1)) if word in vocabulary else 0.0) for word in vocabulary]
    return query_vector

# 计算相似度并返回结果
# def calculate_similarity(query_vector, tfidf_matrix, file_names):
#     similarities = []
#     for idx, tfidf_vector in enumerate(tfidf_matrix):
#         print('-',end='')
#         similarity = sum(x * y for x, y in zip(query_vector, tfidf_vector)) / (
#                     math.sqrt(sum(x ** 2 for x in query_vector)) * math.sqrt(sum(x ** 2 for x in tfidf_vector)))
#         similarities.append((file_names[idx], similarity))
#
#     similarities.sort(key=lambda x: x[1], reverse=True)
#     return similarities
def calculate_similarity(query_vector, tfidf_matrix):
    # 使用 cosine_similarity 计算相似度
    similarities = cosine_similarity([query_vector], tfidf_matrix)

    # 对相似度进行排序，并返回结果
    similarities = similarities[0]  # 取出第一个数组，因为我们只有一个查询向量
    indexed_similarities = list(enumerate(similarities))  # 加入索引，方便排序
    indexed_similarities.sort(key=lambda x: x[1], reverse=True)  # 按照相似度降序排序

    return indexed_similarities[:6]

# def write_to_csv(query, finames,similys):
#     query=query.rstrip("\n")
#     csv_filename = f"{query}.csv"
#     df = pd.DataFrame(data=finames, columns=['file_name'])
#     df = pd.DataFrame(data=similys, columns=['simil'])
#     df.to_csv(csv_filename)

# 主函数
def main(line):
    #文件夹路径
    root_folder = r"E:\大学\自然语言处理\NLP实验1\自然语言处理实验1-数据集\训练集"
    folders = [str(i) for i in range(1, 27)]
    txt_documents = []
    file_names = []
    #
    # 遍历所有文件夹并加载文档
    for folder in folders:
        folder_path = os.path.join(root_folder, folder)
        #print("文件夹路径：", folder_path)
        # 加载文档并预处理
        txt_document, file_name = load_and_preprocess_txt_files(folder_path)
        txt_documents += txt_document
        file_names += file_name

    # with open('txt_documents.txt', 'w') as f:
    #     f.write('\n'.join(txt_documents))
    # print("列表已保存到 txt_documents.txt 文件中。")

    # 读取保存列表的文本文件
    # file_path = 'txt_documents.txt'
    # txt_documents = read_list_from_file(file_path)
    # 计算TF-IDF
    #tfidf_matrix, vocabulary = calculate_tfidf_matrix(txt_documents)
    #np.save('tfidf_matrix.npy', tfidf_matrix)
    #print("TF-IDF 矩阵已保存到 tfidf_matrix.npy 文件中。")
    #with open('vocabulary.txt', 'w') as f:
    #    f.write('\n'.join(vocabulary ))

    vocabulary = read_list_from_file('vocabulary.txt')
    tfidf_matrix = np.load('tfidf_matrix.npy')

    # 输入查询词
    query_ori = line
    query=preprocess_text(query_ori)
    # 处理查询词
    query_vector = process_query(query, vocabulary)

    # 计算相似度并返回结果
    indexed_similarities = calculate_similarity(query_vector, tfidf_matrix)
    # 输出结果
    print("查询结果：")
    finames=[]
    similys=[]
    for idx, similarity in indexed_similarities:
        file_name = file_names[idx]
        #if similarity * 100 < 20:  # 设定相似度阈值
         #   continue
        print("文档名：", file_name)
        finames.append(file_name)
        print("匹配度：{:.2f}%".format(similarity * 100))
        similys.append(similarity*100)
    #csv_filename = write_to_csv(query_ori,finames,similys)
    #print(f"查询结果已保存到文件：{csv_filename}")
    query = query_ori.rstrip("\n")
    csv_filename = f"{query}.csv"
    df = pd.DataFrame()
    df = pd.DataFrame(data=finames, index=None,columns=['file_name'])
    df = pd.DataFrame(data=similys, index=None,columns=['simil'])
    df.to_csv(csv_filename)


if __name__ == "__main__":
    lines = read_and_process_txt_file('测试集.txt' )
    for line in lines:
        print(line)
        main(line)