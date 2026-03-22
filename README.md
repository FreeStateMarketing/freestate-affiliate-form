# FreeState Affiliate Form

![Netlify](https://img.shields.io/badge/deployed-Netlify-brightgreen)
![Firebase](https://img.shields.io/badge/backend-Firebase-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)
[![Netlify Status](https://api.netlify.com/api/v1/badges/3e6e3e4e-6b2e-4b7f-9b8e-5c8b3e9e6c3f/deploy-status)](https://app.netlify.com/sites/freestate-affiliate-form/deploys)

A zero-budget, open-source affiliate sign-up form for FreeState Marketing 101. Built with HTML and Firebase, deployed via Netlify. This form helps us onboard partners who align with our mission of empowerment, wellness, and sustainable systems.

## 🧠 Philosophy

FreeState isn't just a brand—it's a blueprint for resilience.

We build modular systems that empower individuals, not institutions. Every tool we release is designed to be:
- **Repeatable** – so others can build without reinventing the wheel  
- **Zero-budget** – because innovation shouldn't depend on funding  
- **Open-source** – so knowledge flows freely and communities grow stronger  
- **Human-centered** – built for real people solving real problems

This affiliate form is more than a signup—it's an invitation to join a movement rooted in wellness, sustainability, and self-sufficiency. If you believe in grassroots tech, clear documentation, and systems that scale without selling out, you're in the right place.

## 🔧 Tech Stack
- HTML5 + Vanilla JS
- Firebase (Anonymous Auth + Firestore)
- Netlify (Static Hosting)
- Python 3 (Backend - Titan OS)
- OpenAI API (planned integration)

## 🚀 Features

### Frontend (Web Form)
- Collects affiliate info: name, email, website, referral source, notes
- Submits data to Firestore with server timestamp
- Anonymous authentication (no login required)
- Redirects to a thank-you page on success
- Modular structure for future automation:
  - Onboarding flows
  - CSV exports
  - Cloud Functions

### Backend (Titan OS)
- Command registry system for modular operations
- Google Sheets data integration (FETCH_SHEET_DATA scaffold)
- User authentication workflow
- AI task workflow scaffold for page analysis
- Environment-based API key presence validation
- Logging system with timestamp tracking

## 📦 Deployment

### Frontend Deployment
Live site: _[Netlify URL goes here]_  
To deploy manually:
1. Clone this repo
2. Drag folder into [Netlify Drop](https://app.netlify.com/drop)
3. Or connect repo via Netlify dashboard

### Backend Setup (Titan OS)
1. Install Python 3.8 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
