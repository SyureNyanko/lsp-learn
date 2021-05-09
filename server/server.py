from pygls.capabilities import COMPLETION
from pygls.lsp.methods import TEXT_DOCUMENT_DID_OPEN, TEXT_DOCUMENT_DID_CHANGE
from pygls.server import LanguageServer
from pygls.lsp import CompletionItem, CompletionList, CompletionOptions, CompletionParams
from pygls.lsp.types import DidOpenTextDocumentParams, DidChangeTextDocumentParams
from .error_reporting import get_diagnostics


class LarkLanguageServer(LanguageServer):
    CONFIGURATION_SECTION = 'larkLanguageServer'

    def __init__(self):
        super().__init__()


server = LarkLanguageServer()


@server.feature(COMPLETION, CompletionOptions(trigger_characters=[',']))
def completions(params: CompletionParams):
    """Returns completion items."""
    return CompletionList(
        is_incomplete=False,
        items=[
            CompletionItem(label='"'),
            CompletionItem(label='['),
            CompletionItem(label=']'),
            CompletionItem(label='{'),
            CompletionItem(label='}'),
            CompletionItem(label='Item1'),
            CompletionItem(label='Item2'),
        ]
    )


def _validate(ls: LarkLanguageServer, params: DidChangeTextDocumentParams):
    text_doc = ls.workspace.get_document(params.text_document.uri)
    print(text_doc)
    ls.publish_diagnostics(text_doc.uri, get_diagnostics(text_doc.source))


@server.feature(TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls: LarkLanguageServer, params: DidOpenTextDocumentParams):
    _validate(ls, params)


@server.feature(TEXT_DOCUMENT_DID_OPEN)
async def did_open(ls, params: DidOpenTextDocumentParams):
    """Text document did open notification."""
    ls.show_message('Text Document Did Open')
    _validate(ls, params)
