
import pandas as pd
import matplotlib.pyplot as plt

# Sample demonstration dataset
cve = pd.DataFrame({
    "CVE_ID": [f"CVE-2026-{i:04d}" for i in range(201, 221)],
    "Severity": [
        "High", "Medium", "Critical", "High", "Low",
        "Medium", "High", "Critical", "Medium", "High",
        "Low", "Medium", "High", "Critical", "Medium",
        "High", "Low", "Medium", "High", "Critical"
    ],
    "CWE_ID": [
        "CWE-79", "CWE-89", "CWE-200", "CWE-79", "CWE-22",
        "CWE-787", "CWE-125", "CWE-89", "CWE-200", "CWE-22",
        "CWE-79", "CWE-89", "CWE-200", "CWE-787", "CWE-125",
        "CWE-79", "CWE-22", "CWE-89", "CWE-200", "CWE-787"
    ],
    "Vendor": [
        "AlphaSoft", "WebNova", "AlphaSoft", "NetSecure",
        "DataBridge", "CodeCraft", "WebNova", "NetSecure",
        "DataBridge", "CodeCraft", "AlphaSoft", "WebNova",
        "NetSecure", "DataBridge", "CodeCraft", "AlphaSoft",
        "WebNova", "NetSecure", "DataBridge", "CodeCraft"
    ]
})

cwe = pd.DataFrame({
    "CWE_ID": ["CWE-79", "CWE-89", "CWE-200",
               "CWE-22", "CWE-787", "CWE-125"],
    "CWE_Name": [
        "Cross-Site Scripting (XSS)",
        "SQL Injection",
        "Exposure of Sensitive Information",
        "Path Traversal",
        "Out-of-bounds Write",
        "Out-of-bounds Read"
    ]
})

# Merge CVE and CWE datasets
merged = pd.merge(cve, cwe, on="CWE_ID")

print("\n========== CVE DATASET ==========")
print(cve.to_string(index=False))

print("\n========== CWE DATASET ==========")
print(cwe.to_string(index=False))

# Severity distribution
severity = cve["Severity"].value_counts().reindex(
    ["High", "Medium", "Critical", "Low"], fill_value=0
)

print("\n========== SEVERITY DISTRIBUTION ==========")
print(severity.to_string())

plt.figure(figsize=(7, 6))
severity.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Distribution of Vulnerability Severity")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Top vulnerability categories
categories = merged["CWE_Name"].value_counts()

print("\n========== TOP VULNERABILITY CATEGORIES ==========")
print(categories.to_string())

plt.figure(figsize=(9, 5))
categories.sort_values().plot(kind="barh", color="green")
plt.title("Top Vulnerability Categories")
plt.xlabel("Number of Vulnerabilities")
plt.ylabel("CWE Category")
plt.tight_layout()
plt.show()

# Top vendors
vendors = cve["Vendor"].value_counts()

print("\n========== TOP VENDORS ==========")
print(vendors.to_string())

print("\nExperiment 1 completed successfully.")
