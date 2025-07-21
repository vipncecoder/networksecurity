
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