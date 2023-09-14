# XSS_Random
### Features
The Python code provided is a script for testing web URLs for Cross-Site Scripting (XSS) vulnerabilities. XSS is a security issue that can allow malicious attackers to inject and execute scripts within web applications, potentially compromising user data and system security. The script reads target URLs and payloads from user-defined files and employs multithreading to concurrently test the URLs with various payloads and encoding techniques.
<pre>
1) Random String
2) Base64
3) URL Encoded 
</pre>

<pre>
  Note: This is detected only reflected in response , Please test in browser 
</pre>
How to use :

<pre>
root@xxx:~/XSS_Random# python xss_random.py
Enter the path to the target URL file: target.txt
Enter the path to the payload file: xss-all-list.txt
Enter the number of processes to use: 10
</pre>


![](https://raw.githubusercontent.com/0x240x23elu/XSS_Random/main/xss_random.JPG)



<pre>📝 Note: I are not responsible for any misuse or unintended consequences resulting from the use of this code. Users are encouraged to exercise caution, conduct due diligence, and adhere to legal and ethical standards when utilizing this project.

Let's build a positive and responsible coding community together! If you have any questions or concerns, please don't hesitate to reach out. Happy coding! 🌟"</pre>
