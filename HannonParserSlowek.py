# -*- coding: utf-8 -*-
import logging
import argparse
import sys
import re

def def_params():
    parser = argparse.ArgumentParser(
            description='Script to parsing data from html to array_sentences'
    )
    parser.add_argument("-l", "--loghami", action="store_true", help="set debug")
    parser.add_argument("-f", "--file", help="name of file", required=True)
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=loggins.DEBUG)
        print("args:" + str(args))
    return args


def main():
    args=def_params()
    bas_dir = os.path.dirname(os.path.realpath(__file__)
    logging.debug("Only shown in debug mode")


if __name__ == "__main__":
    main()
