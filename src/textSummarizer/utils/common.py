import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and convert it into a ConfigBox object

    Args:
        path_to_yaml (str): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: Empty file
    
    Returns:
        ConfigBox: A ConfigBox type
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully loaded YAML file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"The YAML file is empty.")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create directories if they do not exist
    
    Args:
    path_to_directories (list): A list of directories to be created.
    ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to false.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")
    
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): The path to the file.
    
    Returns:
        str: The size of the file in KB.
    """

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

