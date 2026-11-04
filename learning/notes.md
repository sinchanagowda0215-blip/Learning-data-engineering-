## AI Schema Review

Accepted suggestion: `camera_id`

Reason: It helps distinguish samples recorded by different cameras during the same match.

Rejected suggestions: Extra fields such as confidence, UUID, embedding and quality score are unnecessary for this task.


# Day 1 – Say It Back

1. What is a manifest?

A manifest is a file that contains information about all the rows in a dataset. It tells us where each row came from, its timestamp, label and status. It also tells us whether that row can be used for training or not. This helps us keep track of the dataset and understand what is happening with each row.

2. Why do rejected rows stay in the file?

We keep rejected rows because we should not simply remove them when something goes wrong. By keeping them, we can understand why they were rejected and what happened during the labelling process. It also helps us avoid using incorrect data for training by mistake.

3. Why does the second run get a new folder?

Every time we run the Python script, it creates a new folder instead of replacing the previous output. For example, the first run creates v1 and the second run creates v2. This way, we can keep the previous results safe and compare them with the new results whenever needed.

4. Which two statuses are trainable, and why is unmatched not one of them?

The two trainable statuses are matched and no_positive. A matched row means the generated label successfully matched an existing box, while no_positive means the system correctly found nobody to mark. Unmatched is not trainable because the generated label did not land on an existing box. Even if the row has a label like active, we cannot trust it for training because the label was not matched correctly.
