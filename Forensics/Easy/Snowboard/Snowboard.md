## Snowboard

Find the flag in the jpeg file. Good Luck!

![img](https://github.com/RyanNgCT/CTFLearn/blob/main/Forensics/Easy/Snowboard/images/Snowboard.jpg)

### Approach
We are given the image above. No clue what to do with it. Open it in a hex editor? Why not? 

![hex_out](https://github.com/RyanNgCT/CTFLearn/blob/main/Forensics/Easy/Snowboard/images/hex.png)

Is `CTFlearn{CTFIsEasy!!!}` the flag? Yeah right? Wrong! Hmm I got a hint that it had something to do with `Base64`... Flag was encoded in `Base64`? Why not that's a pretty smart move by the author!

Here is how to encode CTF as `Base64`.
```
$ echo CTF | base64                                                             
Q1RGCg==             # I used the online version hence there was a difference in output
$ strings Snowboard.jpg | grep -i "Q1RG"                                       
Q1RGbGVhcm57U2tpQmFuZmZ9Cg==
```
Thereafter we just have to grep the output of the `strings` command to get the actual flag and decode it back.
```
$ echo Q1RGbGVhcm57U2tpQmFuZmZ9Cg== | base64 -d
CTFlearn{SkiBanff}
```

Hmm but I wanted to take my learning further and find out why the linux versus the online decoder was different. Hence, I chanced upon [this article](https://stackoverflow.com/questions/8817159/what-are-the-differences-between-php-base64-encode-and-nix-base64).

> echo usually outputs a new line character at the end of the string, to suppress that use the -n switch

Wow ok TIL. And when I tried it out, sure enough, `-n` removed the suffix of `Cg==`.

```
$ echo -n 'CTF' | base64                                                      
Q1RG

```

### Resources
* https://www.base64decode.org/ https://www.base64encode.org/
* https://hexed.it/
