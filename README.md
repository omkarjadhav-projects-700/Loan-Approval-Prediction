# Loan Approval Prediction

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

## 📌 Project Overview

This project is a comprehensive **Loan Approval Prediction System** designed to assist financial institutions in automating the loan eligibility process. Leveraging machine learning algorithms, the application analyzes various applicant details—such as credit history, income, employment status, and more—to predict the likelihood of loan approval.

The application is deployed with a user-friendly interface built using **Streamlit**, allowing users to input data and receive instant predictions. To insure portability and consistency, the application is containerized using **Docker**.

## 🚀 Key Features

- **Interactive Web Interface**: Built with Streamlit for seamless user interaction.
- **Real-time Predictions**: Instant feedback on loan approval status based on input data.
- **Comprehensive Data Inputs**: Detailed form capturing financial, personal, and asset-related information.
- **Machine Learning Pipeline**: Robust preprocessing and prediction pipeline using Scikit-Learn.
- **Containerized Deployment**: Fully Dockerized for easy deployment across environments.

## 🛠️ Tech Stack And Tools

| Technology | Description |
| :--- | :--- |
| **Python** | Core programming language for data processing and modeling. |
| **Streamlit** | Framework for building the interactive web application. |
| **Scikit-Learn** | Library used for building the machine learning model. |
| **Pandas & NumPy** | Creating data structures and performing numerical analysis. |
| **Docker** | Containerization platform for consistent deployment. |

## ⚙️ Setup and Installation

### Prerequisites

- Python 3.9+
- Docker (optional, for containerized run)

### Local Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/loan-approval-prediction.git
    cd loan-approval-prediction
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    streamlit run app.py
    ```

## 🐳 Docker Usage

To run the application using Docker, follow these steps:

1.  **Build the Docker Image**
    ```bash
    docker build -t loan-prediction-app .
    ```

2.  **Run the Container**
    ```bash
    docker run -p 8501:8501 loan-prediction-app
    ```

    Access the application at `http://localhost:8501`.

## 📂 Project Structure

```bash
Loan Approval Prediction/
├── .Dockerignore
├── .gitignore
├── .gitlab-ci.yml
├── .jenkinsfile
├── Dockerfile              # Docker configuration
├── Preprocessing.ipynb     # Data preprocessing notebook
├── README.md               # Project documentation
├── app.py                  # Main Streamlit application
├── artifacts/              # Model artifacts folder
├── decision_tree_classifier.ipynb
├── financial_risk_analysis_large.csv
├── logistic_regression.ipynb
├── logs/                   # Application logs
├── random_forest_classifier.ipynb
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup file
├── src/                    # Source code for pipelines
│   └── pipeline/
│       ├── predict_pipeline.py
│       └── ...
└── xgboost_classifier.ipynb
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
