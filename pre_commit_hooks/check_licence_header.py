from __future__ import annotations

import argparse
from typing import Any, Sequence


LICENCE_HEADER_TEXT = "// Copyright © 2022-2024 Obol Labs Inc. Licensed under the terms of a Business Source License 1.1"

def prepend_licence_header(filename):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(LICENCE_HEADER_TEXT.rstrip('\r\n') + '\n\n' + content)

def isLicenceHeaderPresent(filename: Any) -> bool:
    with open(filename, 'r') as f:
        content = f.read()
        return content.startswith(LICENCE_HEADER_TEXT)

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    return_code = 0
    for filename in args.filenames:
        if not isLicenceHeaderPresent(filename):
            prepend_licence_header(filename)
            print(f'Fixing {filename}')
            return_code = 1
    return return_code


if __name__ == '__main__':
    raise SystemExit(main())
