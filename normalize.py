#!/usr/bin/python3

import argparse
import html2text
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', '-d', help='path to directory with html files', default='.')
    parser.add_argument('--file', '-f', help='path to certain html file', default=None)
    parser.add_argument('--out', '-o', help='filename to resulted plane text file', default='normalized.txt')
    args = parser.parse_args()
    
    files = []
    if args.file is not None:
        files.append(args.file)
    else:
        files = [args.dir + f for f in os.listdir(args.dir)]

    normalized_text = ''
    
    for f in files:
        if os.path.isfile(f) and f.endswith('html'):
            html = open(f).read()
            text = html2text.html2text(html).lower()
            normalized_text += text

    with open(args.out, 'w+') as normalized_file:
        normalized_file.write(normalized_text)
