from functools import cache
from pathlib import Path


@cache
def get_version():
    ver = (Path(__file__).parent.parent / 'VERSION').read_text(encoding='utf-8').strip()
    return ver
