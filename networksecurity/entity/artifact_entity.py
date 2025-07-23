
"""This module defines the DataIngestionArtifact class, which is used to represent artifacts produced during the data ingestion process.
            os.makedirs(os.path.dirname(feature_store_file_path), exist_ok=True)"""

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