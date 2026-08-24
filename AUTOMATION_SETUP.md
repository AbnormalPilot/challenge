# Automated Timestamp Update Setup

## Overview
This repository includes automation to update the "Last Updated" timestamp in README.md every hour.

## Components

### 1. Python Script: `update_timestamp.py`
- Updates the timestamp in README.md to the current date/time in IST (Indian Standard Time)
- Can be run manually or via automation
- Already committed to the repository ✅

### 2. GitHub Actions Workflow: `.github/workflows/update-timestamp.yml`
- Runs automatically every hour (at minute 0 of each hour)
- Can also be triggered manually from the GitHub Actions tab
- Uses the Python script to update the timestamp
- Automatically commits and pushes changes if the timestamp changed

## Setup Instructions

### The workflow file needs to be committed manually due to permission restrictions.

**Option 1: Via GitHub Web Interface (Easiest)**
1. Go to your repository on GitHub
2. Navigate to `.github/workflows/` (create the directories if they don't exist)
3. Click "Add file" → "Create new file"
4. Name it `update-timestamp.yml`
5. Copy the content from the local `.github/workflows/update-timestamp.yml` file
6. Commit the file

**Option 2: Via Git with Proper Permissions**
1. Ensure your GitHub token has `workflow` scope/permission
2. Commit and push the workflow file:
   ```bash
   git add .github/workflows/update-timestamp.yml
   git commit -m "Add hourly timestamp update workflow"
   git push
   ```

**Option 3: Manual Trigger Only**
If you prefer not to run hourly automatically:
1. Follow Option 1, but after creating the file
2. Go to "Settings" → "Actions" → "General"
3. Disable scheduled workflows (keep manual workflow_dispatch enabled)
4. Manually trigger updates from the Actions tab whenever needed

## How It Works

### Automated (Once Workflow is Committed)
- GitHub Actions runs the workflow every hour
- The workflow:
  1. Checks out the repository
  2. Runs `python3 update_timestamp.py`
  3. Checks if README.md changed
  4. If changed, commits and pushes the update
  5. If no change, skips the commit

### Manual Execution
You can always manually update the timestamp:

```bash
python3 update_timestamp.py
git add README.md
git commit -m "Update timestamp"
git push
```

Or trigger the workflow manually:
1. Go to your repository on GitHub
2. Click "Actions" tab
3. Select "Update Timestamp in README"
4. Click "Run workflow"
5. Choose branch (usually `main`)
6. Click "Run workflow" button

## Current Status

✅ **Python script (`update_timestamp.py`)** - Committed and working  
✅ **Workflow file created locally** - Located at `.github/workflows/update-timestamp.yml`  
⚠️ **Workflow file NOT YET committed** - Needs manual commit (see Setup Instructions above)

## Testing

Test the Python script locally:
```bash
python3 update_timestamp.py
```

Expected output:
```
✓ README updated with timestamp: 2026-08-24 XX:XX:XX IST
```

## Timezone

The timestamp uses **IST (Indian Standard Time)** which is UTC+5:30.

To change to a different timezone, edit `update_timestamp.py`:
```python
# For UTC
current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

# For EST
est = timezone(timedelta(hours=-5))
current_time = datetime.now(est).strftime("%Y-%m-%d %H:%M:%S EST")
```

## Frequency

The workflow runs every hour by default. To change the frequency, edit the cron schedule in `update-timestamp.yml`:

```yaml
schedule:
  - cron: '0 * * * *'  # Every hour at minute 0
  # - cron: '0 */2 * * *'  # Every 2 hours
  # - cron: '0 0 * * *'  # Daily at midnight
  # - cron: '*/30 * * * *'  # Every 30 minutes
```

## Troubleshooting

**Workflow not running:**
- Check if the workflow file is committed to the repository
- Go to "Settings" → "Actions" → "General" and ensure Actions are enabled
- Check the "Actions" tab for any error messages

**Timestamp not updating:**
- Manually run `python3 update_timestamp.py` to test
- Check if the pattern in README.md matches what the script expects
- Look at workflow logs in the Actions tab

**Permission errors:**
- Ensure the repository has Actions enabled
- Check that GITHUB_TOKEN has write permissions (Settings → Actions → General → Workflow permissions)
