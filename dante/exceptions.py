
"""
Exceptions which can be raised by dante Ubot Itself.
"""


class KazuError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(KazuError):
    ...
