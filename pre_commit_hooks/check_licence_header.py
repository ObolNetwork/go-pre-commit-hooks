from __future__ import annotations

import argparse
from typing import Any, Sequence


LICENCE_HEADER_TEXT = """// Copyright © 2022-2023 Obol Labs Inc.
//
// Use of this software is governed by the Business Source License
// included in the LICENSE file.
//
// As of the Change Date specified in that file, in accordance with
// the Business Source License, use of this software will be governed
// by the GNU General PublicLicense, Version 2.0."""

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
