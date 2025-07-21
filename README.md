# IBM Salary Prediction Project

This project is a data science solution for predicting salaries based on various features. It explores three machine learning models and selects the most effective one for deployment. The repository includes data preprocessing, model training and evaluation, and a user interface for prediction.

## 🗂️ Project Structure

```
.
├── IBM_UI.py                    # Python script for the user interface
├── Ibm (1).ipynb                # Jupyter notebook with EDA and ML models
├── ridge_salary_model (1).pkl  # Serialized model selected as best performing
└── README.md                    # Project documentation
```

## 🔍 Machine Learning Models Used

- Linear Regression
- Ridge Regression
- Lasso Regression

After evaluating the performance of all three models, the best-performing model (Ridge Regression) was selected and saved for deployment.

## 📈 How to Run

### Prerequisites

Ensure Python 3.x is installed with the following libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Launch the Notebook

To explore data analysis, model training, and evaluation:

```bash
jupyter notebook "Ibm (1).ipynb"
```

### Run the UI

To launch the user interface for predictions:

```bash
streamlit run IBM_UI.py
```

## 💾 Model Usage

The best-performing model is saved as `ridge_salary_model (1).pkl`. Load and use it with:

```python
import joblib

# Load the trained Ridge pipeline
ridge_pipeline = joblib.load("ridge_salary_model.pkl")
```

Use this model to predict salary based on input features like job role, experience, etc.

## 📄 License

This project is licensed under the MIT License.
