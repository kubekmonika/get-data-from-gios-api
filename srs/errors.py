"""
Errors for the source code
"""


class SourceCodeError(Exception):
    """Parrent class for the errors"""
    pass


class NoDataReturned(SourceCodeError):
    pass
