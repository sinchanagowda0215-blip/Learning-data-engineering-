Quantity:
True positives : 1
False positives : 2
False negatives : 1
True negatives : 6
Accuracy: 0.70
Positive precision: 1/3
Positive recall: 1/2

Labelling Four Predictions

1. Prediction: A
   Outcome: Correct
   The model correctly identified player A as active.

2. Prediction: nobody
   Outcome: Missed
   Player A was active, but the model failed to identify anyone.

3. Prediction: C
   Outcome: Wrong instance
   Player A was active, but the model identified player C instead.

4. Prediction: A (when nobody is active)
   Outcome: False positive
   The model predicted player A as active even though nobody was active.