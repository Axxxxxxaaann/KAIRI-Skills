#!/usr/bin/env python3
"""
KAIRI-Skills CLI - Command Line Interface for Managing Cybersecurity Skills

Usage:
    kairi list                    - List all available skills
    kairi search <query>          - Search skills by keyword
    kairi show <skill-name>       - Show skill details
    kairi category <cat>         - Filter by category
    kairi install <skill-name>    - Install skill dependencies
    kairi verify <skill-name>     - Verify skill execution

Categories:
    analyzing     - Network, malware, log analysis skills
    auditing      - Security auditing skills
    building      - Tool building and automation skills
"""

import os
import sys
import json
import subprocess
from pathlib import Path

# Colors for terminal output
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_banner():
    banner = f"""
{BOLD}{GREEN}
    ╔═══════════════════════════════════════════╗
    ║                                           ║
    ║   KAIRI-Skills CLI v1.0.0                 ║
    ║   Cybersecurity Skills for AI Agents      ║
    ║                                           ║
    ╚═══════════════════════════════════════════╝
{RESET}
    """
    print(banner)

def list_skills():
    """List all available skills"""
    skills_dir = Path(__file__).parent / "skills"
    skills = sorted([d.name for d in skills_dir.iterdir() if d.is_dir()])

    print(f"\n{BOLD}Available Skills ({len(skills)}){RESET}\n")

    categories = {"analyzing": [], "auditing": [], "building": []}
    for skill in skills:
        if skill.startswith("analyzing"):
            categories["analyzing"].append(skill)
        elif skill.startswith("auditing"):
            categories["auditing"].append(skill)
        elif skill.startswith("building"):
            categories["building"].append(skill)

    for cat, items in categories.items():
        print(f"{BLUE}{BOLD}{cat.upper()}{RESET} ({len(items)} skills)")
        for item in items[:5]:
            print(f"  • {item}")
        if len(items) > 5:
            print(f"  ... and {len(items) - 5} more")
        print()

def search_skills(query):
    """Search skills by keyword"""
    skills_dir = Path(__file__).parent / "skills"
    results = []

    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir():
            skill_file = skill_dir / "SKILL.md"
            if skill_file.exists():
                with open(skill_file) as f:
                    content = f.read().lower()
                    if query.lower() in content:
                        results.append(skill_dir.name)

    print(f"\n{BOLD}Search Results for '{query}'{RESET}\n")
    for result in results:
        print(f"  • {result}")
    print(f"\nFound {len(results)} matching skills")

def show_skill(skill_name):
    """Show detailed skill information"""
    skills_dir = Path(__file__).parent / "skills"
    skill_dir = skills_dir / skill_name

    if not skill_dir.exists():
        print(f"{RED}Skill not found: {skill_name}{RESET}")
        return

    skill_file = skill_dir / "SKILL.md"
    if skill_file.exists():
        with open(skill_file) as f:
            print(f"\n{BOLD}{BLUE}{'=' * 60}{RESET}")
            print(f"{BOLD}{BLUE}Skill: {skill_name}{RESET}")
            print(f"{BOLD}{BLUE}{'=' * 60}{RESET}\n")
            print(f.read())
    else:
        print(f"{RED}SKILL.md not found for {skill_name}{RESET}")

def main():
    if len(sys.argv) < 2:
        print_banner()
        print(__doc__)
        sys.exit(0)

    command = sys.argv[1]

    if command == "list":
        list_skills()
    elif command == "search":
        if len(sys.argv) < 3:
            print(f"{RED}Please provide a search query{RESET}")
            sys.exit(1)
        search_skills(sys.argv[2])
    elif command == "show":
        if len(sys.argv) < 3:
            print(f"{RED}Please provide a skill name{RESET}")
            sys.exit(1)
        show_skill(sys.argv[2])
    else:
        print(f"{RED}Unknown command: {command}{RESET}")
        print(__doc__)
        sys.exit(1)

if __name__ == "__main__":
    main()
