from pathlib import Path

from fastapi import FastAPI
from symspellpy import SymSpell, Verbosity

from app.schemas import LookupRequest, LookupResponse


MAX_EDIT_DISTANCE = 2
DICTIONARY_PATH = Path('./data/kk.txt')

app = FastAPI()

symspell = SymSpell(max_dictionary_edit_distance=MAX_EDIT_DISTANCE)
symspell.load_dictionary(DICTIONARY_PATH, term_index=0, count_index=1, encoding='utf-8')


@app.get("/")
async def read_root():
    """Displays greeting message in homepage

    Returns:
        dict: a dictionary with greeting message
    """

    return {"message": "✌"}


@app.post("/lookup", response_model=LookupResponse)
async def lookup(request_body: LookupRequest):
    """Provide most closest and frequent words using symspell

    Args:
        request_body (LookupRequest): input model with word to lookup

    Returns:
        LookupResponse:
            Dictionary that contains input word, most frequent word and also
            list of closest words sorted by edit distance within max_edit_distance
    """

    word = request_body.word
    closest_words = lookup_word(word, Verbosity.CLOSEST, MAX_EDIT_DISTANCE)
    most_frequent_word = lookup_word(word, Verbosity.TOP, MAX_EDIT_DISTANCE)

    result = {'input_word': word, 'most_frequent': most_frequent_word, 'closest_words': closest_words}
    return LookupResponse(**result)


def lookup_word(word, verbosity, max_edit_distance):
    """Find closest or frequent words to input word

    Args:
        word (str): Input word to lookup
        verbosity (Verbosity): Verbosity mode (Verbosity.TOP, Verbosity.CLOSEST, Verbosity.ALL)
        max_edit_distance (int): Max edit distance

    Returns:
        Union[str, List, None]:
            Either string or list or none.

            Returns str
                If verbosity is set to Verbosity.TOP and input word has
                most frequent word within max_edit_distance. It outputs
                the most frequent word.

            Returns None
                If input word doesn't have any words in dictionary within max_edit_distance.
                For example, this can happen when you pass word in different language

            Returns List
                If verbosity is set to Verbosity.CLOSEST.
                List is empty if input word doesn't have any
                closest words within max_edit_distance.
    """
    suggestions = symspell.lookup(word, verbosity, max_edit_distance)
    words_list = [item.term for item in suggestions]

    if verbosity == Verbosity.CLOSEST:
        return words_list

    if len(words_list) > 0:
        return words_list[0]

    return None
