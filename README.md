# PolishMyMail

PolishMyMail is a Streamlit-based application that assists users in writing structured and well-written emails. The app leverages LangChain and OpenAI to refine email messages based on user preferences, providing both formal and informal tones and optional summaries.

Try the live version of PolishMyMail on Render: [PolishMyMail on Render](https://polishmyemail.onrender.com/)

---

## **Features**

1. **Tone Customization**: Select between formal, informal, or original tones for your email.
2. **Email Summarization**: Generate concise summaries of lengthy emails.
3. **Real-Time Feedback**: Preview the polished email as it is being generated.

---

## **Technologies Used**

- **[Streamlit](https://streamlit.io/)**: For building the interactive user interface.
- **[LangChain](https://langchain.com/)**: Framework for managing AI-driven workflows.
- **[OpenAI](https://openai.com/)**: For email refinement and natural language processing.
- **Python**: The core programming language for the application.

---

## **Repository Structure**

```plaintext
PolishMyMail/
├── app/
│   ├── __init__.py          # Initialization for the app package
│   ├── email_processor.py   # Workflow and email processing logic
│   ├── ai_integration.py    # OpenAI integration
│   ├── streamlit_utils.py   # Streamlit-specific helpers
│   └── config.py            # Configuration and API keys
├── streamlit_app.py         # Main Streamlit application
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
└── .gitignore               # Files and directories to ignore in Git
```

---

## **Getting Started**

Follow these steps to set up and run the application locally:

### Prerequisites

1. Python 3.11 or above.
2. An OpenAI API key (you can obtain one from [OpenAI](https://openai.com/)).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/PolishMyMail.git
   cd PolishMyMail
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key as an environment variable:

   ```bash
   export OPEN_AI_KEY="your-api-key"   # On Windows, use `set OPEN_AI_KEY="your-api-key"`
   ```

### Run the Application

Launch the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Access the application in your browser at `http://localhost:8501`.

---

## **Usage**

1. Enter your email draft in the provided text area.
2. Choose a tone for the email: **Formal**, **Informal**, or **Original**.
3. Check the **Summarize Email** option if a concise version is needed.
4. Click the **Polish My Email** button to receive a refined email.

---

## **Contributing**

Contributions are welcome! To propose a new feature or fix a bug:

1. Fork the repository.
2. Create a new branch for your feature:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes and push the branch:

   ```bash
   git push origin feature-name
   ```

4. Open a pull request with a detailed description.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgments**

- **OpenAI** for their powerful language models.
- **Streamlit** for simplifying app development.
- The open-source community for inspiring this project.

