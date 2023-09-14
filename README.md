# XSS_Random
The Python code provided is a script for testing web URLs for Cross-Site Scripting (XSS) vulnerabilities. XSS is a security issue that can allow malicious attackers to inject and execute scripts within web applications, potentially compromising user data and system security. The script reads target URLs and payloads from user-defined files and employs multithreading to concurrently test the URLs with various payloads and encoding techniques.

How to use :

""root@xxx:~/XSS_Random# python xss_random4.py
Enter the path to the target URL file: target.txt
Enter the path to the payload file: xss-all-list.txt
Enter the number of processes to use: 10
""
