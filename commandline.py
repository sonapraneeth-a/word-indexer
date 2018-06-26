# -*- coding: utf-8 -*-

# Reference: https://docs.python.org/3/library/argparse.html

import logging
import os
import sys
import tempfile

import configargparse

from __init__ import __version__, __project__

LOCAL_CONF_FILE_NAME = "word-indexer.conf"


def parse_args(args=None):
    """
    Parse the arguments/options passed to the program on the command line.
    """
    parse_kwargs = {
        "description": "Download codes submitted on online coding platforms",
        "prog": "solutioncode-dl",
        "epilog": "Details",
        "formatter_class": "argparse.ArgumentDefaultsHelpFormatter"
    }

    conf_file_path = os.path.join(os.getcwd(), LOCAL_CONF_FILE_NAME)
    if os.path.isfile(conf_file_path):
        parse_kwargs["default_config_files"] = [conf_file_path]
    # parser = configargparse.ArgParser(**parse_kwargs)
    parser = configargparse.ArgParser()
    # Options
    # Basic options
    basic = parser.add_argument_group("Basic options")
    basic.add_argument("-i",
                       "--input-dir",
                       nargs="?",
                       dest="input_directory",
                       action="store",
                       default=None,
                       help="Directory containing the text files")
    basic.add_argument("-o",
                       "--output-file",
                       nargs="?",
                       dest="output_file",
                       action="store",
                       default="index.html",
                       help="Output file containing index information")
    parser.add_argument("-v",
                        "--version",
                        action="version",
                        # version="%(prog)s " + __version__,
                        version="{0} {1}".format(__project__, __version__),
                        default=False,
                        help="Display version and exit")
    # parser.add_argument("-h",
    #                    "--help",
    #                    action="help",
    #                    help="Display help information")
    debug = parser.add_mutually_exclusive_group()
    debug.add_argument("-d",
                       "--debug",
                       dest="debug",
                       action="store_true",
                       default=False,
                       help="Print lots of debug information")
    debug.add_argument("-q",
                       "--quiet",
                       dest="quiet",
                       action="store_true",
                       default=False,
                       help="Omit as many messages as possible (only printing errors)")
    # Final parsing of the options
    (args, unparsed) = parser.parse_known_args(args)
    if len(unparsed):
        parser.print_help()
        exit(1)
    if not args.input_directory:
        parser.print_usage()
        logging.error('You must supply one platform name from where you want to download your codes')
        exit(1)

    if args.version:
        print("{0} version: {1}".format(__project__, __version__))
        exit(0)

    if args.debug:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(name)s[%(funcName)s] %(message)s'
        )
    elif args.quiet:
        logging.basicConfig(
            level=logging.ERROR,
            format='%(name)s: %(message)s'
        )
    else:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt='%m/%d/%Y %I:%M:%S %p',
            handlers=[
                logging.FileHandler("{0}\{1}.log"
                                    .format(tempfile.gettempdir(), args.platform)),
                logging.StreamHandler(sys.stdout)
            ]
        )
    logging.info("Logging to {0}".format(tempfile.gettempdir() + "\\" + __project__ + ".log"))
    return args


if __name__ == "__main__":
    argument = "-i \"./input-text-files/cnn-notes\" -o \"index.html\" --debug".split()
    args = parse_args(args=argument)
    print(args)
