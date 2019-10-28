import argparse
from pathlib import Path
import configparser
import csv
import sys


def parse_args():
    parser = argparse.ArgumentParser('ini2csv')
    parser.add_argument('infile', nargs='?', default=sys.stdin)
    parser.add_argument('outfile', nargs='?', default=sys.stdout)
    parser.add_argument('--collapsed', help='collapse the rows to one row per section', action='store_true')

    return parser.parse_args()


def read_cfg(infile):
    config = configparser.ConfigParser()
    config.read(infile)

    return config

def ini2csv(infile, outfile, collapsed=False):
    config: configparser.ConfigParser = read_cfg(infile)

    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        
        if not collapsed:
            for section in config.sections():
                for k, v in config.items(section):
                    writer.writerow((section, k, v))
        else:
            writer.writerow(('header', *config[config.sections()[0]].keys()))

            for section in config.sections():
                writer.writerow((section, *config[section].values()))


if __name__ == "__main__":
    args = parse_args()

    ini2csv(args.infile, args.outfile, args.collapsed)
