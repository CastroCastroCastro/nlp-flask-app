import wikipediaapi
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# download NLTK resources conditionally to avoid bloating the deployment
import os
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
if not os.path.exists(nltk_data_path):
    nltk.download("punkt", download_dir=nltk_data_path)
    nltk.download("stopwords", download_dir=nltk_data_path)
    nltk.download("wordnet", download_dir=nltk_data_path)
    nltk.download("averaged_perceptron_tagger", download_dir=nltk_data_path)

# Wikipedia API function
def get_wiki(pageName):
    wiki = wikipediaapi.Wikipedia(
        language="en",
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent="nlpProject(castr385@umn.edu)"
    )
    page = wiki.page(pageName)
    return page.text if page.exists() else "Page Not Found"

#function to map NLTK POS tags to WordNet POS tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ 
    elif tag.startswith('V'):
        return wordnet.VERB  
    elif tag.startswith('N'):
        return wordnet.NOUN  
    elif tag.startswith('R'):
        return wordnet.ADV  
    else:
        return wordnet.NOUN  

# Main text processing function
def process_text(text):
    # Step 1: Sentence Segmentation
    sentences = sent_tokenize(text)

    # Step 2: Tokenization
    tokens = [word_tokenize(sentence) for sentence in sentences]

    # Step 3: Stop Word Removal
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [
        [word for word in sentence if word.lower() not in stop_words and word.isalpha()]
        for sentence in tokens
    ]

    # Step 4: POS Tagging and Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = []
    for sentence in filtered_tokens:
        pos_tagged = nltk.pos_tag(sentence)  
        lemmatized_sentence = [
            lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tagged
        ]
        lemmatized_tokens.append(lemmatized_sentence)

    return lemmatized_tokens

# function to calculate semantic similarity
def similarity_calculator(doc1, doc2):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([doc1, doc2])
    similarity_score = cosine_similarity(X[0:1], X[1:2])
    return similarity_score[0][0]
