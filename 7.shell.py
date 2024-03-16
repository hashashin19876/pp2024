import subprocess
import shlex

def execute_command(command):
    try:
        # Split the command into arguments
        args = shlex.split(command)
        
        # Execute the command and capture the output
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Print the output
        print(result.stdout)
        
        # Handle any errors
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"Error executing command: {e}")

def main():
    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() == "exit":
            break
        execute_command(user_input)

if __name__ == "__main__":
    main()
