# --------------------------------------------------------------
# file : config.py
#
# brief : Define the global config related functions
#
# author : l.heywang <leonard.heywang@proton.me>
# date : 08-02-2026
# --------------------------------------------------------------

# Import packages
import yaml
import logging


class Config:
    def __init__(self, logger: logging.Logger, filename: str) -> None:
        """
        Init the config class by loading it's values stored from the default yaml file.
        If non existing, creating it.
        """

        with open(filename, "r") as f:
            self.config = yaml.safe_load(f)

        self.logger = logger

        self.logger.info(f"{self.config["documents"][0]}")
