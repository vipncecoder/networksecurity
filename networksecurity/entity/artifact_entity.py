
"""This module defines the DataIngestionArtifact class, which is used to represent artifacts produced during the data ingestion process.
            os.makedirs(os.path.dirname(feature_store_file_path), exist_ok=True) """
"""This module defines the DataValidationArtifact class, which is used to represent artifacts produced during the data validation process.
It includes paths for valid and invalid training and testing data, as well as a drift report file path."""

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Data class for data ingestion artifacts.
    """
    trained_file_path:str
    test_file_path:str


@dataclass
class DataValidationArtifact:
    """
    Data class for data validation artifacts.
    """
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str    

"""This module defines the ModelTrainerArtifact class, which is used to represent artifacts produced during the model training process.
It includes paths for the trained model file and metric artifacts for both training and testing datasets."""
@dataclass
class ClassificationMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float
    
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    train_metric_artifact: ClassificationMetricArtifact
    test_metric_artifact: ClassificationMetricArtifact    