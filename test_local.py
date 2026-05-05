#!/usr/bin/env python3
"""
Local test script for TTS Agent
Run this to test the agent locally before pushing to GitHub
"""

import os
import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from tts_generator import (
    parse_directors_note,
    extract_description_from_transcript,
    generate_speech,
)


def test_parse_directors_note():
    """Test parsing director's notes"""
    print("Testing director's note parsing...")
    
    test_cases = [
        {
            "input": "Style: Promo/Hype. Pace: Natural. Accent: American (Gen).",
            "expected": {"style": "Promo/Hype", "pace": "Natural", "accent": "American (Gen)"}
        },
        {
            "input": "Style: Informative, Pace: Slow, Accent: British",
            "expected": {"style": "Informative", "pace": "Slow", "accent": "British"}
        },
        {
            "input": "",
            "expected": {"style": "Natural", "pace": "Natural", "accent": "American (Gen)"}
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = parse_directors_note(test["input"])
        print(f"  Test {i}: ", end="")
        if result == test["expected"]:
            print(f"✓ PASS")
        else:
            print(f"✗ FAIL")
            print(f"    Input: {test['input']}")
            print(f"    Expected: {test['expected']}")
            print(f"    Got: {result}")


def test_extract_description():
    """Test extracting descriptions from bracketed text"""
    print("\nTesting description extraction from transcript...")
    
    test_cases = [
        {
            "input": "[intrigue] You don't just want a car. [desire] You want a sanctuary.",
            "expected": "intrigue, desire"
        },
        {
            "input": "Normal text without brackets",
            "expected": "narration"
        },
        {
            "input": "[opening] Welcome. [middle] Content. [closing] Thank you.",
            "expected": "opening, middle, closing"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = extract_description_from_transcript(test["input"])
        print(f"  Test {i}: ", end="")
        if result == test["expected"]:
            print(f"✓ PASS")
        else:
            print(f"✗ FAIL")
            print(f"    Input: {test['input']}")
            print(f"    Expected: {test['expected']}")
            print(f"    Got: {result}")


def test_full_generation():
    """Test full speech generation (requires API key)"""
    print("\nTesting full speech generation...")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("  ⚠️  GEMINI_API_KEY not set. Skipping full generation test.")
        print("     Set it with: export GEMINI_API_KEY='your-key-here'")
        return
    
    print("  ✓ API key found. Ready for generation test.")
    
    # Example transcript with descriptions
    transcript = """[intrigue] You don't just want a car. [desire] You want a sanctuary. 
[information] Introducing the all-new Aetheris Sedan. With whisper-quiet cabin technology and an interior designed around you. 
[inspiration] It's not just about getting to your destination. [confident] It's about arriving inspired. Move beautifully."""
    
    print(f"  Transcript: {transcript[:50]}...")
    
    directors_note = "Style: Promo/Hype. Pace: Natural. Accent: American (Gen)."
    audio_profile = "A smooth, premium commercial voice."
    
    try:
        print("  Attempting to generate speech...")
        output_files = generate_speech(
            transcript=transcript,
            voice_name="Orus",
            audio_profile=audio_profile,
            directors_note=directors_note,
            api_key=api_key,
            output_dir="./test_output",
            auto_extract_description=True,
        )
        print(f"  ✓ Generated {len(output_files)} file(s)")
        for file_path in output_files:
            if Path(file_path).exists():
                size = Path(file_path).stat().st_size / 1024
                print(f"    - {file_path} ({size:.1f} KB)")
    except Exception as e:
        print(f"  ✗ Generation failed: {e}")


def main():
    print("=" * 60)
    print("TTS Agent - Local Test Suite")
    print("=" * 60)
    
    # Run tests
    test_parse_directors_note()
    test_extract_description()
    test_full_generation()
    
    print("\n" + "=" * 60)
    print("Test suite complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Verify all tests passed ✓")
    print("2. Commit and push to GitHub")
    print("3. Set GEMINI_API_KEY secret in GitHub repo")
    print("4. Trigger 'Generate Speech' workflow from Actions tab")


if __name__ == "__main__":
    main()
