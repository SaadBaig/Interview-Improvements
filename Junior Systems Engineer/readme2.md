# Junior Systems Engineer 7/29/20

Back to basics. This interview was for a Junior Systems Engineer position, and I don't think I did that well. Lets change that:

I was asked to create a program that would output how many times the word test appears on every line in a file. I created my own "test.txt" file:

This is a test of the emergency test system
Testing to see if my program can detect multiple tests in a single line
Please test my program to see if it can read the test.txt file and outputs the number of tests per line. 
Test test test test test
Best, rest, messed, blessed, testy test test

I created a script in Python which is also attached in this repo, that does this functionality. Here's the program and the output:

```python
with open('test.txt', 'r') as searchfile:
        for line in searchfile:
                count = line.count.lower()("test")
                print(count)
```
Output: 

```bash
2
2
3
5
3
```

I was asked how to find the operating system information for a Linux machine. I didn't know outside of prodding using nmaps -sV flag because pentesting. But now I do:
```➜  ~ uname -a
Darwin Saads-MacBook-Pro.local 19.5.0 Darwin Kernel Version 19.5.0: Tue May 26 20:41:44 PDT 2020; root:xnu-6153.121.2~2/RELEASE_X86_64 x86_64```

I was asked how to find out which program is using the most amount of CPU usage. I had 0 clue. I knew it used the command ```ps aux```, but I couldn't figure out the rest.The command was ```ps aux | sort -nrk 3,3 | head -n 5```:

```bash
➜  ~ ps aux | sort -nrk 3,3 | head -n 5
root               251  11.5  0.6  6517468 213864   ??  S    10Jul20  76:53.65 nessusd -q
_windowserver      208   6.7  0.3 10393320 105120   ??  Ss   10Jul20 276:18.30 /System/Library/PrivateFrameworks/SkyLight.framework/Resources/WindowServer -daemon
titanium         97711   5.0  0.3  6665760  98044   ??  S    Sun09AM   5:44.40 /System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal
titanium         37987   4.9  1.5  7138640 489992   ??  S     8:10AM   4:28.64 /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
_hidd              159   2.1  0.0  5610004   9468   ??  Ss   10Jul20  54:24.81 /usr/libexec/hidd
```

I was asked where a majority of Linux config files are located. I incorrectly said ```/bin```. It was ```/etc```. 

I was given a scenario where a server wasn't resolving to the correct IP address. Assuming we didn't have access to the localhosts file, how could we force an ARP cache reset. I didn't know. Until now. In the DNS stack, there exists, TTL or Time to Live. TTL can be thought of as an expiration date that is put on a DNS record and tells the resolver how long it should keep said record in its cache. For example, we can set example.com's TTL for 3600 seconds or 1 hour. This means that the resolver will no query to the server until the TTL runs out. 