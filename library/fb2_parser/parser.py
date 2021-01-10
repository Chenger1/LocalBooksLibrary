import xml.etree.ElementTree as ET

from fb2_parser.utils import normalize_text


class FB2Parser:
    def __init__(self, filename):
        self.root = ET.parse(filename).getroot()
        self.cleanup()

    def cleanup(self):
        """
            Clean file`s elements from an extra part of the string
            For example, before cleaning element looks like:
            <Element '{http://www.gribuser.ru/xml/fictionbook/2.0}description' at 0x037F1CF8
            After cleaning:
            <Element 'description' at 0x037F1CF8
            It`s need to find specific elements in file
        """
        for element in self.root.iter():
            element.tag = element.tag.partition('}')[-1]

    def get_info_about_book(self) -> dict:
        info_tags = ['genre', 'annotation']
        book_info = {}
        for tag in info_tags:
            tag_text = list(self.root.find(f'.//{tag}').itertext())
            book_info[tag] = ' '.join(normalize_text(tag_text))
        book_info['author'] = self.get_author_info()
        return book_info

    def get_author_info(self) -> str:
        tag = self.root.find(f'.//author')
        tag = list(filter(lambda elem: elem.tag != 'id' and elem.tag != 'author', list(tag)))
        return ' '.join([elem.text for elem in tag])


def define_fb2_parser(file_path: str) -> FB2Parser:
    try:
        with open(file_path, encoding='utf-8') as xml_file:
            parser = FB2Parser(xml_file)
    except UnicodeDecodeError:
        with open(file_path, encoding='utf-8', errors='ignore') as xml_file:
            parser = FB2Parser(xml_file)
    finally:
        return parser


if __name__ == '__main__':

    file = 'D:\\Personal\\Books\\Self_development\\Branden_Shest-stolpov-samoocenki.ZIZAxQ.525105.fb2'
    #file = 'D:\\Personal\\Books\\Self_development\\Dahigg_Sila-privychki.389992.fb2'
    #file = 'D:\\Personal\\Books\\Self_development\\kak-priobretat-druzey-i-okazyvat-vliyanie-na-lyudey-jHGuW.fb2'
    with open(file, encoding='utf-8') as file:
        p = FB2Parser(file)
        p.get_info_about_book()
