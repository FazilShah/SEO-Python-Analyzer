from run_through_urls import scrape_details
from run_through_urls import scrape_faster


class get_scrapped_data:

    def __init__(self, filename):
        get_scrapped_data.filename = filename
        get_scrapped_data.get_data = scrape_faster(get_scrapped_data.filename)

    @staticmethod
    def duplicate_titles():
        duplicate_title_pages = []
        flipped = {}
        dict_titles = get_scrapped_data.get_data[0]
        for key, value in dict_titles.items():
            if value is not None:
                if value not in flipped:
                    flipped[value] = [key]
                else:
                    flipped[value].append(key)

        for key, value in flipped.items():
            if len(value) > 1:
                duplicate_title_pages.append(value)
            else:
                pass
        return duplicate_title_pages

    @staticmethod
    def duplicate_meta_descriptions():
        duplicate_md_pages = []
        flipped = {}
        dict_md = get_scrapped_data.get_data[1]
        for key, value in dict_md.items():
            if value is not None:

                if value not in flipped:
                    flipped[value] = [key]
                else:
                    flipped[value].append(key)

        for key, value in flipped.items():
            if len(value) > 1:
                duplicate_md_pages.append(value)
            else:
                pass
        return duplicate_md_pages

    @staticmethod
    def get_missing_descriptions():
        missing_descriptions = []
        dict_missing = get_scrapped_data.get_data[1]
        for key, value in dict_missing.items():
            if value is None:
                missing_descriptions.append(key)
            else:
                pass

        return missing_descriptions

    @staticmethod
    def get_missing_titles():
        missing_titles = []
        dict_missing = get_scrapped_data.get_data[0]
        for key, value in dict_missing.items():
            if value is None:
                missing_titles.append(key)
            else:
                pass

        return missing_titles