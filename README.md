# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS 

*NAME* : VIVEK KUMBHAKAR

*INTERN ID* :CT04DF361

*DOMAIN* : CYBERSECURITY AND ETHICAL HACKING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

##Project Description
In today's digital landscape, maintaining the integrity of files is paramount, especially in environments where data breaches and unauthorized modifications are constant threats. This project, the File Integrity Checker, addresses a fundamental cybersecurity need: ensuring that critical files on a system remain unaltered from their trusted state. It acts as a digital watchdog, providing a robust mechanism to detect any unauthorized changes, corruptions, or tampering attempts.

The core problem this tool solves is the silent and often unnoticed alteration of files. Imagine a scenario where a crucial system configuration file, an application executable, or a sensitive document is subtly modified by malware or an insider threat. Without an integrity check, such changes could go undetected for extended periods, leading to system compromise, data exfiltration, or operational failures. This tool mitigates this risk by establishing a cryptographic baseline of files and continuously monitoring them against this trusted reference.

The importance of file integrity cannot be overstated. It is a cornerstone of a strong security posture, supporting principles like non-repudiation (proving data hasn't been altered), compliance with various regulatory standards (e.g., GDPR, HIPAA, PCI DSS), and incident response. Detecting file changes early allows administrators to quickly identify potential security incidents, isolate compromised systems, and initiate recovery procedures before extensive damage occurs. Furthermore, in forensics, proving file integrity is vital for evidence admissibility. This project serves as a foundational exercise in understanding and implementing such a critical security control. It's a simple yet powerful demonstration of cryptographic hashing in a real-world security application.

Features & Functionality
This Python-based File Integrity Checker offers two primary functionalities:

Baseline Initialization:

Scans a specified target directory recursively (including all subdirectories and their files).

For each file encountered, it calculates a cryptographic hash (SHA256 by default, but configurable).

Stores these file paths and their corresponding hash values in a baseline.json file. This baseline.json file serves as the trusted snapshot of the directory's state at a given point in time.

Includes metadata such as the scan timestamp, the scanned directory path, and the hashing algorithm used, providing context for future checks.

Integrity Check:

Loads the previously created baseline.json file.

Rescans the same target directory, recalculating hashes for all current files.

Compares the newly calculated hashes against the stored baseline hashes.

Identifies and reports:

Modified Files: Files whose hash values no longer match the baseline, indicating a change in content.

New Files: Files present in the current scan but not found in the baseline.

Deleted Files: Files found in the baseline but no longer present in the current scan.

Provides clear console output indicating whether any changes were detected or if the integrity matches the baseline perfectly.
Technologies Used
Python 3.x: The primary programming language for the entire script.

hashlib Library: A built-in Python module essential for generating secure hash values (specifically SHA256, but can be extended to other algorithms like MD5, SHA1, etc.). This library provides cryptographic hashing functions.

os Module: Used extensively for interacting with the operating system, including:

os.walk(): For recursively traversing directory structures.

os.path.join(): For safely constructing file paths across different operating systems.

os.path.abspath(): For converting relative paths to absolute paths, ensuring consistent referencing.

os.path.relpath(): For calculating file paths relative to the monitored directory, making the baseline portable and human-readable.

json Module: Used for reading from and writing to the baseline.json file, facilitating easy storage and retrieval of file paths and their hashes in a structured format.

datetime Module: For timestamping baseline creation, aiding in audit and tracking.

How to Run / Usage
Clone the Repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name/Task1_FileIntegrityChecker
Initialize Baseline:
To create the initial trusted baseline for a directory (e.g., my_monitored_dir):

Bash

python file_integrity_checker.py init my_monitored_dir baseline.json sha256
(Ensure my_monitored_dir exists and contains files you wish to monitor.)

Check Integrity:
To check for changes against the established baseline:

Bash

python file_integrity_checker.py check my_monitored_dir baseline.json sha256
Learning Outcomes & Concepts Demonstrated
This project provides practical experience with:

File System Interaction: Navigating and interacting with files and directories programmatically.

Cryptographic Hashing: Understanding the role of one-way hash functions in ensuring data integrity and detecting tampering.

Baseline Security: Implementing a fundamental concept in security monitoring where a known good state is used for comparison.

Change Detection: Developing logic to identify additions, modifications, and deletions in a monitored environment.

Modular Programming: Structuring code into functions for initialization and checking.

Command-Line Interface (CLI) Development: Accepting arguments to control script behavior.

JSON Data Handling: Storing and retrieving structured data.

This tool is a foundational step into system security and monitoring, crucial for any aspiring cybersecurity professional.
