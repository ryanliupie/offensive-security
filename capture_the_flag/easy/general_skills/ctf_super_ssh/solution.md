### Super SSH 

### Description 

Using a Secure Shell (SSH) is going to be pretty important. Can you ssh as ctf-player to titan.picoctf.net at port 59200 to get the flag? You'll also need the password 6abf4a82. If asked, accept the fingerprint with yes.

### Inspection

``` bash
ssh ctf-player@titan.picoctf.net -p 59200
```

- Once the connection is established, I get the flag `picoCTF{s3cur3_c0nn3ct10n_65a7a106}`
