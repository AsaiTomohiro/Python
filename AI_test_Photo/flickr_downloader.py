from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os, time, sys

def download(keyword, savedir, api_key, api_secret, max_count=300, size_type="q"):
    if not os.path.exists(savedir): os.mkdir(savedir)
    if max_count > 500: max_count = 500
    url_type = "url_" + size_type
    flickr = FlickrAPI(api_key, api_secret, format='parsed-json')
    res = flickr.photos.search(
        text=keyword, 
        per_page=max_count,
        media='photos',
        sort="relevance",
        safe_search=1,
        extras=url_type+',license')
    # print result
    photos = res['photos']
    try:
        # download photos
        for i, photo in enumerate(photos['photo']):
            url = photo[url_type]
            filepath = savedir + '/' + photo['id'] + '.jpg' # 保存先
            if os.path.exists(filepath): continue
            print(str(i + 1) + ":download=" + url)
            urlretrieve(url, filepath)
            time.sleep(1)
    except:
        import traceback
        traceback.print_exc()

