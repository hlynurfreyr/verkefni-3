import requests

def minify( css_file, out_file):
    with open(css_file, 'r') as c:
        css = c.read()

    payload = {'input': css}
    url = 'https://cssminifier.com/raw'
    r = requests.post(url, payload)

    with open(out_file, 'w') as m:
        m.write(r.text)