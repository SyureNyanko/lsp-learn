from pygls.capabilities import COMPLETION, TEXT_DOCUMENT_DID_OPEN
from pygls.server import LanguageServer
from pygls.lsp import CompletionItem, CompletionList, CompletionOptions, CompletionParams
from pygls.lsp.types import DidOpenTextDocumentParams
server = LanguageServer()


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


@server.feature(TEXT_DOCUMENT_DID_OPEN)
async def did_open(ls, params: DidOpenTextDocumentParams):
    """Text document did open notification."""
    ls.show_message('Text Document Did Open')
    _validate(ls, params)
