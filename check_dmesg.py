#!/usr/bin/env python

import argparse
import subprocess
import sys


def get_dmesg(log_level):
    """
    Get the output of dmesg -l log_level
    :param log_level: log level to check for
    :return: output of dmesg -l log_level
    """
    result = subprocess.run(["/usr/bin/dmesg", "-l", log_level], stdout=subprocess.PIPE)
    return result.stdout


def parse_arguments(args):
    """
    Parse Commandline Arguments
    :param args: *args positional arguments
    :return: Commandline arguments parsed by argparse
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--log-level",
        metavar="log_level",
        dest="log_level",
        help="dmesg log level to check for",
        choices=[
            "emerg",
            "alert",
            "crit",
            "err",
            "warn",
            "notice",
            "info",
            "debug",
        ],
        default="err",
    )

    return parser.parse_args(args)


def main():
    """
    script main
    :return: exit code
    """
    exit_code = 0
    exit_message = "OK - No Errors"
    error_message = ""

    args = parse_arguments(sys.argv[1:])

    dmesg_ouput = get_dmesg(args.log_level)

    if len(dmesg_ouput) > 0:
        exit_code = 1
        error_message = dmesg_ouput

    if exit_code == 1:
        exit_message = "WARNING - %s" % error_message

    print(exit_message)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
