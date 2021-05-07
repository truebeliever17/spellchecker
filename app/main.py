from pathlib import Path

from fastapi import FastAPI
from symspellpy import SymSpell, Verbosity


DICTIONARY_PATH = Path('/data/kk.txt')

app = FastAPI()

symspell = SymSpell(max_dictionary_edit_distance=2)
symspell.load_dictionary(DICTIONARY_PATH, term_index=0, count_index=1)


@app.get("/")
async def read_root():
    """Displays greeting message in homepage

    Returns:
        dict: a dictionary with greeting message
    """

    return {"message": "✌"}