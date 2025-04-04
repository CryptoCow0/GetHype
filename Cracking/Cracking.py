import subprocess

# Example: Run hashcat with SHA256 mode (-m 1400) and a wordlist
command = [
    "hashcat", 
    "-m", "1400",             # Hash type (SHA256)
    "target_hash.txt",        # File containing the target hash
    "wordlist.txt"
]

result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
