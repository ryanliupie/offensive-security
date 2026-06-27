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

### Primary Scopes 

There are three primary scopes when testing an application. The level of testing significantly impacts the results of the engagement. The first 3 describe how much information the test gets before testing. 

- <b>1. Black-Box</b> → In this test, the tester is not given any knowledge, they are on their own. This means time spent on information gathering and enumeration heavily increases to understand the attack surface of the target. 

- <b>2. White-Box</b> →  This is a type test where the tester is given internal knowledge such as source code, architectural diagrams, design details, etc... Overall, a lot of knowledge about the system. 

- <b>3. Grey-Box</b> → This is the `most popular` type of test as it is a mix of Black and Grey testing processes. The tester will have <b>limited knowledge</b> of the internal components of the application or piece of software. This type of test saves time, and is often chosen for well-hardened attack surfaces. 

- <b> 4. Red Teaming → </b> describes the <b>style/objective</b>: act like an attacker to test the organization's detection, response, people, processes, and controls. It can be any of the above types.

- <b>5. Purple Teaming</b> → is more of a <b>collaboration model</b>: red teams work with blue team to improve detections, logging, response playbooks, and technical controls. 
<hr>

### Evasiveness

- <b>Non-evasive:</b> The pentest team is not trying to avoid detection at all, speed and coverage is what matters. The goal is simply to "find any vulnerabilities" and not "test the blue". This is common for compliance-driven tests or internal pentests. 

- <b>Hybrid-evasive:</b> The team gradually escalates loudness in stages; finds exploitable issues but increasingly also test whether the SOC notices. It is mainly to map out a <b>detection threshold curve</b> (at what level of stealth does SOC team notice and respond?). 

- <b>Fully evasive:</b> The explicit goal is to test detection and response capabilities, measuring whether the SOC catches you, so noise is the enemy throughout. 
<hr>

### Precautionary Measures during a Penetration Test  

As we know, we always need to understand the specific violations in laws around a penetration test. It is important to protect people from `unauthorized access` and `exploitation of their data`, and `ensure their privacy`. 

- Obtain written consent from the authorized representative of the computer or network being tested on. 
- Conduct testing within the scope and respect any limitations specified. 
- Make sure not to cause any damages to networks, systems, or endpoints. 
- Do not access, use, or disclose any personal information during the test without permission. 
- Do not intercept communications without approval 
- Do not conduct penetration tests on systems, endpoints, or networks that are covered by HIPAA (specific to the US, different in other countries such as Canada)
<hr>

### Deterministic & Stochastic processes

`Deterministic` means each step is caused by the previous finding 

- You scan a host → find port 80 open → enumerate the web app → find login page → test inputs → discover SQL injection.

`Stochastic` means the next step is only probable, not guaranteed. 

- You send phishing emails → maybe someone clicks, maybe nobody does. You can only estimate the probability.
<hr>

### Penetration Testing Stages 

<b>Pre-Engagement:</b> This phase is all about educating the client on the penetration test including the scope and restricted activities. This can include: 

- Non-disclosure Agreement
- Goals 
- Scope 
- Time Estimation 
- Rules of Engagement 

 <b>Information Gathering:</b> This stage involves collecting as much available data about the target. `Passive reconnaissance` is the idea of performing this step by not interacting with the target at all. For instance, OSINT and research are examples. `Direct reconnaissance` is the interaction with the target such as port scanning. There is much more of a risk as there is a higher chance of detection.  

<b>Vulnerability Assessment:</b> We analyze the results from the `Information Gathering` stage, looking for known vulnerabilities in systems, applications, and various versions of each to discover possible attack vector; this can be done manually and through automation. 

<b>Exploitation:</b> Once a vulnerability is discovered, this the stage where you try to exploit by using publicly available exploits, or exploiting application logic directly to initially gain access to the system(s).  

<b>Privilege Escalation/Post-Exploitation:</b> Once a `foothold` is established on a system, the pentester attempts to expand access, gain additional permissions, gather credentials, maintain persistence, or further control the environment. 

- `Horizontal privilege escalation` → You access another account or resource at the same privilege level.

- `Vertical privilege escalation` → You gain higher privileges than you originally had (root, admin, or system).

<b>Lateral Movement:</b> This is the internal movement of the target company to try and access other hosts on the same or higher privilege level. Lateral movement is about moving across systems. Privilege escalation is about increasing or changing access level. They 

<b>Proof-of-Concept:</b> This is where the pentester must write clear and concise documentation on the following test. This includes proving the vulnerability is real, the attack path is realistic, and the possible impact. It is not "we found X vulnerability", it is more geared towards "Here is how vulnerability X was found through multiple vulnerable chains to compromise the environment". 

<b>Post-Engagement:</b> Detailed documentation is prepared for the client to see the severity of vulnerabilities found. At this stage, traces of actions are cleaned up on hosts and servers. Additionally, testing data is archived per contractual obligations, and sometimes, data is retained in case a post-remediation assessment is performed to retest the client's fixes. 
<hr>

### Types of NDAs 

| Type | Description |
|------|-------------|
| `Unilateral NDA` | `One party` obligates to maintain confidentiality and allows other party to share information to third parties. I would have the pentest team sign the unilateral NDA as they have seen sensitive systems and vulnerabilities. |
| `Bilateral NDA` | `Both parties` are obligated to keep resulting information confidential. A company would share their sensitive systems, credentials, architecture, while the pentest team would share their tooling/processes, techniques and methodologies. | 
| `Multilateral NDA` | This NDA involves `more than 2 parties`. For example, if a company suffers a ransomware incident, they may bring a forensics teams, external law firm, and a cloud provider support team. All parties must sign the NDA. 
| 


### Total Documents for a Penetration Test 

| # | Document | Meaning |
|---|---|---|
| 1 | `NDA` | Confidentiality agreement. Not leaking sensitive information. `After` initial contact.|
| 2 | `Scoping Questionnaire` | Initial form used to understand what the client wants tested. `Before` the pre-engagement meeting. |
| 3 | `Scoping Document` | Clean summary of what is in scope, based on the questionnaire and discussions. `During` the pre-engagement meeting. |
| 4 | `Penetration Testing Proposal / Contract / SoW` | The formal agreement: what work will be done, timeline, cost, responsibilities, and scope. `During` the pre-engagement meeting. |
| 5 | `Rules of Engagement` | The “testing rules”: what is allowed, what is not allowed, testing windows, contacts, escalation process, and limits. `Before` the kick-off meeting |
| 6 | `Contractors Agreement` | Extra permission for physical assessments, like badge testing, office entry testing, or social engineering. `Before` the kick-off meeting |
| 7 | `Reports` | The deliverables that explain findings, evidence, proof-of-concept, risk, and remediation. `During` and `after` the conducted penetration test.
|