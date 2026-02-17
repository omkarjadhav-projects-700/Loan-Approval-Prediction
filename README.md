# 🏦 Loan Approval Prediction

<div align="center">
  <img src="https://cdn.simpleicons.org/streamlit/FF4B4B" height="40" alt="Streamlit" />
  <img src="https://cdn.simpleicons.org/python/3776AB" height="40" alt="Python" />
  <img src="https://cdn.simpleicons.org/docker/2496ED" height="40" alt="Docker" />
  <img src="https://cdn.simpleicons.org/pandas/150458" height="40" alt="Pandas" />
  <img src="https://cdn.simpleicons.org/scikit-learn/F7931E" height="40" alt="Scikit-Learn" />
  <img src="https://cdn.simpleicons.org/numpy/013243" height="40" alt="NumPy" />
</div>

<br />

<div align="center">
  <strong>An intelligent system for automating loan eligibility assessments leveraging Machine Learning.</strong>
</div>

<br />

## 📌 Usage & Technologies

This project utilizes a modern stack to deliver accurate predictions within a containerized environment.

| Logo | Technology | Description |
| :---: | :--- | :--- |
| <img src="https://cdn.simpleicons.org/python/3776AB" width="30"/> | **Python** | Core language for data processing and model logic. |
| <img src="https://cdn.simpleicons.org/streamlit/FF4B4B" width="30"/> | **Streamlit** | Interactive web application framework. |
| <img src="https://cdn.simpleicons.org/docker/2496ED" width="30"/> | **Docker** | Containerization for consistent deployment. |
| <img src="https://cdn.simpleicons.org/pandas/150458" width="30"/> | **Pandas** | High-performance data manipulation and analysis. |
| <img src="https://cdn.simpleicons.org/scikit-learn/F7931E" width="30"/> | **Scikit-Learn** | Machine learning library for predictive modeling. |
| <img src="https://cdn.simpleicons.org/numpy/013243" width="30"/> | **NumPy** | Fundamental package for scientific computing. |

## 📖 Project Overview

The **Loan Approval Prediction System** helps financial institutions make data-driven decisions. By analyzing applicant profiles—including credit history, income, and assets—the system predicts loan eligibility with high accuracy. This tool reduces manual review time and mitigates risk.

The application serves a user-friendly interface where loan officers or applicants can input details and receive instant feedback.

## 🚀 Key Features

*   **⚡ Real-Time Predictions**: Instant loan status (Approved/Rejected) based on ML algorithms.
*   **📊 Interactive Dashboard**: Clean, responsive Streamlit UI for easy data entry.
*   **🏭 Containerized**: Production-ready Docker support ensuring "works on my machine" reliability.
*   **📈 Comprehensive Analysis**: Takes into account over 40 financial and personal factors.

## 🐳 Docker Deployment

Run the application instantly using Docker.

1.  **Build the Image**
    ```bash
    docker build -t loan-prediction-app .
    ```

2.  **Run the Container**
    ```bash
    docker run -p 8501:8501 loan-prediction-app
    ```

    Visit `http://localhost:8501` to use the app.

## ⚙️ Local Development Setup

If you prefer running without Docker:

1.  **Clone & Enter**
    ```bash
    git clone https://github.com/yourusername/loan-approval-prediction.git
    cd loan-approval-prediction
    ```

2.  **Environment Setup**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch App**
    ```bash
    streamlit run app.py
    ```

## 📂 Repository Structure

```tree
Loan Approval Prediction/
├── .gitlab-ci.yml          # CI/CD Pipeline Configuration
├── Dockerfile              # Docker Container Definition
├── app.py                  # Main Application Entry Point
├── requirements.txt        # Python Dependencies
├── src/                    # Source Code & Pipelines
│   └── pipeline/           # Training and Prediction Pipelines
├── artifacts/              # Trained Models & Preprocessors
├── notebooks/              # Jupyter Notebooks (Analysis)
└── README.md               # Project Documentation
```

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
