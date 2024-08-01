from python_project.builder import Builder
from python_project.interrogator import get_project_model
import subprocess

def main():
    print('[==== Hello Mr Python developer ====]')

    # TODO: read form a config file
    output_path = '/mnt/c/code-lab/python_lab'
    print(f'[--- Default Project Output Path ---]: {output_path}')
    path_input = input('Y = Set project output path. N/Empty = Use default): ').strip()
    if path_input == 'y':        
        output_path = input('Enter the project output path: ').strip()
        if not output_path:
            print('[==== Good bey ;) ====]')
            return

    model = get_project_model()
    if not model:
        print('[==== Good bey ;) ====]')
        return

    builder = Builder(output_path)
    print(f'project name: {model.project_name}')
    print(f'venv name: {model.venv_name}')
    builder.build(model)

    print('[==== All done, good bey ;) ====]')

if __name__ == "__main__":
    main()