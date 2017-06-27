#
# script for parsing products' xml
# and creating data models to be used by ui
#

import xml.etree.ElementTree as ET
from models import Pagination, Data, Image, Category, Unit, Logo, Links


class ProductParser:

    def __init__(self, file_path):
        self.file_path = file_path
        tree = ET.parse(file_path)
        self.root = tree.getroot()

        for child in self.root:
            if child.tag == 'meta':
                self.meta = child

    def get_pagination(self):
        """
        function parser the pagination xml file
        """
        for pagination in self.meta:
            total = pagination.find('total').text
            count = pagination.find('count').text
            per_page = pagination.find('per_page').text
            current_page = pagination.find('current_page').text
            total_pages = pagination.find('total_pages').text

            links = []

            for child in pagination:
                if child.tag == 'links':
                    next = child.find('next').text
                    links.append(Links(next))
            return Pagination(total, count, per_page,
                              current_page, total_pages, links)

    def get_all_data(self):
        """
        function parses the products xml file
        and returns list of products
        """

        lst = []

        for data in self.root.findall('data'):
            lst.append(self.process_data_tag(data))

        return lst

    def process_data_tag(self, data):

        id = data.find('id').text
        name = data.find('name').text
        description = data.find('description').text
        updated_at = data.find('updated_at').text
        created_at = data.find('created_at').text

        category = []
        units = []
        images = []
        logo = []

        # processing all child tags of data
        for child in data:

            # getting <category> from data
            if child.tag == 'category':
                id = child.find('id').text
                name = child.find('name').text
                category.append(Category(id, name))

            # getting <units> from data
            if child.tag == 'units':
                for data_tag in child:
                    id = data_tag.find('id').text
                    name = data_tag.find('name').text
                    key = data_tag.find('key').text
                    value = data_tag.find('value').text
                    units.append(Unit(id, name, key, value))

            # getting <images> from data
            if child.tag == 'images':
                for data_tag in child:

                    id = data_tag.find('id').text
                    name = data_tag.find('name').text
                    thumb = data_tag.find('thumb').text
                    aspectRatio = data_tag.find('aspectRatio').text
                    listing_medium = data_tag.find('listing_medium').text
                    listing_small = data_tag.find('listing_small').text
                    listing_large = data_tag.find('listing_large').text
                    square_medium = data_tag.find('square_medium').text
                    square_small = data_tag.find('square_small').text
                    square_large = data_tag.find('square_large').text

                    images.append(Image(id, name, thumb, aspectRatio,
                                        listing_medium, listing_small,
                                        listing_large, square_medium,
                                        square_small, square_large))

            # getting <logo> from data
            if child.tag == 'logo':
                for data_tag in child:

                    id = data_tag.find('id').text
                    name = data_tag.find('name').text
                    thumb = data_tag.find('thumb').text
                    aspectRatio = data_tag.find('aspectRatio').text
                    listing_medium = data_tag.find('listing_medium').text
                    listing_small = data_tag.find('listing_small').text
                    listing_large = data_tag.find('listing_large').text
                    square_medium = data_tag.find('square_medium').text
                    square_small = data_tag.find('square_small').text
                    square_large = data_tag.find('square_large').text

                    logo.append(Logo(id, name, thumb, aspectRatio,
                                     listing_medium, listing_small,
                                     listing_large, square_medium,
                                     square_small, square_large))

        return Data(id, name, description, category, units, images,
                    updated_at, created_at, logo)


def get_data():
    pp = ProductParser('test.xml')
    return pp.get_all_data()
    # return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L' , 'M']


if __name__ == "__main__":
    pp = ProductParser('test.xml')

    # getting all data
    data = pp.get_all_data()
    for product in data:
        product.show_data_details()

    # getting pagination information
    pagination = pp.get_pagination()
    pagination.show_pagination_details()
