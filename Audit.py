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
        print(dict_titles)
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
    def get_titles_with_less_content():
        low_titles = []
        dict_low_titles = get_scrapped_data.get_data[0]
        for key, value in dict_low_titles.items():
            if value is not None:
                if len(value) <= 10:
                    low_titles.append(key)
                    print(value)
        return low_titles

    @staticmethod
    def get_meta_des_with_less_content():
        low_meta = []
        dict_low_meta = get_scrapped_data.get_data[1]
        for key, value in dict_low_meta.items():
            if value is not None:
                if len(str(value)) <= 30:
                    low_meta.append(key)
        return low_meta


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
    @staticmethod
    def get_missing_h1():
        missing_h1 = []
        dict_missing = get_scrapped_data.get_data[2]
        print(dict_missing)
        for key, value in dict_missing.items():
            if len(value) == 0:
                missing_h1.append(key)
        return missing_h1

    @staticmethod
    def get_duplicate_h1():
        duplicate_h1 = []
        flipped = {}
        dict_h1 = get_scrapped_data.get_data[2]
        for key, value in dict_h1.items():
            if len(value) !=0:
                for item in value:
                    if item not in flipped:
                        flipped[item] = [key]
                    else:
                        flipped[item].append(key)

        for key, value in flipped.items():
            if len(value) > 1:
                duplicate_h1.append(value)
            else:
                pass
        print(duplicate_h1)
        return duplicate_h1

    @staticmethod
    def get_missing_canonicals():
        missing_canonicals = []
        dict_canonicals = get_scrapped_data.get_data[3]
        for key, value in dict_canonicals.items():
            if value is None:
                missing_canonicals.append(key)
        return  missing_canonicals

    @staticmethod
    def improper_canonicals():
        improper = []
        dict_canonicals = get_scrapped_data.get_data[3]
        for key, value in dict_canonicals.items():
            if value is not None:
                if value != key:
                    improper.append(key)
        return improper

    @staticmethod
    def missing_viewports():
        missing_viewports = []
        dict_missing_v = get_scrapped_data.get_data[4]
        for key, value in dict_missing_v.items():
            if value is False:
                missing_viewports.append(key)

        return missing_viewports

