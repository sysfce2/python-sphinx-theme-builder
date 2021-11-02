"""Compilation entrypoint."""

from typing import List

import click

from ..nodejs import generate_assets
from ..project import Project


class CompileCommand:
    """Compile the current project's assets."""

    interface: List[click.Parameter] = []

    def run(self) -> int:
        """Make it happen."""
        project = Project.from_cwd()
        project.validate_file_structure_and_contents()
        generate_assets(project)

        return 0