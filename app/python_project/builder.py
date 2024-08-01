import os
import shutil
import subprocess
from python_project.project_model import ProjectModel

# This class creates the following directory structure
# root
#   .venv
#   app
#       main.py
#       __init__.py
#   .gitignore
#   README.md

class Builder:
    def __init__(self, project_output_path: str):
        self.__project_output_path = project_output_path
        self.__project_path = ''

    def build(self, project_model: ProjectModel) -> None:
        print("Builder.build()")
        try:
            # Define paths
            script_dir = os.path.dirname(os.path.abspath(__file__))
            python_exe_path = os.path.join(script_dir, '../..', '.venv', 'bin', 'python')
            root_template_directory = os.path.join(script_dir, '../..', 'code_templates')
            app_template_directory = os.path.join(root_template_directory, 'app')

            # Create project directory
            self.__project_path = self.__get_full_project_path(project_model.project_name)            
            project_app_directory = self.__prepare_project_directory()

            # Create virtual environment with path to venv python.exe            
            self.__make_virtual_env(project_model.venv_name, python_exe_path)

            # Copy root level code template files
            self.__populate_project_with_template_files(root_template_directory, self.__project_path)

            # Replace variables in root level code template files
            self.__replace_variables(self.__project_path, "$PROJECT_NAME$", project_model.project_name)

            # Copy root level code template files            
            self.__populate_project_with_template_files(app_template_directory, project_app_directory)
        except Exception as e:
            print(f'Exception: {e}')


    def __replace_variables(self, directory_path: str, placeholder: str, new_value: str) -> None:
        for f in os.listdir(directory_path):
            file_path = os.path.join(directory_path, f)
            if os.path.isfile(file_path):

                with open(file_path, 'r') as file:
                    content = file.read()

                updated_content = content.replace(placeholder, new_value)
                with open(file_path, 'w') as file:
                    file.write(updated_content)

                print(f'[--- Template file updated ---]: {file_path}')


    def __populate_project_with_template_files(self, source_directory, destination_directory_path: str) -> None:
        for f in os.listdir(source_directory):
            file_path = os.path.join(source_directory, f)
            if os.path.isfile(file_path):
                destination_file_path = os.path.join(destination_directory_path, f)
                shutil.copy(file_path, destination_file_path)


    def __prepare_project_directory(self) -> str:
        project_app_directory = os.path.join(self.__project_path, 'app')
        os.makedirs(project_app_directory, exist_ok=True)
        if os.path.isdir(project_app_directory):
            print(f'[--- Project app dir created ---]: {project_app_directory}')
            return project_app_directory
        raise Exception(f'Path not valid: {project_app_directory}')


    def __make_virtual_env(self, venv_name: str, python_exe_path: str) -> None:
        os.chdir(self.__project_path)
        result = subprocess.run([python_exe_path, '-m', 'venv', venv_name], check=True)
        if (result.returncode != 0):
            raise Exception('Venv creation failed')
        venv_path = os.path.join(self.__project_path, venv_name)
        if os.path.isdir(venv_path) == False:
            raise Exception(f'Venv directory failed to be created at: {venv_path}')
        print(f'[--- Venv created ---]: {venv_path}')


    def __get_full_project_path(self, project_name: str) -> str:        
        path = os.path.join(self.__project_output_path, project_name)
        os.makedirs(path, exist_ok=True)
        if os.path.isdir(path):
            print(f'[--- Project created ---]: {path}')
            return path
        raise Exception(f'Path not valid: {path}')