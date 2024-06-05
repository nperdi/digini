import urllib.request

def check_network_access():
    try:
        response = urllib.request.urlopen("http://www.ncbi.nlm.nih.gov/")
        # response = urllib.request.urlopen("http://rhodes.mm.di.uoa.gr/test")
        print("Response code:", response.getcode())
    except Exception as e:
        print("Network access failed:", e)

check_network_access()