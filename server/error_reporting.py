from typing import List, Union
import logging
from lark import UnexpectedToken
from pygls.lsp.types import (Diagnostic, Range, Position)
from .grammar import lark_parser


def user_repr(error: Union[UnexpectedToken]):
    if isinstance(error, UnexpectedToken):
        expected = ', '.join(error.accepts or error.expected)
        return f"Unexpected token {str(error.token)!r}. Expected one of :\n{{{expected}}}"
    else:
        return str(error)


def get_diagnostics(doctext: str):
    diagnostics: List[Diagnostic] = []

    def on_error(e: UnexpectedToken):
        diagnostics.append(Diagnostic(
            range=Range(
                start=Position(line=e.line - 1, character=e.column - 1),
                end=Position(line=e.line - 1, character=e.column)
            ), message=user_repr(e)))
        return True

    try:
        lark_parser.parse(doctext, on_error=on_error)
    except Exception:
        logging.exception("parser raised exception")
    return diagnostics
