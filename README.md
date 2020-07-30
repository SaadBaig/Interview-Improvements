# Interview Improvements
 
 I decided to make this repo to showcase my weaknesses I was exposed to during technical interviews for various job roles. I want to use this as a showcase of what once were weaknesses that have become strengths. I try to push these updates out within 24 hours of an interview as to keep the information in my head as fresh as possible.

## Junior Systems Engineer 7/29/20

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


## Cyber Security Analyst II 5/27/20

**Linux ```at```:** I was asked about what program/utility in Linux is able to do a single task. I gave the answer of a ```cron``` job. ```cron``` jobs are scheduled tasks that run at a specified time repeatedly. However a more appropriate answer was the  ```at``` utility. The key difference between ```cron``` and ```at``` is that an ```at``` job is used to schedule a task to only run once at 1 time. If I need this task to run more than one time, thats where ```cron``` comes into play. 

**Linux ```mv``` command:** I was asked what unix utility is used to rename a file. Me as a GUI scrub said that I was unaware of how to change a filename outside of the GUI. Enter ```mv```, a command used not only to move a file to a new directory, but also is the main utility to rename a file.  I knew ```mv``` was used to move a file, however I did not know that it also is used to rename a file. 

**Kerberos:** I was asked about how Kerberos works. The answer I gave was a ticket based authentification system that is supported by every major OS. I didn't understand the inner workings, how authentication actually worked, or anything beyond what I said. Lets change that:

Kerberos refers to the 3 headed dog in Greek Mythology. This is an key detail as Kerberos uses (atleast) 3 parties to implement its 2 main purposes; security and authentication. It starts off with a request from a user, say Zeus, wanting to access a resource from a file server. Before we let Zeus have access to this file server, we need to verify Zeus's identity and make sure he is authorized to access this resource. A trusted 3rd party called a **Key Distribution Center** or ```KDC``` is used to do this verification. The ```KDC``` is compromised of 2 servers, the **Authentication Server**, ```AS``` and a **Ticket Granting Server**, ```TGS```. Zeus needs to request a "ticket" to access the file server. This request will be send to the AS partially encrypted with his user password as the encryption key. The **AS** will attempt to verify the users credentials by decrypting the request using Zeus's password as the shared secret key. Once this process suceedes, a ticket called a ```TGT``` or Ticket Granting Ticket will be generated by the **TGS** which is encrypted with a shared secret key that is only known to the **KDC**. This TGT is sent back to Zeus. Zeus's system will send this encrypted TGT ticket along with the request to access the file server to the **TGS** and attempt to decrypt it using the shared secret key generated by the KDC. A token will be generated that is encrypted with a key now only known to the TGS and the file server that Zeus is trying to access. Finally Zeus system will use this token to access the file server which can only be decrypted via the shared private key only known between the TGS and the file server. Zeus now has been fully verified and is able to access the file server for a specified amount of time according to the ticket. The system is analogous to somebody buying a movie ticket. The ticket is only good for 1 movie at a certain time on a certain day. The ticket is invalid in any other scenario. 

**Linux Package Managers:** I was asked about package managers for Linux. I gave an example of 3 package managers, ```apt``` or Advanced Package Tool, ```yum```, Yellowdog Updater, and for OS X ```homebrew```. However there are plenty more such as ```rpm``` or Red Hat Package Manager, ```DPKG``` for Debian based distro's. There's plenty more but these are the most popular ones. 

**Windows Process Monitor**. I was asked what programs/utilies I could use on a Windows OS to investigate a potential piece of malware. I responded saying I would first start with a Windows Defender scan to locate the malicious file. After I aquired a file path to the malware, I would start digging around and see if I can find more clues on when this file structure was created, what user created it and when it happened. I would try to coorelate the time of file creation with information in Windows Restore to see what major installs and activities happened around that date and time to further pin point how this malware could've gotten onto the system. One of the utilies I failed to mention was Process Monitor. Process Monitor allows you to see real time information about said process. Information such as registry and threat/process actitivity is shown. The interviewer also mentioned that you can see potential command line arguments that the malware could be using to launch itself. So much more like traversing the thread stack, process tree used to visualize processes referenced from a trace, registry key generation, and even boot time logging. I'll be using Process Manager instead of Task Manager to get myself more aquanted with the utility. 

**DNS Amplification:** I was asked what issues could arrise from having port 53 open for inbound DNS requests. I did not know the answer. DNS Amplification is a form of denial of service (DDoS). We start off with an open DNS server that is open to taking in a DNS name lookup request, but with the source IP spoofed to be the target IP instead. The DNS server is now sending this request to the target IP rather than the source IP. A byproduct of this action is a response that is much larger than the requested data sent. For example, my malicious DNS query might only send out 300 bytes, but the response sent to the target IP may be 6000 bytes. Multiply this traffic by thousands or millions and now we have a hugely amplified flood of data being sent to a victim IP rather than the source IP potentially knocking the client offline, a DDoS. 

**Pass the Hash:** I ended up describing a form of pass the hash, the Golden Ticket pass the hash which steals the Golten Ticket hash from a Kerberos enabled Active Directory server. The general concept of a pass the hash is stealing a hash that is used for authentication, masquerading as a legitimate user to gain access to directory objects. 

**Unix Process ID 1:** I was asked about Process ID 1 on Linux. I had 0 (ha) clue. Process 1 consists of the processes used to start up and shut down the Linux OS. Aptly named as ```PID 1``` it is the first process, ```init``` loaded by the Linux kernel. ```PID 1``` remains from system boot till shutdown. For the curious as to what ```PID 0```, it is the scheduler for Linux. Can't create processes, and memory management/paging if you don't have a scheduler to allocate CPU time to each process. A great resource I ended up falling back on is located here: https://github.com/0xAX/linux-insides/blob/master/SUMMARY.md

**Steps before a DNS query is requested:** I was asked what happens before a DNS query is sent. I did not know the answer. I do now though. Firstly the OS's host file located at ```C:\Windows\System32\drivers\etc\hosts``` on Windows or ```etc/hosts``` on Unix will be checked to try to see if an hostname can be resolved to an IP address. This file is also the DNS's cache in Windows. If this lookup fails, then the browsers cache will be the 2nd and final attempt at resolving a hostname without having to do a costly DNS lookup. The reason the OS does these 2 preliminary checks is to prevent the DNS server from constantly having to do a fresh query for an IP. Generally speaking, websites don't usually change much, and so doing the same lookup is resource intensive. I've ran into this error myself where I try to look at my updated github.io, however the browser cache has an old version of the website. On OS X I have to ``` Shift + F5``` to force a refresh cache so I can see my latest changes.