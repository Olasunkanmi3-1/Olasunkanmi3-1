### **🛠️ Building a Splunk SOC from Scratch**

A hands-on journey from installation to a fully functional Security Operations Center (SOC) with automated alerting and dashboards, built on Splunk's free license.

---

#### **🔧 Phase 1: Installation & Data Ingestion**

*   **Goal:** Install Splunk and ingest sample log data.
*   **Process:** Downloaded Splunk Enterprise, used the free license (500MB/day), and uploaded sample `security_logs.log` and `web_server_logs.log` files.
*   **Key Challenge:** Initial searches returned "No results" due to the default time picker.
*   **Solution:** Adjusted the time range to **"All time"** to include historical logs.

---

#### **🔍 Phase 2: Mastering SPL (Search Processing Language)**

The core of Splunk is transforming raw logs into intelligence using the pipe (`|`) operator.

**Example Query: Analyzing Web Traffic**
```spl
source="web_server_logs.log"
| rex "\s(?<status>\d{3})\s" 
| stats count by status
```

**Example Query: Hunting Failed Logins**
```spl
source="security_logs.log" failed
| rex "user: (?<user>\w+)"
| rex "IP: (?<ip>[\d.]+)"
| table _time, user, ip
```

---

#### **📊 Phase 3: Building the Operational Dashboard**

Created a **"Web Traffic Monitor"** dashboard to visualize key metrics at a glance, including:
-   A pie chart of HTTP status codes.
-   A pie chart of top active users.

[![Splunk Dashboard View](https://github.com/Major241/cyber-portfolio/blob/main/images/splunk_dashboard.png.png?raw=true)](https://github.com/Major241/cyber-portfolio/blob/main/images/splunk_dashboard.png.png?raw=true)
*The operational dashboard providing real-time insights.*

---

#### **⚠️ Phase 4: Implementing Proactive Alerting**

**Goal:** Get automated alerts for a rise in server errors (HTTP 500).

**Configured Alert:**
-   **Search:** `source="web_server_logs.log" status=500 | stats count`
-   **Trigger:** Results > 1
-   **Schedule:** Run every hour
-   **Action:** Send email to analyst

[![Splunk Alert Configuration](https://github.com/Major241/cyber-portfolio/blob/main/images/splunk_alert.png.png?raw=true)](https://github.com/Major241/cyber-portfolio/blob/main/images/splunk_alert.png.png?raw=true)
*Configuring an alert to proactively notify of issues.*

---

#### **✅ Core SOC Workflow Demonstrated**

This setup replicates a fundamental analyst workflow:
1.  **Daily Review:** Check the **Web Traffic Monitor** dashboard for health and anomalies.
2.  **Alert Triage:** Investigate email alerts for critical events like server errors.
3.  **Threat Hunting:** Proactively search logs for patterns like multiple failed logins.
4.  **Tool Maintenance:** Continuously refine queries, alerts, and dashboards.

---

#### **🛠️ Tools Used**
-   Splunk Enterprise (Free License)
-   Custom Sample Logs
-   Windows

**Source:** [Splunk Enterprise Download](https://www.splunk.com/en_us/download/splunk-enterprise.html)

---
