import sys

def process(obj):
    a = obj.url
    return a
class runner(object):
    def __init__(self, url):
        self.url = url
def run(URL='http://127.0.0.1'):
    print(process(runner(URL)))
if __name__ == "__main__":
    run(sys.argv[0])
