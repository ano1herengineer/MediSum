import streamlit as st
from Utils.Agent import Cardiologist, Psychologist, Pulmonologist, MultidisciplinaryTeam
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

# Constants
UPLOAD_FOLDER = 'uploads'
RESULT_PATH = 'results/final_diagnosis.txt'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.dirname(RESULT_PATH), exist_ok=True)

# Set the Groq API key as an environment variable
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

# Streamlit App
st.title("MediScan AI – Smart Medical Report Analyzer")
st.write("Upload a medical report in `.txt` format or directly input text to analyze and get a diagnosis.")

# Option to choose input method
input_method = st.radio(
    "Choose how to provide the medical report:",
    ("Upload a .txt file", "Enter text directly")
)

# Initialize a variable to hold the medical report content
medical_report = None

if input_method == "Upload a .txt file":
    # File uploader for .txt files
    uploaded_file = st.file_uploader("Upload your medical report", type=["txt"])
    if uploaded_file:
        # Save uploaded file
        filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"File uploaded successfully: {uploaded_file.name}")

        # Read the medical report
        with open(filepath, "r") as file:
            medical_report = file.read()

        # Display the uploaded report
        st.subheader("Uploaded Medical Report")
        st.text_area("Medical Report Content", medical_report, height=300)

elif input_method == "Enter text directly":
    # Text area for direct text input
    medical_report = st.text_area("Enter the medical report text here:", height=300)

# Analyze the report if content is available
if medical_report and st.button("Analyze Report"):
    st.info("Analyzing the report. Please wait...")

    # Run individual specialists
    agents = {
        "Cardiologist": Cardiologist(medical_report),
        "Psychologist": Psychologist(medical_report),
        "Pulmonologist": Pulmonologist(medical_report)
    }

    responses = {}
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(agent.run): name for name, agent in agents.items()}
        for future in as_completed(futures):
            agent_name = futures[future]
            responses[agent_name] = future.result()

    # Run multidisciplinary agent
    team_agent = MultidisciplinaryTeam(
        cardiologist_report=responses["Cardiologist"],
        psychologist_report=responses["Psychologist"],
        pulmonologist_report=responses["Pulmonologist"]
    )
    final_diagnosis = team_agent.run()

    # Save the diagnosis
    final_diagnosis_text = "### Final Diagnosis:\n\n" + final_diagnosis
    with open(RESULT_PATH, "w") as result_file:
        result_file.write(final_diagnosis_text)

    # Display the final diagnosis
    st.subheader("Final Diagnosis")
    st.text_area("Diagnosis", final_diagnosis_text, height=300)
    st.success("Analysis complete. Final diagnosis displayed above.")