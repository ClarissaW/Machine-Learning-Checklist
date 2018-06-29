import nltk
from nltk.corpus import stopwords

text = "This is Andrew's text, isn't it?"

tokenizer = nltk.tokenize.WhitespaceTokenizer()
tokens = tokenizer.tokenize(text)

stops = set(stopwords.words('english')) #It is more effient than the one without set()
filtered_words = [token for token in tokens if token not in stops]
print(filtered_words)
