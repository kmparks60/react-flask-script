import os
import subprocess

def create_file(file_path, content=""):
	with open(file_path, "w") as file:
		file.write(content)

script_directory = os.path.dirname(os.path.realpath(__file__))

project_folder_name = input("What would you like to name your project directory? ")
react_project_name = input("What would you like to name your React project? ")

react_project_path = os.path.join(script_directory, project_folder_name)
os.makedirs(react_project_path, exist_ok=True)

os.chdir(react_project_path)

create_react_app_command = f"npx create-react-app {react_project_name}"
subprocess.run(create_react_app_command, shell=True)

flask_files = ["config.py", "models.py", "app.py", "seed.py"]

for flask_file in flask_files:
	flask_file_path = os.path.join(react_project_path, flask_file)
	create_file(flask_file_path)