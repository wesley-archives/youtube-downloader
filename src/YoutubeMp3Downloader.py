import yt_dlp
import os

class YoutubeMp3Downloader:
    
    def __init__(self):
        self.download_dir = os.path.join(os.path.dirname(__file__), '..', 'downloads')
        
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(self.download_dir, '%(title)s.%(ext)s'),
            'quiet': True,
            'noplaylist': True
        }

    def downloadFromPlaylist(self, url):
        """Download all audio tracks from a YouTube playlist in mp3 format."""
        playlist_opts = self.ydl_opts.copy()
        playlist_opts['noplaylist'] = False
        with yt_dlp.YoutubeDL(playlist_opts) as ydl:
            ydl.download([url])

    def downloadFromUrl(self, url):
        """Download audio from a YouTube video using its URL."""
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])

    def downloadFromSearch(self, query):
        """Download the first result from a YouTube search query."""
        search_opts = self.ydl_opts.copy()
        search_opts['default_search'] = 'ytsearch'
        with yt_dlp.YoutubeDL(search_opts) as ydl:
            ydl.download([query])

    def downloadFromFileByTitle(self, file):
        """Read a file containing titles (one per line), search YouTube, and download the audio."""
        with open(file, 'r') as f:
            for line in f:
                title = line.strip()
                if title:
                    self.downloadFromSearch(title)

    def downloadFromFileByUrl(self, file):
        """Read a file containing URLs (one per line) and download the audio."""
        with open(file, 'r') as f:
            for line in f:
                url = line.strip()
                if url:
                    self.downloadFromUrl(url)
