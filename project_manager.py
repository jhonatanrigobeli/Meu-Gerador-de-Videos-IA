"""
Project Manager Module - Handles project creation, listing, and deletion
Implements Fase 4: Project Management
"""

import json
import shutil
from pathlib import Path
from datetime import datetime
from config import PROJECTS_DIR


class ProjectManager:
    """Manages video projects"""

    def __init__(self):
        self.projects_dir = PROJECTS_DIR
        self.projects_dir.mkdir(parents=True, exist_ok=True)
        self.projects_file = self.projects_dir / ".projects.json"

    def _normalize_name(self, title):
        """Convert title to valid directory name"""
        return title.replace(" ", "_").replace("/", "_").lower()

    def _load_projects(self):
        """Load projects metadata from JSON"""
        if self.projects_file.exists():
            with open(self.projects_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _save_projects(self, projects):
        """Save projects metadata to JSON"""
        with open(self.projects_file, 'w', encoding='utf-8') as f:
            json.dump(projects, f, indent=2, ensure_ascii=False)

    def create_project(self, title, description="", language="pt-BR"):
        """
        Create a new project
        
        Args:
            title: Project title
            description: Project description
            language: Project language (pt-BR, en-US, etc)
            
        Returns:
            Project metadata dictionary
        """
        project_name = self._normalize_name(title)
        project_path = self.projects_dir / project_name
        
        # Check if project already exists
        if project_path.exists():
            raise ValueError(f"Projeto '{title}' já existe!")
        
        # Create project directory structure
        project_path.mkdir(parents=True, exist_ok=True)
        (project_path / "scenes").mkdir(exist_ok=True)
        (project_path / "images").mkdir(exist_ok=True)
        (project_path / "videos").mkdir(exist_ok=True)
        (project_path / "audio").mkdir(exist_ok=True)
        (project_path / "prompts").mkdir(exist_ok=True)
        
        # Create project metadata
        project_data = {
            "title": title,
            "name": project_name,
            "path": str(project_path),
            "description": description,
            "language": language,
            "created_at": datetime.now().isoformat(),
            "status": "criado",
            "script": None,
            "scenes": [],
            "images": [],
            "videos": [],
        }
        
        # Save project metadata
        project_meta_file = project_path / "meta.json"
        with open(project_meta_file, 'w', encoding='utf-8') as f:
            json.dump(project_data, f, indent=2, ensure_ascii=False)
        
        # Update global projects list
        projects = self._load_projects()
        projects[project_name] = project_data
        self._save_projects(projects)
        
        return project_data

    def list_projects(self):
        """
        List all projects
        
        Returns:
            List of project metadata dictionaries
        """
        projects = self._load_projects()
        return list(projects.values())

    def get_project(self, project_name):
        """
        Get specific project metadata
        
        Args:
            project_name: Normalized project name
            
        Returns:
            Project metadata dictionary
        """
        projects = self._load_projects()
        if project_name in projects:
            return projects[project_name]
        raise ValueError(f"Projeto '{project_name}' não encontrado!")

    def update_project(self, project_name, updates):
        """
        Update project metadata
        
        Args:
            project_name: Normalized project name
            updates: Dictionary with fields to update
        """
        projects = self._load_projects()
        if project_name not in projects:
            raise ValueError(f"Projeto '{project_name}' não encontrado!")
        
        projects[project_name].update(updates)
        self._save_projects(projects)
        
        # Also update the project's meta.json
        project_path = Path(projects[project_name]['path'])
        project_meta_file = project_path / "meta.json"
        with open(project_meta_file, 'w', encoding='utf-8') as f:
            json.dump(projects[project_name], f, indent=2, ensure_ascii=False)

    def delete_project(self, project_name):
        """
        Delete a project
        
        Args:
            project_name: Normalized project name
        """
        projects = self._load_projects()
        if project_name not in projects:
            raise ValueError(f"Projeto '{project_name}' não encontrado!")
        
        # Delete project directory
        project_path = Path(projects[project_name]['path'])
        if project_path.exists():
            shutil.rmtree(project_path)
        
        # Update projects list
        del projects[project_name]
        self._save_projects(projects)
