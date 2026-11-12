from pathlib import Path


def yolo_to_xyxy(line, width, height):
    class_id, cx, cy, bw, bh = line.split()

    cx, cy, bw, bh = (float(v) for v in (cx, cy, bw, bh))

    cx *= width
    cy *= height
    bw *= width
    bh *= height

    left = cx - bw / 2
    top = cy - bh / 2

    return int(class_id), (left, top, left + bw, top + bh)


def read_label(filename):
    path = Path(__file__).parent / "labels" / filename

    line = path.read_text().strip()

    if not line:
        print(f"{filename}: Empty label file (no objects)")
        return

    class_id, box = yolo_to_xyxy(line, 100, 100)

    # Convert whole-number coordinates to integers for clean output.
    box = tuple(int(round(value)) for value in box)

    print(f"{filename}: class={class_id}, box={box}")


if __name__ == "__main__":
    read_label("example_100.txt")
    read_label("a.txt")
    read_label("c.txt")