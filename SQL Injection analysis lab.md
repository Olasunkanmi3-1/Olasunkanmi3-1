## 🗄️ SQL Injection Analysis: What I Learned from a Wireshark Lab
I analyzed a real SQL injection attack using a packet capture (PCAP) file in Wireshark.

This lab was not about launching an attack, it was about **understanding how attackers think and operate by observing real traffic**.

---

### 🔍 Lab Objective

The goal was to:

* Analyze captured network traffic
* Identify SQL injection attempts
* Understand how attackers extract sensitive data step by step

---

### 🛠️ Tools Used

* Wireshark (packet analysis)
* PCAP file (captured attack traffic)

---

### 🌐 Initial Observation

After loading the PCAP file into Wireshark, I identified the two main systems involved in the attack:

* **Attacker:** `10.0.2.4`
* **Target:** `10.0.2.15`

<img width="487" height="361" alt="beginning" src="https://github.com/user-attachments/assets/2864a326-e356-44fb-930c-cdda1f877269" />


The traffic showed a series of HTTP requests between both systems over a short period, indicating an active attack session.

---

### ⚠️ Step 1: Testing for Vulnerability

The attacker began with a simple input:

```sql
1=1
```

This condition is always true, and it was used to test if the web application was vulnerable to SQL injection.

👉 Instead of returning an error, the application returned valid data.

That confirmed the system was vulnerable.

<img width="492" height="363" alt="1" src="https://github.com/user-attachments/assets/01bdc27b-b897-427f-ba73-5d85f123cbbc" />


---

### ⚠️ Step 2: Extracting Database Information

After confirming the vulnerability, the attacker escalated the attack with:

```sql
1' or 1=1 union select database(), user()#
```
<img width="487" height="358" alt="database rq" src="https://github.com/user-attachments/assets/e9d53b8a-bffb-472f-a9f9-d3b7a7279ef8" />


This revealed:

* Database name
* Database user

At this point, the attacker had already gained **critical backend information**.

<img width="472" height="431" alt="2nd 1=1" src="https://github.com/user-attachments/assets/fba00e15-a706-419f-b46d-30ead33c6eb7" />


---

### ⚠️ Step 3: System Information Disclosure

Next, the attacker queried the database version:

```sql
1' or 1=1 union select null, version()#
```
<img width="487" height="358" alt="system version rq" src="https://github.com/user-attachments/assets/1f744d1f-9a30-4c5e-a67d-8ca17cedaf5c" />



This exposes the database version, which can help attackers identify known vulnerabilities.

<img width="472" height="431" alt="system info" src="https://github.com/user-attachments/assets/57e826d5-56b9-4ff8-a182-d3e63c0faef1" />


---

### ⚠️ Step 4: Enumerating Tables

The attacker then moved to discover available tables:

```sql
1' or 1=1 union select null, table_name from information_schema.tables#
```
<img width="472" height="431" alt="http stream l28" src="https://github.com/user-attachments/assets/9ce29236-bdf6-40b0-8ab4-8652cfa303e0" />

This returned a large list of tables within the database.

👉 This step is critical because it maps out where valuable data is stored.

<img width="472" height="431" alt="more on 28" src="https://github.com/user-attachments/assets/fb262650-e24c-4efb-a0cd-9f9172c2be03" />


---

### ⚠️ Step 5: Extracting Sensitive Data

Finally, the attacker executed:

```sql
1' or 1=1 union select user, password from users#
```
<img width="472" height="431" alt="stream on 28" src="https://github.com/user-attachments/assets/03eb91f8-6bb9-408e-af08-45fa5d0b836f" />


This returned:

* Usernames
* Password hashes

<img width="472" height="431" alt="moew" src="https://github.com/user-attachments/assets/67ed224a-3549-46a3-8ca4-6aa3d659e12d" />


---

### 🔓 Post-Exploitation Insight

The password hashes obtained can then be cracked using tools like **CrackStation** to reveal plaintext passwords.
<img width="906" height="373" alt="result of hash" src="https://github.com/user-attachments/assets/33003858-d1ec-4c93-b98c-865ed3e88440" />


👉 This is where a data breach becomes fully exploitable.

---

### 🧠 Key Takeaways

This lab helped me understand that:

* SQL injection can start from very simple inputs
* Poor input validation can expose entire databases
* Attackers follow a structured process:

  1. Test vulnerability
  2. Extract information
  3. Escalate access
* Sensitive data like passwords can be retrieved if systems are not properly secured

---

### 🔐 Prevention Insight

From what I learned, some ways to prevent SQL injection include:

* Input validation and sanitization
* Use of prepared statements (parameterized queries)
* Limiting database permissions
* Proper error handling

---

### 💡 Final Reflection

What stood out to me is how **simple the attack started**, but how quickly it escalated into full data exposure.

 It really shows that small vulnerabilities can lead to major breaches if not properly handled.


Understanding attacks at this level makes it easier to defend against them.




