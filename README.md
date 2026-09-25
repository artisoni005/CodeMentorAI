# 💻 CodeMentor AI

## AI Coding Mentor & Intelligent Debugger

## 🚀 Live Demo

👉 [Try CodeMentor AI](https://codementorai-ic27cgk7bbyh2ftxh2vt2j.streamlit.app/)

## 💻 GitHub Repository

👉 [View Source Code](https://github.com/artisoni005/CodeMentorAI)

CodeMentor AI is an AI-powered coding mentor designed to help beginner programmers **understand and debug programming errors** instead of simply providing a replacement solution.

The system follows a structured debugging workflow where different AI agents perform different responsibilities such as code analysis, bug diagnosis, fix suggestion, review, and test-case generation.

---

## 🎯 Problem Statement

Beginners often know that their program is not working but struggle to understand:

* What is wrong with their code
* Why the error is occurring
* Which part of the code is responsible
* How the problem should be corrected
* Whether the correction actually solves the problem

Traditional AI coding assistants may immediately provide corrected code without sufficiently explaining the underlying problem.

CodeMentor AI focuses on **learning-oriented debugging and explanation**.

---

## 💡 Our Solution

CodeMentor AI analyzes a user's program through a structured multi-agent debugging workflow.

The user provides:

* Programming language
* Source code
* Expected behavior
* Error message or failing behavior

The system then performs the following process:

```text
User Code
    ↓
Code Analyzer Agent
    ↓
Bug Diagnosis Agent
    ↓
Fix Agent
    ↓
Reviewer Agent
    ↓
Test Case Generator
    ↓
Debugging Report
```

Each stage has a specific responsibility instead of asking one AI prompt to perform everything at once.

---

# 🤖 Agentic AI Architecture

## 1. Code Analyzer Agent

The Analyzer Agent studies the code before attempting to fix it.

It identifies:

* What the program is trying to do
* Important variables and data structures
* Main control flow
* Potentially problematic sections
* Syntax or logical concerns

It does **not immediately provide corrected code**.

---

## 2. Bug Diagnosis Agent

The Diagnosis Agent receives:

* Original code
* Expected behavior
* Error/failing behavior
* Analyzer's analysis

It identifies:

* The likely bug
* Root cause
* Responsible section of code
* Why the problem occurs

The diagnosis is explained in beginner-friendly language.

---

## 3. Fix Agent

The Fix Agent uses the diagnosis to suggest a correction.

It provides:

* Required change
* Reason the change works
* Corrected code
* Beginner-friendly explanation

The objective is to avoid unnecessary modifications to the original program.

---

## 4. Reviewer Agent

The Reviewer Agent evaluates the proposed correction.

It checks:

* Whether the bug was addressed
* Whether the expected behavior is satisfied
* Whether new problems were introduced
* Whether the correction is logically appropriate
* Whether additional issues exist

This creates a second level of verification instead of blindly accepting the generated fix.

---

## 5. Test Case Generator

The Test Case Generator creates test cases that can be used to verify the solution.

It considers:

* Normal test cases
* Edge cases
* Expected results
* What each test verifies

This helps beginners understand how to validate their corrected program.

---

# 🌟 Key Features

### 🔍 Intelligent Code Analysis

Understand the structure and behavior of the submitted program.

### 🐛 Root Cause Diagnosis

Identify the underlying reason for the programming error.

### 🔧 Guided Fix Suggestions

Explain what should be changed and why.

### 🔎 Fix Review

Review the proposed correction for possible problems.

### 🧪 Test Case Generation

Generate normal and edge-case scenarios for verification.

### 💡 Hint Mode

Provides debugging guidance without immediately revealing the complete correction.

### 👨‍💻 Beginner-Friendly Explanations

Technical problems are explained in simple language.

### 🎭 Demo Mode

Allows the complete workflow to be demonstrated without depending on the Gemini API.

### 🤖 Live AI Mode

Uses Gemini to perform the AI-powered debugging workflow.

---

# 🛠️ Technology Stack

| Technology        | Purpose                             |
| ----------------- | ----------------------------------- |
| Python            | Core programming language           |
| Streamlit         | Web-based user interface            |
| Google Gemini API | AI-powered analysis and debugging   |
| google-genai      | Gemini API integration              |
| python-dotenv     | Environment variable management     |
| Git/GitHub        | Version control and project sharing |

---

# 📁 Project Structure

```text
CodeMentor AI/
│
├── app.py
│
├── agents/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── diagnoser.py
│   ├── fixer.py
│   ├── reviewer.py
│   ├── test_generator.py
│   └── workflow.py
│
├── services/
│   ├── __init__.py
│   └── gemini_service.py
│
├── prompts/
│   ├── __init__.py
│   └── debugging_prompts.py
│
├── tests/
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd "CodeMentor AI"
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Gemini API

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Do not upload the `.env` file to GitHub.

---

## 5. Run the Application

```bash
python -m streamlit run app.py
```

The CodeMentor AI interface will open in your browser.

---

# 🧑‍💻 How to Use

### Step 1

Select the programming language.

### Step 2

Enter your source code.

### Step 3

Describe the expected behavior.

### Step 4

Enter the error message or explain the failing behavior.

### Step 5

Select:

* Demo Mode or Live AI Mode
* Normal Mode or Hint Mode

### Step 6

Click **Start Debugging**.

The system then presents the debugging results through the agent workflow.

---

# 🧪 Example

### Input

```c
#include <stdio.h>

int main() {

    int numbers[5] = {10, 20, 30, 40, 50};

    for(int i = 0; i <= 5; i++) {
        printf("%d\n", numbers[i]);
    }

    return 0;
}
```

### Expected Behavior

Print all five numbers.

### Problem

The loop accesses index `5`, although the valid indexes are:

```text
0 1 2 3 4
```

### CodeMentor AI Workflow

```text
Analyzer
   ↓
Identifies array and loop structure

Diagnoser
   ↓
Identifies incorrect loop boundary

Fixer
   ↓
Suggests changing <= to <

Reviewer
   ↓
Checks whether the correction solves the problem

Test Generator
   ↓
Creates test cases to verify the correction
```

---

# 🔐 Security

API keys are stored using environment variables.

The `.env` file should be included in `.gitignore`:

```text
.env
venv/
__pycache__/
```

Never commit your Gemini API key to GitHub.

---

# 🔮 Future Scope

Possible future improvements include:

* Automatic code execution
* Execution feedback
* Multiple debugging iterations
* Automatic language detection
* Code quality analysis
* Time and space complexity analysis
* Advanced explanation mode
* Automatic test execution
* More programming language support
* Persistent debugging history

---

# 🏆 Hackathon Objective

CodeMentor AI focuses on transforming AI from a simple **code generator** into an **interactive coding mentor**.

Instead of simply answering:

> "Here is the corrected code."

the system follows a structured process:

```text
Understand
   ↓
Diagnose
   ↓
Explain
   ↓
Correct
   ↓
Review
   ↓
Test
```

This makes the debugging process more educational and useful for beginner programmers.

---

# 👥 Team

**Project:** CodeMentor AI
**Category:** AI Coding Mentor & Debugger
**Domain:** Agentic AI / Generative AI / Developer Tools

---

# 📌 Conclusion

CodeMentor AI provides a structured and beginner-friendly approach to programming debugging.

By dividing the debugging process into specialized agents, the system helps users understand **what went wrong, why it went wrong, how to correct it, and how to verify the correction**.

````

### One important thing before GitHub

In the README, replace:

```text
YOUR_GITHUB_REPOSITORY_URL
````

with your actual repository URL **after you create the GitHub repository**.

Also, **don't add any API key to the README**.

Now we should move quickly to the **final 20–30 minute phase: testing + GitHub + your 2-minute presentation/demo script**.
