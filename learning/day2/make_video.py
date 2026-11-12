import cv2
import numpy as np
from pathlib import Path

FPS = 30
SECONDS = 3
WIDTH, HEIGHT = 320, 180
SOURCE_ID = "clip_a"


def main() -> None:
    path = str(Path(__file__).resolve().parent / "clip_a.mp4")

    writer = cv2.VideoWriter(
        path,
        cv2.CAP_FFMPEG,
        cv2.VideoWriter_fourcc(*"mp4v"),
        FPS,
        (WIDTH, HEIGHT),
    )

    if not writer.isOpened():
        raise RuntimeError("FFMPEG could not open the video writer.")

    for frame_index in range(FPS * SECONDS):
        image = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

        x = frame_index
        cv2.rectangle(image, (x, 40), (x + 30, 100), (0, 0, 255), -1)

        cv2.putText(
            image,
            f"f={frame_index}",
            (8, 24),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            1,
        )

        writer.write(image)

    writer.release()

    if not Path(path).exists() or Path(path).stat().st_size == 0:
        raise RuntimeError("Video file was not created properly.")

    print("Video created successfully:", path)


if __name__ == "__main__":
    main()