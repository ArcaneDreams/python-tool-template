import os
import pathlib
import re

from python_tool_template import __title__


def sanitize_name(name: str) -> str | None:
    """
    This function sanitizes a given name by removing invalid characters.

    It replaces characters that are not alphanumeric or hyphens with hyphens.

    :param name: The input name to be sanitized.
    :type name: str
    :raises ValueError: If the input name is invalid or null.
    :return: A sanitized version of the input name, or None if the name is invalid.
    :rtype: str | None
    """
    if not name:
        raise ValueError("The name is invalid or null")
    return re.sub(r'[^a-zA-Z0-9\-]+', '-', name)


def get_app_name() -> str:
    """

    :return:
    """
    return sanitize_name(__title__)


def get_app_home() -> str:
    """
    Get the absolute path to the home of the application on the system.
    :return:
    """
    if not (app_name := get_app_name()):
        raise ValueError("The app name is invalid or null")
    return os.path.join(pathlib.Path.home(), app_name)


def get_app_home_path(*paths) -> str:
    """

    :param paths:
    :return:
    """
    if not paths:
        raise ValueError("The paths are invalid or null")
    return os.path.join(get_app_home(), *paths)
