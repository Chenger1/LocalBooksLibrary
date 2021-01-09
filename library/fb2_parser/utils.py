from typing import List
from unicodedata import normalize


def clear_text_from_spaces(text: List[str]) -> List[str]:
    return [line.strip() for line in text]


def clear_from_unicode_symbols(text: List[str]) -> List[str]:
    new_text = []
    for line in text:
        if '\xa0' in line:
            new_text.append(normalize('NFKD', line))
        else:
            new_text.append(line)

    return new_text


def normalize_text(text: List[str]) -> List[str]:
    text = clear_text_from_spaces(text)
    text = clear_from_unicode_symbols(text)
    return text
