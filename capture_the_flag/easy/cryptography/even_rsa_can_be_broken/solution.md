## EVEN RSA CAN BE BROKEN???

### Description 

This service provides you an encrypted flag. Can you decrypt it with just N & e? Connect to the program with `netcat: $ nc verbal-sleep.picoctf.net 59107`

### Inspection 

Starting off, <b>RSA</b> stands for Rivest, Shamir, and Adlemen. It is a type of asymmetric encryption algorithm; note that a public key is used for encryption and a private key for decryption. 

There are a couple of components used (able to see in python code): 

- Public key (e)
- private key (d)
- Two prime numbers (P & Q), multiplied (N)

<b>Key generation:</b> The user picks 2 large prime numbers (`p` and `q`) and multiplies to create a modulus `n`. 

<b>Public Key:</b> Modulus `n` and <i>public exponent</i> `e` are shared to anyone openly. Anyone can use this to encrypt a message. 

<b>Private Key:</b> A <i>secret exponent</i> `d` is calculated using `p` and `q`. This is the only key that can decrypt a message. 

<b>Encryption/Decryption</b>

- Encryption: Ciphertext = Message^<i>e</i>
- Decryption: Plaintext = Message^<i>d</i>

RSA is not necessarily used for encrypting large data such as files, videos, or databases. This is because it is computational heavy as it uses a lot of math. Other algorithms such as <b>AES</b>, are quicker to use instead. However, it is great a encrypting small secrets, verifying digital signatures and helping two way systems securely agree on a key. 
<hr>

When we connect using `netcat: $ nc verbal-sleep.picoctf.net 59107`: we are given: 

- `N`: 14607716388291096817787506431231107697338643316976680612781713561711205426114871904746310233751452580228449888722081366136051573747906422056733863478167814

- `e`: 65537

- `ciphertext`: 1451729751358801657366803899661400112431970602934174957270656037734411519023615044832893730363149203393726044441847772198830784455570811461800451003089811

We can make a python script based off the given values. 