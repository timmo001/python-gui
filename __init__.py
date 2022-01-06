"""Python GUI"""
from argparse import ArgumentParser
import logging

from pythongui.main import Main

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
FORMAT = "%(asctime)s %(levelname)s (%(threadName)s) [%(name)s] %(message)s"

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-ll",
        "--log-level",
        dest="log_level",
        help="Log level",
        default="INFO",
    )

    args = parser.parse_args()

    logging.basicConfig(
        format=FORMAT,
        datefmt=DATE_FORMAT,
        level=args.log_level.upper(),
    )
    logger = logging.getLogger(__name__)

    Main(args)
