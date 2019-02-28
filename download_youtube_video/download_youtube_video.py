# Available options
# https://github.com/rg3/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312
import youtube_dl

opts = {
    # 'writeinfojson': True,
    # 'skip_download': True,
    'outtmpl': '/home/alex/Videos/youtube/downloads/%(title)s.%(ext)s',
    'format': '22',
    # 'listformats': True
}

#%%
ydl = youtube_dl.YoutubeDL(opts)
link = 'https://www.youtube.com/watch?v=QILNSgou5BY'

with ydl:
    result = ydl.extract_info(url=link, download=True)
    print(result['view_count'])

