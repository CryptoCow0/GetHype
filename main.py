import subprocess
import concurrent.futures
from typing import List


# we will need to change this for loop 
scripts = [f"script{i}.py" for i in range(1, 21)]
input_str = "hello world"

def run_script(script_name: str) -> str:
    result = subprocess.run(
        ["python", script_name, input_str],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip()  # or result.stderr if you want errors


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results: List[str] = list(executor.map(run_script, scripts))
    
    for i, output in enumerate(results, 1):
        print(f"Output from script{i}.py: {output}")

if __name__ == "__main__":
    main()