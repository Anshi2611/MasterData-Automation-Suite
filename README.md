🚀 Master Data Automation Suite

An enterprise workflow automation solution built using **Python, Selenium, Pandas, and Excel-driven processing** to automate the complete lifecycle of master data management — from record creation to approval.

The suite consists of two automation bots:

- 📝 **Maker Bot** – Creates Generic Parameter records from Excel input.
- ✅ **Approval Bot** – Searches, validates, and approves pending records automatically.

This project transforms a repetitive manual workflow into a scalable and efficient automation process.

---

🎯 Problem Statement

Managing master data manually required users to:

- Read requests from Excel sheets
- Extract Group Codes and related information
- Open the application
- Navigate through multiple screens
- Create records individually
- Submit each record for approval
- Search records one by one
- Validate approval conditions
- Approve records manually

For large datasets, the process became repetitive, time-consuming, and prone to human error.

---

📊 Before vs After Automation

Before Automation (Manual Process)

For every request:

1. Open Common Masters Application
2. Navigate to Seed Data
3. Search individual records manually
4. Verify Group Code, Group Name, and Description
5. Create records one by one
6. Submit records for approval
7. Search pending records manually
8. Validate approval conditions
9. Approve each record individually

Challenges

❌ Repetitive manual work

❌ High operational effort

❌ Time-consuming navigation

❌ Slow approval turnaround

❌ Increased chances of human error

❌ Difficult to process bulk records

---

After Automation

The automation suite:

✅ Reads requests directly from Excel

✅ Extracts required information automatically

✅ Creates records in bulk

✅ Submits records for approval

✅ Searches records automatically

✅ Validates approval conditions

✅ Approves matching records automatically

✅ Processes hundreds of records with minimal intervention

---

Business Impact

| Metric | Manual | Automated |
|----------|----------|----------|
| Record Creation | Manual | Automated |
| Data Entry | Manual | Automated |
| Record Search | Manual | Automated |
| Approval Validation | Manual | Automated |
| Bulk Processing | Limited | Supported |
| Human Effort | High | Low |
| Error Probability | Moderate | Minimal |
| Processing Speed | Slow | Fast |

Estimated Outcome

- ⏱️ Reduced manual effort by **90%+**
- ⚡ Faster record creation and approval
- 🎯 Improved operational accuracy
- 📈 Increased productivity
- 🔄 End-to-end workflow automation

---

🏗️ Solution Architecture

```text
                Excel Input
                     │
                     ▼
        ┌─────────────────────────┐
        │      Maker Bot          │
        │ Create Master Records   │
        └─────────────┬───────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │   Common Masters App    │
        └─────────────┬───────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │     Approval Bot        │
        │ Search & Approve Data   │
        └─────────────────────────┘
```

---

📝 Maker Bot

Functionality

The Maker Bot:

- Reads requests from Excel
- Extracts:
  - Group Code
  - Group Name
  - Description
- Opens Generic Parameter Creation Screen
- Populates all required fields
- Selects Generic Parameter Type
- Submits records for approval
- Handles page refresh and navigation automatically

Workflow

```text
Excel File
    │
    ▼
Extract Data
    │
    ▼
Navigate to Create Screen
    │
    ▼
Populate Form Fields
    │
    ▼
Submit For Approval
```

---

 ✅ Approval Bot

Functionality

The Approval Bot:

- Reads Group Codes from Excel
- Searches records automatically
- Filters matching records
- Validates:
  - Generic Parameter
  - Created By
  - Status
- Identifies pending records
- Clicks Approve automatically

Workflow

```text
Excel File
    │
    ▼
Extract Group Code
    │
    ▼
Search Record
    │
    ▼
Validate Conditions
    │
    ▼
Approve Record
```

---

⚙️ Tech Stack

| Technology | Usage |
|------------|--------|
| Python | Core Development |
| Selenium | Browser Automation |
| Pandas | Data Processing |
| NumPy | Data Manipulation |
| OpenPyXL | Excel Integration |
| ChromeDriver | Browser Control |

---

📂 Project Structure

```text
MasterData-Automation-Suite/
│
├── maker_bot.py
├── approval_bot.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── sample_data/
│   └── sample_input.xlsx
│
└── screenshots/
```

---

📦 Installation

Clone the repository:

```bash
git clone https://github.com/Anshi2611/MasterData-Automation-Suite.git
```

Move into the project directory:

```bash
cd MasterData-Automation-Suite
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

▶️ Usage

Run Maker Bot:

```bash
python maker_bot.py
```

Run Approval Bot:

```bash
python approval_bot.py
```

---

📋 Requirements

Create a `requirements.txt` file:


selenium
pandas
numpy
openpyxl
```

Install:

```bash
pip install -r requirements.txt
```

---

🔒 Security Notes

Before pushing code publicly:

- Remove hardcoded credentials
- Remove internal URLs if required
- Exclude confidential Excel files
- Exclude screenshots and logs
- Use environment variables for secrets

Example:

```python
import os

USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")
```

---

 🚀 Future Enhancements

- CAPTCHA Handling Integration
- Automated Report Generation
- Email Notifications
- Audit Logging
- Dashboard Monitoring
- Scheduler Support
- Retry Mechanism for Failed Records

---

👩‍💻 Author
 Anshika Gupta

B.Tech Computer Science (Data Science)

Interests:

- Process Automation
- Data Analytics
- AI/ML
- Business Process Optimization
- Enterprise Workflow Automation



⭐ If you found this project useful, consider giving it a star!
