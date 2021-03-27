## Don't Bump Your Head(er)
Try to bypass my security measure on this site! http://165.227.106.113/header.php

### Approach
Here is the page when viewed in a web browser.


I first fired up Burp when I saw that this was regarding headers and reloded the page. 

![burp_int]()


The comment seemed suspicious but I had no success in submitting it as the flag, hence it wasn't that straightforward (being a medium challenge too), so I tried to forward the response to the Repeater Function. There I copied the comment into the `User-Agent` field to get:
`User-Agent: Sup3rS3cr3tAg3nt`

![incorrect]()

![burp_rep]()

Thereafter, the response says: 
```
Sorry, it seems as if you did not just come from the site, "awesomesauce.com".
<!-- Sup3rS3cr3tAg3nt  -->
```

Hmm... so what in the header has got to do with mentioning a site? I took a hint--the `Referer` field, which was not initially present. After we set `Referer: awesomesauce.com`and press `Go`, we get a response with out flag, which is: `flag{did_this_m3ss_with_y0ur_h34d}`.
![flag]()
