from io import StringIO
from typing import IO

from rich.console import Console
from rich.containers import Renderables

_console: Console | None = None


def get_package_console() -> Console:
    """
    Get the console instance that is used across the package.
    """
    global _console
    if not _console:
        _console = Console(soft_wrap=True, stderr=True, record=True)
    return _console


def _get_renderable_console(stream: IO[str]) -> Console:
    """

    :param stream:
    :return:
    """
    return Console(file=stream, soft_wrap=True, stderr=True, no_color=True)


def render_out(renderables: Renderables) -> str:
    """
    Render the renderables to the console
    :param renderables: The iterable of renderables to render out to the console
    :return:
    """
    contents: str = ""
    with StringIO(contents) as render_stream:
        renderable_console = _get_renderable_console(stream=render_stream)
        for renderable in renderables:
            renderable_console.print(renderable)
        output = render_stream.getvalue()
    if not output:
        raise ValueError("The output specified is invalid or null")
    return output
