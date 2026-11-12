### 1. Why is a frame shuffle a leak for video?

When we randomly split individual frames, frames from the same video can end up in both training and validation. Since nearby frames look very similar, the model might already have seen almost the same scene during training. This can lead to data leakage and misleading validation results. That's why we should split by source instead of individual frames.

### 2. What does seed 42 buy you, and what does it not guarantee about quality?

Seed 42 helps us get the same random split every time we run the code. This makes our results repeatable and easier to compare. However, it does not guarantee that the split is good, balanced or free from data leakage. We still need to check how the data is split.

### 3. When is accuracy a misleading score?

Accuracy can be misleading when one class has many more samples than the other. For example, if we have 16 passive and 4 active candidates, a model that predicts everyone as passive gets 80% accuracy but completely misses all active candidates. So, accuracy alone cannot tell us whether the model is performing well.

### 4. Which score answers "did we mark the right player?"

Application-level outcomes answer this question. We need to check whether the system marked the correct player, missed the active player, selected the wrong player or marked someone active when nobody was active.