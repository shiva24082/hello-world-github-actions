#!/usr/bin/env python3
from datetime import datetime
import os

def main():
    print("=" * 50)
    print("🚀 HELLO WORLD - GITHUB ACTIONS DEMO")
    print("=" * 50)
    
    # Get today's date
    today = datetime.now()
    today_formatted = today.strftime("%d-%m-%Y")
    
    # Display information
    print(f"📅 Today's Date: {today_formatted}")
    print(f"📅 Requested Date: 03-02-2026")
    
    # Environment check
    if 'GITHUB_ACTIONS' in os.environ:
        print("🌍 Environment: GitHub Actions")
        print(f"   Runner OS: {os.getenv('RUNNER_OS', 'Unknown')}")
        print(f"   Workflow: {os.getenv('GITHUB_WORKFLOW', 'Unknown')}")
    else:
        print("💻 Environment: Local Machine")
    
    # Date comparison
    if today_formatted == "03-02-2026":
        print("✅ PERFECT MATCH! Running on exactly 03-02-2026")
    else:
        print(f"📊 Status: Today is {today_formatted}, waiting for 03-02-2026")
    
    # Additional information
    print("\n📊 Additional Info:")
    print(f"   Time: {today.strftime('%H:%M:%S')}")
    print(f"   Year: {today.year}")
    print(f"   Month: {today.month}")
    print(f"   Day: {today.day}")
    
    print("\n" + "=" * 50)
    print("✨ Program completed successfully! ✨")
    print("=" * 50)

if __name__ == "__main__":
    main()
