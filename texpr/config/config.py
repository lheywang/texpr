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

        # Load the config, or creating a new one...
        try:
            with open(filename, "r") as f:
                self.config = yaml.safe_load(f)
                self.logger.info(
                    f"Found {len(self.config["documents"])} documents : {[t["type"] for t in self.config["documents"]]}"
                )
        except FileNotFoundError:
            self.config = {}
            self.logger.info(f"No config file where found. Creating an empty one.")
        except Exception as e:
            self.logger.error(
                f"Unresolved error occured while parsing the yaml config : {e}"
            )
        self.config_file = filename

        # Copy the logger reference locally
        self.logger = logger

        return

    def add_template(self) -> None:
        pass

    def add_settings(self) -> None:
        pass

    def add_chapter(self) -> None:
        pass

    def add_lang(self) -> None:
        pass

    # TODO:
    # - Validate config file, if loaded.
    # - Create project structure (pathlib)
    #
