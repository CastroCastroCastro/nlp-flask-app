from flask import Flask, request, jsonify, render_template
from nlpLogic import get_wiki, process_text, get_wordnet_pos, similarity_calculator


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_pages():
    data = request.json
    page1 = get_wiki(data.get('content1'))
    page2 = get_wiki(data.get('content2'))
    
    if page1 == "Page Not Found" or page2 == "Page Not Found":
        return jsonify({"error": "Page Not Found"}), 404
    
    page1_tokens = process_text(page1)
    page2_tokens = process_text(page2)
    
    # Flatten Tokenized Sentences for Similarity Calculation
    flat_text1 = " ".join([" ".join(sentence) for sentence in page1_tokens])
    flat_text2 = " ".join([" ".join(sentence) for sentence in page2_tokens])
    
    similarity_score = similarity_calculator(flat_text1, flat_text2)
    
    return jsonify ({
        "similarity_score": similarity_score, 
        "page1_tokens": page1_tokens,
        "page2_tokens": page2_tokens
    })

if __name__ == '__main__':
    app.run(debug=True)