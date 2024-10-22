# YouTube Downloader (Personal Use)

This is a simple YouTube downloader project for personal use. It allows you to download YouTube videos as MP3 or MP4 files via a command-line interface. The downloader offers options to fetch videos from URLs, playlists, or search queries, as well as downloading from lists stored in text files.

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

## Acknowledgements

This project is for educational purposes only. Please respect the YouTube terms of service and do not use this project for commercial purposes.
