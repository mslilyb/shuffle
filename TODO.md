# This is a To Do List

**This is my todo list for coding related projects. It will be split into issues and steps to address them. The issues will be numbered, and the steps will reference the issue number to clarify what they are for.**

## Issues

1.  As per Dr. Korf,
> The current strawman.py builds two weight matrices: one for observed sites and one for non-observed sites. Then, when someone hands you a new sequence, you check which one it matches better to determine which class it belongs to. But this isn't the way most people use PWMs. Usually they use a single observed matrix and some probability threshold. We should have some code that replicates this use pattern.
10:23
So we need a function that optimally finds the threshold to split the training set. Then use that threshold on the testing set to evaluate performance. All of this done in a cross-validation context just like strawman.py currently does.

2.  Udemy Coursework must continue!


## Steps

* (Issue 1) Obtain statistical definitions of position weight matrices in a context that matches what the prompt is saying, including the use of a probability threshold
  * Optionally, also define kmeans clustering, apriori and what a k position weight matrix is.

* (Issue 1) Take a look at strawman.py and deterine the requisite knowledge to tackle this problem

* (Issue 2) Download and set up the IntelliJ IDE as per the instructions on the video 
