# PDF Query System

A full-stack web application that allows users to upload PDF documents and query them using AI-powered natural language processing.

## Features

- 🔐 **User Authentication**: Secure login/register system with JWT tokens
- 📄 **PDF Upload**: Drag-and-drop PDF file upload with validation
- 🤖 **AI-Powered Queries**: Ask questions about your documents using Google's Gemini AI
- 🔍 **RAG System**: Retrieval-Augmented Generation for accurate document-based responses
- 🎨 **Modern UI**: Beautiful, responsive frontend with real-time feedback
- 🔒 **Protected Routes**: All PDF operations require authentication

## Architecture

- **Frontend**: HTML/CSS/JavaScript with modern UI design
- **Backend**: FastAPI with SQLAlchemy for authentication and RAG system
- **Database**: SQLite (can be upgraded to PostgreSQL/MySQL for production)
- **AI**: Google Gemini 2.0 Flash for natural language processing
- **Vector Database**: ChromaDB for document embeddings and similarity search

## Prerequisites

- Python 3.8 or higher
- Google AI API key (for Gemini)
- Modern web browser

## Quick Start

### 1. Clone and Setup

```bash
# Navigate to the project directory
cd Project

# Run the startup script (this will install dependencies and start the server)
python start_backend.py
```

### 2. Set up Google AI API Key

You need a Google AI API key for the Gemini model. Get one from [Google AI Studio](https://makersuite.google.com/app/apikey).

Set the environment variable:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Or create a `.env` file in the `Backend/` directory:
```
GOOGLE_API_KEY=your-api-key-here
SECRET_KEY=your-secret-key-here
```

### 3. Access the Application

1. **Backend API**: http://localhost:8000
2. **API Documentation**: http://localhost:8000/docs
3. **Frontend**: Open `Frontend/index.html` in your browser

## Usage

### 1. Authentication

1. Open `Frontend/index.html` in your browser
2. Click "Create Account" to register a new user
3. Or use existing credentials to login
4. You'll be redirected to the dashboard after successful authentication

### 2. Upload PDF Documents

1. In the dashboard, click the upload area or drag & drop PDF files
2. Supported: PDF files up to 10MB each
3. Files are processed and indexed for AI queries

### 3. Query Your Documents

1. Type your question in the query textarea
2. Click "Send Query" or press Ctrl+Enter
3. Get AI-powered responses based on your uploaded documents

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/email/login` - Login with email/password
- `GET /auth/me` - Get current user info
- `POST /auth/logout` - Logout user

### PDF Operations (Protected)
- `POST /upload` - Upload PDF files
- `POST /query` - Query uploaded documents
- `GET /files` - List uploaded files
- `DELETE /files` - Clear all uploaded files

## Project Structure

```
Project/
├── Backend/
│   ├── main.py              # Main FastAPI application
│   ├── Auth/
│   │   └── email_auth.py    # Authentication module
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
├── Frontend/
│   ├── index.html          # Login/Register page
│   └── dashboard.html      # Main application dashboard
├── auth.db                 # SQLite database
├── start_backend.py        # Startup script
└── README.md              # This file
```

## Technical Details

### Backend Technologies
- **FastAPI**: Modern, fast web framework
- **SQLAlchemy**: Database ORM
- **Passlib**: Password hashing
- **PyJWT**: JWT token handling
- **ChromaDB**: Vector database for embeddings
- **Sentence Transformers**: Text embedding model
- **Google Generative AI**: LLM for responses

### Frontend Technologies
- **Vanilla JavaScript**: No framework dependencies
- **Modern CSS**: Flexbox, Grid, CSS Variables
- **Local Storage**: Token and user data persistence
- **Fetch API**: HTTP requests to backend

### Security Features
- Password hashing with bcrypt
- JWT token authentication
- Protected API endpoints
- CORS configuration
- Input validation and sanitization

## Development

### Running in Development Mode

The startup script runs the server with auto-reload enabled. Any changes to the backend code will automatically restart the server.

### Manual Setup

If you prefer manual setup:

```bash
# Install dependencies
pip install -r Backend/requirements.txt

# Set environment variables
export GOOGLE_API_KEY="your-api-key"

# Run the server
cd Backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Database

The application uses SQLite by default. The database file (`auth.db`) is created automatically when you first run the application.

For production, consider using PostgreSQL or MySQL:

```python
# In Backend/main.py, change DATABASE_URL
DATABASE_URL = "postgresql://user:password@localhost/dbname"
```

## Troubleshooting

### Common Issues

1. **"GOOGLE_API_KEY not set"**
   - Set the environment variable or add it to `.env` file

2. **"Module not found" errors**
   - Run `pip install -r Backend/requirements.txt`

3. **CORS errors in browser**
   - Make sure the backend is running on `http://localhost:8000`
   - Check browser console for specific error messages

4. **Authentication fails**
   - Clear browser local storage and try again
   - Check if the backend is running and accessible

### Logs

Check the terminal where you started the backend for error messages and logs.

## Production Deployment

For production deployment:

1. **Security**: Change the `SECRET_KEY` to a strong, random value
2. **Database**: Use PostgreSQL or MySQL instead of SQLite
3. **CORS**: Configure `allow_origins` with your frontend domain
4. **Environment**: Use proper environment variable management
5. **HTTPS**: Serve over HTTPS in production
6. **Process Manager**: Use Gunicorn with Uvicorn workers

## License

This project is for educational purposes. Feel free to modify and use as needed.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

If you encounter any issues:

1. Check the troubleshooting section
2. Review the API documentation at `http://localhost:8000/docs`
3. Check the browser console for frontend errors
4. Review the backend logs in the terminal 