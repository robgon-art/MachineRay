import urllib
import re
from bs4 import BeautifulSoup
import time

file_path = "art/wikiart"
base_url = "https://www.wikiart.org"

# iterate through all artists by last name alphabetically
for c in range(ord('n'), ord('z')+1):
    char = chr(c)
    artist_list_url = base_url + '/en/Alphabet/' + char + '/text-list'

    genre_soup = BeautifulSoup(urllib.request.urlopen(artist_list_url), "lxml")
    artist_list_main = genre_soup.find("main")
    lis = artist_list_main.find_all("li")

    # for each list element
    for li in lis: 
        born = 0
        died = 0

        # get the date range
        for line in li.text.splitlines():
            if line.startswith(",") and "-" in line:
                parts = line.split('-')
                if len(parts) == 2:
                    born = int(re.sub("[^0-9]", "",parts[0]))
                    died = int(re.sub("[^0-9]", "",parts[1]))

        # look for artists who may have created work that could in public domain
        if born>1850 and died>0 and (born<1900 or died<1950):
            link = li.find("a")
            artist = link.attrs["href"]

            if artist == "/en/salvador-dali": # skip Dali
                continue

            # get the artist's main page
            artist_url = base_url + artist
            artist_soup = BeautifulSoup(urllib.request.urlopen(artist_url), "lxml")

            # only look for artists with the word abstract on their main page
            if "Abstract" in artist_soup.text or "abstract" in artist_soup.text or "Avant-garde" \
                in artist_soup.text or "avant-garde" in artist_soup.text:
                print(artist + " " + str(born) + " - " + str(died))

                # get the artist's web page for the artwork
                url = base_url + artist + '/all-works/text-list'
                artist_work_soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")

                # get the main section
                artist_main = artist_work_soup.find("main")
                image_count = 0
                artist_name = artist.split("/")[2]

                # get the list of artwork
                lis = artist_main.find_all("li")

                # for each list element
                for li in lis:
                    link = li.find("a")

                    if link != None:
                        painting = link.attrs["href"]

                        # get the painting
                        url = base_url + painting
                        print(url)

                        try:
                            painting_soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")

                        except:
                            print("error retreiving page")
                            continue

                        # check the copyright
                        if "Public domain" in painting_soup.text:

                            #check the genre
                            genre = painting_soup.find("span", {"itemprop":"genre"})
                            if genre != None and genre.text == "abstract":

                                # get the url
                                og_image = painting_soup.find("meta", {"property":"og:image"})
                                image_url = og_image["content"].split("!")[0] # ignore the !Large.jpg at the end
                                print(image_url)

                                save_path = file_path + "/" + artist_name + "_" + str(image_count) + ".jpg"

                                #download the file
                                try:
                                    print("downloading to " + save_path)
                                    time.sleep(0.2)  # try not to get a 403                    
                                    urllib.request.urlretrieve(image_url, save_path)
                                    image_count = image_count + 1
                                except Exception as e:
                                    print("failed downloading " + image_url, e) 
