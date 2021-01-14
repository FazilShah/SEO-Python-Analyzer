from Scrap_Webpage import scrape
from multiprocessing.dummy import Pool


def scrape_details(line):
    print("Scraping " + line + "\n")
    page = scrape(line.strip())
    title = page.get_title()
    print(line + " " + title)
    dict_titles.update({line: title})
    meta_descriptions = page.get_meta_description()
    dict_meta_d.update({line: meta_descriptions})
    h1_text = page.get_h1_tags()
    h1_tags.update(({line:h1_text}))


def scrape_faster(filename):
    clean_url_list = get_urls_from_file(filename)
    global dict_meta_d
    dict_meta_d = {}

    global dict_titles
    dict_titles = {}

    global h1_tags
    h1_tags = {}
    pool = Pool(8)

    pool.map(scrape_details, clean_url_list)
    pool.close()
    pool.join()

    return dict_titles, dict_meta_d, h1_tags


def get_urls_from_file(filename):
    with open(filename) as file:
        list_of_url = file.read().split('\n')
        # print(list_of_url)
        list_of_url.remove('')
        clean_url_list = [url for url in list_of_url if (
                    'jpeg' in url or '#' in url or 'pdf' in url or 'png' in url or 'jpg' in url or 'tag' in url or 'tel' in url) == False]
        return clean_url_list
