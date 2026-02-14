# --------------------------------------------------------------
# file : main.py
#
# brief : Main script for the texpr script ! Handle the top
#         level logic.
#
# author : l.heywang <leonard.heywang@proton.me>
# date : 08-02-2026
# --------------------------------------------------------------

# Import packages
import yaml

from config import Config
from logger import setup_logger


# Main
def main() -> None:
    logger = setup_logger(True, "texpr.log")
    cfg = Config(logger, "example/config.yaml")


# For debug
if __name__ == "__main__":
    main()
