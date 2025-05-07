# MediScan AI

MediScan AI is a smart medical report analyzer that leverages AI agents to provide diagnoses based on uploaded medical reports. It supports both a web-based interface using Streamlit and a Flask-based backend for flexible deployment.

---

## Features

- **Streamlit Interface**: Upload medical reports and get instant diagnoses via a user-friendly web interface.
- **Flask Backend**: A robust backend for handling file uploads and running AI agents.
- **AI Agents**: Specialized agents (Cardiologist, Psychologist, Pulmonologist) analyze medical reports and provide individual diagnoses.
- **Multidisciplinary Team**: Combines individual diagnoses into a final comprehensive diagnosis.
- **Concurrent Processing**: Uses multithreading for efficient analysis.

---

## Requirements

Ensure you have Python 3.8 or later installed. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Dependencies

The `requirements.txt` file includes:

- `streamlit`: For the web-based interface.
- `flask`: For the backend server.
- `langchain-core`: Core library for AI agents.
- `langchain-groq`: Additional AI functionality.
- `concurrent.futures`: For multithreading.
- `jinja2`: Template rendering for Flask.
- `numpy`: Numerical computations.
- `pandas`: Data manipulation.
- `requests`: HTTP requests.

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/mediscan_ai.git
    cd mediscan_ai
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Create necessary directories**:
    Ensure the following directories exist:
    - `uploads/`: For storing uploaded medical reports.
    - `results/`: For saving final diagnosis reports.

---

## Usage

### Streamlit Interface

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open the provided URL in your browser.
3. Upload a `.txt` medical report and view the diagnosis.

### Flask Backend

1. Run the Flask app:
    ```bash
    python app.py
    ```
2. Access the app at [https://medisum-zckdd6pvfuwuybdcbjg4yn.streamlit.app/](https://medisum-zckdd6pvfuwuybdcbjg4yn.streamlit.app/).
3. Upload a `.txt` medical report and view the diagnosis.

---

## Project Structure

```
mediscan_ai/
├── app.py                # Streamlit app
├── backend/
│   ├── app.py            # Flask backend
│   ├── ai_agents.py      # AI agent logic
│   └── utils.py          # Utility functions
├── uploads/              # Directory for uploaded reports
├── results/              # Directory for final diagnosis reports
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## Example Workflow

1. Upload a medical report (e.g., `Medical_Report_1.txt`).
2. The AI agents analyze the report:
    - **Cardiologist**: Provides a cardiovascular diagnosis.
    - **Psychologist**: Provides a psychological diagnosis.
    - **Pulmonologist**: Provides a pulmonary diagnosis.
3. The Multidisciplinary Team combines these diagnoses into a final report.
4. The final diagnosis is saved in `results/final_diagnosis.txt`.

---

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

