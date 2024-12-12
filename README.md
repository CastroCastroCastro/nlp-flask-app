## **NLP Wikipedia Similarity Flask App**

### **Project Description**

This is a Natural Language Processing (NLP) project that compares the similarity between the content of two Wikipedia pages. The web application is built using Flask and leverages NLP techniques such as tokenization, stop word removal, and lemmatization to process the text. It calculates the semantic similarity using TF-IDF vectorization and cosine similarity.

---

### **Features**

- **Wikipedia Content Fetching:** Uses the Wikipedia API to retrieve content from specified Wikipedia pages.
- **NLP Processing:** Implements preprocessing steps like tokenization, stop word removal, and lemmatization.
- **Semantic Similarity Calculation:** Computes the similarity score between two pages using TF-IDF and cosine similarity.
- **Flask Web App:** Provides a simple web interface to input Wikipedia pages and view the similarity results.
- **Dynamic Display:** Shows processed tokens and the calculated similarity score in the web interface.

---

### **Technologies Used**

- **Python** (Flask, NLTK, Wikipedia-API, scikit-learn)
- **HTML/CSS** (Frontend)
- **JavaScript** (Frontend interaction)
- **Flask** (Web Framework)

---

### **Project Structure**

```
nlp-flask-app/
├── app.py
├── nlpLogic.py
├── requirements.txt
├── vercel.json
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
└── README.md
```

---

### **Setup Instructions**

Follow these steps to run the project locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/CastroCastroCastro/nlp-flask-app.git
   cd nlp-flask-app
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask App**

   ```bash
   python app.py
   ```

5. **Access the App**

   Open your browser and go to `http://127.0.0.1:5000`.

---

### **How to Use the App**

1. Enter the titles of two Wikipedia pages in the input fields.
2. Click the **"Compare"** button.
3. View the similarity score and the processed tokens for each page.

---

### **Example Input and Output**

- **Input Wikipedia Pages:**
  - Page 1: *Albert Einstein*
  - Page 2: *Isaac Newton*

- **Output:**
  ```
  Similarity Score: 0.65
  ```

  Displays the processed tokens and the similarity score between the two pages.

---

### **Future Improvements**

- **Deployment Fix:** Resolve the current deployment issue on Vercel caused by the serverless function size limit.
- **Model Optimization:** Optimize NLP models and libraries to reduce deployment size.
- **Error Handling:** Improve error handling for edge cases, such as network issues or invalid inputs.
- **UI Enhancements:** Improve the user interface and experience with better styling and loading indicators.

---

### **Author**

**Jonathan Castro**

- **Email:** [castr385@umn.edu](mailto:castr385@umn.edu)
- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/jonathancastro-/)
- **Personal Website:** [castrojonathan.com](https://castrojonathan.com)

---
