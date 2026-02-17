import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
import os

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from sklearn.utils import resample

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

# Define mappings at module level for pickling
def apply_mappings(df):
    df = df.copy()
    health_insurance_map = {"Insured": 1, "Uninsured": 0}
    life_insurance_map = {"Insured": 1, "Uninsured": 0}
    car_insurance_map = {"Insured": 1, "Uninsured": 0}
    home_insurance_map = {"Insured": 1, "Uninsured": 0}
    education_level_map = {
        'High School': 1,
        'Associate': 2,
        'Bachelor': 3,
        'Master': 4,
        'Doctorate': 5
    }
    
    if "HealthInsuranceStatus" in df.columns:
        df["HealthInsuranceStatus"] = df["HealthInsuranceStatus"].map(health_insurance_map)
    if "LifeInsuranceStatus" in df.columns:
        df["LifeInsuranceStatus"] = df["LifeInsuranceStatus"].map(life_insurance_map)
    if "CarInsuranceStatus" in df.columns:
        df["CarInsuranceStatus"] = df["CarInsuranceStatus"].map(car_insurance_map)
    if "HomeInsuranceStatus" in df.columns:
        df["HomeInsuranceStatus"] = df["HomeInsuranceStatus"].map(home_insurance_map)
    if "EducationLevel" in df.columns:
        df["EducationLevel"] = df["EducationLevel"].map(education_level_map)
    
    return df

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            logging.info("Defining data transformation pipeline")

            categorical_columns = [
                "LoanPurpose", "HomeOwnershipStatus", "EmploymentStatus", "MaritalStatus", "EmployerType"
            ]
            
            # Step 1: Mapping
            mapping_transformer = FunctionTransformer(apply_mappings, validate=False)

            # Step 2: Column Transformer (OHE)
            # We want to OHE specific columns and pass through the rest
            preprocessor_step = ColumnTransformer(
                transformers=[
                    ("cat", OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False), categorical_columns),
                ],
                remainder='passthrough',
                verbose_feature_names_out=False
            )

            # Step 3: Scaling
            # Apply scaler to everything coming out of the preprocessor_step (which is OHE cols + passed through cols)
            scaler_step = StandardScaler()

            pipeline = Pipeline(steps=[
                ("mapping", mapping_transformer),
                ("preprocessor", preprocessor_step),
                ("scaler", scaler_step)
            ])

            return pipeline

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "LoanApproved"

            # Upsampling only on Training Data
            logging.info("Upsampling minority class in training data")
            
            # Separate majority and minority classes
            df_majority = train_df[train_df[target_column_name] == 0]
            df_minority = train_df[train_df[target_column_name] == 1]
            
            # Upsample minority class
            df_minority_upsampled = resample(
                df_minority, 
                replace=True,     # sample with replacement
                n_samples=len(df_majority),    # to match majority class
                random_state=42
            )
            
            # Combine majority class with upsampled minority class
            train_df_upsampled = pd.concat([df_majority, df_minority_upsampled])
            train_df = train_df_upsampled # overwrite original train_df with upsampled one
            
            logging.info(f"Upsampled train shape: {train_df.shape}")

            input_feature_train_df = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.")

            # Fit on Train, Transform on Train and Test
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)