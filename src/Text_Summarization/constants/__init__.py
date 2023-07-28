# feeding all the paths, like the paths should not be hard coded at a place, so we will store it in a variable in order to retrieve them later
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")