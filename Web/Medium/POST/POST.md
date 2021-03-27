## POST

This website requires authentication, via POST. However, it seems as if someone has defaced our site. Maybe there is still some way to authenticate? http://165.227.106.113/post.php

### Approach

This challenge was interesting. We are first presented with this page:

![page](https://github.com/RyanNgCT/CTFLearn/blob/main/Web/Medium/POST/dependencies/post.png)

Seems like something to do with `POST` requests, which I studied in my Web Application Pentesting Module last semester (at the time of writing).

I first fired up Burp Suite Community, turned on `Intercept Traffic` and reloaded the page. The proxy registered a suspicious `GET` response, containing the username and password of the user.
I found [this article](https://www.educative.io/edpresso/how-to-perform-a-post-request-using-curl), which seemed to be helpful.

![burp_resp](https://github.com/RyanNgCT/CTFLearn/blob/main/Web/Medium/POST/dependencies/Burp_resp.png)

I then proceeded on to craft the payload. The examplar payload given was:
```
$ curl -d "user=user1&pass=abcd" -X POST https://example.com/login
```

Replacing the fields with the corresponding information for this challenge, we get:
```
$ curl -d "user=admin&pass=71urlkufpsdnlkadsf" -X POST http://165.227.106.113/post.php
<h1>This site takes POST data that you have not submitted!</h1><!-- username: admin | password: 71urlkufpsdnlkadsf --> 
```

However, this failed to work out as shown in the output, which was exactly the same as the one we started out with. I thought this had something to do with `Base64` encoding since I experienced something similar in another CTF where we had to encode `No` in the Authorization field of the header as `Tm8=`.
I crafted another payload:
```
$ curl -d "user=YWRtaW4=&pass=NzF1cmxrdWZwc2RubGthZHNm" -X POST http://165.227.106.113/post.php
<h1>This site takes POST data that you have not submitted!</h1><!-- username: admin | password: 71urlkufpsdnlkadsf -->  
```

Hmm... so its not an encoding issue? Trying something else, I replaced `user` with `username` and `pass` with `password`, since different websites may use different naming conventions (but I didn't change the encoding ofc, to experiment with one variable at a time.
```
$ curl -d "username=YWRtaW4=&password=NzF1cmxrdWZwc2RubGthZHNm" -X POST http://165.227.106.113/post.php
<h1>Seems like your credentials are wrong!</h1>
```

Wow... a different error message, we are getting super close! If we take a look carefully in the `GET` request in Burp, the Encoding field reads: `Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8`. Alamak!  🤦 I've done it again by not reading 😅😅
It accepts `text/html`, meaning **plaintext** can be accepted too!

![burp_req](https://github.com/RyanNgCT/CTFLearn/blob/main/Web/Medium/POST/dependencies/Burp_req.png)

So the final payload will be:
```
curl -d "username=admin&password=71urlkufpsdnlkadsf" -X POST http://165.227.106.113/post.php
<h1>flag{p0st_d4t4_4ll_d4y}</h1> 
```

And we get the flag `flag{p0st_d4t4_4ll_d4y}`.


