# 1. Pre-Engagement

The entire pre-engagement process consists of three essential components: 

1. `Scoping Questionnaire`: Sending the client a questionnaire to better understand the service they are seeking. The penetration testing team may include their services and ask them to choose: 
    - Internal Vulnerability Assessment or External Vulnerability Assessment
    - Internal Penetration Test or External Penetration Test
    - Wireless Security Assessment
    - Application Security Assessment
    - Physical Security Assessment
    - Social Engineering Assessment
    - Red Team Assessment
    - Web Application Security Assessment


2. `Pre-engagement meeting`: This meeting serves as a discussion to understand all relevant and essential components with the customer before the penetration test. It helps making the <b>Scope of Work (SOW)</b>/ <b>Penetration Testing Proposal</b>. The most crucial element of this meeting is the detailed presentation of the penetration test to our client and its focus. As we already know, each piece of infrastructure is unique for the most part, and each client has particular preferences on which they place the most importance. Finding out these priorities is an essential part of this meeting.

3. `Kick-off meeting`: This meeting occurs after all the contractual documents are signed. It usually includes make stakeholders such as IT, Governance, technical support staff, account executives, etc. It is like a pre-engagement meeting, but it simply highlights the nature of the pentest. 

- It is also explained that if a critical vulnerability is found (typically only generated during external pentests), the pentest will stop and be reported to the company. This allows them to identify this risk and whether they would need an immediate patch. For example it could be remote code execution (RCE) or a SQL injection. 

- It is also important to inform that it many leave `many alerts` in their security systems, `lock some users` during the test, and may `negatively impact their networks`.  

However, as mentioned before, an <b>NDA</b> must be signed by all parties. It is important to understand `who in the company is permitted` to contract for a penetration test as not all parties can do it. 
- This can include: 
    - Chief Executive Officer (CEO)
    - Chief Technical Officer (CTO)
    - Chief Information Security Officer (CISO)
    - Chief Security Officer (CSO)
    - Chief Risk Officer (CRO)
    - Chief Information Officer (CIO)
    - VP of Internal Audit
    - Audit Manager
    - VP or Director of IT/Information Security
<hr>

# 2. Information Gathering

### OSINT 

<b>Open-Source Intelligence</b> refers to all publicly available information specific to the target. This can be social media, stack-overflow, different websites, etc... Often, repos on `Github` are not set up properly where sensitive information may be posted on public repos such as API or SSH keys. Previously mentioned, many developers may post code on `StackOverflow` which can contain vulnerabilities that attackers than use to exploit. 

### Infrastructure Enumeration

For this step, we are trying to identify the companies position on the internet and intranet by using OSINT and the first active scans. Services such as DNS are used to create a map of the client's servers and hosts. This let's us develop an understanding of how their infrastructure is structured. This can include: 
- name servers 
- mail servers 
- web servers 
- cloud instances 

An accurate list of hosts and their IP addresses is developed and then are compared to our scope to see if they are included in the list. We also try to determine the companies security measures as it will be easier to disguise our attacks (evasive testing). For instance, identifying a web application firewall can give us an understanding on what type of alerts are triggered in their environment. A `password spraying` attack may be used to try and authenticate to as many usernames using a single, commonly used password. This would allow a foothold into the network. 

### Service Enumeration 

A `service` is anything that is bound to a port that you can interact with over the internet or locally. It is important to understand the version of the service and what it provides. 

- <b>Remote access/management</b>
    - SSH (22), Telnet (23), RDP (3389), VNC (5900), WinRM (5985/5986)
    - `Banner grabbing =` connecting to a service and reading whatever text is displays about itself before any authentication. These services are important for this use.  
        - If you do `nc <target-ip> 22`, you may get `SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5`. The adversary may search CVE databases for any vulnerabilities, or determine any exploits with this version. However, there are instances where banners may be stripped or fake. 

- <b>File transfer/sharing</b>
    - FTP (21), SFTP (22), SMB (445/139), NFS (2049), TFTP (69)
    - SMB is `significant` and will be talked about later. 

- <b>Web services</b>
    - HTTP/HTTPS(80/443)
    - Includes the web server itself (Apache, nginx, IIS) and whatever is running on top of it. 

- <b>Mail services</b> 
    - SMTP (25), POP3 (110), IMAP (143) and their TLS variants

- <b>Directory/authentication services</b>
    - LDAP (389/636), Kerberos (88)
    - These are important when it comes to an internal/AD-focused test. 

- <b>Databases</b>
    - MySQL (3306), MSSQL (1433), PostgreSQL (5432), Oracle (1521), MongoDB (27017), Redis (6379)
    - Many of these allow direct unauthenticated connection if misconfigured.  

### Host Enumeration 

This is the step <i>before/alongside</i> service enumeration, but instead of asking "what's running on this port", you are asking "what is the `host` or `machine`?". We try to identify the OS running on the OS/host, services used and also the different versions tied to those services. 


