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
import os
from pathlib import Path


class Config:
    def __init__(self, logger: logging.Logger, filename: str) -> None:
        """
        Init the config class by loading it's values stored from the default yaml file.
        If non existing, creating it.
        """

        # Copy the logger reference locally
        self.logger = logger
        self.config_file = filename

        # Load the config, or creating a new one...
        try:
            with open(filename, "r") as f:
                self.config = yaml.safe_load(f)
                self.logger.info(
                    f"Found {len(self.config["documents"])} documents : {[t["type"] for t in self.config["documents"]]}"
                )

        except FileNotFoundError:
            self.config = {}
            self.logger.warning(f"No config file where found. Creating an empty one.")

            # Add default elements : 
            self.config["documents"] = [
                {
                    "type": "CV",
                    "template": "Insert/Your/Template.tex here",
                    "features": {"has_cover": False, "has_toc": False, "has_bibliography": False}
                }
            ]

            # Write the file
            self.update_config()

        except Exception as e:
            self.logger.error(
                f"Unresolved error occured while parsing the yaml config : {e}"
            )

        # Validate the provided config
        if self._validate_config() == False:
            self.logger.error("Failed to validate the config. Check errors messages before.")

        # Ensure files are consistents
        self.folder_list = ["templates", "content", "build", "chapters", "data"]
        self._create_structure()

        return
    
    def update_config(self) -> None:
        # Load the config, or creating a new one...
        try:
            with open(self.config_file, "w") as f:
                yaml.dump(self.config, f)
                self.logger.info(
                    f"Wrote the config to {self.config_file}."
                )
        except Exception as e:
            self.logger.error(
                f"Unresolved error occured while parsing the yaml config : {e}"
            )

        return
    
    def _validate_config(self) -> bool:

        # Mandatory keys. These are the bare minimal needed for a project to be valid.
        required = ["type", "template", "features"] 

        for document in self.config["documents"]:
            keys = document.keys()

            for req in required:
                if req not in keys:
                    self.logger.warning(f"Missing key in config : {req} for document {document.get("type", None)}")
                    return False
            

        return True

    def _create_structure(self) -> bool:

        # Create base folders
        self.folders = {}
    
        for folder in self.folder_list:
            self.folders["folder"] = Path(f"{folder}")
            self.folders["folder"].mkdir(parents=True, exist_ok=True)
            self.logger.info(f"Creating folder {folder}")

        return True
    
    def add_document(self) -> None:
        pass

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
