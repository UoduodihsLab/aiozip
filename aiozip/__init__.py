"""
AIOZip: Native asynchronous library for file archiving.
"""
__version__ = "0.2.0"

from .uncompress import uncompress
from .compress import compress
from .exceptions import (
    AiozipError,
    UnsupportedFormatError,
    CorruptArchiveError,
    ArchiveNotFoundError,
)

__all__ = [
    # Core functions
    "uncompress",
    "compress",

    # Exceptions
    "AiozipError",
    "UnsupportedFormatError",
    "CorruptArchiveError",
    "ArchiveNotFoundError",
]
