import glob
import json
import os
import re
import subprocess
import time

from bs4 import BeautifulSoup
from selenium import webdriver

# ~ from selenium.webdriver.common.action_chains import ActionChains
# from pymongo import MongoClient


driver = webdriver.Firefox()
# client = MongoClient()
# client = MongoClient('localhost', 27017)
# db = client.pantip_test3


def prelim_info(url):
    driver.get(url)

    """ID"""
    topic_id = url.split("/")[-1]
    # ~ print(topic_id)

    """Title"""
    topic_name = driver.find_element_by_tag_name("title").text.strip(" - Pantip")
    # ~ print(topic_name)

    """Total pages"""
    pages = driver.find_elements_by_xpath(
        '//*[contains(@id, "page")]'
    )  # get all elements with page-ID   – from //*[@id="page-7"]
    visible_pages = [page.get_attribute("id") for page in pages][
        :-3
    ]  # list of all page buttons. up/down/paging only for single page (which I axe))

    """----OP----"""
    OP_raw = driver.find_element_by_xpath(
        '//*[@id="topic-' + topic_id + '"]/div/div[4]'
    )

    """--OP Text--"""
    OP_text_wrapper = OP_raw.find_element_by_class_name("display-post-story-wrapper")
    OP_text = OP_text_wrapper.find_element_by_class_name("display-post-story").text
    # ~ print(OP_text)

    """OP Footer"""
    OP_footer_raw = OP_raw.find_element_by_class_name("display-post-story-footer")
    OP_footer_first_child = OP_footer_raw.find_element_by_class_name(
        "display-post-action"
    )
    OP_footer_second_child = OP_footer_first_child.find_element_by_class_name(
        "display-post-avatar"
    )

    """--OP User--"""
    OP_user_raw = OP_footer_second_child.find_element_by_class_name(
        "display-post-avatar-inner"
    )
    OP_user = OP_user_raw.find_element_by_tag_name("a").text
    # ~ print(OP_user)

    """--OP User Link"""
    OP_user_link = OP_user_raw.find_element_by_tag_name("a").get_attribute("href")
    OP_user_link = OP_user_link.split("/")[-1]
    # ~ print(OP_user_link)

    """--OP Datetime--"""
    OP_datetime_raw = OP_footer_second_child.find_element_by_class_name(
        "display-post-timestamp"
    )
    OP_datetime = OP_datetime_raw.find_element_by_tag_name("abbr").get_attribute(
        "data-utime"
    )
    # ~ print(OP_datetime)

    if not visible_pages:
        max_page = 1
    else:
        max_page = visible_pages[-1].split("-")[-1]

    return topic_id, topic_name, OP_text, OP_user, OP_user_link, OP_datetime, max_page


def scrape(page):
    driver.get(page)
    html_page = driver.page_source
    soup = BeautifulSoup(html_page, "html.parser")

    comment_section = soup.select("div#comments-jsrender")
    sections = comment_section[0].find_all("div", id=re.compile("^comment-"))

    comment_ids = []
    comment_texts = []
    users = []
    user_links = []
    datetimes = []

    for section in sections:

        if section.find(class_="display-post-name"):
            comment_id_raw = section.find_all("span", class_="display-post-number")[0]
            comment_id = comment_id_raw.contents[0].split()[-1]
            comment_ids.append(comment_id)
            # print(comment_id)

            comment_text_raw = section.find_all("div", class_="display-post-story")[0]
            comment_text = comment_text_raw.get_text().strip()
            comment_texts.append(comment_text)
            # print(comment_text)

            """same section"""
            user_raw = section.find_all("a", class_="display-post-name")[0]
            user = user_raw.contents[0]
            users.append(user)
            # print(user)

            user_link = user_raw.get("href")
            # print(user_link)
            user_links.append(user_link.split("/")[-1])
            """end user section"""

            datetime_raw = section.find_all("span", class_="display-post-timestamp")[0]
            datetime = [x.get("data-utime") for x in datetime_raw.select("abbr")][0]
            datetimes.append(datetime)
            # print(datetime)

            # print('----\n\n\n')
            # ~ break
    return comment_ids, comment_texts, users, user_links, datetimes


def json_dump(filename, l):
    with open(filename, "w", encoding="utf8") as f:
        json.dump(l, f, ensure_ascii=False, indent=4)


def main(url):

    """Prelim Info"""
    (
        topic_id,
        topic_name,
        OP_text,
        OP_user,
        OP_user_link,
        OP_datetime,
        max_page,
    ) = prelim_info(url)

    print("Total page(s):", max_page)

    all_comment_ids = []
    all_comment_texts = []
    all_users = []
    all_user_links = []
    all_datetime = []

    """Append OP details"""
    all_comment_ids.append("0")
    all_comment_texts.append(OP_text)
    all_users.append(OP_user)
    all_user_links.append(OP_user_link)
    all_datetime.append(OP_datetime)

    current_page = 1  # change back to 1
    while current_page <= int(max_page):
        page_url = url + "/page" + str(current_page)

        comment_ids, comment_texts, users, user_links, datetimes = scrape(page_url)
        all_comment_ids.extend(comment_ids)
        all_comment_texts.extend(comment_texts)
        all_users.extend(users)
        all_user_links.extend(user_links)
        all_datetime.extend(datetimes)
        print("----", current_page, "done!----")

        current_page += 1

    # all_comment_ids = [int(ID) for ID in all_comment_ids]
    # all_datetime = [datetime.datetime.strptime(date, '%m/%d/%Y %H:%M:%S') for date in all_datetime]
    # all_comment_texts = [comment.replace('\n', ' ').replace('\t', ' ') for comment in all_comment_texts]

    # os.mkdir(topic_id)
    # json_dump(topic_id + '/' + 'topic_name.json', topic_name)
    # json_dump(topic_id + '/' + 'comment_ids.json', all_comment_ids)
    # json_dump(topic_id + '/' + 'comment_texts.json', all_comment_texts)
    # json_dump(topic_id + '/' + 'users.json', all_users)
    # json_dump(topic_id + '/' + 'datetime.json', all_datetime)

    def create_ebook():
        def comments(comment_id, comment_text, user):
            content = (
                "<b>"
                + comment_id
                + "</b><p>"
                + comment_text
                + "</p><p><b>—"
                + user
                + "</b></p>"
            )

            # content = "<b>" + comment_id + "</b><p>" + comment_text + "</p><b>—" + user + "</b>"
            return content

        header = "<meta charset='utf-8'/><h1>" + topic_name + "</h1><hr>"

        comments_html = ""
        for comment_id, comment_text, user in zip(
            all_comment_ids, all_comment_texts, all_users
        ):
            comments_html += comments(comment_id, comment_text, user)

        with open(topic_id + ".html", "w", encoding="utf8") as f:
            f.write(header + comments_html)

    create_ebook()
    print("fucking done")


# main('https://pantip.com/topic/31754895') # 131
# ~ main('https://pantip.com/topic/36282724') # 7
# main('https://pantip.com/topic/36270818') # 2
# main('https://pantip.com/topic/36378685') # 1
main("https://pantip.com/topic/33054306")
driver.quit()

files = glob.glob("*.html")

workers = []
while files or workers:
    while len(workers) < 4 and files:
        f = files[0]
        files = files[1:]
        w = subprocess.Popen(["ebook-convert", f, os.path.splitext(f)[0] + ".epub"])
        workers.append(w)
    for w in list(workers):
        if w.poll() is not None:
            workers.remove(w)
    time.sleep(0.1)
