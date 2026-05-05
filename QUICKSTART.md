# ⚡ TTS Agent - Quick Start Guide

## What You Have

A complete **Google Gemini 3.1 Flash TTS Agent** system that:
- ✅ Accepts CUSTOM values for all parameters (not limited to presets!)
- ✅ Provides sensible defaults for everything
- ✅ Parses director's notes automatically
- ✅ Extracts descriptions from bracketed text `[description]`
- ✅ Works locally via CLI
- ✅ Works on GitHub Actions via workflow
- ✅ Based on official Google AI Studio SDK

## Files Created

```
tts-agent/
├── tts_generator.py              # Main agent (✓ Ready to use)
├── example_aetheris.py           # Example from original SDK code
├── examples_custom_parameters.py # Examples showing custom values
├── test_local.py                 # Local test suite
├── .github/workflows/
│   └── tts-generate.yml          # GitHub Actions workflow
├── voice_profiles.json           # Voice & profile configurations
├── requirements.txt              # Dependencies
├── .env.example                  # Environment template
├── setup.bat                     # Windows setup
├── setup.sh                      # macOS/Linux setup
├── .gitignore                    # Git ignore rules
├── README.md                     # Full documentation
└── QUICKSTART.md                 # This file
```

## 🚀 Get Started in 2 Minutes

### Step 1: Install Dependencies
```bash
cd C:\Users\Mahesh Babu J\Desktop\python_codes\tts-agent
pip install -r requirements.txt
```

### Step 2: Set API Key
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="AIzaSyAKxY-HRH7zqq29-GYTEbyuLVLq9g3MiSY"

# Windows CMD
set GEMINI_API_KEY=AIzaSyAKxY-HRH7zqq29-GYTEbyuLVLq9g3MiSY

# macOS/Linux
export GEMINI_API_KEY="AIzaSyAKxY-HRH7zqq29-GYTEbyuLVLq9g3MiSY"
```

### Step 3: Run Example
```bash
python example_aetheris.py
```

This generates the **Aetheris Sedan commercial** from the original SDK code.

## 📖 How It Works

### 1️⃣ Original SDK Code (From Google)
```
# Audio Profile
A smooth, premium commercial voice.

# Director's note
Style: Promo/Hype. Pace: Natural. Accent: American (Gen).

## Transcript:
[intrigue] You don't just want a car. [desire] You want a sanctuary...
```

### 2️⃣ TTS Agent Processes It
- **Parses Director's Note** → Extracts: Style, Pace, Accent
- **Extracts Descriptions** → [intrigue], [desire], etc. → Filename
- **Applies Audio Profile** → Guides voice generation
- **Uses Voice** → Orus (or any custom voice)

### 3️⃣ Generates Audio
Output: `intrigue_desire_information_inspiration_confident_0.wav` (300-500 KB)

## 🎯 Usage Examples

### Example 1: CLI with Original SDK Format
```bash
python tts_generator.py "[intrigue] You don't just want a car. [desire] You want a sanctuary. Introducing the all-new Aetheris Sedan." \
  --voice Orus \
  --audio-profile "A smooth, premium commercial voice." \
  --directors-note "Style: Promo/Hype. Pace: Natural. Accent: American (Gen)."
```

**What happens:**
- ✓ Description extracted: `intrigue, desire`
- ✓ Director's note parsed: Style=Promo/Hype, Pace=Natural, Accent=American (Gen)
- ✓ Output: `intrigue_desire_0.wav`

### Example 2: With Explicit Parameters
```bash
python tts_generator.py "Python is a programming language" \
  --voice Sage \
  --style Natural \
  --pace Slow \
  --accent British \
  --description "python-tutorial" \
  --output-dir ./educational
```

### Example 3: Custom Parameters (Most Flexible!)
```bash
python tts_generator.py "Your text here" \
  --voice "MyCustomVoice" \
  --audio-profile "My special audio profile" \
  --style "MyCustomStyle" \
  --pace "MyCustomPace" \
  --accent "MyCustomAccent" \
  --description "my-output"
```

**⭐ ALL PARAMETERS ACCEPT CUSTOM VALUES:**
- ✓ voice: Not limited to Orus/Achernar/Pax/Sage
- ✓ audio-profile: Use any custom description
- ✓ style: Not limited to predefined styles
- ✓ pace: Use any pace value
- ✓ accent: Use any accent value

### Example 4: Python Script
```python
from tts_generator import generate_speech

output_files = generate_speech(
    transcript="[intrigue] You don't just want a car. [desire] You want a sanctuary.",
    voice_name="Orus",
    audio_profile="A smooth, premium commercial voice.",
    directors_note="Style: Promo/Hype. Pace: Natural. Accent: American (Gen).",
    api_key="your-api-key",
    auto_extract_description=True,
)
print(f"Generated: {output_files}")
```

## 🔧 GitHub Actions Usage

✅ **Now with Full Custom Value Support!**

GitHub Actions form now accepts custom values for all parameters:

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "TTS Agent setup"
   git remote add origin https://github.com/YOUR_USERNAME/tts-agent.git
   git push -u origin main
   ```

2. **Add Secret**
   - Settings → Secrets → New repository secret
   - Name: `GEMINI_API_KEY`
   - Value: Your API key

3. **Trigger Workflow**
   - Go to Actions tab
   - Select "Generate Speech"
   - Click "Run workflow"
   - Fill in form with:
     - **Transcript**: Your text
     - **Voice**: Orus, Pax, or ANY custom voice name
     - **Audio Profile**: Select or enter custom
     - **Style**: Natural, Promo/Hype, or ANY custom
     - **Pace**: Slow, Natural, Fast, or ANY custom
     - **Accent**: American (Gen), British, or ANY custom
     - **Description**: Optional (auto-extracted if omitted)
     - **Director's Note**: Optional

4. **Download Results**
   - Download from Artifacts
   - Or download from GitHub Release

## 🗣️ Voice Profiles

Available voices with descriptions:

```json
{
  "Orus": "Soft, Higher pitch - Great for friendly commercials",
  "Achernar": "Soft, Higher pitch - Similar to Orus",
  "Pax": "Deep, warm, authoritative - Perfect for documentaries",
  "Sage": "Clear, professional, informative - Ideal for educational"
}
```

*Note: These are defaults - you can use ANY voice name you want!*

## 🧪 Local Testing

Run the test suite before deploying:

```bash
python test_local.py
```

This tests:
- ✓ Director's note parsing
- ✓ Description extraction
- ✓ Full speech generation (if API key set)

## 💡 Examples with Custom Values

Try the custom parameters example:

```bash
python examples_custom_parameters.py
```

Shows how to use:
- ✓ Custom commercial voice
- ✓ Custom educational content
- ✓ Custom documentary voice
- ✓ Custom friendly voice
- ✓ All custom parameters

## ⚠️ Troubleshooting

### "API key not provided" Error
```bash
$env:GEMINI_API_KEY="your-key-here"
```

### "No audio generated" Error
- Check transcript length (should be meaningful)
- Verify API key is valid
- Check Google Cloud quota

### Import Errors
```bash
pip install --upgrade google-genai python-dotenv
```

## 🎬 Next Steps

1. ✅ Test locally: `python example_aetheris.py`
2. ✅ Try custom text: `python tts_generator.py "Your text"`
3. ✅ Try custom values: `python examples_custom_parameters.py`
4. ✅ Run tests: `python test_local.py`
5. ✅ Deploy to GitHub
6. ✅ Use GitHub Actions for automated generation

---

**API Key Used:** AIzaSyAKxY-HRH7zqq29-GYTEbyuLVLq9g3MiSY

**Based on:** Google AI Studio Gemini 3.1 Flash TTS SDK

**Ready to generate speech!** 🎙️
