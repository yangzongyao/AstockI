# %%
import requests
import os

try:
    response = requests.get('http://localhost:4040/api/tunnels').json()
    url = response["tunnels"][0]["public_url"]
except:
    os._exit(0)

with open('README.md', 'r') as f:
    txt = f.readlines()

url_index = txt.index('### ngrok public url :\n') + 1
txt[url_index] = url + ' \n'

with open('README.md', 'w') as f:
    f.writelines(txt)
# %%
os.system('git add .')
os.system('git commit -m "auto update ngrok"')
os.system('git push origin master')