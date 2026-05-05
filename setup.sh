#!/bin/bash
# Quick start guide for TTS Agent

echo "🎙️  Text-to-Speech Agent - Quick Start"
echo "======================================"
echo ""

# Check if GEMINI_API_KEY is set
if [ -z "$GEMINI_API_KEY" ]; then
    echo "⚠️  GEMINI_API_KEY environment variable not set!"
    echo "Set it with: export GEMINI_API_KEY='your-api-key-here'"
    echo ""
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "Usage:"
echo "  Local: python tts_generator.py \"Your text here\" --voice Orus"
echo "  GitHub: Push to repo and use 'Generate Speech' workflow"
echo ""
echo "For more info: cat README.md"
