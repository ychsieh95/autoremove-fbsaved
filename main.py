import argparse
import time
from selenium import webdriver


class FacebookSavedItemRemover():
    def __init__(self, username, password):
        self.driver = webdriver.Edge()
        self.driver.get('https://www.facebook.com/')

        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_xpath('//button[@name="login"]').click()
        print('[ INFO ] Try to login Facebook')
        time.sleep(5)

        if self.is_login():
            print('[  OK  ] Login Facebook successful')
        else:
            print('[FAILED] Login Facebook failed')

    def __remove(self, url, keyword):
        click_count = 0
        while True:
            self.driver.get(url)
            time.sleep(5)

            wrapper = self.driver.find_elements_by_xpath('//div[@class="_3ixn"]')
            if wrapper:
                wrapper[0].click()
                time.sleep(2)

            saved_items = self.driver.find_elements_by_xpath('//div[@aria-label="More"]')
            if len(saved_items) == 1:
                print('[ INFO ] Stop auto-removed because it\'s not any saved item exists')
                break

            saved_items.pop(0)
            for saved_item in saved_items:
                try:
                    saved_item.click()
                    time.sleep(1)

                    span = saved_item.find_element_by_xpath(f'//span[text()="{keyword}"]')
                    span.click()
                    time.sleep(1)

                    click_count += 1
                    print('[  OK  ] Removed saved item. (Counter: {})'.format(click_count))
                    self.driver.execute_script("window.scrollTo(0, 193);")
                    time.sleep(1)
                except Exception as ex:
                    print('[FAILED] {}'.format(ex))
                    continue
        return click_count

    def is_login(self):
        login_btn = self.driver.find_elements_by_xpath('//label[@id="loginbutton"]/input')
        return not login_btn

    def remove_saved(self):
        self.__remove(url='https://www.facebook.com/saved/?dashboard_section=ALL', keyword='Unsave')

    def remove_links(self):
        self.__remove(url='https://www.facebook.com/saved/?dashboard_section=LINKS', keyword='Unsave')

    def remove_videos(self):
        self.__remove(url='https://www.facebook.com/saved/?dashboard_section=VIDEOS', keyword='Unsave')

    def remove_photos(self):
        self.__remove(url='https://www.facebook.com/saved/?dashboard_section=PHOTOS', keyword='Unsave')

    def remove_places(self):
        self.__remove(url='https://www.facebook.com/saved/?dashboard_section=PLACES', keyword='Unsave')

    def remove_products(self):
        self.__remove(url='https://www.facebook.com/saved/?dashboard_section=PRODUCTS', keyword='Unsave')

    def remove_events(self):
        self.__remove(url='https://www.facebook.com/saved/?dashboard_section=EVENTS', keyword='Unsave')

    def remove_offers(self):
        self.__remove(url='https://www.facebook.com/saved/?dashboard_section=OFFERS', keyword='Unsave')

    def remove_unlisted_only(self):
        self.__remove(url='https://www.facebook.com/saved/?unlisted_only=true', keyword='Unsave')

    def remove_seen(self):
        self.__remove(url='https://www.facebook.com/saved/?seen_state_filter=1', keyword='Unsave')

    def remove_archived(self):
        self.__remove(url='https://www.facebook.com/saved/?dashboard_section=ARCHIVED', keyword='取消封存')


def rm_option(option):
    options = {
        'all'          : fb_remover.remove_saved,
        'links'        : fb_remover.remove_links,
        'videos'       : fb_remover.remove_videos,
        'photos'       : fb_remover.remove_photos,
        'places'       : fb_remover.remove_places,
        'products'     : fb_remover.remove_products,
        'events'       : fb_remover.remove_events,
        'offers'       : fb_remover.remove_offers,
        'unlisted_only': fb_remover.remove_unlisted_only,
        'seen'         : fb_remover.remove_seen,
        'archive'      : fb_remover.remove_archived
    }
    remove_method = options.get(option)
    if remove_method:
        remove_method()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A CLI tool for removing saved items in Facebook.')
    parser.add_argument(
        '-u', '--username',
        action='store',
        required=True,
        help='facebook username')
    parser.add_argument(
        '-p', '--password',
        action='store',
        required=True,
        help='facebook password')
    parser.add_argument(
        '-o', '--option',
        action='store',
        default='all',
        help='options of remove: all, links, videos, photos, places, products, events, offers, unlisted_only, seen, archive')

    args = parser.parse_args()
    fb_remover = FacebookSavedItemRemover(username=args.username, password=args.password)
    if fb_remover.is_login():
        rm_option(args.option)