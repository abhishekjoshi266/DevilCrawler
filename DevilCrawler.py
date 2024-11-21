import requests as r
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin as uj
import time as t

class C:
    def __init__(s):
        s.v = set()

    def c(s, u):
        if u in s.v:
            return
        print(f"Crawling: {u}")
        s.v.add(u)

        try:
            res = r.get(u)
            if res.status_code == 200:
                s.p(res.text, u)
            else:
                print(f"Failed to retrieve {u} with status code: {res.status_code}")
        except r.exceptions.RequestException as e:
            print(f"Error crawling {u}: {e}")

    def p(s, h, b):
        soup = bs(h, 'html.parser')
        for l in soup.find_all('a', href=True):
            f = uj(b, l['href'])
            if f not in s.v:
                s.c(f)
                t.sleep(1)

    def sr(s, fp):
        with open(fp, 'w') as f:
            for u in s.v:
                f.write(u + '\n')
        print(f"Results saved to {fp}")

def db():
    b = r"""

      +=====================================+
      |╔╦╗┌─┐┬  ┬┬┬    ╔═╗┬─┐┌─┐┬ ┬┬  ┌─┐┬─┐|
      | ║║├┤ └┐┌┘││    ║  ├┬┘├─┤││││  ├┤ ├┬┘|
      |═╩╝└─┘ └┘ ┴┴─┘  ╚═╝┴└─┴ ┴└┴┘┴─┘└─┘┴└─|
      +=====================================+  
                                                            
                                                                                     
    ==========================================
                Devil Crawler
    ==========================================
    Description: This tool helps you to crawl
                 websites which is known as web
                 spidering or web crawling.
    
    Created By: Abhishek Joshi
    Version: 1.0
    ==========================================
    """
    print(b)

if __name__ == "__main__":
    db()
    w = C()
    u = input("Enter the URL to start crawling: ")

    print("\nDevil Crawler started! Take a beer or cup of tea while the scan is in progress...\n")

    try:
        w.c(u)
    except KeyboardInterrupt:
        print("\nCrawling stopped by user.")
    
    fp = '/home/devilcrawl.txt'
    w.sr(fp)
    print(f"Visited URLs: {len(w.v)}")
    print("Exiting...")