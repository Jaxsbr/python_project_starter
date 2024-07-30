from python_project.project_model import ProjectModel

def get_project_model() -> ProjectModel:
    project_name = ''
    venv_name = ''

    while True:
        project_name = input('Enter the project name: ').strip()
        if project_name:
            break

        retry = input('Project name cannot be empty. Do you want to retry? (Y/N): ').strip()
        if retry == 'n':
            print('Input process cancelled.')
            return None

    while True:
        venv_name = input ('Enter the virtual environment name: ').strip()
        if venv_name:
            break

        retry = input('Virtual environment name cannot be empty. Do you want to retry? (Y/N): ').strip()
        if retry == 'n':
            print('Input process cancelled')
            return None

    return ProjectModel(project_name, venv_name)
