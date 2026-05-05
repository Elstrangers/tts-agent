#!/usr/bin/env python3
"""
Google AI Studio Text-to-Speech Agent
Generates speech from text with customizable voice settings and audio profiles.
Uses Gemini 3.1 Flash TTS model with director's notes parsing.
"""

import argparse
import json
import mimetypes
import os
import re
import struct
import sys
from pathlib import Path
from google import genai
from google.genai import types


def save_binary_file(file_path, data):
    """Save binary audio data to file."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, "wb") as f:
        f.write(data)
    print(f"✓ Audio file saved: {file_path}")
    return str(file_path)


def parse_directors_note(directors_note: str) -> dict:
    """Extract style, pace, and accent from director's note text.
    
    Expected format:
    Style: Promo/Hype. Pace: Natural. Accent: American (Gen).
    """
    parsed = {
        "style": "Natural",
        "pace": "Natural",
        "accent": "American (Gen)"
    }
    
    if not directors_note:
        return parsed
    
    # Extract Style
    style_match = re.search(r'Style:\s*([^.]+?)(?:\.|,|$)', directors_note, re.IGNORECASE)
    if style_match:
        parsed["style"] = style_match.group(1).strip()
    
    # Extract Pace
    pace_match = re.search(r'Pace:\s*([^.]+?)(?:\.|,|$)', directors_note, re.IGNORECASE)
    if pace_match:
        parsed["pace"] = pace_match.group(1).strip()
    
    # Extract Accent
    accent_match = re.search(r'Accent:\s*([^.]+?)(?:\.|,|$)', directors_note, re.IGNORECASE)
    if accent_match:
        parsed["accent"] = accent_match.group(1).strip()
    
    return parsed


def extract_description_from_transcript(transcript: str) -> str:
    """Extract bracketed descriptions from transcript.
    
    Example: [intrigue] You don't just want a car. -> extracts 'intrigue'
    Returns comma-separated list of all bracketed descriptions.
    """
    descriptions = re.findall(r'\[([^\]]+)\]', transcript)
    if descriptions:
        return ", ".join(descriptions)
    return "narration"


def parse_audio_mime_type(mime_type: str) -> dict:
    """Parse MIME type to extract audio parameters."""
    parameters = {}
    if "audio/mpeg" in mime_type:
        parameters["bits_per_sample"] = 16
        parameters["rate"] = 24000
    elif "audio/wav" in mime_type:
        parameters["bits_per_sample"] = 16
        parameters["rate"] = 24000
    else:
        parameters["bits_per_sample"] = 16
        parameters["rate"] = 24000
    return parameters


def convert_to_wav(audio_data: bytes, mime_type: str) -> bytes:
    """Convert audio data to WAV format with proper header."""
    parameters = parse_audio_mime_type(mime_type)
    bits_per_sample = parameters["bits_per_sample"]
    sample_rate = parameters["rate"]
    num_channels = 1
    data_size = len(audio_data)
    
    byte_rate = sample_rate * num_channels * bits_per_sample // 8
    block_align = num_channels * bits_per_sample // 8
    
    # WAV header
    wav_header = struct.pack(
        '<4sI4s4sIHHIIHH4sI',
        b'RIFF',
        36 + data_size,
        b'WAVE',
        b'fmt ',
        16,
        1,
        num_channels,
        sample_rate,
        byte_rate,
        block_align,
        bits_per_sample,
        b'data',
        data_size,
    )
    
    return wav_header + audio_data


def build_transcript_with_directors_note(transcript, audio_profile, directors_note="", style="Natural", pace="Natural", accent="American (Gen)"):
    """Build formatted transcript with audio profile and director's note.
    
    If directors_note is provided, parse it for style/pace/accent.
    Otherwise use the provided parameters.
    """
    
    # Parse directors_note if provided
    if directors_note:
        parsed = parse_directors_note(directors_note)
        style = parsed.get("style", style)
        pace = parsed.get("pace", pace)
        accent = parsed.get("accent", accent)
    
    # Build the prompt in SDK format
    prompt = f"""Read the following transcript based on the audio profile and director's note.

# Audio Profile
{audio_profile}

# Director's note
Style: {style}. Pace: {pace}. Accent: {accent}.

## Transcript:
{transcript}"""
    return prompt


def generate_speech(
    transcript,
    voice_name="Orus",
    audio_profile="A smooth, premium commercial voice.",
    directors_note="",
    style="Natural",
    pace="Natural",
    accent="American (Gen)",
    api_key=None,
    output_dir="./output",
    description="",
    auto_extract_description=True,
):
    """Generate speech using Google AI Studio Text-to-Speech API.
    
    Args:
        transcript: Text transcript to convert to speech (can include [descriptions])
        voice_name: Prebuilt voice name (Orus, Achernar, Pax, Sage)
        audio_profile: Audio profile description
        directors_note: Director's note (will parse for Style, Pace, Accent)
        style: Voice style (overridden if in directors_note)
        pace: Speech pace (overridden if in directors_note)
        accent: Accent type (overridden if in directors_note)
        api_key: Google API key
        output_dir: Output directory for audio files
        description: Output filename description
        auto_extract_description: Auto-extract descriptions from bracketed text in transcript
    """
    
    # Initialize client
    if api_key is None:
        api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("API key not provided. Set GEMINI_API_KEY environment variable or pass api_key parameter.")
    
    client = genai.Client(api_key=api_key)
    model = "gemini-3.1-flash-tts-preview"
    
    # Auto-extract description from bracketed text if not provided
    if not description and auto_extract_description:
        description = extract_description_from_transcript(transcript)
    
    # Parse director's note to extract parameters
    if directors_note:
        parsed = parse_directors_note(directors_note)
        style = parsed.get("style", style)
        pace = parsed.get("pace", pace)
        accent = parsed.get("accent", accent)
    
    # Build transcript with directors note
    formatted_transcript = build_transcript_with_directors_note(
        transcript, audio_profile, directors_note, style, pace, accent
    )
    
    print(f"\n🎙️  Generating speech with:")
    print(f"   Voice: {voice_name}")
    print(f"   Audio Profile: {audio_profile}")
    print(f"   Style: {style} | Pace: {pace} | Accent: {accent}")
    print(f"   Description: {description}")
    if directors_note:
        print(f"   Director's Note: {directors_note[:100]}...")
    
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=formatted_transcript),
            ],
        ),
    ]
    
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        response_modalities=["audio"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name=voice_name
                )
            )
        ),
    )
    
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Generate and save audio
    file_index = 0
    output_files = []
    
    try:
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if chunk.parts is None:
                continue
            
            if chunk.parts[0].inline_data and chunk.parts[0].inline_data.data:
                inline_data = chunk.parts[0].inline_data
                data_buffer = inline_data.data
                file_extension = mimetypes.guess_extension(inline_data.mime_type)
                
                if file_extension is None:
                    file_extension = ".wav"
                    data_buffer = convert_to_wav(inline_data.data, inline_data.mime_type)
                
                # Create filename with description if provided
                file_name = f"{description or 'speech'}_{file_index}" if description else f"speech_{file_index}"
                file_path = os.path.join(output_dir, f"{file_name}{file_extension}")
                
                output_file = save_binary_file(file_path, data_buffer)
                output_files.append(output_file)
                file_index += 1
            else:
                if text := chunk.text:
                    print(f"Response: {text}")
        
        print(f"\n✓ Successfully generated {len(output_files)} audio file(s)")
        return output_files
        
    except Exception as e:
        print(f"✗ Error generating speech: {e}", file=sys.stderr)
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Generate speech using Google AI Studio Text-to-Speech (Gemini 3.1 Flash)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Simple usage
  python tts_generator.py "You don't just want a car. You want a sanctuary."
  
  # With custom voice and audio profile
  python tts_generator.py "[intrigue] You don't just want a car. [desire] You want a sanctuary." \\
    --voice Orus \\
    --audio-profile "A smooth, premium commercial voice." \\
    --directors-note "Style: Promo/Hype. Pace: Natural. Accent: American (Gen)."
  
  # With parameters separately (overrides director's note)
  python tts_generator.py "Your transcript here" \\
    --voice Pax \\
    --style "Informative" \\
    --pace "Slow" \\
    --accent "British"
        """
    )
    
    parser.add_argument("transcript", help="Text transcript to convert to speech (can include [descriptions])")
    parser.add_argument("--voice", default="Orus", 
                       help="Voice name: Orus, Achernar, Pax, Sage (default: Orus)")
    parser.add_argument("--audio-profile", default="A smooth, premium commercial voice.", 
                       help="Audio profile description")
    parser.add_argument("--directors-note", default="", 
                       help="Director's note (format: 'Style: X. Pace: Y. Accent: Z.')")
    parser.add_argument("--style", default="Natural", 
                       help="Voice style: Natural, Promo/Hype, Calm, Energetic, Informative, Dramatic, Conversational")
    parser.add_argument("--pace", default="Natural", 
                       help="Speech pace: Slow, Natural, Fast")
    parser.add_argument("--accent", default="American (Gen)", 
                       help="Accent: American (Gen), American (Southern), British, Canadian, Indian, Australian")
    parser.add_argument("--api-key", 
                       help="Google API key (or use GEMINI_API_KEY environment variable)")
    parser.add_argument("--output-dir", default="./output", 
                       help="Output directory for audio files (default: ./output)")
    parser.add_argument("--description", default="", 
                       help="Output filename description (auto-extracted from [brackets] if not provided)")
    parser.add_argument("--no-auto-extract", action="store_true",
                       help="Disable auto-extraction of description from bracketed text")
    
    args = parser.parse_args()
    
    try:
        output_files = generate_speech(
            transcript=args.transcript,
            voice_name=args.voice,
            audio_profile=args.audio_profile,
            directors_note=args.directors_note,
            style=args.style,
            pace=args.pace,
            accent=args.accent,
            api_key=args.api_key,
            output_dir=args.output_dir,
            description=args.description,
            auto_extract_description=not args.no_auto_extract,
        )
        
        print("\n📁 Output files:")
        for file_path in output_files:
            print(f"   - {file_path}")
        
        return 0
    
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
