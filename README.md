# WiseBite - AI-Powered Food Safety Analyzer

WiseBite is an AI-powered food safety analyzer that helps users make informed decisions about food products based on their personal health profiles, allergies, and medical conditions.

## Features

- **Barcode Scanning**: Scan product barcodes to get instant safety analysis
- **Image Analysis**: Upload ingredient label images for analysis
- **Personalized Safety Assessment**: Get hazard levels based on your specific allergies and medical conditions
- **Real-time News**: Stay updated on product recalls and controversies
- **User Profiles**: Save your allergy and medical information

## Setup Instructions

### Backend Setup

1. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_google_gemini_api_key_here
   NEWS_API_KEY=your_news_api_key_here
   ```

4. **Run the backend**:
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Install dependencies**:
   ```bash
   cd frontend
   npm install
   ```

2. **Run the development server**:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`

## API Endpoints

- `POST /analyze`: Analyze a product by barcode
- `POST /analyze-label`: Analyze a product from an uploaded image
- `POST /extract-barcode`: Extract barcode from an image
- `GET /product-news`: Get news articles about a product

## Recent Fixes

- Updated to use the new `google-genai` package (replacing deprecated `google-generativeai`)
- Fixed frontend build issues by adding missing `index.html`
- Resolved dependency conflicts in the frontend
- Added proper virtual environment setup for Python
- Updated API calls to use the new Google AI SDK

## Environment Variables

- `GEMINI_API_KEY`: Required. Your Google Gemini API key
- `NEWS_API_KEY`: Optional. NewsAPI key for product news features

## Technologies Used

- **Backend**: FastAPI, Python, Google Gemini AI
- **Frontend**: React, TypeScript, Vite, Tailwind CSS
- **APIs**: Open Food Facts, NewsAPI