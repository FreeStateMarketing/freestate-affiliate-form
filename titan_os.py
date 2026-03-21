#!/usr/bin/env python3
"""
titan_os.py - FreeState Marketing Titan OS
A modular backend system for Google Sheets integration and AI-powered page analysis.
"""

import os
import sys
import time
from datetime import datetime
from typing import Dict, Any

# Optional dependency for .env file support
try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

# Configuration constants
CENTISECONDS_PER_SECOND = 100
AI_TASK_DELAY_SECONDS = 1  # Simulated delay before AI task execution


class CommandRegistry:
    """Registry for managing system commands."""
    
    def __init__(self):
        self.commands = {}
        self._register_default_commands()
    
    def _register_default_commands(self):
        """Register default system commands."""
        self.commands['FETCH_SHEET_DATA'] = self._fetch_sheet_data
        self.commands['AI_TASK'] = self._ai_task
    
    def _fetch_sheet_data(self) -> Dict[str, Any]:
        """Fetch data from Google Sheets."""
        # Placeholder for Google Sheets integration
        return {'status': 'SUCCESS', 'message': 'Sheet data fetched successfully'}
    
    def _ai_task(self, prompt: str) -> Dict[str, Any]:
        """Execute AI task with proper API key validation."""
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key or api_key.strip() == '':
            return {
                'status': 'ERROR',
                'message': 'API KEY INVALID',
                'error': 'OpenAI API key not found or empty. Please set OPENAI_API_KEY environment variable.'
            }
        
        # Validate API key format (basic validation)
        if not api_key.startswith('sk-'):
            return {
                'status': 'ERROR',
                'message': 'API KEY INVALID',
                'error': 'Invalid API key format. OpenAI API keys should start with "sk-"'
            }
        
        # Placeholder for actual AI API call
        # In production, this would call OpenAI API
        return {
            'status': 'SUCCESS',
            'message': 'AI response generated',
            'response': f'Analysis for: {prompt}'
        }
    
    def execute(self, command: str, **kwargs) -> Dict[str, Any]:
        """Execute a registered command."""
        if command not in self.commands:
            return {'status': 'ERROR', 'message': f'Unknown command: {command}'}
        
        return self.commands[command](**kwargs)


class TitanOS:
    """Main Titan OS class for managing system operations."""
    
    def __init__(self):
        self.registry = None
        self.authenticated = False
        self.start_time = datetime.now()
    
    def _format_timestamp(self, elapsed: float) -> str:
        """Format elapsed time as [MM:SS:CC] timestamp."""
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        centiseconds = int((elapsed % 1) * CENTISECONDS_PER_SECOND)
        return f"[{minutes:02d}:{seconds:02d}:{centiseconds:02d}]"
    
    def log(self, message: str):
        """Log a message with timestamp."""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        timestamp = self._format_timestamp(elapsed)
        print(f"{timestamp} {message}")
    
    def bootstrap(self):
        """Bootstrap the Titan OS system."""
        self.log("LOADED: titan_os.py")
        self.registry = CommandRegistry()
        self.log("SYSTEM: Bootstrapped Command Registry.")
    
    def scan_environment(self):
        """Scan and sync environmental data."""
        self.log("Scanning Environment...")
        # Simulate environment scanning
        time.sleep(2)
        self.log("Environmental Data Synced.")
    
    def fetch_sheet_data(self):
        """Fetch data from Google Sheets."""
        self.log("TX >> FETCH_SHEET_DATA")
        result = self.registry.execute('FETCH_SHEET_DATA')
        if result['status'] == 'SUCCESS':
            self.log("RX << SUCCESS")
            self.log("Inventory Updated.")
        else:
            self.log(f"RX << ERROR: {result.get('message', 'Unknown error')}")
        return result
    
    def authenticate_user(self):
        """Authenticate user."""
        # Placeholder for actual authentication
        self.authenticated = True
        self.log("USER AUTHENTICATED.")
    
    def ai_task(self, strategy: str):
        """Execute an AI task with the given strategy."""
        self.log(f"AI TASK (strategy): {strategy}")
        result = self.registry.execute('AI_TASK', prompt=strategy)
        
        if result['status'] == 'ERROR':
            self.log(f"AI RESPONSE: ERROR: {result['message']}")
            return result
        else:
            self.log(f"AI RESPONSE: {result.get('response', 'Success')}")
            return result
    
    def run_demo(self):
        """Run a demo scenario matching the problem statement."""
        self.bootstrap()
        self.scan_environment()
        self.fetch_sheet_data()
        self.authenticate_user()
        
        # Wait a bit before AI task (simulating the 1 minute delay in logs)
        time.sleep(AI_TASK_DELAY_SECONDS)
        
        # This should fail if API key is not set
        result = self.ai_task("How can we improve this page?")
        return result


def main():
    """Main entry point."""
    # Check if .env file exists and load it
    if DOTENV_AVAILABLE:
        load_dotenv()
    else:
        print("Warning: python-dotenv not installed. Environment variables must be set manually.")
    
    titan = TitanOS()
    result = titan.run_demo()
    
    # Exit with error code if AI task failed
    if result.get('status') == 'ERROR':
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
