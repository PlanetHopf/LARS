A list of links to any issues that you think show your progress and any commits, along with an explanation why you picked those contributions. 
I will look at your GitHub repository in any case to see what progress you have made, but if there is anything you think stands out, please point me directly to it.
I expect there to be at least 1 contribution per team member in the form of comments on issues, commits, etc.
Contributions should be meaningfully show progress on the project. A commit that fixes a typo does not count as a meaningful contribution; expanding on the readme by adding the coding conventions you plan to employ does count.
A list of any issues that you were able to complete and close.
At this point, you ideally getting closer to be finished with your "must have" issues. However, there is no strict requirement for how many issues you should have closed by now for this assignment. 


Peter Call Experience

I was working on a Python project and encountered a challenge with GitHub Actions, specifically with it not accessing folders in the main branch for testing. Initially, I suspected the problem might be related to workflow configuration or path specifications. I faced a ModuleNotFoundError in my test_wiki.py script, which couldn't locate the Wikipedia_Data module. This error indicated an issue with Python paths in my GitHub Actions workflow. We then put the file into an accessible location by putting it on the main head of the directory. Later, Ian figured out there were dependency issues related to pip installs and we needed to put that in those into the yml file. Overall, it was a bit of a headache because I think that the way our code is structured is by accessing other files and the github workflow struggles with that somehow. I think it still has to do with the pathing, but I’m not sure how.

Ian Chapman Experience

I thought this was going to be a smooth process. However, the workflow actions kept failing. Our we had our test files in a separate folder and we could not figure out how to call them from there. Once we pulled them out of the files we recieved a different error. Which was progress. However, it took us a while to understand that we had to include the dependencies in the .yml file. After adding all the requisite dependencies it worked fine. Afterward, I tried to update the .py file with the search bar. However, afterward the test files would not run even though the change was made on a different code chunk than the test was designed for.
