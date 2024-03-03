import re
from pytube import YouTube, Playlist
import xlsxwriter

myPlaylist = Playlist('https://www.youtube.com/playlist?list=PLreQuyISKhq6ak7nqy9IdpyquDo8AezjC')
myPlaylist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

def getPlaylistVideos(playlistUrl):
    videoTitles = []
    videoUrls = []
    for url in playlistUrl.video_urls:
        yt = YouTube(url)
        videoTitles.append(yt.title)
        videoUrls.append(yt.watch_url)
    return videoTitles, videoUrls


def writeToExcel(videoTitles, videoUrls):
    workbook = xlsxwriter.Workbook('ΛίσταΡεμπέτικα.xlsx')
    worksheet = workbook.add_worksheet('Λίστα τραγουδιών')
    worksheet.write_row(0, 0, ["Τίτλος", "URL"])
    for i, (title, url) in enumerate(zip(videoTitles, videoUrls), start=2):
        worksheet.write(f'A{i}', title)
        worksheet.write(f'B{i}', f'{url}')

    workbook.close()

titles, urls = getPlaylistVideos(myPlaylist)
writeToExcel(titles, urls)