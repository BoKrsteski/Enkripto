#!/bin/bash
SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECTDIR="$(dirname "$SCRIPTDIR")"
if ! command -v python3 >/dev/null 2>&1;
then
  echo "Python3 is not installed!"
  exit 1
fi
python3 -m venv "$PROJECTDIR/.venv"
"$PROJECTDIR/.venv/bin/python" -m pip install -r "$SCRIPTDIR/requirements.txt"
