# 🧠 AI-POWERED RESUME BUILDER

![License](https://img.shields.io/badge/license-MIT-green) ![Django](https://img.shields.io/badge/Django-5.x-blue)

An AI-powered web application that helps users create, preview, and download stunning resumes. Leveraging Google Gemini's generative AI API, it can automatically generate a complete resume from just a job description — no manual input required!

---

## **Project Description**

The AI-Powered Resume Builder is a web application designed to simplify and enhance the resume creation process. Leveraging artificial intelligence, this tool helps users generate professional, tailored resumes by analyzing their input and suggesting relevant content, formatting, and keywords. Say goodbye to generic resumes and stand out to potential employers with a resume optimized for success.

## 🚀 Features

- 🔐 **User Authentication** (Login & Register)
- 📝 **Resume Form** with sections for:
  - Personal Info
  - Education (multi-entry)
  - Experience (multi-entry)
  - Skills, Summary, Certifications, Achievements
- 🤖 **AI Resume Generator** via Google Gemini API
  - Paste a job description → get a tailored resume!
- 👀 **Live Resume Preview** in multiple templates:
  - Classic, Professional, Modern, Elegant
- 📄 **Download Resume as PDF**
- 💡 **Job-Resume Matching** (AI-powered suggestions)
- 📱 Responsive design ready for deployment

---

## **Getting Started**

Follow these steps to set up and run the AI-Powered Resume Builder on your local machine.

### **Prerequisites**

Make sure you have the following installed:

* **Python** (v3.9 or higher)
* **pip** (Python package installer)

## 🔧 Tech Stack

- **Backend**: Django 5.1+
- **Frontend**: HTML, CSS
- **AI Engine**: Google Gemini (via `google-generativeai`)
- **PDF Export**: `xhtml2pdf`
- **Session & Form Handling**: Django Forms + Formsets

---

## 📦 Installation

### 🔁 Clone the repository
```bash
git clone https://github.com/omkaryadav18/ai-resume-builder.git
cd Prosume
```

### 📦 Install dependencies
```bash
pip install -r requirements.txt
```

### 🔑 Configure Gemini API
Create a `.env` file and add:
```env
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## 🛠️ Usage

### ⚙️ Run the development server:
```bash
python manage.py migrate
python manage.py createsuperuser  # (optional)
python manage.py runserver
```

Then visit: `http://127.0.0.1:8000/`

---

## 🧪 Test AI Resume Generation

1. Go to **“Generate Resume using AI”**
2. Paste a job description
3. Click “Generate”
4. Preview or Download the auto-generated resume

---

## 📁 Project Structure

```
prosume/
│
├── resume/                # Django app
│   ├── templates/resume/  # HTML templates
│   ├── models.py          # Resume
│   ├── views.py           # All views (including AI + PDF)
│   ├── forms.py           # Forms + Formsets
│
├── users/
    ├── registration/
      ├── login.html
      ├── register.html
    ├── dashboard.html 
    ├── home.py         
├── manage.py
├── requirements.txt
├── README.md
```

---

## ✅ To-Do / Improvements

- [ ] Add user profile photos
- [ ] Support LinkedIn-style download
- [ ] Save Gemini-generated resume directly into DB
- [ ] Mobile-first Tailwind UI polish

---

## 📝 License

This project is open-source under the **MIT License**. Feel free to use, modify, and share!

---

## 🙌 Acknowledgements

- [Google Gemini API](https://ai.google.dev/)
- [Django Project](https://www.djangoproject.com/)
- [xhtml2pdf](https://github.com/xhtml2pdf/xhtml2pdf)
