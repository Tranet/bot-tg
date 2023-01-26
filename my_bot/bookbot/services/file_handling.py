import re

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
        dct = [',', '.', ':', ';', '!', '?']
        if len(text[size - 1:size + 2].split('..')) == 2:
            s = text[start:size - 2]
            m = 0
            for i in dct:
                k = s.rfind(i)
                if k > m:
                    m = k
            res = s[:m + 1]
        else:
            s = text[start:]
            m = 0
            for i in dct:
                k = s.rfind(i, 0, size)
                if k > m:
                    m = k
            rs = re.split(';,?:.!', s[:m + 1])
            res = ''.join(rs)

        return res, len(res)


# Функция, формирующая словарь книги
def prepare_book(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        chank = file.read()
        starts = 0
        n = 1
        while chank:
            txt, start = _get_part_text(chank, starts, PAGE_SIZE)
            book[n] = txt.lstrip()
            n += 1
            chank = chank[start:]


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
