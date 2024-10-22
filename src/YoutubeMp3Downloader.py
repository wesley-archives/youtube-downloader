import yt_dlp
import os

class YoutubeMp3Downloader:
    
    def __init__(self):
        self.base_download_dir = os.path.join(os.path.dirname(__file__), '..', 'downloads')
        
        if not os.path.exists(self.base_download_dir):
            os.makedirs(self.base_download_dir)
        
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'noplaylist': True
        }

    def _get_channel_name(self, info_dict):
        """Extracts and sanitizes the channel name from the video metadata."""
        channel = info_dict.get('uploader', 'UnknownChannel')
        return ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in channel)

    def _download_with_channel_subdir(self, url, index=None, total=None):
        """Fetch metadata, create directory for the channel, and download the audio."""        
        ydl_opts = self.ydl_opts.copy()
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)

                if not isinstance(info_dict, dict):
                    raise ValueError(f"Expected 'info_dict' to be a dictionary, got {type(info_dict)}")

                channel_name = self._get_channel_name(info_dict)
                download_dir = os.path.join(self.base_download_dir, channel_name)
                
                if not os.path.exists(download_dir):
                    os.makedirs(download_dir)

                ydl_opts['outtmpl'] = os.path.join(download_dir, '%(title)s.%(ext)s')

                if index is not None and total is not None:
                    print(f"Downloading ({index}/{total}): {info_dict.get('title', 'Unknown Title')}, by {channel_name}")

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

        except Exception as e:
            print(f"Error downloading {info_dict.get('title', 'Unknown Title')}: {e}")


    def downloadFromPlaylist(self, url, start_index=1):
        """Download all audio tracks from a YouTube playlist in mp3 format, starting from a given index."""
        playlist_opts = self.ydl_opts.copy()
        playlist_opts['noplaylist'] = False
        playlist_opts['extract_flat'] = True

        print("Fetching playlist information, please wait...\n")

        try:
            with yt_dlp.YoutubeDL(playlist_opts) as ydl:
                playlist_info = ydl.extract_info(url, download=False)
                total_videos = len(playlist_info['entries'])

                print(f"{total_videos} videos found in the playlist.")

                if not playlist_info['entries']:
                    print("No videos found in the playlist.")
                    return

                for index, video_info in enumerate(playlist_info['entries'], start=1):
                    if index < start_index:
                        continue
                    
                    video_url = video_info.get('url', video_info.get('webpage_url'))
                    
                    if video_url:
                        print(f"\nProcessing video {index}/{total_videos}, please wait...")
                        
                        try:
                            self._download_with_channel_subdir(f"https://www.youtube.com/watch?v={video_info['id']}", index, total_videos)
                        except Exception as e:
                            print(f"Error downloading video {index}/{total_videos}: {e}")
                    else:
                        print(f"Skipping video {index}/{total_videos}: Unable to extract URL.")

        except Exception as e:
            print(f"An error occurred while downloading playlist: {e}")



    def downloadFromUrl(self, url):
        """Download audio from a YouTube video using its URL."""
        self._download_with_channel_subdir(url)

    def downloadFromSearch(self, query):
        """Download the first result from a YouTube search query."""
        search_opts = self.ydl_opts.copy()
        search_opts['default_search'] = 'ytsearch'
        
        with yt_dlp.YoutubeDL(search_opts) as ydl:
            info_dict = ydl.extract_info(query, download=False)
            video_url = info_dict['entries'][0]['webpage_url']
            self._download_with_channel_subdir(video_url)

    def downloadFromFileByTitle(self, file):
        """Read a file containing titles (one per line), search YouTube, and download the audio."""
        with open(file, 'r') as f:
            lines = f.readlines()
            total_titles = len(lines)
            
            for index, line in enumerate(lines, start=1):
                title = line.strip()
                if title:
                    print(f"Searching for '{title}' ({index}/{total_titles})")
                    self.downloadFromSearch(title)

    def downloadFromFileByUrl(self, file):
        """Read a file containing URLs (one per line) and download the audio."""
        with open(file, 'r') as f:
            lines = f.readlines()
            total_urls = len(lines)
            
            for index, line in enumerate(lines, start=1):
                url = line.strip()
                if url:
                    self._download_with_channel_subdir(url, index, total_urls)
