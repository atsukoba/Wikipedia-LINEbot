import wikipedia


# init language setting
lang = "ja"
wikipedia.set_lang(lang)


def tokenize(text: str) -> list:
    """Tokenize input Sentence to list of word"""
    return text.split()


def search(text: str, rank=0) -> "wikipedia.wikipedia.WikipediaPage":
    """Search Wikipedia page by Word

    arg
    ---
    rank : int : Return the contents of the search result of the set rank.
    """
    return wikipedia.page(wikipedia.search(text)[rank])


def encode(page: "wikipedia.wikipedia.WikipediaPage") -> str:
    """Transform data into the text for LINE message
    """
    return f"Result: {page.title}\n\n{page.summary}\n\n{page.url}"


def answer(text: str) -> str:
    page = search(text)
    return encode(page)


def change_lang(language: str) -> None:
    global lang
    lang = language
    return


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.parse_args()

    