# YouTube Downloader (Personal Use)

This is a YouTube downloader project intended strictly for personal use. It allows you to download YouTube videos as MP3 (audio) or MP4 (video) files through a command-line interface. This tool supports downloading from single URLs, playlists, search queries, or from lists of URLs saved in text files.

> ⚠️ Note: This tool is intended only for downloading non-copyrighted content or videos with explicit permission for free use. Always respect [YouTube's Terms of Service](https://www.youtube.com/t/terms) and copyright laws. Unauthorized downloading of copyrighted material is strictly prohibited.

## Features

- Download YouTube videos in MP3 format (audio only)
- Download YouTube videos in MP4 format (video)
- Download via URL, playlist, search, or file-based inputs

## Project Structure

```plaintext
downloads/
src/
    YoutubeMp3Downloader.py
    YoutubeMp4Downloader.py
    Menu.py
main.py
```

## Usage

### Requirements

- Python 3x
- FFmpeg
- yt-dlp
- Virtualenv (optional)

### Installation

1. Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the program:

```bash
python main.py
```

4. Follow the on-screen instructions to download YouTube videos or music.

5. Your downloads will be saved in the `downloads/` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements and Disclaimer

This project is intended for personal use only. Please respect YouTube’s Terms of Service and copyright laws. Only download videos that are either non-copyrighted or have been released under a free-use license. Unauthorized downloading of copyrighted content may lead to legal consequences. Use this tool responsibly.