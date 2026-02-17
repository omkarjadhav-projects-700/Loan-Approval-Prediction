import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Loan Approval Prediction", layout="wide")

st.title("Loan Approval Prediction App")
st.markdown("Predict if a loan application will be approved based on applicant details.")

st.sidebar.header("User Input Features")

def user_input_features():
    with st.form("loan_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Personal Info")
            age = st.number_input("Age", min_value=18, max_value=100, value=30)
            marital_status = st.selectbox("Marital Status", ['Single', 'Married', 'Divorced', 'Widowed'])
            education_level = st.selectbox("Education Level", ['High School', 'Associate', 'Bachelor', 'Master', 'Doctorate'])
            dependents = st.number_input("Number of Dependents", min_value=0, max_value=20, value=0)
            employment_status = st.selectbox("Employment Status", ['Employed', 'Self-Employed', 'Unemployed'])
            employer_type = st.selectbox("Employer Type", ['Private', 'Government', 'Self-Employed', 'Unemployed'])
            job_tenure = st.number_input("Job Tenure (Years)", min_value=0, max_value=50, value=5)
            home_ownership = st.selectbox("Home Ownership Status", ['Own', 'Rent', 'Mortgage', 'Other'])

        with col2:
            st.subheader("Loan Details")
            loan_amount = st.number_input("Loan Amount", min_value=1000, value=10000)
            loan_duration = st.number_input("Loan Duration (Months)", min_value=1, value=12)
            loan_purpose = st.selectbox("Loan Purpose", ['Business', 'Home', 'Education', 'Personal', 'Auto', 'Other'])
            interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=5.0)
            
            st.subheader("Insurance Status")
            health_insurance = st.selectbox("Health Insurance", ['Insured', 'Uninsured'])
            life_insurance = st.selectbox("Life Insurance", ['Insured', 'Uninsured'])
            car_insurance = st.selectbox("Car Insurance", ['Insured', 'Uninsured'])
            home_insurance = st.selectbox("Home Insurance", ['Insured', 'Uninsured'])
            other_insurance = st.number_input("Other Insurance Policies", min_value=0, value=0)

        with col3:
            st.subheader("Financial Info")
            income = st.number_input("Annual Income", min_value=0, value=50000)
            credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=700)
            monthly_debt = st.number_input("Monthly Debt Payments", min_value=0, value=500)
            credit_util = st.number_input("Credit Card Utilization Rate", min_value=0.0, max_value=1.0, value=0.3)
            open_credit_lines = st.number_input("Number of Open Credit Lines", min_value=0, value=5)
            credit_inquiries = st.number_input("Number of Credit Inquiries", min_value=0, value=0)
            dti = st.number_input("Debt To Income Ratio", min_value=0.0, value=0.3)
            bankruptcy = st.number_input("Bankruptcy History (Count)", min_value=0, value=0)
            previous_defaults = st.number_input("Previous Loan Defaults", min_value=0, value=0)
            payment_history = st.number_input("Payment History (Score)", min_value=0, value=0)
            credit_history_len = st.number_input("Length of Credit History (Years)", min_value=0, value=5)

        st.subheader("Assets & Liabilities")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            savings = st.number_input("Savings Balance", min_value=0, value=5000)
            checking = st.number_input("Checking Balance", min_value=0, value=2000)
        with c2:
            investment = st.number_input("Investment Balance", min_value=0, value=0)
            retirement = st.number_input("Retirement Balance", min_value=0, value=0)
        with c3:
            emergency = st.number_input("Emergency Fund", min_value=0, value=1000)
            total_assets = st.number_input("Total Assets", min_value=0, value=10000)
        with c4:
            total_liabilities = st.number_input("Total Liabilities", min_value=0, value=5000)
            net_worth = st.number_input("Net Worth", value=5000)
        
        st.subheader("Expenses & Balances")
        e1, e2, e3 = st.columns(3)
        with e1:
            mortgage_bal = st.number_input("Mortgage Balance", min_value=0, value=0)
            rent_pay = st.number_input("Rent Payments", min_value=0, value=0)
            auto_loan_bal = st.number_input("Auto Loan Balance", min_value=0, value=0)
            personal_loan_bal = st.number_input("Personal Loan Balance", min_value=0, value=0)
            student_loan_bal = st.number_input("Student Loan Balance", min_value=0, value=0)

        with e2:
            utility_hist = st.number_input("Utility Payment History", min_value=0.0, value=0.0)
            monthly_savings = st.number_input("Monthly Savings", min_value=0, value=500)
            annual_bonus = st.number_input("Annual Bonuses", min_value=0, value=0)
            annual_xp = st.number_input("Annual Expenses", min_value=0, value=20000)
        
        with e3:
            housing_cost = st.number_input("Monthly Housing Costs", min_value=0, value=1000)
            transport_cost = st.number_input("Monthly Transport Costs", min_value=0, value=200)
            food_cost = st.number_input("Monthly Food Costs", min_value=0, value=400)
            health_cost = st.number_input("Monthly Healthcare Costs", min_value=0, value=100)
            entertainment_cost = st.number_input("Monthly Entertainment Costs", min_value=0, value=100)

        submit_button = st.form_submit_button("Predict Loan Approval")

    if submit_button:
        data = CustomData(
            CreditScore=credit_score,
            AnnualIncome=income,
            LoanAmount=loan_amount,
            LoanDuration=loan_duration,
            Age=age,
            EmploymentStatus=employment_status,
            MaritalStatus=marital_status,
            NumberOfDependents=dependents,
            EducationLevel=education_level,
            HomeOwnershipStatus=home_ownership,
            MonthlyDebtPayments=monthly_debt,
            CreditCardUtilizationRate=credit_util,
            NumberOfOpenCreditLines=open_credit_lines,
            NumberOfCreditInquiries=credit_inquiries,
            DebtToIncomeRatio=dti,
            BankruptcyHistory=bankruptcy,
            LoanPurpose=loan_purpose,
            PreviousLoanDefaults=previous_defaults,
            InterestRate=interest_rate,
            PaymentHistory=payment_history,
            SavingsAccountBalance=savings,
            CheckingAccountBalance=checking,
            InvestmentAccountBalance=investment,
            RetirementAccountBalance=retirement,
            EmergencyFundBalance=emergency,
            TotalAssets=total_assets,
            TotalLiabilities=total_liabilities,
            NetWorth=net_worth,
            LengthOfCreditHistory=credit_history_len,
            MortgageBalance=mortgage_bal,
            RentPayments=rent_pay,
            AutoLoanBalance=auto_loan_bal,
            PersonalLoanBalance=personal_loan_bal,
            StudentLoanBalance=student_loan_bal,
            UtilityBillsPaymentHistory=utility_hist,
            HealthInsuranceStatus=health_insurance,
            LifeInsuranceStatus=life_insurance,
            CarInsuranceStatus=car_insurance,
            HomeInsuranceStatus=home_insurance,
            OtherInsurancePolicies=other_insurance,
            EmployerType=employer_type,
            JobTenure=job_tenure,
            MonthlySavings=monthly_savings,
            AnnualBonuses=annual_bonus,
            AnnualExpenses=annual_xp,
            MonthlyHousingCosts=housing_cost,
            MonthlyTransportationCosts=transport_cost,
            MonthlyFoodCosts=food_cost,
            MonthlyHealthcareCosts=health_cost,
            MonthlyEntertainmentCosts=entertainment_cost
        )
        
        feature_df = data.get_data_as_data_frame()
        st.write("Input Data Summary:")
        st.dataframe(feature_df)
        
        try:
            pipeline = PredictPipeline()
            prediction = pipeline.predict(feature_df)
            
            if prediction[0] == 1:
                st.success("Congratulations! The loan is likely to be APPROVED.")
            else:
                st.error("Sorry, the loan is likely to be REJECTED.")
        except Exception as e:
            st.error(f"Error during prediction: {e}")

if __name__ == "__main__":
    user_input_features()
