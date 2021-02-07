from typing import Dict
import zipfile
from xml.etree import ElementTree as ET


class EpubParser:
    def __init__(self, fname: str):
        self.zip = zipfile.ZipFile(fname)

    def get_info_about_book(self) -> Dict[str, str]:
        content_file_name = self.get_meta_inf_data()
        data_from_content_file = self.get_data_from_content_file(content_file_name)
        data_about_book = self.get_metainfo_about_book(data_from_content_file)
        return data_about_book

    def cleanup(self, element: ET.Element) -> ET.Element:
        """
                    Clean file`s elements from an extra part of the string
                    For example, before cleaning element looks like:
                    <Element '{http://www.idpf.org/2007/opf}role'>
                    After cleaning:
                    <Element 'role'>
                    It`s need to find specific elements in file
                """
        for elem in element.iter():
            elem.tag = elem.tag.partition('}')[-1]
        return element

    def get_meta_inf_data(self) -> str:
        """
            METAINF tag contains info about full path to content file
        """
        txt = self.zip.read('META-INF/container.xml')
        tree = self.cleanup(ET.fromstring(txt))
        cfname = tree.findall('rootfiles/rootfile/[@full-path]')[0].attrib['full-path']
        return cfname

    def get_data_from_content_file(self, content_file_name: str) -> ET.Element:
        """
            Get metadata element form content file
        """
        content_file = self.zip.read(content_file_name)
        tree = self.cleanup(ET.fromstring(content_file))
        content = tree.findall('metadata')[0]
        return content

    def get_metainfo_about_book(self, data_from_content_file: ET.Element) -> Dict[str, str]:
        """
        Finds list of tags below in metadata element in puts them into dict
        """
        data = {}
        for elem in ['creator', 'description', 'genre']:
            try:
                text = data_from_content_file.find(elem).text
                if elem == 'creator':  # change tag because of model attributes - 'author'
                    data['author'] = text
                elif elem == 'description':  # 'annotation' in model
                    data['annotation'] = text
                else:
                    data[elem] = text
            except AttributeError:
                continue
        return data


if __name__ == '__main__':
    f2 = 'Path to test books'
    parser = EpubParser(f2)
    d = parser.get_info_about_book()
