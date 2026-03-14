## Riddle Registry 

### Description 

Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered. Find the PDF file here "Hidden Confidential Document" and uncover the flag within the metadata.

### Inspection 

- We have inspected the PDF, nothing is there, sometimes the flag is right on it. 

We can use the following commands to take note of the pdf in bash:

    ```bash

    file confidential.pdf # checks file version 
    ls -lh confidential.pdf # shows permissions, file size, owner, and modification time 
    sha256sum confidential.pdf # Computes the SHA-256 cryptographic hash of the file
    ```

- PDFs carry metadata such as the author, checksum, keywords, and an XMP metadata block that can hold arbitrary bits. 

- In a real world environment, download this file in a VM. We can use something called a <b>Meta Data Inspector Tool</b> which can be found online such as <a href="https://www.metadata2go.com/"> metadata2go</a>. This can show us all hidden metadata for audio, video, document, ebook & image files. 

When we upload the `confidential.pdf` into this tool, we get the following: 

- <b>Author:</b> `cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOTk5ZTJhNH0=`. The Author is a metadata field that says who created the file. The gibberish is a string that is <b>Base64 encoded</b>. This type of format is used to represent data is ASCII text form, often for storage or transmission through text-based systems. Some systems can handle this format more easily than raw bytes or special characters. NOTE! it does not protect the data, just encoded it to look like something else: Some characteristics are: 

    - It uses <b>A–Z, a–z, 0–9, +, /</b>
    - Often ends with `=` or `==`
    - Looks like random letters but still readable in ASCII  

- When we decode, we get `picoCTF{puzzl3d_m3tadata_f0und!_c999e2a4}`
<hr>

### Tips for forensics CTFS 

- <b>Always record hashes:</b> Do this before you touch the file as it is a good habit and for reproducabiltiy. 