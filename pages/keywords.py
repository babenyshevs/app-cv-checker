import os
from collections import Counter
import pandas as pd
import streamlit as st

import nltk
from nltk import ngrams
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')
file_path = 'data/gen_councelor.txt'
folder_path = "data/"

st.markdown("# Keywords")
st.sidebar.markdown("# Keywords")

class KeywordExtractor:
    def __init__(self, file_path, folder_path=None):
        self.file_path = file_path
        if folder_path is not None:
            self.text = self._read_folder(folder_path)
        else:
            self.text = self._read_file(file_path)
        self.processed_text = self._process_text(self.text)

    def _read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def _read_folder(self, folder_path):
        _text = ""
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                _text += self._read_file(file_path)
        return _text

    def _process_text(self, text):
        tokens = nltk.word_tokenize(text)
        stop_words = stopwords.words('english')
        stop_words.extend(["experience", "product", "team"])
        filtered_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
        return lemmatized_tokens

    def _extract_keywords(self, n):
        processed_tokens = self._process_text(self.text)
        n_grams = list(ngrams(processed_tokens, n))
        n_gram_frequencies = Counter(n_grams)
        _keyword_frequency = n_gram_frequencies.most_common()
        return _keyword_frequency

    def extract_keywords(self, min_n=1, max_n=5, drop_duplicate=True):
        self.keyword_frequency = {}
        for n in reversed(range(min_n,max_n)):
            ngram_keywords = self._extract_keywords(n)
            for key_freq_pair in ngram_keywords:
                n_key = "_".join(key_freq_pair[0]) # normalize ngram text
                n_freq = key_freq_pair[1]
                keys = self.keyword_frequency.keys()
                if drop_duplicate:
                    if sum([n_key in key for key in keys]) == 0: # not presented even partially in other keys
                        self.keyword_frequency[n_key] = n_freq
                else:
                    self.keyword_frequency[n_key] = n_freq

    def display_keywords(self, top_n=10):
        print("Keywords with frequencies:")
        df_keywords = pd.DataFrame(self.keyword_frequency.items(), 
                                   columns=["keyword","frequency"]).sort_values("frequency", ascending=False).reset_index(drop=True)
        st.write(df_keywords.head(top_n))


if __name__ == "__main__":
    ke = KeywordExtractor(
                        file_path=file_path, 
                        folder_path=folder_path
                        )
    ke.extract_keywords(2, 4, False)
    ke.display_keywords(5)