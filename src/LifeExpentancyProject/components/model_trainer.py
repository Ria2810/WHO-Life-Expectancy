import pandas as pd
import os
from LifeExpentancyProject import logger
from sklearn.ensemble import RandomForestRegressor
import joblib
from LifeExpentancyProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        Train = train_data.drop(self.config.target_column, axis=1)
        x_test = test_data.drop(self.config.target_column, axis=1)
        Target = train_data[self.config.target_column]
        y_test = test_data[self.config.target_column]


        lr = RandomForestRegressor(n_estimators=self.config.n_estimators, max_depth=self.config.max_depth,  min_samples_split=self.config.min_samples_split)
        lr.fit(Train, Target)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))