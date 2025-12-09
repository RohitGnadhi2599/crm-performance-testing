CRM PERFORMANCE TESTING FRAMEWORK (JMETER + PYTHON AUTOMATION)

Overview:
This project provides a complete performance testing framework for CRM applications. It includes JMeter-based test plans for Login API and Lead Creation API, along with Python automation scripts that execute the tests, generate results, and analyze performance metrics.

Features:

JMeter test plans for load and stress testing

Automated execution using Python

CSV result analysis via pandas

Response time, throughput, and error rate calculation

Easily configurable user load, ramp-up, and test duration

Folder Structure:
crm-performance-testing/
jmeter-testplans/
login_test.jmx
lead_creation_test.jmx
python-automation/
run_jmeter.py
parse_results.py
results/
sample_report.csv
README.md

Technologies Used:

Apache JMeter

Python

Pandas

CSV reporting

Architecture:

Python script triggers JMeter test plan

JMeter runs load tests and generates CSV output

Python parser analyzes metrics from CSV

Final results printed to console or saved for reporting

Setup Instructions:

Install Apache JMeter from: https://jmeter.apache.org/download_jmeter.cgi

Install Python dependencies:
pip install pandas

Running Tests:
Execute all tests automatically:
python python-automation/run_jmeter.py

Analyze the results:
python python-automation/parse_results.py

Sample Output:
Avg Response Time: 120 ms
Max Response Time: 540 ms
Throughput: 185 requests/sec
Error Rate: 0.0%

Future Improvements:

Add Grafana dashboard integration

Add spike and endurance testing

Add parameterized test data

Integrate with Jenkins CI/CD pipeline
