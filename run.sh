#!/bin/bash

# Prompt the user for the project name
read -p "Enter the project name: " project_name

# Define the base directory where the new project folder will be created
base_dir=~/CodeLab

# Expand the tilde to ensure the full path is resolved
base_dir=$(eval echo "$base_dir")

# Combine the base directory with the project name to form the project path
project_path="${base_dir}/${project_name}"

# Create the new directory for the project
if mkdir -p "$project_path"; then
    echo "Project directory created at: $project_path"
else
    echo "Failed to create project directory. Please check permissions."
    exit 1
fi

# Prompt the user for the project type
read -p "Enter the project type: 1 = simple | 2 = pygame | 3 = ui-pyqt5: " project_type

# Determine the subdirectory based on the project type
case $project_type in
    1)
        project_type_str="simple"
        ;;
    2)
        project_type_str="pygame"
        ;;
    3)
        project_type_str="ui-pyqt5"
        ;;
    *)
        echo "Invalid project type selected!"
        exit 1
        ;;
esac

# Prompt the user for the source directory to copy files from
source_dir="${base_dir}/python_project_starter/code_templates/${project_type_str}"

# Verify the source directory exists
if [ ! -d "$source_dir" ]; then
    echo "Source directory does not exist. Exiting." $source_dir
    exit 1
fi

# Copy all files and folders recursively from source to the new project directory
if cp -r "$source_dir/" "$project_path/"; then
    echo "Files and folders copied successfully to $project_path"
else
    echo "Failed to copy files. Please check permissions and paths."
    exit 1
fi

# Navigate to the newly created project directory
cd "$project_path" || { echo "Failed to navigate to $project_path"; exit 1; }

# Replace placeholder in README.md with the project name (macOS compatible)
if [ -f "$project_path/README.md" ]; then
    sed -i '' "s/# %PROJECT_NAME%/# $project_name/" "$project_path/README.md"
    echo "Updated README.md with project name: $project_name"
else
    echo "README.md not found in the copied files."
fi

# Instantiate a Git repository and create an empty root commit
if git init && git commit -m 'root commit' --allow-empty; then
    echo "Initialized a new Git repository and created a root commit."
else
    echo "Failed to initialize Git repository."
    exit 1
fi

# Create a Python virtual environment in the project directory
if python -m venv .venv; then
    echo "Virtual environment created at $project_path/.venv"
else
    echo "Failed to create virtual environment."
    exit 1
fi

# Launch the new project in VSCode
if command -v code >/dev/null 2>&1; then
    code .
    echo "VSCode launched for project: $project_path"
else
    echo "VSCode is not installed or not in PATH. Please install VSCode or adjust your PATH."
    exit 1
fi

echo "Script completed successfully."
