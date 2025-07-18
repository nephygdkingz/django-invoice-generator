import os
import subprocess

# Get all step branches
branches = subprocess.check_output(['git', 'branch', '-r']).decode().strip().split('\n')
step_branches = [b.strip().replace('origin/', '') for b in branches if 'step-' in b]

# Generate markdown table
table = "| Step | Branch Name | Description |\n|------|-------------|-------------|\n"
for i, branch in enumerate(step_branches):
    table += f"| Step {i+1} | `{branch}` | Description here |\n"

# Read current README
with open("README.md", "r") as f:
    content = f.read()

# Find where to insert the branch list
start = content.find("### 📚 Tutorial Branches")
end = content.find("## 📦 Tech Stack")

# Replace the section
new_content = content[:start] + "### 📚 Tutorial Branches\n\n" + table + "\n" + content[end:]

# Write back to README
with open("README.md", "w") as f:
    f.write(new_content)

print("✅ README updated with branch list")