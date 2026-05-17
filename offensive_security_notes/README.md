# Introduction

<b>Penetration Test:</b> It is an `authorized audit` of a computer system's security and defenses as agreed by the owners of the system. 

Hackers are sorted into three hats: 

1. <b>White Hat</b> → These are considered "good people", where they use their skills to benefit people. Most of the time, they are known as "ethical hackers" or "pentesters". 

2. <b>Grey Hat</b> → These people try to help others; but in the process, they do so in an illegal or unethical manner, kind of like Robin Hood. 

3. <b>Black Hat</b> → These people are cyber criminals that often try to seek damage or gain some sort of financial benefit at the cost of others. 

### Rules of Engagement (ROE)

The ROE is a document that outlines how a penetration engagement should be conducted. It looks like this <a href="https://sansorg.egnyte.com/dl/bF4I3yCcnt/"> "SANS example</a>". This ROE often is sorted into three main sections: 

- <b>Permission:</b> This section gives explicit permission for the engagement to be carried out. This legally protects individuals and organizations by the activities carried out. 

- <b>Test Scope:</b> This section annotates specific targets to which the engagement should apply. For example, the penetration test may only apply to specific servers or applications. 

- <b>Rules:</b> Defines techniques permitted during the engagement. For instance, phishing attacks may be prohibited, but MITM attacks are allowed. 
<hr>
 
## Penetration Testing Methodologies

These methodologies are the steps a penetration tester takes during an engagement. 

### 1. Information Gathering 

This stage involves collecting as much publicly available data about a target or an organization. Another name for this is called `passive reconnaissance` which is the idea of performing this step by not interacting with the target at all. For instance, OSINT and research are examples. 

### 2. Enumeration/Scanning 

This stage involves discovering applications and services running on the systems. For instance, finding a web server that may be vulnerable. 

### 3. Exploitation 

Once a vulnerability is discovered, this the stage where you try to exploit by using publicly available exploits, or exploiting application logic directly. 

### 4. Privilege Escalation  

Once successfully exploited, (also known as a <b>Foothold</b>), this stage is the attempt to try to expand your access to a system. 

- Horizontal → This escalation means you access another account of the same person group

- Vertical → This escalation is where you access another account of another permission group (i.e. an administrator)

### 5. Post-exploitation 

There are a feb sub-stages in this step: 

1. What other hosts can be targeted (pivoting)
2. What additional information can we gather form the host now that we are a privileged user 
3. Covering your tracks 
4. Reporting 
<hr>

## Primary Scopes 

There are three primary scopes when testing an application. The level of testing significantly impacts the results of the engagement. The first 3 describe how much information the test gets before testing. 

- <b>1. Black-Box</b> → In this test, the tester is not given any knowledge, they are on their own. This means time spent on information gathering and enumeration heavily increases to understand the attack surface of the target. 

- <b>2. White-Box</b> →  This is a type test where the tester is given internal knowledge such as source code, architectural diagrams, design details, etc... Overall, a lot of knowledge about the system. 

- <b>3. Grey-Box</b> → This is the `most popular` type of test as it is a mix of Black and Grey testing processes. The tester will have <b>limited knowledge</b> of the internal components of the application or piece of software. This type of test saves time, and is often chosen for well-hardened attack surfaces. 

- <b> 4. Red Teaming → </b> describes the <b>style/objective</b>: act like an attacker to test the organization's detection, response, people, processes, and controls. It can be any of the above types.

- <b>5. Purple Teaming</b> → is more of a <b>collaboration model</b>: red teams work with blue team to improve detections, logging, response playbooks, and technical controls. 
<hr>

## Types of Testing Environments 

It is important to consider what is to be tested. This can be summarized in the following categories: 

| Category          | Examples |
|------------------|----------|
| Network          | Routers, switches, traffic |
| Web Applications | Frontend/backend web systems |
| Mobile           | iOS/Android apps |
| API              | REST/GraphQL endpoints |
| Thick Clients    | Desktop applications |
| IoT              | Embedded/smart devices |
| Cloud            | AWS, Azure, GCP infrastructure |
| Source Code      | Code-level review |
| Physical Security| Buildings, hardware access |
| Employees        | Social engineering |
| Hosts            | Endpoints, OS-level |
| Servers          | Backend systems |
| Security Policies| Configurations and rules |
| Firewalls        | Network filtering devices |
| IDS/IPS          | Detection and prevention systems |

<hr>

## Laws and Regulations 

When performing a penetration test, it is important to understand the specific laws per 