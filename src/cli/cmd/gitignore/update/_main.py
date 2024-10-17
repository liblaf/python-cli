from pathlib import Path

import httpx


def main(gitignore: Path) -> None:
    lines: list[str] = gitignore.read_text().splitlines()
    result: list[str] = []
    between_markers: bool = False
    for line in lines:
        if line.startswith("# Created by"):
            between_markers = True
            url: str = line.removeprefix("# Created by ").strip()
            resp: httpx.Response = httpx.get(url)
            result += resp.text.splitlines()
        elif line.startswith("# End of"):
            between_markers = False
        elif not between_markers:
            result.append(line)
    gitignore.write_text("\n".join(result) + "\n")
