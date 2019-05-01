import parser
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('text', help='add Text to test as input reply data')
args = argparser.parse_args()


def check(text: str) -> bool:
    return "Result:" in text


def main(text: str) -> str:
    for lang in ["ja", "en", "cn"]:
        print(f"Now checking {text}... in {lang}")
        result = parser.answer(lang + " " + text)
        if check(result):
            print(f"OK:", result.split("\n")[0])


if __name__ == "__main__":
    main(args.text)
