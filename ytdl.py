from pytube import YouTube

VIDEO_SAVE_DIRECTORY = "./videos"

class VideoDownloader:
    def __init__(self, video_file_path):
        self.video_file_path = video_file_path
	
    def download(self):
        with open(self.video_file_path, 'r') as file:
            video_urls = file.readlines()
            print(video_urls)
        for video_url in video_urls:
            video_url = video_url.strip()  # Remove leading/trailing whitespace and newlines
            if video_url:
                self._download_video(video_url)

    def _download_video(self, video_url):
        try:
            video = YouTube(video_url)
            video_stream = video.streams.get_highest_resolution()
            video_stream.download(VIDEO_SAVE_DIRECTORY)
            print(f"Video '{video.title}' was downloaded successfully")
        except Exception as e:
            print(f"Failed to download video: {str(e)}")

if __name__ == "__main__":
    video_file_path = "videos.txt"  # Provide the path to your videos.txt file here
    downloader = VideoDownloader(video_file_path)
    downloader.download()

