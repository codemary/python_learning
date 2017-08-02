from requests import get


def nytimes_api(api_key, end_point, section):

    payload = {'api-key': api_key}
    r = get('https://api.nytimes.com/svc/' + end_point +
            '/v2/' + section + '.json', params=payload)
    print(r.url)
    top_stories = r.json()
    results = top_stories['results']
    f = open(end_point + '_' + section + '.csv', 'w')
    f.write("title,url")
    f.write('\n')
    for r in results:
        title = r["title"]
        url = r["url"]
        record = title + ',' + url + '\n'
        f.write(record)
        print(record)
    f.close()


nytimes_api("28e368b2af754f25a589ee9fe5383561", "topstories", "food")
