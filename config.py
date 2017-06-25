"""
Config file to edit following
    - Change XML URL path
    - Assign which categories are shown on the menu
    - Control speed of scroll rate. If the list of items in a categories
      section is longer than the screen it should scroll.
    - Control what categories show on the menu.
    - Flower category has 3 “strain” options that may also be limited.
      There may be situations where a menu only shows 1 flower
      category strain.
    - Change amount of time between XML updates
"""

class Config:

    def __init__(self, file_path):
        pass

    def get_xml_url(self):
        pass

    def set_xml_url(self, url):
        pass

    def get_menu_categories(self):
        """
        function returns the list of categories
        to be shown on menu
        """

        # FIXME - read config.ini in future and return categories from it
        return ['Edibles', 'Topicals', 'Drinks']

