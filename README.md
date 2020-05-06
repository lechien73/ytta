# YouTube Transcript Downloader

This is a simple YouTube Transcript Automator. It uses the [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api) to retrieve the text of a video transcript.

The purpose is to write the text of the transcript to a text file without any timing or duration information. This is helpful when uploading a transcript to an edited or lengthened video, or downloading the auto-generated transcript so it can be edited easily in a text editor.

## Usage

First, clone or download this repository.
Then, install the [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api) module. You can do this either by typing:
```
pip3 install -r requirements.txt
```
or
```
pip3 install youtube-transcript-api
```
Then, add your video URLS to your video list file one per line. You can use either the short address format from YouTube Studio, or the long address format from the YouTube website. If you use the long address format, then remove any extra URL parameters. Here are examples of acceptable URLS:

Short form URL: `https://youtu.be/-ACZIssOB94`

Long form URL: `https://www.youtube.com/watch?v=OmajI6m2Cvw`

You can add comments to the list file, by putting a `#` at the beginning of a line. These comments will be ignored. You can look at `videos.txt` as an example.

Finally, run `python3 ytta.py <list file>`.

So, if you use the supplied `videos.txt` file, it would be: `python3 ytta.py videos.txt`

This will process the videos and write the text of the transcript to a file called `ts_[YouTube Video ID].txt`

You can also call YTTA with the `-l` switch and supply a YouTube link as an argument, if you just want to get the transcript text for one video. Again, short and long format YouTube URLs are accepted.

So, `python3 ytta.py -l https://www.youtube.com/watch?v=uFZn6W3bokM` would retrieve the transcript of just this one video and write it to a file called: `ts_uFZn6W3bokM.txt`

### Limitations

The YouTube Transcript API filters out HTML tags in the transcript. It's a good idea to check if any HTML tags are present in the transcript and add them back manually afterwards.

### License

This script is provided under the MIT license. Please see LICENSE.txt for more information.
_____
Matt Rudge, April 2020
