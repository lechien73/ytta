# YouTube Transcript Downloader

This is a simple YouTube Transcript Automator. It uses the [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api) to retrieve the text of a video transcript.

The purpose is to write the text of the transcript to a text file without any timing or duration information. This is helpful when uploading a transcript to an edited or lengthened video.

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
Then, add your video URLS to the `video.txt` file. You can use either the short address format from YouTube Studio, or the long address format from the YouTube website. If you use the long address format, then remove any extra URL parameters. Here are examples of acceptable URLS:

`https://youtu.be/-ACZIssOB94`

`https://www.youtube.com/watch?v=OmajI6m2Cvw`

You can add comments to the `video.txt` file, by putting a `#` at the beginning of a line. These comments will be ignored.

Finally, run `python3 ytta.py`. This will process the videos and write the text of the transcript to a file called `ts_[YouTube Video ID].txt`

### License

This script is provided under the MIT license. Please see LICENSE.txt for more information.
_____
Matt Rudge, April 2020