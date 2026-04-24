# Contributing to KAIRI-Skills

Thank you for your interest in contributing to KAIRI-Skills!

## 🎯 How to Contribute

### Adding New Skills

1. **Fork the repository**
   ```bash
   git clone https://github.com/Axxxxxxaaann/KAIRI-Skills.git
   cd KAIRI-Skills
   ```

2. **Create a new branch for your skill**
   ```bash
   git checkout -b skills/add-[skill-name]
   ```

3. **Follow the skill structure**
   ```
   skills/
   └── your-skill-name/
       ├── SKILL.md          # Required: Main skill documentation
       ├── LICENSE           # Required: MIT License
       ├── references/
       │   └── api-reference.md
       └── scripts/
           └── agent.py
       ```

4. **Write comprehensive SKILL.md**
   ```markdown
   # Skill Name

   ## Overview
   [Brief description of the skill]

   ## When to Use
   [When should someone use this skill?]

   ## Prerequisites
   - [Required tool/software]
   - [Required knowledge]

   ## Workflow
   ### Step 1: [Name]
   [Description with code blocks]

   ### Step 2: [Name]
   [Description with code blocks]

   ## Verification
   [How to verify the skill was executed correctly]
   ```

5. **Submit a pull request**
   - Use clear commit messages
   - Include skill summary in PR description

### Skill Categories

- **Analyzing** (70 skills): Network analysis, log analysis, malware analysis
- **Auditing** (15 skills): Security audits, compliance checks
- **Building** (15 skills): Building security tools, detection rules

## 📋 Contribution Guidelines

### Quality Standards

- [ ] SKILL.md must include all sections (Overview, When to Use, Prerequisites, Workflow, Verification)
- [ ] Code examples must be tested and working
- [ ] Include at least 2 verification methods
- [ ] Use clear, descriptive naming

### File Naming

- Use kebab-case: `network-scanning-nmap`
- No spaces or special characters
- Descriptive names: `analyzing-network-traffic-with-wireshark` not `wireshark`

### Documentation

- Use Markdown formatting
- Include code blocks with syntax highlighting
- Add links to official documentation
- Provide real-world use cases

## 🐛 Reporting Issues

Found a bug or want a new skill? Please:

1. Check existing issues first
2. Create a detailed issue with:
   - Skill name
   - Description
   - Use case
   - Expected outcome

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Join our community and help build the future of cybersecurity automation!**

[![Discord](https://img.shields.io/badge/Discord-Join-blue?style=flat-square)](https://discord.gg/kairi)
[![Twitter](https://img.shields.io/badge/Twitter-Follow-blue?style=flat-square)](https://twitter.com/kairi)
