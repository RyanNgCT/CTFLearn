## QR Code

For this challenge, it involved a few steps but was rather straightforward.

Firstly, I scanned the QR Code with my phone. This outputted what looked like a string of `Base64` encoded string: `c3ludCB2ZiA6IGEwX29icWxfczBldHJnX2RlX3BicXI=`.

After decoding, the resultant string is `synt vf : a0_obql_s0etrg_de_pbqr`, but we have not gotten our flag. Looking at it, it seemed like some crypto was involved and eventully I was able to naarrow down it to `ROT-13`, through the hints in the comments.


We then have our flag after decoding it using the `ROT-13` algorithm (have to enclose it in the flag format): `CTFlearn{n0_body_f0rget_qr_code}`.
