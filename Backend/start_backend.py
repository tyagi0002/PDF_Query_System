#!/usr/bin/env python3
"""
Startup script for the PDF Query System Backend
"""

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def check_requirements():
    """Check if requirements.txt exists"""
    requirements_file = Path("Backend/requirements.txt")
    if not requirements_file.exists():
        print("❌ requirements.txt not found in Backend directory")
        sys.exit(1)
    print("✅ requirements.txt found")

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "Backend/requirements.txt"
        ], check=True)
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def check_environment():
    """Check environment variables"""
    # Load .env file first
    env_file = Path("Backend/.env")
    if env_file.exists():
        load_dotenv(env_file)
        print("✅ .env file loaded")
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("⚠️  GOOGLE_API_KEY environment variable not set")
        print("   You can set it with: export GOOGLE_API_KEY='your-api-key'")
        print("   Or create a .env file in the Backend directory")
    else:
        print("✅ GOOGLE_API_KEY found")

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = Path("Backend/.env")
    if not env_file.exists():
        print("📝 Creating .env file...")
        with open(env_file, "w") as f:
            f.write("# Environment variables for PDF Query System\n")
            f.write("# Add your Google API key here:\n")
            f.write("GOOGLE_API_KEY=your-api-key-here\n")
            f.write("SECRET_KEY=your-secret-key-here\n")
        print("✅ .env file created")
        print("📝 Please edit Backend/.env and add your actual API keys")

def start_server():
    """Start the FastAPI server"""
    print("🚀 Starting PDF Query System Backend...")
    print("📍 Server will be available at: http://localhost:8000")
    print("📚 API documentation at: http://localhost:8000/docs")
    print("🔑 Authentication endpoints:")
    print("   - Register: POST /auth/register")
    print("   - Login: POST /auth/email/login")
    print("   - Logout: POST /auth/logout")
    print("📄 PDF endpoints:")
    print("   - Upload: POST /upload")
    print("   - Query: POST /query")
    print("   - Files: GET /files")
    print("\nPress Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "Backend.main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000",
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n👋 Server stopped")

def main():
    """Main function"""
    print("🔧 PDF Query System Backend Setup")
    print("=" * 40)
    
    # Change to project root directory
    os.chdir(Path(__file__).parent)
    
    check_python_version()
    check_requirements()
    install_dependencies()
    create_env_file()  # Create .env file first
    check_environment()  # Then check environment variables
    
    print("\n" + "=" * 40)
    start_server()

if __name__ == "__main__":
    main() 