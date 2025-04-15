import requests
import json
import os
session = requests.Session()
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://portal.abs.xyz',
    'priority': 'u=1, i',
    'referer': 'https://portal.abs.xyz/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}
PROXIES = None
file_path = os.path.join(os.path.dirname(__file__), 'config.json')
if not os.path.exists(file_path):
    exit("请在当前目录下创建config.json文件，并添加x-privy-token和authorization字段")
with open(file_path, "r") as f:
    config = json.load(f)
    token = config["x-privy-token"]
    authorization = config["authorization"]

def get_id(address):
    response = requests.get(
        'https://backend.portal.abs.xyz/api/user/address/{}'.format(address),
        headers=headers,proxies=PROXIES
    ).json()
    id = response["user"]["id"]
    print(  "用户ID：", id)
    return id

def guanzhu(id):
    headers["x-privy-token"] = token
    headers["authorization"] = authorization
    json_data = {
        'followeeId': id,
    }
    response = requests.post('https://backend.portal.abs.xyz/api/user/follow', headers=headers, json=json_data,proxies=PROXIES).json()
    if response["id"]:
        print("关注成功")
        return True
    else:  
        print("关注失败", response)
        return False

def get_follows_id():
    params = {
        'limit': '20',
    }
    headers["x-privy-token"] = token
    headers["authorization"] = authorization
    response = requests.get('https://backend.portal.abs.xyz/api/user/387040/followers', params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data["items"]:
            return [item["id"] for item in data["items"]]
        else:
            print("没有关注的用户")
    else:
        print("请求失败，状态码：", response.status_code)

def is_follow(id):
    response = session.get('https://backend.portal.abs.xyz/api/user/387040/follows/{}'.format(id), headers=headers,proxies=PROXIES)
    if response.status_code == 200:
        if response.json()["result"]:
            print(id,"已关注")
            return True
        else:
            print(id,"未关注")
            return False
    else:
        print("请求失败，状态码：", response.status_code)
        return False

def main():
    followers =get_follows_id()
    print("followers:", followers)
    if not followers:
        print("没有关注的用户")
        return
    for follow_id in followers:
        if not is_follow(follow_id):
            guanzhu(follow_id)
if __name__ =="__main__":
    main()
