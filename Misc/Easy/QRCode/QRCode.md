## QR Code

Do you remember something known as QR Code? Simple. Here for you: [Link](https://mega.nz/#!eGYlFa5Z!8mbiqg3kosk93qJCP-DBxIilHH2rf7iIVY-kpwyrx-0)

### Approach

For this challenge, it involved a few steps but was rather straightforward.

Firstly, I scanned the QR Code with my phone. This outputted what looked like a string of `Base64` encoded string: `c3ludCB2ZiA6IGEwX29icWxfczBldHJnX2RlX3BicXI=`.


![QR](https://github.com/RyanNgCT/CTFLearn/tree/main/Misc/Easy/QRCode/images/qrcode.39907201.png)


After decoding, the resultant string is `synt vf : a0_obql_s0etrg_de_pbqr`, but we have not gotten our flag. Looking at it, it seemed like some crypto was involved and eventully I was able to naarrow down it to `ROT-13`, through the hints in the comments.
<br>
![B64](https://github.com/RyanNgCT/CTFLearn/tree/main/Misc/Easy/QRCode/images/Base64%20Decode.png)


We then have our flag after decoding it using the `ROT-13` algorithm (have to enclose it in the flag format).
<br>
![ROT](https://github.com/RyanNgCT/CTFLearn/tree/main/Misc/Easy/QRCode/images/ROT13.png)



The flag is `CTFlearn{n0_body_f0rget_qr_code}`.
