#!/usr/bin/env python3
"""
Example: Aetheris Sedan Commercial
Based on the official Google AI Studio SDK code.

This demonstrates how to use the TTS Agent with:
- Description from bracketed text: [intrigue], [desire], [information], [inspiration], [confident]
- Audio profile: A smooth, premium commercial voice.
- Director's note: Style: Promo/Hype. Pace: Natural. Accent: American (Gen).
- Voice: Orus
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import tts_generator
sys.path.insert(0, str(Path(__file__).parent))

from tts_generator import generate_speech


def example_aetheris_commercial():
    """Generate the Aetheris Sedan commercial from the original SDK code."""
    
    # This is the exact transcript from the original Google AI Studio code
    transcript = """[intrigue] You don't just want a car. [desire] You want a sanctuary. 
[information] Introducing the all-new Aetheris Sedan. With whisper-quiet cabin technology and an interior designed around you. 
[inspiration] It's not just about getting to your destination. [confident] It's about arriving inspired. 
Aetheris. Move beautifully."""
    
    # Original settings from the SDK code
    audio_profile = "A smooth, premium commercial voice."
    directors_note = "Style: Promo/Hype. Pace: Natural. Accent: American (Gen)."
    voice_name = "Orus"
    
    print("=" * 70)
    print("TTS Agent - Aetheris Sedan Commercial Example")
    print("=" * 70)
    print("\n📝 Transcript:")
    print(f"   {transcript[:60]}...")
    print("\n🎤 Settings:")
    print(f"   Voice: {voice_name}")
    print(f"   Audio Profile: {audio_profile}")
    print(f"   Director's Note: {directors_note}")
    print("\n✨ What the agent will do:")
    print("   1. Auto-extract descriptions: intrigue, desire, information, inspiration, confident")
    print("   2. Parse director's note: Style=Promo/Hype, Pace=Natural, Accent=American (Gen)")
    print("   3. Use audio profile to guide voice generation")
    print("   4. Generate audio with voice: Orus")
    print("   5. Save as: intrigue_desire_information_inspiration_confident_0.wav")
    print("\n" + "=" * 70)
    
    # Check for API key
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("\n❌ ERROR: GEMINI_API_KEY environment variable not set!")
        print("\nSet it with one of these methods:")
        print("  Windows PowerShell: $env:GEMINI_API_KEY='AIzaSyAKxY-HRH7zqq29-GYTEbyuLVLq9g3MiSY'")
        print("  Windows CMD:        set GEMINI_API_KEY=AIzaSyAKxY-HRH7zqq29-GYTEbyuLVLq9g3MiSY")
        print("  macOS/Linux:        export GEMINI_API_KEY='AIzaSyAKxY-HRH7zqq29-GYTEbyuLVLq9g3MiSY'")
        return
    
    print("\n✓ API key found. Starting generation...\n")
    
    try:
        # Generate speech using the agent
        output_files = generate_speech(
            transcript=transcript,
            voice_name=voice_name,
            audio_profile=audio_profile,
            directors_note=directors_note,
            api_key=api_key,
            output_dir="./aetheris_output",
            auto_extract_description=True,
        )
        
        print("\n" + "=" * 70)
        print("✅ SUCCESS!")
        print("=" * 70)
        print("\nGenerated files:")
        for file_path in output_files:
            file_size = Path(file_path).stat().st_size / 1024
            print(f"  ✓ {file_path} ({file_size:.1f} KB)")
        print("\n" + "=" * 70)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(example_aetheris_commercial())
