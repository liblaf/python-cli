#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

mkdir --parents docs/
typer cli.cmd utils docs --output docs/help.md
prettier --write docs/help.md
