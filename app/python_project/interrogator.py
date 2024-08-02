from python_project.project_model import ProjectModel
from prompt_collector.collector import Collector

def get_project_model() -> ProjectModel:
    collector = Collector('[======================]', '[---------------------]')
    project_name = collector.collect_value('project name')
    venv_name = collector.collect_value('virtual environment name')
    return ProjectModel(project_name, venv_name)
