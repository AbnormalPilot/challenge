#!/usr/bin/env python3
"""
Automated README Timestamp Updater
Updates the timestamp in README.md with the current date and time in IST.
"""
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path


def update_readme_timestamp():
    readme_path = Path(__file__).parent / "README.md"
    
    if not readme_path.exists():
        print(f"Error: {readme_path} not found")
        return False
    
    content = readme_path.read_text()
    
    # Indian Standard Time is UTC+5:30
    ist = timezone(timedelta(hours=5, minutes=30))
    current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")
    
    pattern = r'\*\*Last Updated:\*\* \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} IST'
    new_timestamp = f"**Last Updated:** {current_time}"
    
    updated_content = re.sub(pattern, new_timestamp, content)
    
    if updated_content == content:
        print("Warning: No timestamp pattern found to update")
        return False
    
    readme_path.write_text(updated_content)
    print(f"✓ README updated with timestamp: {current_time}")
    return True


if __name__ == "__main__":
    update_readme_timestamp()
