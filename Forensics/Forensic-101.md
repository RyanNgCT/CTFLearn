## Forensic-101
Think the flag is somewhere in there. Would you help me find it? [Link](https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c)

### Approach
The file given was an image of a minion with some text. I used exiftool and file to determine the type of file I was dealing with (in case the file header was incorrect etc.). 
Note that I renamed the file to `Forensics101.jpg` for easy identification of the challenge in future.
```
$ exiftool Forensics101.jpg 
ExifTool Version Number         : 12.16
File Name                       : Forensics101.jpg
Directory                       : .
File Size                       : 9.5 KiB
File Modification Date/Time     : 2021:03:26 23:41:08-04:00
File Access Date/Time           : 2021:03:26 23:41:46-04:00
File Inode Change Date/Time     : 2021:03:26 23:41:46-04:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Image Width                     : 236
Image Height                    : 218
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 236x218
Megapixels                      : 0.051
```

Here is the input of the `file` command.
```
$ file Forensics101.jpg 
Forensics101.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 236x218, components 3
```

Alright. So no hidden files contained within the image.

I then tried to use `strings` with `grep`, as used previously in my [volatility writeup](https://github.com/RyanNgCT/wonderland-ctf). Since the expected flag would usually be in the format of `CTFlearn{}`, I tried to match the first few characters.

```
$ strings Forensics101.jpg| egrep -i "CTFlearn"
```

However, there was no output for this. Then I thought that since it was an easy challenge, the command to be used should be rather straight forward so I used `strings` by itself.
```
$ strings Forensics101.jpg                                                                         
JFIF
 , #&')*)
-0-(0%()(
((((((((((((((((((((((((((((((((((((((((((((((((((
L?~f
:UwR
y>2|
*'?-
yhH_&
Lmz'
 +f[
!"1$246B`35A

...

n%CeoQ=m8
`"n<P
 i}\D
X`(
8kF=
~9%]Tn
flag{wow!_data_is_cool}
$lqU
AG{u
Xm*CnC
@'hnQ
ax+p
bdQG
D_ O
```

And sure enough, towards the end of the output, the flag was found but with a different format! 🤦 The flag is `flag{wow!_data_is_cool}`.
