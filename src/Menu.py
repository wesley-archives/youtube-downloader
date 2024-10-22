from src.YoutubeMp3Downloader import YoutubeMp3Downloader
from src.YoutubeMp4Downloader import YoutubeMp4Downloader

def main_menu():
    mp3_downloader = YoutubeMp3Downloader()
    mp4_downloader = YoutubeMp4Downloader()

    while True:
        print("\nHi, welcome to YT Downloader, please choose your option:")
        print("1. MP3 Downloader")
        print("2. MP4 Downloader")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            handle_mp3_downloader(mp3_downloader)
        elif choice == '2':
            handle_mp4_downloader(mp4_downloader)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def handle_mp3_downloader(mp3_downloader):
    while True:
        print("\nMP3 Downloader Options:")
        print("1. Download from URL")
        print("2. Download from Playlist")
        print("3. Download from Search")
        print("4. Download from File (Titles)")
        print("5. Download from File (URLs)")
        print("6. Back to Main Menu")

        mp3_choice = input("Enter your choice (1/2/3/4/5/6): ")

        if mp3_choice == '1':
            url = input("Enter the YouTube URL: ")
            try:
                mp3_downloader.downloadFromUrl(url)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif mp3_choice == '2':
            url = input("Enter the Playlist URL: ")
            try:
                mp3_downloader.downloadFromPlaylist(url)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif mp3_choice == '3':
            query = input("Enter the search query: ")
            try:
                mp3_downloader.downloadFromSearch(query)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif mp3_choice == '4':
            file_path = input("Enter the file path (with titles): ")
            try:
                mp3_downloader.downloadFromFileByTitle(file_path)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif mp3_choice == '5':
            file_path = input("Enter the file path (with URLs): ")
            try:
                mp3_downloader.downloadFromFileByUrl(file_path)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif mp3_choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

def handle_mp4_downloader(mp4_downloader):
    while True:
        print("\nMP4 Downloader Options:")
        print("1. Download from URL")
        print("2. Download from Playlist")
        print("3. Download from Search")
        print("4. Download from File (Titles)")
        print("5. Download from File (URLs)")
        print("6. Back to Main Menu")

        mp4_choice = input("Enter your choice (1/2/3/4/5/6): ")

        if mp4_choice == '1':
            url = input("Enter the YouTube URL: ")
            try:
                mp4_downloader.downloadFromUrl(url)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif mp4_choice == '2':
            url = input("Enter the Playlist URL: ")
            try:
                mp4_downloader.downloadFromPlaylist(url)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif mp4_choice == '3':
            query = input("Enter the search query: ")
            try:
                mp4_downloader.downloadFromSearch(query)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif mp4_choice == '4':
            file_path = input("Enter the file path (with titles): ")
            try:
                mp4_downloader.downloadFromFileByTitle(file_path)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif mp4_choice == '5':
            file_path = input("Enter the file path (with URLs): ")
            try:
                mp4_downloader.downloadFromFileByUrl(file_path)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif mp4_choice == '6':
            break
        else:
            print("Invalid choice, please try again.")
