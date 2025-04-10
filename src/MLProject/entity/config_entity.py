from dataclasses import dataclass
from pathlib import Path

# An entity is a return type of a function

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path