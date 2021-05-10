# Spell Checker
[SymSpell](https://github.com/wolfgarbe/SymSpell) based Spell Checker of Kazakh Language. This is my student project for the NLP course.

This is just API with one endpoint, that returns the closest words and the most frequent one. It **DOES NOT** tell if your word is correct or not. It just gives suggestions. You can read more details below in [Examples](https://github.com/truebeliever17/spellchecker#-examples).

This project doesn't have any frontend part yet, I think I will add it somewhere in the future because I am just lazy. I am considering doing it using [streamlit](https://streamlit.io/), or maybe just Vue.js. 

The dictionary was taken from [here](https://github.com/hermitdave/FrequencyWords). But it only contains around ~5000 words which is small for any language. So I am looking for a better dictionary. If you have one, please let me know!

🏗 **Tech stack (TL;DR)**: [fastapi](https://github.com/tiangolo/fastapi), [uvicorn](https://github.com/encode/uvicorn), [symspellpy](https://github.com/mammothb/symspellpy)

## 🔮 Installation

This project requires Python 3.7+. Or maybe not, I don't know, I just selected the minimum version as 3.7 ¯\\_(ツ)\_/¯

Therefore if you have a Python version of less than 3.7 you may see some warning or error messages. So it's better to run it on new versions of Python.

1. Clone the repository
    ```sh
    $ git clone https://github.com/truebeliever17/spellchecker.git
    $ cd spellchecker
    ```

2. Install all dependencies

   Using pip:
    ```sh
    $ pip install -r requirements.txt
    ```
   Or using poetry:
   ```sh
    $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    $ poetry install
    ```
    
3. Run the live server
     ```sh
    $ uvicorn app.main:app
    ```
    
## 🧿 Examples

You can check and use my [API](https://symspellchecker.herokuapp.com/) that deployed to Heroku. If the page is not responding just wait around one minute to let Heroku start the dyno. This is because I am using a free dyno 🍜

There is also auto-generated documentation 😍 from FastAPI. Just type `docs` at the end of the url. Like `https://localhost:8000/docs`

As I said before I have only one endpoint, which is `/lookup`. It takes a word and returns suggested words.

__Response Body:__
```
inputWord: original word from the input request body
mostFrequent: most frequent word within maximum edit distance
closestWords: list of words within maximum edit distance that sorted by edit distance and then by frequency
```

__Example Input:__
```json
{
  "word": "акша"
}
```

__Example Output:__
```json
{
  "inputWord": "акша",
  "mostFrequent": "ақша",
  "closestWords": [
    "ақша"
  ]
}
```


It only supports words by now. But your input may contain spaces. See the example below:

__Example Input:__
```json
{
  "word": "бала га"
}
```

__Example Output:__
```json
{
  "inputWord": "бала га",
  "mostFrequent": "балаға",
  "closestWords": [
    "балаға",
    "балама"
  ]
}
```

If you give a word that doesn't have any close words within maximum edit distance then it returns an empty list for closest words and null for most frequent. See the example below:

__Example Input:__
```json
{
  "word": "hello"
}
```

__Example Output:__
```json
{
  "inputWord": "hello",
  "mostFrequent": null,
  "closestWords": []
}
```

And it shows pydantic validation error if input word is empty or types are mismatched:

__Example Input:__
```json
{
  "word": ""
}
```

__Example Output:__
```json
{
  "detail": [
    {
      "loc": [
        "body",
        "word"
      ],
      "msg": "ensure this value has at least 1 characters",
      "type": "value_error.any_str.min_length",
      "ctx": {
        "limit_value": 1
      }
    }
  ]
}
```

__Example Input:__
```json
{
  "word": ["hello", "world"]
}
```

__Example Output:__
```json
{
  "detail": [
    {
      "loc": [
        "body",
        "word"
      ],
      "msg": "str type expected",
      "type": "type_error.str"
    }
  ]
}
```
