"""
YTTA - YouTube Transcript Automator
Should that be "Automater"? I don't know!
Simple script using the YouTube Transcript API to retrieve
the transcript of videos and write the text to a new file
without timing or duration data.

(c) Matt Rudge
Code Institute, April 2020
MIT License
"""

import sys
import re

from youtube_transcript_api import YouTubeTranscriptApi


def get_video_urls(list_file):
    """
    Helper function to read the videos.txt file
    and return a list of URLS
    """

    try:
        with open(list_file) as f:
            videos = f.read().split("\n")
    except IOError:
        sys.exit("Error: File not found")

    return videos


def get_id_or_none(line):
    """
    Allows for comments in the videos.txt file
    Returns either the video ID or None
    """

    if line[0] == "#" or len(line) <= 1:
        video_id = None

    else:
        result = re.search("([^\/|\=]*)$", line)
        video_id = result.group(0) if result else None

    return video_id


def write_transcript(video_id):
    """
    The tofu and two veg of the whole shebang
    Gets the transcript from YouTube and writes
    text and no timings to a text file
    """

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    with open(f"ts_{video_id}.txt", "w") as o:
        o.write("\n".join([line["text"] for line in transcript]))


def main(file_mode, file_or_url):
    """
    Main program function. Calls the other helper
    functions
    """

    if file_mode:
        videos = get_video_urls(file_or_url)
    else:
        videos = [file_or_url]

    for video in videos:

        video_id = get_id_or_none(video)

        if video_id:
            print(f"Processing: {video}")
            write_transcript(video_id)

        else:
            print("Warning: Skipped line")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Usage: python3 ytta.py <list filename> OR -l <YouTube link>")
    
    if sys.argv[1] == "-l":
        main(False, sys.argv[2])
    else:
        main(True, sys.argv[1])
