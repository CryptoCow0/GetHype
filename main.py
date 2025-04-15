import subprocess
import concurrent.futures
from typing import List


# we will need to change this for loop 
scripts = [f"./Hashing/script{i}.py" for i in range(1, 21)]
input_str = input("Welcome to this educational tool intended on teaching you the security level of your password, please input the password you would like to try: ")

def run_script(script_name: str) -> str:
    result = subprocess.run(
        ["python", script_name, input_str],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip()
  # or result.stderr if you want errors

# should run all 20 programs in parrallel on the same given input string
def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # result:  executor.map(run_script,'./Hashing/MD5.py')
        results: List[str] = list(executor.map(run_script, scripts))
    
    for i, output in enumerate(results, 1):
        print(f"Output from script {i}.py: {output}")

if __name__ == "__main__":
    main()