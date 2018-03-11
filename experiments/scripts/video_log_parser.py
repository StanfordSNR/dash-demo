#!/usr/bin/env python3

import argparse
import re


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('logfile', type=str, help='Log file to parse')
    return parser.parse_args()


VIDEO_EVENT_RE = re.compile(r'\"VIDEO_EVENT\s+(\w+)\s+(\d+)\",')
DASH_FETCH_VIDEO_CHUNK_RE = re.compile(r'getNextFragment - request is http://[\w.:\d]+/static/dash/media/(\d+x\d+-\d+)/(\d+).m4s')
DASH_FETCH_AUDIO_CHUNK_RE = re.compile(r'getNextFragment - request is http://[\w.:\d]+/static/dash/media/(\d+k)/(\d+).chk')

TIMESTAMP_RE = re.compile(r'^\[\d+:\d+:\d+/(\d+\.\d+):INFO:CONSOLE\(\d+\)\]')


def main(logfile):
    with open(logfile) as fp:
        for line in fp:
            line = line.strip()

            timestamp_match = TIMESTAMP_RE.search(line)
            if not timestamp_match:
                continue
            timestamp = float(timestamp_match.group(1))

            video_event_match = VIDEO_EVENT_RE.search(line)
            if video_event_match:
                print(timestamp, video_event_match.group(1),
                      video_event_match.group(2))
            del video_event_match

            dash_fetch_video_match = DASH_FETCH_VIDEO_CHUNK_RE.search(line)
            if dash_fetch_video_match:
                print(timestamp, 'video', dash_fetch_video_match.group(1),
                      dash_fetch_video_match.group(2))
            del dash_fetch_video_match

            dash_fetch_audio_match = DASH_FETCH_AUDIO_CHUNK_RE.search(line)
            if dash_fetch_audio_match:
                print(timestamp, 'audio', dash_fetch_audio_match.group(1),
                      dash_fetch_audio_match.group(2))
            del dash_fetch_audio_match


if __name__ == '__main__':
    main(**vars(get_args()))
