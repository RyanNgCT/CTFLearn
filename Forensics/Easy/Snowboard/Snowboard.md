## Snowboard

Find the flag in the jpeg file. Good Luck!

![img]()

### Approach
We are given the image above. No clue what to do with it. Open it in a hex editor? Why not? 
![hex_out]()


Is `CTFlearn{CTFIsEasy!!!}` the flag? Yeah right? Wrong! Hmm I got a hint that it had something to do with `Base64`... Flag was encoded in `Base64`? Why not that's a pretty smart move by the author!

Here is how to encode CTF as `Base64.
```
$ echo CTF | base64                                                             
Q1RGCg==             #I used the online version hence there was a difference in output
$ strings Snowboard.jpg | grep -i "Q1RG"                                       
Q1RGbGVhcm57U2tpQmFuZmZ9Cg==
```
Thereafter we just have to grep the output of the `strings` command to get the actual flag and decode it back.
```
$ echo Q1RGbGVhcm57U2tpQmFuZmZ9Cg== | base64 -d
CTFlearn{SkiBanff}
```
