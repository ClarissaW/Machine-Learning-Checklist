import nltk
nltk.download_shell()

text = "feet cats woves talked"

tokenizer = nltk.tokenize.TreebankWordTokenizer()
tokens = tokenizer.tokenize(text)

stemmer = nltk.stem.PorterStemmer()
print(''.join(stemmer.stem(token) for token in tokens))

lemmatizer = nltk.stem.WordNetLemmatizer()
print(''.join(lemmatizer.lemmatize(token) for token in tokens))
