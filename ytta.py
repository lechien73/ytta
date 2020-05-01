from youtube_transcript_api import YouTubeTranscriptApi


def get_video_urls():
    """
    Helper function to read the videos.txt file
    and return a list of URLS
    """

    with open("videos.txt") as f:
        videos = f.read().split("\n")

    return videos


def get_id_or_none(line):
    """
    Allows for comments in the videos.txt file
    Returns either the video ID or None
    """

    if line[0] == "#" or len(line) <= 1:
        video_id = None

    elif line[16] == "/":
        video_id = line[17:]
    
    elif line[31] == "=":
        video_id = line[32:]
    
    else:
        video_id = None
        print("Error: Unrecognised URL")

    return video_id


def write_transcript(video_id):
    """
    The meat and two veg of the whole shebang
    Gets the transcript from YouTube and writes
    text and no timings to a text file
    """

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    with open("ts_" + video_id + ".txt", "w") as o:
        for line in transcript:
            o.write(line["text"] + "\n")


def main():
    """
    Main program function. Calls the other helper
    functions
    """

    videos = get_video_urls()

    for video in videos:

        video_id = get_id_or_none(video)

        if video_id:
            print("Processing: %s" % video)
            write_transcript(video_id)
            
        else:
            print("Comment line - skipping")

if __name__ == "__main__":
    main()
