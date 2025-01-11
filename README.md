# Arogya-Pandit

# Automated ATS Resume Scoring using Large Language Models and Gemini API Integration

![image](https://github.com/user-attachments/assets/e2932afd-7e54-4312-99f3-04be0c47695f)

# Overview

Welcome to the Gemini Applicant Tracking System (ATS)! This system is developed using the powerful Gemini model to streamline the hiring process by analyzing job descriptions and resumes. It provides valuable insights such as job description match, missing keywords, and profile summary.


## Features
- **Job Description Match:** The system evaluates how well a candidate's resume matches the provided job description, helping recruiters quickly identify suitable candidates.

- **Missing Keywords:** It identifies keywords or skills that are missing in the resume but are crucial for the job, enabling recruiters to guide candidates on enhancing their profiles.

- **Profile Summary:** The system generates a concise profile summary highlighting key strengths and qualifications, facilitating a quick understanding of the candidate's suitability for the position.

## Requirements
- Python 3.10
- Gemini model api key (Note: Ensure you have the necessary credentials and permissions to access the Gemini API)

  ## Installation
1. Clone the repository:
   ```base
   Git clone :- https://github.com/mukeshkumarsoni4/Arogya-Pandit.git
     ```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Gemini API credentials:
 - Obtain API credentials from the makersuit platform.

 - Create a file named .env in the project root directory.

 - Add the following lines to .env:
   ```bash
   GOOGLE_API_KEY= "your_api_key"
   ```

# Technologies Used
1. Streamlit: An open-source app framework for creating web apps with Python.
2. PyPDF2: A PDF toolkit for extracting text from PDF files.
3. google.generativeai: Google's Generative AI for generating intelligent responses.
4. python-dotenv: A module to load environment variables from a .env file.

# Brief Overview of Technologies
1. Streamlit: Allows the creation of interactive web applications with minimal code, perfect for data-driven applications.
2. PyPDF2: Helps in reading and extracting text from PDF files, which is crucial for processing resume files.
3. python-dotenv: Manages environment variables, keeping sensitive data like API keys secure and separate from the codebase.

   ## Usage
1. Run the application:
```bash
streamlit run app.py
```

2. Access the application through your web browser at http://localhost:8501/

3. Input the job description and candidate's resume in the provided fields.

4. Click the "Submit" button to initiate the analysis.

5. Review the results, including the job description match, missing keywords, and profile summary.

# Project Demonstration & Documentation

## Demonstration Video

[![Watch the video](https://img.youtube.com/vi/udUqNwTcHBs/0.jpg)](https://youtu.be/udUqNwTcHBs)


## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

## Contact
If you have any questions or issues, feel free to reach out to the maintainers:

Maintainer: Mukesh Kumar Soni
Email: mukeshkumar32670@gmail.com

Happy recruiting with Gemini ATS!

   
