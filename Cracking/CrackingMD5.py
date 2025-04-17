import subprocess

batch_script = r"C:\Users\Migue\Desktop\Spring 2025\Cryptography\GetHype\GetHype\Cracking\windowsisstupid.bat"

# Run the batch script
result = subprocess.run(
    batch_script,
    capture_output=True,
    text=True,
    shell=True
)

# Print output
print("STDOUT:")
print(result.stdout)
print("STDERR:")
print(result.stderr)
