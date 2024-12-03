import wikipediaapi
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('averaged_perceptron_tagger_eng')

def get_wiki(pageName):
    wiki = wikipediaapi.Wikipedia(
    language="en",
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="'nlpProject(castr385@umn.edu)"
    )
    
    page = wiki.page(pageName)
    if page.exists():
        return page.text
    else:
        return("Page Not Found")


# Function to map NLTK POS tags to WordNet POS tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ  # Adjective
    elif tag.startswith('V'):
        return wordnet.VERB  # Verb
    elif tag.startswith('N'):
        return wordnet.NOUN  # Noun
    elif tag.startswith('R'):
        return wordnet.ADV  # Adverb
    else:
        return wordnet.NOUN  # Default to noun

# Main text processing function
def process_text(text):
    # Step 1: Sentence Segmentation
    sentences = sent_tokenize(text)

    # Step 2: Tokenization
    tokens = [word_tokenize(sentence) for sentence in sentences]
    # print("Tokens:", tokens)

    # Step 3: Stop Word Removal
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [
        [word for word in sentence if word.lower() not in stop_words and word.isalpha()]
        for sentence in tokens
    ]
    # print("Filtered Tokens:", filtered_tokens)

    # Step 4: POS Tagging and Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = []
    for sentence in filtered_tokens:
        pos_tagged = nltk.pos_tag(sentence)  # POS tagging
        lemmatized_sentence = [
            lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tagged
        ]
        lemmatized_tokens.append(lemmatized_sentence)
    
    # print("Lemmatized Tokens:", lemmatized_tokens)
    return lemmatized_tokens

# Test the process_text function
# sample_text = "Albert Einstein was a physicist. He developed the theory of relativity."
# processed = process_text(sample_text)
# print(processed)

import spacy

nlp = spacy.load("en_core_web_sm")

def parse_dependencies(text1):
    doc = nlp(text1)
    print("Dependency Parsing:")
    for token in doc:
        print(f"{token.text} -> {token.dep_} -> {token.head.text}")
        
#calculate semantic value
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity_calculator(doc1, doc2):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([doc1, doc2])
    similarity_score = cosine_similarity(X[0:1], X[1:2])
    return similarity_score[0][0]

def main():
    print("Welcome to the Wikipedia Text Similarity Tool!")
    
    # Input Wikipedia Titles
    title1 = input("Enter the title of the first Wikipedia page: ")
    title2 = input("Enter the title of the second Wikipedia page: ")
    
    try:
        # Fetch Wikipedia Content
        text1 = get_wiki(title1)
        text2 = get_wiki(title2)

        # Print the first 500 characters of each text for sanity check
        print(f"\nFirst 50 characters of Text 1 ({title1}):\n{text1[:50]}")
        print(f"\nFirst 50 characters of Text 2 ({title2}):\n{text2[:50]}")
        
        # Preprocess the Texts
        processed_text1 = process_text(text1)
        processed_text2 = process_text(text2)

        # Flatten Tokenized Sentences for Similarity Calculation
        flat_text1 = " ".join([" ".join(sentence) for sentence in processed_text1])
        flat_text2 = " ".join([" ".join(sentence) for sentence in processed_text2])
        
        # Dependency Parsing on Raw Text (Optional)
        print("\nDependency Parsing for Text 1:")
        parse_dependencies(text1[:50])  # Parse the first 1000 characters of raw text
        
        print("\nDependency Parsing for Text 2:")
        parse_dependencies(text2[:50])  # Parse the first 1000 characters of raw text
        
        # Calculate Similarity
        similarity_score = similarity_calculator(flat_text1, flat_text2)
        print(f"\nSimilarity Score between the two pages: {similarity_score:.2f}")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()