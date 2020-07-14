import urllib.request
from bs4 import BeautifulSoup
import os


const_url = f"http://transcripts.foreverdreaming.org/viewtopic.php?f=192&t="


def get_str_ep_num(ep):
    if ep < 10:
        str_ep = "0" + str(ep)
    else:
        str_ep = str(ep)
    return str_ep


def extract_season1():
    ep = 1
    while ep < 10:
        curr_url = "1174" + str(ep)
        str_ep = get_str_ep_num(ep)
        write_script_to_file(curr_url, str_ep, 1)
        ep += 1


def extract_season2():
    ep = 1
    while ep <= 10:
        curr_ep_in_url = ep - 1
        curr_url = "1175" + str(curr_ep_in_url)
        str_ep = get_str_ep_num(ep)
        write_script_to_file(curr_url, str_ep, 2)
        ep += 1


def extract_season3():
    curr_urls = ["", "16621", "16731", "16825", "16972", "17338", "17520", "17616", "17724", "17848", "17952"]
    ep = 1
    while ep <= 10:
        str_ep = get_str_ep_num(ep)
        write_script_to_file(curr_urls[ep], str_ep, 3)
        ep += 1


def extract_season4():
    curr_urls = ["", "25268", "25604", "25753", "25894", "26103", "26236", "26350", "26494", "26627", "26764",
                 "30045", "30162", "30278", "30344", "30367", "30427", "30507", "30636", "30744", "30831"]
    ep = 1
    while ep <= 20:
        str_ep = get_str_ep_num(ep)
        write_script_to_file(curr_urls[ep], str_ep, 4)
        ep += 1


def extract_season5():
    curr_urls = ["", "32010", "", "32011", "32012", "32013", "32014", "32015", "32016", "32017", "32018",
                 "32353", "32410", "32455", "32482", "32484", "32495", "32505", "32566", "32609", "32697"]
    write_script_to_file(curr_urls[1], "1", 5)
    ep = 3
    while ep <= 20:
        str_ep = get_str_ep_num(ep)
        write_script_to_file(curr_urls[ep], str_ep, 5)
        ep += 1


def extract_season6():
    curr_urls = ["", "35461", "35463", "35536", "35575", "35602", "35652", "35689", "35732", "35784", "35817"]
    ep = 1
    while ep <= 10:
        str_ep = get_str_ep_num(ep)
        write_script_to_file(curr_urls[ep], str_ep, 6)
        ep += 1


# extract one episode transcript to text file
def write_script_to_file(curr_url, ep, se):
    episode = []
    url = const_url + curr_url
    web_page = urllib.request.urlopen(url)
    html_page = BeautifulSoup(web_page, 'html.parser')
    lines = html_page.findAll('p')
    for e in lines:
        line = e.text.strip()
        episode.append(line)
    curr_dir = os.getcwd()
    if (se == 5) and (ep == "1" or ep == "2"):
        file_name = curr_dir + f"/transcripts/season{se}/s0{se}ep01&02.txt"
    else:
        file_name = curr_dir + f"/transcripts/season{se}/s0{se}ep{ep}.txt"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(f"Season: {se} Episode: {ep}\n")
        for line in episode:
            f.write("%s\n" % line)


def read():
    extract_season1()
    extract_season2()
    extract_season3()
    extract_season4()
    extract_season5()
    extract_season6()
