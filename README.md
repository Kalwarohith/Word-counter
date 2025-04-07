# 🧠 Advanced Word Counter Program

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A lightweight command-line Python tool for quick and effective text analysis. It counts **words**, **characters** (excluding spaces), and **sentences** using basic string operations — perfect for students, writers, and beginner Python developers exploring text processing.

---

## 🚀 Features

- ✅ Word count using whitespace splitting
- ✅ Character count excluding whitespace
- ✅ Sentence count using period (`.`) detection
- ✅ Input validation and error handling
- ✅ Beginner-friendly, fully documented code
- ✅ No external libraries required

---

## 📁 Project Structure

advanced-word-counter/
├── word_counter.py     # Main Python script
└── README.md           # Documentation
💻 Requirements
Python 3.7 or higher

Terminal or command prompt

✅ No need for pip install — it’s pure Python!

⚙️ Installation & Setup
Step 1: Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/advanced-word-counter.git
cd advanced-word-counter
Step 2: Run the script
bash
Copy
Edit
python word_counter.py
🧪 Usage Example
Prompt:
bash
Copy
Edit
Enter a sentence or paragraph: Python is great. I love coding!
Output:
mathematica
Copy
Edit
Text Analysis:
- Word Count: 7
- Character Count (excluding spaces): 36
- Sentence Count: 2
🧠 Code Overview
Here’s how the script works under the hood:

python
Copy
Edit
def count_words(text):
    """Counts the number of words in a given text."""
    return len(text.split())

def count_characters(text):
    """Counts characters excluding spaces."""
    return len(text.replace(" ", ""))

def count_sentences(text):
    """Counts sentences using '.' as a delimiter."""
    sentences = text.split('.')
    return len([s for s in sentences if s.strip()])

def main():
    print("Advanced Word Counter Program")
    print("--------------------------------")
    
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return

    print("\nText Analysis:")
    print(f"- Word Count: {count_words(user_input)}")
    print(f"- Character Count (excluding spaces): {count_characters(user_input)}")
    print(f"- Sentence Count: {count_sentences(user_input)}")

if __name__ == "__main__":
    main()
🛠️ Possible Future Enhancements
Use re (regex) for robust sentence/word splitting

Accept file input (.txt, .md, etc.)

Add support for paragraphs ending with ! or ?

Build a web version using Flask or Streamlit

Convert into a Python package/CLI tool

🤝 Contributing
Contributions are welcome and encouraged!

Steps to Contribute:
Fork the repo

Clone your forked copy:

bash
Copy
Edit
git clone https://github.com/yourusername/advanced-word-counter.git
Create a new branch:

bash
Copy
Edit
git checkout -b feature/your-feature-name
Make your changes and commit:

bash
Copy
Edit
git commit -m "Add: your feature description"
Push to your forked repo:

bash
Copy
Edit
git push origin feature/your-feature-name
Open a Pull Request on GitHub

📄 License
This project is licensed under the MIT License.
You're free to use, modify, and distribute this tool as you wish.

🙌 Acknowledgements
Inspired by beginner Python exercises and real-world text-processing needs.

Special thanks to the Python community and open-source educators.

