# Text-to-Speech Agent with Google AI Studio (Gemini 3.1 Flash)

Generate customizable speech using Google's Gemini 3.1 Flash TTS model via GitHub Actions and Python CLI.

**Flexible Parameter System:** All parameters (voice, style, pace, accent, audio profile) accept CUSTOM values with sensible defaults.

Based on the official Google AI Studio SDK with enhanced parsing and workflow automation.

## Features

✅ **Flexible Parameter System**
- All parameters accept CUSTOM values (not limited to presets)
- Sensible defaults provided for each parameter
- Override any setting as needed

✅ **Automatic Parameter Extraction**
- Parse director's notes to extract Style, Pace, and Accent automatically
- Extract descriptions from bracketed text in transcripts `[description]`
- Full Google AI Studio SDK compatibility

✅ **Customizable Voice Settings**
- Multiple prebuilt voices (Orus, Achernar, Pax, Sage) - or use any custom voice name
- Audio profiles (commercial, friendly, narrator, etc.) - or define custom profiles
- Director's notes for voice direction
- Style, pace, and accent control - fully customizable

✅ **Multiple Input Methods**
- CLI: Run locally with command-line arguments
- GitHub Actions: Trigger via workflow dispatch with custom values
- Automated artifact generation and releases

✅ **Output Management**
- Automatic WAV format conversion
- Artifact upload to GitHub Actions
- Release creation with generated audio

## Quick Start

### Windows
```bash
cd C:\Users\Mahesh Babu J\Desktop\python_codes\tts-agent
setup.bat
```

### macOS/Linux
```bash
cd tts-agent
chmod +x setup.sh
./setup.sh
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Google API Key

**Option A: Environment Variable**
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your-api-key-here"

# Windows CMD
set GEMINI_API_KEY=your-api-key-here

# macOS/Linux
export GEMINI_API_KEY="your-api-key-here"
```

**Option B: .env File**
```bash
cp .env.example .env
# Edit .env and add your API key
```

**Option C: GitHub Secrets (for GitHub Actions)**
1. Go to your GitHub repo → Settings → Secrets and variables → Actions
2. Create new secret: `GEMINI_API_KEY`
3. Paste your API key

Get your API key: [Google AI Studio](https://aistudio.google.com/app/apikey)

## Usage

### Example 1: Using Original SDK Format

Based on the official Google AI Studio code:

```bash
python tts_generator.py "[intrigue] You don't just want a car. [desire] You want a sanctuary. [information] Introducing the all-new Aetheris Sedan. With whisper-quiet cabin technology and an interior designed around you. [inspiration] It's not just about getting to your destination. It's about arriving inspired. [confident] Aetheris. Move beautifully." \
  --voice Orus \
  --audio-profile "A smooth, premium commercial voice." \
  --directors-note "Style: Promo/Hype. Pace: Natural. Accent: American (Gen)."
```

**What happens:**
- Descriptions `[intrigue]`, `[desire]`, etc. are auto-extracted → filename: `intrigue_desire_information_..._0.wav`
- Director's note is parsed → Style: Promo/Hype, Pace: Natural, Accent: American (Gen)
- Audio profile is applied
- Voice "Orus" generates the speech

### Example 2: Commercial Voice

```bash
python tts_generator.py "Introducing the all-new Aetheris Sedan. Move beautifully." \
  --voice Orus \
  --audio-profile "A smooth, premium commercial voice." \
  --style "Promo/Hype" \
  --pace Natural \
  --accent "American (Gen)" \
  --description "car-commercial" \
  --output-dir ./commercials
```

### Example 3: Documentary Narrator

```bash
python tts_generator.py "The Amazon rainforest spans over 5.5 million square kilometers..." \
  --voice Pax \
  --audio-profile "A documentary-style narrator voice." \
  --style Informative \
  --pace Slow \
  --accent British \
  --description "amazon-doc" \
  --output-dir ./documentaries
```

### Example 4: Educational Content

```bash
python tts_generator.py "Python is a high-level programming language..." \
  --voice Sage \
  --audio-profile "A clear educational voice for learning content." \
  --style Natural \
  --pace Natural \
  --description "python-tutorial" \
  --output-dir ./educational
```

### Example 5: With Long Director's Note

```bash
python tts_generator.py "Welcome to our premium service" \
  --voice Orus \
  --audio-profile "A smooth, premium commercial voice." \
  --directors-note "Style: Promo/Hype. Pace: Natural. Accent: American (Gen). This is a premium luxury brand announcement. The narrator should sound sophisticated, confident, and slightly mysterious. Start with intrigue, build to excitement, and end with confidence." \
  --description "premium-service" \
  --output-dir ./output
```

## CLI Arguments Reference

```
positional arguments:
  transcript             Text transcript to convert to speech (can include [descriptions])

optional arguments:
  --voice VOICE          Voice name (default: Orus)
                         ✓ Prebuilt voices: Orus, Achernar, Pax, Sage
                         ✓ Or use ANY custom voice name you want
  
  --audio-profile PROFILE
                         Audio profile description (default: "A smooth, premium commercial voice.")
                         ✓ Examples: "A warm, friendly voice", "A documentary narrator", etc.
                         ✓ Or use ANY custom profile description
  
  --directors-note NOTE  Director's note (format: 'Style: X. Pace: Y. Accent: Z.')
                         Automatically parses to extract Style, Pace, and Accent
  
  --style STYLE          Voice style (default: Natural)
                         ✓ Examples: Natural, Promo/Hype, Calm, Energetic, Informative, Dramatic, Conversational
                         ✓ Or use ANY custom style value
  
  --pace PACE            Speech pace (default: Natural)
                         ✓ Examples: Slow, Natural, Fast
                         ✓ Or use ANY custom pace value
  
  --accent ACCENT        Accent (default: American (Gen))
                         ✓ Examples: American (Gen), British, Indian, Australian, Canadian
                         ✓ Or use ANY custom accent value
  
  --api-key KEY          Google API key (or use GEMINI_API_KEY env var)
  
  --output-dir DIR       Output directory for audio files (default: ./output)
  
  --description DESC     Output filename description (auto-extracted from [brackets] if not provided)
  
  --no-auto-extract      Disable auto-extraction of description from bracketed text
  
  -h, --help             Show help message

KEY POINT: All parameters accept CUSTOM values with defaults provided!
```

### Custom Parameter Examples

**Example 1: Custom Voice and Profile**
```bash
python tts_generator.py "Your text" \
  --voice "CustomVoice" \
  --audio-profile "My special custom profile description"
```

**Example 2: Custom Style and Pace**
```bash
python tts_generator.py "Your text" \
  --style "MyCustomStyle" \
  --pace "VeryFast" \
  --accent "MyCustomAccent"
```

**Example 3: All Custom Parameters**
```bash
python tts_generator.py "Your text" \
  --voice "MyVoice" \
  --audio-profile "My profile" \
  --style "MyStyle" \
  --pace "MyPace" \
  --accent "MyAccent" \
  --description "my-custom-output"
```

## Local Testing

Run the test suite before deploying:

```bash
python test_local.py
```

This will test:
- ✓ Director's note parsing
- ✓ Description extraction from bracketed text
- ✓ Full speech generation (if API key is set)

## GitHub Actions Usage

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
   - Fill in form:
     - Transcript: Your text
     - Voice: Choose from dropdown
     - Audio Profile: Select profile
     - Style/Pace/Accent: Choose from options
     - Description: Optional (auto-extracted if omitted)
     - Director's Note: Optional

4. **Get Results**
   - Download from Artifacts
   - Or download from GitHub Release

## Voice Profiles

```json
{
  "Orus": "Soft, Higher pitch - Great for friendly commercials",
  "Achernar": "Soft, Higher pitch - Similar to Orus",
  "Pax": "Deep, warm, authoritative - Perfect for documentaries",
  "Sage": "Clear, professional, informative - Ideal for educational"
}
```

## File Structure

```
tts-agent/
├── .github/
│   └── workflows/
│       └── tts-generate.yml      # GitHub Actions workflow
├── tts_generator.py              # Main Python script
├── test_local.py                 # Local test suite
├── voice_profiles.json           # Voice and profile configurations
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variables template
├── setup.bat                     # Windows setup script
├── setup.sh                      # macOS/Linux setup script
├── README.md                     # This file
└── output/                       # Generated audio files (created on first run)
```

## How It Works

### Director's Note Parsing

Input:
```
Style: Promo/Hype. Pace: Natural. Accent: American (Gen).
```

Parsed into:
- `style`: Promo/Hype
- `pace`: Natural
- `accent`: American (Gen)

### Description Extraction

Input transcript:
```
[intrigue] You don't just want a car. [desire] You want a sanctuary.
```

Extracted descriptions: `intrigue, desire`

Output filename: `intrigue_desire_0.wav`

### Full Prompt Construction

Combines all elements into proper Google AI Studio SDK format:

```
Read the following transcript based on the audio profile and director's note.

# Audio Profile
A smooth, premium commercial voice.

# Director's note
Style: Promo/Hype. Pace: Natural. Accent: American (Gen).

## Transcript:
[intrigue] You don't just want a car. [desire] You want a sanctuary...
```

## Troubleshooting

### "API key not provided" Error
```bash
# Set environment variable
export GEMINI_API_KEY="your-key-here"

# Or pass directly
python tts_generator.py "text" --api-key "your-key-here"

# Or create .env file
cp .env.example .env
# Edit .env and add your key
```

### "No audio generated" Error
- Check transcript length (should be meaningful text)
- Verify API key is valid
- Check your Google Cloud quota
- Review error message in console

### GitHub Actions Workflow Not Found
- Ensure `.github/workflows/tts-generate.yml` is in repo
- Commit and push to GitHub
- Wait a few seconds for Actions to recognize the workflow

### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade google-genai

# Or use requirements file
pip install -r requirements.txt
```

## API Documentation

- [Google Generative AI Python SDK](https://github.com/googleapis/python-genai)
- [Gemini 3.1 Flash TTS Model](https://ai.google.dev/api/rest/v1beta)
- [Google AI Studio](https://aistudio.google.com/)

## Performance Notes

- Gemini 3.1 Flash TTS supports streaming audio generation
- Audio is automatically converted to WAV format
- Typical generation time: 5-30 seconds per transcript
- File size varies by transcript length (usually 100KB-1MB)

## License

MIT License

## Support

For issues:
1. Check the troubleshooting section
2. Run `python test_local.py` to verify setup
3. Check GitHub Actions logs for workflow errors
4. Review API documentation for quota limits

