from python_project.builder import Builder
from python_project.interrogator import get_project_model

def main():
    print('[==== Hello Mr Python developer ====]')
    model = get_project_model()
    if not model:
        print('[==== Good bey ;) ====]')

    builder = Builder('c:\\Users\\JacoBrink\\Desktop')
    print(f'project name: {model.project_name}')
    print(f'venv name: {model.venv_name}')
    builder.build(model)
    print('[==== All done, good bey ;) ====]')

if __name__ == "__main__":
    main()