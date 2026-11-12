### 1. What does an IoU of 1 mean? What does an IoU near 0.14 mean at a 0.5 threshold?
IoU = 1 means two bounding boxes overlap completely. They are identical.
IoU near 0.14 means the boxes have very little overlap.
Since 0.14 is below the threshold of 0.5, the boxes are classified as `unmatched`.

### 2. Why is an empty file different from a missing file?
An empty file means the image was processed and confirmed to contain no target objects. It is a negative training example.
A missing file means no label was provided for that image. We cannot assume that the image contains no objects.

### 3. What do the four numbers after the class ID mean?

The four numbers in YOLO format represent:

1. Normalized center X coordinate.
2. Normalized center Y coordinate.
3. Normalized bounding box width.
4. Normalized bounding box height.

These values are normalized using the image width and height, so they generally fall between 0 and 1.