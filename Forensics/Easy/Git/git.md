## Git Is Good

The flag used to be there. But then I redacted it. Good Luck. https://mega.nz/#!3CwDFZpJ!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc

### Approach

After unzipping the `zip` file, I found that the resultant folder was empty (or was it 👀)... 

![incorrect_flag](https://github.com/RyanNgCT/CTFLearn/blob/main/Forensics/Easy/Git/wrongflag.png)

Some knowledge in git made me suspect they were hidden directories and files (i.e. using the `.` prefix-meaning that it is hidden unless we do a `ls -la` in the command line). Using [this article](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History), we can gain some inspiration of how to extract the contents of the commit. 


```                                                                             
$ git log -p -2                                              
commit d10f77c4e766705ab36c7f31dc47b0c5056666bb (HEAD -> master)
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:33:18 2016 -0400

    Edited files

diff --git a/flag.txt b/flag.txt
index 8684e68..c5250d0 100644
--- a/flag.txt
+++ b/flag.txt
@@ -1 +1 @@
-flag{protect_your_git}
+flag{REDACTED}

commit 195dd65b9f5130d5f8a435c5995159d4d760741b
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:32:44 2016 -0400

    Edited files

diff --git a/flag.txt b/flag.txt
index c5250d0..8684e68 100644
--- a/flag.txt
+++ b/flag.txt
@@ -1 +1 @@
-flag{REDACTED}
+flag{protect_your_git}
```

This the flag is `flag{protect_your_git}`.
