import subprocess
import os

JMETER = "/usr/local/apache-jmeter/bin/jmeter"

def run_test(testfile, outfile):
    cmd = [
        JMETER,
        "-n",            # non-GUI mode
        "-t", testfile,  # test plan
        "-l", outfile    # results
    ]
    print(f"Running test: {testfile}")
    subprocess.run(cmd)
    print(f"Results saved to: {outfile}")

if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)

    run_test("jmeter-testplans/login_test.jmx", "results/login_results.csv")
    run_test("jmeter-testplans/lead_creation_test.jmx", "results/lead_results.csv")
