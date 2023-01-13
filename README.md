# RenameSubtitles
Rename subtitles to match with the corresponding video file name.

# Function

## before

```bash
[VCB-Studio]
├── subs
|   ├── sub01.ass
│   └── sub02.ass
└── videos
    ├── [VCB-Studio] Sora no Otoshimono [01][Hi10p_1080p][x264_flac].mkv
    └── [VCB-Studio] Sora no Otoshimono [02][Hi10p_1080p][x264_flac].mkv
```

## after

```bash
[VCB-Studio]
├── subs
|   ├── [VCB-Studio] Sora no Otoshimono [01][Hi10p_1080p][x264_flac].ass
│   └── [VCB-Studio] Sora no Otoshimono [02][Hi10p_1080p][x264_flac].ass
└── videos
    ├── [VCB-Studio] Sora no Otoshimono [01][Hi10p_1080p][x264_flac].ass
    ├── [VCB-Studio] Sora no Otoshimono [02][Hi10p_1080p][x264_flac].ass
    ├── [VCB-Studio] Sora no Otoshimono [01][Hi10p_1080p][x264_flac].mkv
    └── [VCB-Studio] Sora no Otoshimono [02][Hi10p_1080p][x264_flac].mkv
```