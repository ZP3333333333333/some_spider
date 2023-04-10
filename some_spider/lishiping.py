import requests

url = "https://www.pearvideo.com/video_1127534"
contId = url.split("_")[1]
# print(contId)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    , "Referer": "https://www.pearvideo.com/video_1127534"
}
videoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.4060045770521099"
resp = requests.get(videoStatus, headers=headers)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']

systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
print(srcUrl)
with open("../a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
print("over!!!")

# https://video.pearvideo.com/mp4/short/20170809/cont-1127534-10733030-hd.mp4
# https://video.pearvideo.com/mp4/short/20170809/1681045241990-10733030-hd.mp4
# https://video.pearvideo.com/mp4/short/20170809/1681045835019-10733030-hd.mp4
