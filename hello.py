#!/usr/bin/env python3
from datetime import datetime
import os
import sys
import platform

def get_system_info():
    """Get system information"""
    info = {
        "python_version": sys.version,
        "platform": platform.platform(),
        "processor": platform.processor(),
        "github_actions": 'GITHUB_ACTIONS' in os.environ,
        "runner_os": os.getenv('RUNNER_OS', 'Unknown'),
        "workspace": os.getenv('GITHUB_WORKSPACE', 'Unknown')
    }
    return info

def main():
    print("=" * 60)
    print("🚀 HELLO WORLD - GITHUB ACTIONS DEMO")
    print("=" * 60)
    
    # Get today's date
    today = datetime.now()
    today_formatted = today.strftime("%d-%m-%Y")
    today_time = today.strftime("%H:%M:%S")
    
    # Get system info
    sys_info = get_system_info()
    
    # Display main information
    print(f"\n📅 DATE INFORMATION")
    print(f"   Today's Date: {today_formatted}")
    print(f"   Current Time: {today_time}")
    print(f"   Requested Date: 03-02-2026")
    
    # Date comparison
    if today_formatted == "03-02-2026":
        print("   ✅ PERFECT MATCH! Running on exactly 03-02-2026")
        exit_code = 0
    else:
        days_until = (datetime(2026, 2, 3) - today).days
        if days_until > 0:
            print(f"   ⏳ Status: {days_until} days until 03-02-2026")
        else:
            print(f"   📅 Status: {abs(days_until)} days since 03-02-2026")
        exit_code = 0
    
    # Environment information
    print(f"\n🌍 ENVIRONMENT")
    if sys_info['github_actions']:
        print("   ✅ Running in GitHub Actions")
        print(f"   Runner OS: {sys_info['runner_os']}")
        print(f"   Workspace: {sys_info['workspace']}")
    else:
        print("   💻 Running locally")
    
    # System information
    print(f"\n🔧 SYSTEM INFO")
    print(f"   Platform: {sys_info['platform']}")
    print(f"   Python: {sys.version.split()[0]}")
    print(f"   Processor: {sys_info['processor']}")
    
    # GitHub context (if available)
    print(f"\n📊 GITHUB CONTEXT")
    for key in ['GITHUB_WORKFLOW', 'GITHUB_RUN_ID', 'GITHUB_REPOSITORY']:
        if key in os.environ:
            print(f"   {key}: {os.environ[key]}")
    
    # Generate artifact content
    print(f"\n📁 ARTIFACTS TO BE GENERATED")
    print("   1. execution.log - Detailed execution log")
    print("   2. output.txt - Program output summary")
    
    print("\n" + "=" * 60)
    print("✨ Program completed successfully! ✨")
    print("=" * 60)
    
    return exit_code

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
