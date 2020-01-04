import bs4
import urllib.request, urllib.error
import os
import argparse
import sys
import json

# How To
# -n: ダウンロードする画像の数量 (デフォルト 10枚)
# -o: 画像の保存先 (デフォルト　<DEFAULT_SAVE_DIRECTORY>で指定する)

def get_soup(url,header):
    r = urllib.request.urlopen(urllib.request.Request(url,headers=header))
    return bs4.BeautifulSoup(r,'html.parser')

def main(args, search):
    parser = argparse.ArgumentParser(description='Options for scraping Google images')
    parser.add_argument('-n', '--num_images', default=10, type=int, help='num of images to scrape')
    parser.add_argument('-o', '--directory', default='<DEFAULT_SAVE_DIRECTORY>', type=str, help='output directory')
    args = parser.parse_args()

    # 複数のキーワードを"+"で繋げる
    query = search.split()
    query = '+'.join(query)
    max_images = args.num_images

    # 画像をフォルダーでグループする
    save_directory = args.directory + '/' + query
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # スクレーピング
    query = urllib.parse.quote(query)
    url="https://www.google.co.jp/search?q="+query+"&source=lnms&tbm=isch"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)
    ActualImages=[]

    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))
    for i , (img , Type) in enumerate( ActualImages[0:max_images]):
        try:
            Type = Type if len(Type) > 0 else 'jpg'
            print("Downloading image {} ({}), type is {}".format(i, img, Type))
            raw_img = urllib.request.urlopen(img).read()
            f = open(os.path.join(save_directory , "img_"+str(i)+"."+Type), 'wb')
            f.write(raw_img)
            f.close()
        except Exception as e:
            print ("could not load : "+img)
            print (e)

if __name__ == '__main__':
    from sys import argv
    try:

        with open('configs/stores.json') as f:
            df = json.load(f)

        for search in df:
            main(argv, search)

    except KeyboardInterrupt:
        pass
    sys.exit()
