"""tau - An annotated data object format for Olink data"""

from importlib.metadata import PackageNotFoundError, version

import taudata._io as io

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__all__ = ["io"]
