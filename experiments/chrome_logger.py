#!/usr/bin/env python3
# This program loads a page using chrome and saves the log output

import argparse
import os
import sys
import shutil
import time
import random
import string
from subprocess import Popen


TMP_DATA_PREFIX = '/tmp/chrome-log'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str,
                        help='Page to request')
    parser.add_argument('-t', '--duration', type=int, default=600,
                        help='Time to log results in seconds')
    parser.add_argument('-o', '--output', type=str,
                        help='Place to store logs')
    return parser.parse_args()


ALPHANUMERIC_CHARS = string.digits + string.ascii_letters


def random_string(length):
    return ''.join(random.choice(ALPHANUMERIC_CHARS) for i in range(length))


def main(url, duration, output):
    tmp_usr_dir = '{}-{}'.format(TMP_DATA_PREFIX, random_string(6))
    try:
        cmd = [
            'google-chrome',
            '--enable-logging',
            '--v=0',
            '--disable-application-cache',
            '--no-first-run',
            '--user-data-dir={}'.format(tmp_usr_dir),
            url
        ]
        child = Popen(cmd, stdout=None, stderr=None)

        time.sleep(duration)
        child.kill()
        child.wait()

        chrome_log_file = os.path.join(tmp_usr_dir, 'chrome_debug.log')
        if not os.path.isfile(chrome_log_file):
            raise Exception('No log output from chrome')

        if output:
            shutil.move(chrome_log_file, output)
        else:
            with open(chrome_log_file) as fp:
                sys.stdout.write(fp.read())
    finally:
        shutil.rmtree(tmp_usr_dir)


if __name__ == '__main__':
    main(**vars(get_args()))
