## 1. Good AI Response

Trainable IDs: 1, 2, 5, 8.

The easy mistake is row 3 (`unmatched`). It already has the label `active`, so it looks finished. The status says the label never landed on a real box, so training on it would teach a box that is not in the annotations.

## 2. Weak AI Response

Train all rows where the label is active or passive. That gives you more data.

## 3. Which rule did the weak reply drop?

The weak reply dropped the rule that only rows with `matched` or `no_positive` status are trainable. It selected rows based on their labels instead of checking their status, which could allow incorrect rows like row 3 (`unmatched`) into training.
