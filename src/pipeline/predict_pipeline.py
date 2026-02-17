
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 CreditScore: int,
                 AnnualIncome: int,
                 LoanAmount: int,
                 LoanDuration: int,
                 Age: int,
                 EmploymentStatus: str,
                 MaritalStatus: str,
                 NumberOfDependents: int,
                 EducationLevel: str,
                 HomeOwnershipStatus: str,
                 MonthlyDebtPayments: int,
                 CreditCardUtilizationRate: float,
                 NumberOfOpenCreditLines: int,
                 NumberOfCreditInquiries: int,
                 DebtToIncomeRatio: float,
                 BankruptcyHistory: int,
                 LoanPurpose: str,
                 PreviousLoanDefaults: int,
                 InterestRate: float,
                 PaymentHistory: int,
                 SavingsAccountBalance: int,
                 CheckingAccountBalance: int,
                 InvestmentAccountBalance: int,
                 RetirementAccountBalance: int,
                 EmergencyFundBalance: int,
                 TotalAssets: int,
                 TotalLiabilities: int,
                 NetWorth: int,
                 LengthOfCreditHistory: int,
                 MortgageBalance: int,
                 RentPayments: int,
                 AutoLoanBalance: int,
                 PersonalLoanBalance: int,
                 StudentLoanBalance: int,
                 UtilityBillsPaymentHistory: float,
                 HealthInsuranceStatus: str,
                 LifeInsuranceStatus: str,
                 CarInsuranceStatus: str,
                 HomeInsuranceStatus: str,
                 OtherInsurancePolicies: int,
                 EmployerType: str,
                 JobTenure: int,
                 MonthlySavings: int,
                 AnnualBonuses: int,
                 AnnualExpenses: int,
                 MonthlyHousingCosts: int,
                 MonthlyTransportationCosts: int,
                 MonthlyFoodCosts: int,
                 MonthlyHealthcareCosts: int,
                 MonthlyEntertainmentCosts: int
                 ):
        
        self.CreditScore = CreditScore
        self.AnnualIncome = AnnualIncome
        self.LoanAmount = LoanAmount
        self.LoanDuration = LoanDuration
        self.Age = Age
        self.EmploymentStatus = EmploymentStatus
        self.MaritalStatus = MaritalStatus
        self.NumberOfDependents = NumberOfDependents
        self.EducationLevel = EducationLevel
        self.HomeOwnershipStatus = HomeOwnershipStatus
        self.MonthlyDebtPayments = MonthlyDebtPayments
        self.CreditCardUtilizationRate = CreditCardUtilizationRate
        self.NumberOfOpenCreditLines = NumberOfOpenCreditLines
        self.NumberOfCreditInquiries = NumberOfCreditInquiries
        self.DebtToIncomeRatio = DebtToIncomeRatio
        self.BankruptcyHistory = BankruptcyHistory
        self.LoanPurpose = LoanPurpose
        self.PreviousLoanDefaults = PreviousLoanDefaults
        self.InterestRate = InterestRate
        self.PaymentHistory = PaymentHistory
        self.SavingsAccountBalance = SavingsAccountBalance
        self.CheckingAccountBalance = CheckingAccountBalance
        self.InvestmentAccountBalance = InvestmentAccountBalance
        self.RetirementAccountBalance = RetirementAccountBalance
        self.EmergencyFundBalance = EmergencyFundBalance
        self.TotalAssets = TotalAssets
        self.TotalLiabilities = TotalLiabilities
        self.NetWorth = NetWorth
        self.LengthOfCreditHistory = LengthOfCreditHistory
        self.MortgageBalance = MortgageBalance
        self.RentPayments = RentPayments
        self.AutoLoanBalance = AutoLoanBalance
        self.PersonalLoanBalance = PersonalLoanBalance
        self.StudentLoanBalance = StudentLoanBalance
        self.UtilityBillsPaymentHistory = UtilityBillsPaymentHistory
        self.HealthInsuranceStatus = HealthInsuranceStatus
        self.LifeInsuranceStatus = LifeInsuranceStatus
        self.CarInsuranceStatus = CarInsuranceStatus
        self.HomeInsuranceStatus = HomeInsuranceStatus
        self.OtherInsurancePolicies = OtherInsurancePolicies
        self.EmployerType = EmployerType
        self.JobTenure = JobTenure
        self.MonthlySavings = MonthlySavings
        self.AnnualBonuses = AnnualBonuses
        self.AnnualExpenses = AnnualExpenses
        self.MonthlyHousingCosts = MonthlyHousingCosts
        self.MonthlyTransportationCosts = MonthlyTransportationCosts
        self.MonthlyFoodCosts = MonthlyFoodCosts
        self.MonthlyHealthcareCosts = MonthlyHealthcareCosts
        self.MonthlyEntertainmentCosts = MonthlyEntertainmentCosts

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "CreditScore": [self.CreditScore],
                "AnnualIncome": [self.AnnualIncome],
                "LoanAmount": [self.LoanAmount],
                "LoanDuration": [self.LoanDuration],
                "Age": [self.Age],
                "EmploymentStatus": [self.EmploymentStatus],
                "MaritalStatus": [self.MaritalStatus],
                "NumberOfDependents": [self.NumberOfDependents],
                "EducationLevel": [self.EducationLevel],
                "HomeOwnershipStatus": [self.HomeOwnershipStatus],
                "MonthlyDebtPayments": [self.MonthlyDebtPayments],
                "CreditCardUtilizationRate": [self.CreditCardUtilizationRate],
                "NumberOfOpenCreditLines": [self.NumberOfOpenCreditLines],
                "NumberOfCreditInquiries": [self.NumberOfCreditInquiries],
                "DebtToIncomeRatio": [self.DebtToIncomeRatio],
                "BankruptcyHistory": [self.BankruptcyHistory],
                "LoanPurpose": [self.LoanPurpose],
                "PreviousLoanDefaults": [self.PreviousLoanDefaults],
                "InterestRate": [self.InterestRate],
                "PaymentHistory": [self.PaymentHistory],
                "SavingsAccountBalance": [self.SavingsAccountBalance],
                "CheckingAccountBalance": [self.CheckingAccountBalance],
                "InvestmentAccountBalance": [self.InvestmentAccountBalance],
                "RetirementAccountBalance": [self.RetirementAccountBalance],
                "EmergencyFundBalance": [self.EmergencyFundBalance],
                "TotalAssets": [self.TotalAssets],
                "TotalLiabilities": [self.TotalLiabilities],
                "NetWorth": [self.NetWorth],
                "LengthOfCreditHistory": [self.LengthOfCreditHistory],
                "MortgageBalance": [self.MortgageBalance],
                "RentPayments": [self.RentPayments],
                "AutoLoanBalance": [self.AutoLoanBalance],
                "PersonalLoanBalance": [self.PersonalLoanBalance],
                "StudentLoanBalance": [self.StudentLoanBalance],
                "UtilityBillsPaymentHistory": [self.UtilityBillsPaymentHistory],
                "HealthInsuranceStatus": [self.HealthInsuranceStatus],
                "LifeInsuranceStatus": [self.LifeInsuranceStatus],
                "CarInsuranceStatus": [self.CarInsuranceStatus],
                "HomeInsuranceStatus": [self.HomeInsuranceStatus],
                "OtherInsurancePolicies": [self.OtherInsurancePolicies],
                "EmployerType": [self.EmployerType],
                "JobTenure": [self.JobTenure],
                "MonthlySavings": [self.MonthlySavings],
                "AnnualBonuses": [self.AnnualBonuses],
                "AnnualExpenses": [self.AnnualExpenses],
                "MonthlyHousingCosts": [self.MonthlyHousingCosts],
                "MonthlyTransportationCosts": [self.MonthlyTransportationCosts],
                "MonthlyFoodCosts": [self.MonthlyFoodCosts],
                "MonthlyHealthcareCosts": [self.MonthlyHealthcareCosts],
                "MonthlyEntertainmentCosts": [self.MonthlyEntertainmentCosts]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
