import subprocess

# subprocess.run(["ls", "-l", "README.md"])

# command="uname"
# command_argument="-a"
# print(f"Gathering system information with command: {command} {command_argument}")
# subprocess.run([command, command_argument])

command="ps"
command_argument="-x"
print(f"Gathering system information with command: {command} {command_argument}")
subprocess.run([command, command_argument])