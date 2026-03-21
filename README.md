# FreeState Affiliate Form

![Netlify](https://img.shields.io/badge/deployed-Netlify-brightgreen)
![Firebase](https://img.shields.io/badge/backend-Firebase-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)
[![Netlify Status](https://api.netlify.com/api/v1/badges/3e6e3e4e-6b2e-4b7f-9b8e-5c8b3e9e6c3f/deploy-status)](https://app.netlify.com/sites/freestate-affiliate-form/deploys)

A zero-budget, open-source affiliate sign-up form for FreeState Marketing 101. Built with HTML and Firebase, deployed via Netlify. This form helps us onboard partners who align with our mission of empowerment, wellness, and sustainable systems.

## 🧠 Philosophy

FreeState isn’t just a brand—it’s a blueprint for resilience.

We build modular systems that empower individuals, not institutions. Every tool we release is designed to be:
- **Repeatable** – so others can build without reinventing the wheel  
- **Zero-budget** – because innovation shouldn’t depend on funding  
- **Open-source** – so knowledge flows freely and communities grow stronger  
- **Human-centered** – built for real people solving real problems

This affiliate form is more than a signup—it’s an invitation to join a movement rooted in wellness, sustainability, and self-sufficiency. If you believe in grassroots tech, clear documentation, and systems that scale without selling out, you’re in the right place.


## 🔧 Tech Stack
- HTML5 + Vanilla JS
- Firebase (Anonymous Auth + Firestore)
- Netlify (Static Hosting)
- Python 3 (Backend - Titan OS)
- OpenAI API (AI-powered page analysis)

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
- Google Sheets data integration (FETCH_SHEET_DATA)
- User authentication workflow
- AI-powered page analysis with OpenAI integration
- Proper API key validation to prevent invalid key errors
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
   ```
3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Add your OpenAI API key to `.env`:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```
5. Run Titan OS:
   ```bash
   python3 titan_os.py
   ```

**Expected Output:**
```
[00:00:00] LOADED: titan_os.py
[00:00:00] SYSTEM: Bootstrapped Command Registry.
[00:00:00] Scanning Environment...
[00:02:00] Environmental Data Synced.
[00:02:00] TX >> FETCH_SHEET_DATA
[00:02:00] RX << SUCCESS
[00:02:00] Inventory Updated.
[00:02:00] USER AUTHENTICATED.
[00:03:00] AI TASK (strategy): How can we improve this page?
[00:03:00] AI RESPONSE: Analysis for: How can we improve this page?
```

**Note:** If you see `ERROR: API KEY INVALID`, ensure your OpenAI API key is properly set in the `.env` file.

## 🛠️ Roadmap
- Add form validation
- Trigger onboarding emails via Cloud Functions
- Export affiliate data to CSV
- Add status update logic (approved/rejected)

## 🤝 Contributing
This project is built for resilience and repeatability. If you're passionate about grassroots tech, modular systems, or community empowerment, we welcome your input. Fork the repo, submit PRs, or reach out via FreeState channels.

## ❓ FAQ

**Q: How do I test the form locally?**  
A: Open `index.html` in your browser. No server required.

**Q: Where does the data go?**  
A: Firestore → `affiliates` collection. You can view it in Firebase Console.

**Q: Can I customize the fields?**  
A: Yes. Edit `index.html` and `main.js` to match your data needs.

**Q: Can I use this for other FreeState modules?**  
A: Absolutely. This form is modular and repeatable by design.

**Q: Is this production-ready?**  
A: It’s a blueprint—robust, scalable, and open-source. You can extend it with validation, email triggers, and admin dashboards.


## 🖼️ Screenshots

### Affiliate Sign-Up Form
![Affiliate Form](screenshots/form.png)

### Confirmation Page
![Thank You](screenshots/thank_you.png)

## 📅 Changelog

### v1.0.0 – Initial Launch
- Firestore integration
- Anonymous auth
- Redirect logic
- Screenshots added
- Philosophy section added
- Badge wall added to README

### v1.1.0 – Planned
- Form validation (client-side)
- CSV export for affiliate data
- Cloud Function triggers for onboarding
- Admin dashboard for affiliate status


---

**Q: How do I use Titan OS?**  
A: Install Python dependencies with `pip install -r requirements.txt`, configure your `.env` file with your OpenAI API key, and run `python3 titan_os.py`.

**Q: Why am I getting "API KEY INVALID" error?**  
A: This means your OpenAI API key is either missing or invalid. Make sure you've:
1. Created a `.env` file from `.env.example`
2. Added a valid OpenAI API key (starts with `sk-`)
3. Set the `OPENAI_API_KEY` environment variable

**Q: What does Titan OS do?**  
A: Titan OS is a modular backend system that handles Google Sheets integration, user authentication, and AI-powered page analysis. It's designed to extend the affiliate form with automation and intelligence.

