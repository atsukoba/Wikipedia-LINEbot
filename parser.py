import wikipedia


# init language setting
lang = "ja"
wikipedia.set_lang(lang)


def tokenize(text: str) -> list:
    """Tokenize input Sentence to list of word"""
    splited = text.split()
    if len(splited) == 1:
        return splited
    elif len(splited) == 2:
        change_lang(splited[0])
        return splited[1]
    else:
        pass


def search(text: str, rank=0) -> "wikipedia.wikipedia.WikipediaPage":
    """Search Wikipedia page by Word

    arg
    ---
    rank : int : Return the contents of the search result of the set rank.
    """
    try:
        page = wikipedia.page(wikipedia.search(text)[rank])            
    except wikipedia.exceptions.DisambiguationError:
        page = wikipedia.page(wikipedia.search(text)[rank+1])
    return page


def encode(page: "wikipedia.wikipedia.WikipediaPage") -> str:
    """Transform data into the text for LINE message
    """
    return f"Result: {page.title}\n\n{page.summary}\n\n{page.url}"


def answer(text: str) -> str:
    word = tokenize(text)
    page = search(word)
    return encode(page)


def change_lang(language: str) -> None:
    global lang
    lang = language
    wikipedia.set_lang(lang)
    return


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.parse_args()

    
