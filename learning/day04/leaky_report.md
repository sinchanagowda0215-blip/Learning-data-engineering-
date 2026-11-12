### Validation frames

The script generated the following six validation frames:
src02-f01
src00-f03
src02-f02
src09-f00
src06-f01
src06-f00

### Source with leftover training frames

The source `src02` appears in the validation set with two frames:

src02-f01
src02-f02

But two other frames from the same source are still available for training:
src02-f00
src02-f03

### What I understood

Since frames from the same video can look very similar, the model could memorize patterns from the training frames and perform well on similar validation frames from the same video. This can lead to data leakage and misleading validation results.