from requests import get
from random import choice
from colorama import Fore
from bs4 import BeautifulSoup
from configs.config import CONFIG
from traceback import format_exc as print_traceback


def find_targets(file_path: str) -> list:
    """
    choose where collect the urls
    :param file_path: ad urls file path
    :return: a list with urls
    """
    targets = list()
    with open(file_path, "r+") as ad_urls:
        for url in ad_urls:
            targets.append(url.strip())
    return targets


def get_free_proxies() -> list:
    """
    get brazilian free proxies on free-proxy-list.net
    :return: list with proxies ip
    """
    proxies = list()
    # get the HTTP response and construct soup objects
    soup_free_proxy_list = BeautifulSoup(get(CONFIG["proxies_url"]).content, "html.parser")

    # collecting proxies ips
    for row in soup_free_proxy_list.find("table", 
                                         attrs={"class": "table table-striped table-bordered"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue

    return proxies[:120]


def click_simulator(google_url_ad: str, proxies_ips: list) -> None:
    """
    click simulator by requests GET
    :param google_url_ad: ad url
    :param proxies_ips: list with ip:port of proxy
    :return: None
    """
    for proxy_ip in proxies_ips:
        try:
            response = get(google_url_ad,
                           proxies={"http": "http://" + proxy_ip},
                           headers=choice(CONFIG["headers"]),
                           timeout=60)
            if response.status_code == 200:
                print(CONFIG["logs"]["process_clicking_ad"].format(Fore.LIGHTRED_EX,
                                                                   Fore.LIGHTWHITE_EX,
                                                                   response.url,
                                                                   Fore.LIGHTRED_EX,
                                                                   proxy_ip,
                                                                   Fore.LIGHTWHITE_EX))
                continue
            else:
                print(CONFIG["logs"]["error_proxy_fail"].format(Fore.LIGHTYELLOW_EX,
                                                                Fore.LIGHTWHITE_EX,
                                                                Fore.LIGHTRED_EX,
                                                                Fore.LIGHTWHITE_EX,
                                                                proxy_ip))
                continue

        except KeyboardInterrupt:
            print(CONFIG['logs']['key_interrupt'].format(Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX, print_traceback()))
            print(CONFIG["logs"]["process_done"].format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
            exit(0)
        except Exception:
            print(CONFIG["logs"]["error_proxy_fail"].format(Fore.LIGHTYELLOW_EX,
                                                            Fore.LIGHTWHITE_EX,
                                                            Fore.LIGHTRED_EX,
                                                            Fore.LIGHTWHITE_EX,
                                                            proxy_ip))
            continue


def ads_click_flooding(google_ads_urls: list, proxies_list: list) -> None:
    """
    floods domains with many requests to take down the ad
    :param google_ads_urls: list with ad urls
    :param proxies_list: list with proxy ips
    :return: None
    """
    for ad_data in google_ads_urls:
        click_simulator(ad_data, proxies_list)
