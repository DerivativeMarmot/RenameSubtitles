# RenameSubtitles
Rename subtitles to match with the corresponding video file name.

# Function

## before

```bash
[VCB-Studio]
├── subs
│   ├── sub01.ass
│   └── sub02.ass
└── videos
    ├── [VCB-Studio] Masou Gakuen HxH 01 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).mkv
    └── [VCB-Studio] Masou Gakuen HxH 02 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).mkv
```

## after

```bash
[VCB-Studio]
├── subs
│   ├── [VCB-Studio] Masou Gakuen HxH 01 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).ass
│   └── [VCB-Studio] Masou Gakuen HxH 02 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).ass
└── videos
    ├── [VCB-Studio] Masou Gakuen HxH 01 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).ass
    ├── [VCB-Studio] Masou Gakuen HxH 02 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).ass
    ├── [VCB-Studio] Masou Gakuen HxH 01 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).mkv
    └── [VCB-Studio] Masou Gakuen HxH 02 (BDrip 1920x1080 HEVC-YUV420P10 FLAC).mkv
```
