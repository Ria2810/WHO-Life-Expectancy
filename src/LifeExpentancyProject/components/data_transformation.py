import os
from LifeExpentancyProject import logger
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from LifeExpentancyProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):

        df = pd.read_csv(self.config.data_path)

        # Handling missing values
        imputer = SimpleImputer(missing_values=np.nan, strategy='mean', fill_value=None)

        df['Life expectancy ']=imputer.fit_transform(df[['Life expectancy ']])
        df['Adult Mortality']=imputer.fit_transform(df[['Adult Mortality']])
        df['Alcohol']=imputer.fit_transform(df[['Alcohol']])
        df['Hepatitis B']=imputer.fit_transform(df[['Hepatitis B']])
        df[' BMI ']=imputer.fit_transform(df[[' BMI ']])
        df['Polio']=imputer.fit_transform(df[['Polio']])
        df['Total expenditure']=imputer.fit_transform(df[['Total expenditure']])
        df['Diphtheria ']=imputer.fit_transform(df[['Diphtheria ']])
        df['GDP']=imputer.fit_transform(df[['GDP']])
        df['Population']=imputer.fit_transform(df[['Population']])
        df[' thinness  1-19 years']=imputer.fit_transform(df[[' thinness  1-19 years']])
        df[' thinness 5-9 years']=imputer.fit_transform(df[[' thinness 5-9 years']])
        df['Income composition of resources']=imputer.fit_transform(df[['Income composition of resources']])
        df['Schooling']=imputer.fit_transform(df[['Schooling']])

        # Handling Outliers

        # Specify the list of columns you want to handle outliers for
        cols_to_handle_outliers = [
            'Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure',
            'Hepatitis B', 'Measles ', ' BMI ', 'under-five deaths ', 'Polio',
            'Total expenditure', 'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population',
            ' thinness  1-19 years', ' thinness 5-9 years',
            'Income composition of resources', 'Schooling'
        ]

        # Perform outlier handling for each specified column
        for col_name in cols_to_handle_outliers:
            # Calculate quartiles and IQR
            q1 = df[col_name].quantile(0.25)
            q3 = df[col_name].quantile(0.75)
            iqr = q3 - q1

            # Define the lower and upper bounds for outliers
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            # Replace outliers with the mean value of the column
            df[col_name] = np.where((df[col_name] > upper_bound) | (df[col_name] < lower_bound), np.mean(df[col_name]), df[col_name])

       
        # Handling categorical values
        
        cols_to_encode = ['Country', 'Status']

        # Apply label encoding to X
        label_encoder_df = LabelEncoder()
        for col in cols_to_encode:
            df[col] = label_encoder_df.fit_transform(df[col])
        
        # Scaling
        cols_to_scale = ['Country', 'Year', 'Adult Mortality',
       'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B',
       'Measles ', ' BMI ', 'under-five deaths ', 'Polio', 'Total expenditure',
       'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population',
       ' thinness  1-19 years', ' thinness 5-9 years',
       'Income composition of resources', 'Schooling']

        # Apply Min-Max scaling to the specified columns
        scaler = MinMaxScaler()
        df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
        
        
        # Split the data

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(df)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)