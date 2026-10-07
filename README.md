# NPC 🌿
### Nature's Personal Companion

> **Most AI wants you to stay on your screen. This one wants you to leave it.**

**NPC (Nature's Personal Companion)** is a tiny AI-powered field game that turns an ordinary place into a small adventure.

Tell NPC where you are, how much time you have, your mood, and who you're with. It gives you a **field persona**, a **mission**, and a set of **objectives** designed to make you notice and interact with the world around you.

Then you put your phone away and go complete the quest.

Because sometimes you need an NPC to tell you to **touch grass.** 🌱

---

## 🎮 What does NPC do?

NPC generates a personalized real-world **Field Assignment** based on your situation.

You choose:

- 📍 **Where you are** — park, campus, city, neighbourhood, waterfront, etc.
- ⏱️ **How much time you have** — from 5 to 60 minutes
- 🧠 **Your mood** — bored, stressed, curious, energetic, and more
- 👥 **Who you're with** — alone, with a friend, or in a group

NPC then creates:

### 🪪 A Field Persona
Become something like a **Wildlife Detective**, **Urban Explorer**, **Sound Collector**, or **Tiny Things Investigator**.

### 🧭 A Mission
A small adventure tailored to your surroundings and available time.

### 🎯 Objectives
A handful of things to observe, find, notice, or do.

### 🚫 A Field Rule
A fun constraint that makes the mission more interesting.

### ✅ A Completion Condition
A clear way to know when you've finished your quest.

The goal isn't to give you another checklist.

**It's to make the real world feel a little more interesting.**

---

## 🌳 Why?

AI is increasingly good at keeping us on screens.

Generate an image.  
Write something.  
Summarize something.  
Ask another question.

NPC uses AI for the opposite purpose.

The AI generates the experience **once**, and then the user is encouraged to stop looking at the screen and actually go outside.

> **The screen gives you the quest. The world is the game.**

---

## ✨ Example

You tell NPC:

```text
Where: University campus
Time: 20 minutes
Mood: Bored
Company: A friend
```

NPC might respond:

> 🪪 **FIELD ASSIGNMENT**
>
> **Persona:** Campus Cartographer
>
> **Mission:** Your campus has more landmarks than you think. Explore the area around you and build a mental map using only things you notice along the way.
>
> **Objectives:**
> 1. Find three things that could serve as landmarks.
> 2. Notice something you have walked past before but never really looked at.
> 3. Find two different sounds coming from different directions.
> 4. Compare one part of the campus with another.
>
> **🚫 Field Rule:** No photographs. Your memory is the map.
>
> **✅ Mission Complete When:** You and your companion can describe your route and three things you noticed that you probably wouldn't have noticed otherwise.

Your phone has done its job.

**Now go.**

---

## 🧠 How It Works

NPC is deliberately simple.

```text
User
  │
  │  environment
  │  time
  │  mood
  │  company
  ▼
Flask backend
  │
  │  structured prompt
  ▼
Gemma
  │
  │  field assignment
  ▼
JSON response
  │
  ▼
Interactive assignment card
```

The AI is not just an optional chatbot layered onto the project.

**Gemma is responsible for creating the actual game content** — the persona, mission, objectives, rule, and completion condition.

---

## 🛠️ Built With

- **Python**
- **Flask**
- **Vanilla HTML, CSS & JavaScript**
- **Gemma** via the Google GenAI API
- **python-dotenv**

No database.  
No accounts.  
No GPS tracking.  
No maps.  
No complicated frontend framework.

Just a tiny web app and an AI generating tiny adventures.

---

## 🔒 Safety

NPC's assignments are designed to stay simple and safe.

The AI is instructed **not** to:

- Send users into dangerous, restricted, or isolated places
- Ask users to approach strangers
- Ask users to touch unknown plants, animals, insects, or objects
- Require unsafe road crossings
- Require spending money
- Require confidently identifying species
- Require leaving the general area described by the user

Use common sense and ignore any instruction that feels unsafe or inappropriate for your surroundings.

---

## 💻 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/theikosB/nature-personal-companion.git
cd nature-personal-companion
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

**Never commit your `.env` file.**

### 5. Run the app

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

Choose your situation, generate your assignment, and go complete it.

---

## 🤝 Contributing

NPC is intentionally small, so contributions can be equally small.

Some ideas:

- Add new field personas
- Improve mission-generation prompts
- Add new environments or moods
- Improve the UI
- Add better safety constraints
- Add interesting game mechanics
- Translate NPC into another language

If you have an idea that makes people spend **less time looking at the screen and more time experiencing the world**, it probably belongs here.

---

## 🌱 The Philosophy

NPC isn't trying to replace going outside with an AI experience.

It's trying to use AI for exactly one thing:

**getting you to stop using AI.**

So close the laptop.

Put down the phone.

Go outside.

**Your quest is waiting.** 🧭