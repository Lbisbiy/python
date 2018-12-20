# -*- coding: utf-8 -*-
import os

from Helper import Parser
from Helper.GetURL import GetURL
from dotenv import load_dotenv

CUR_DIR = os.path.dirname(__file__)
DOTENV_PATH = os.path.dirname(__file__) + '/env'


def search_data(url_for_parse):

    pages = parser.quantity_pages()
    for page in range(1, pages):
        url = url_for_parse + os.environ["url_part_for_page"] + str(page)
        parser.parsing_page(parser.get_html(url))


if __name__ == '__main__':
    load_dotenv(DOTENV_PATH)
    url_for_parse = GetURL.get_base_url(
        os.environ["host"],
        os.environ["area"],
        os.environ["object"],
        os.environ["model"]
    )
    parser = Parser.Parser(url_for_parse)
    search_data(url_for_parse)



