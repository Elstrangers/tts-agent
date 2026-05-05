#!/usr/bin/env python3
"""
Examples: TTS Agent with Custom Parameters

Demonstrates how to use custom values for:
- voice_name
- audio_profile
- style
- pace
- accent
- description
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tts_generator import generate_speech


def example_1_custom_commercial():
    """Example 1: Custom commercial voice"""
    print("\n" + "="*70)
    print("Example 1: Custom Commercial Voice")
    print("="*70)
    
    generate_speech(
        transcript="Discover the luxury that moves you. Premium craftsmanship meets innovation.",
        voice_name="Pax",  # Custom voice: deep and authoritative
        audio_profile="A sophisticated, luxury brand voice with premium tone.",  # Custom profile
        style="Promo/Hype",
        pace="Natural",
        accent="British",  # Custom accent
        description="luxury-commercial",
        output_dir="./examples/custom_commercial",
    )


def example_2_educational_custom():
    """Example 2: Custom educational content"""
    print("\n" + "="*70)
    print("Example 2: Custom Educational Content")
    print("="*70)
    
    generate_speech(
        transcript="[intro] Machine learning is transforming technology. [main] Neural networks mimic human brain functions. [conclusion] Understanding AI is essential for future careers.",
        voice_name="Sage",  # Professional voice
        audio_profile="A clear, engaging educational voice for complex topics.",  # Custom
        style="Informative",  # Custom style
        pace="Slow",  # Custom pace: slower for learning
        accent="American (Gen)",
        description="ml-fundamentals",
        output_dir="./examples/educational",
        auto_extract_description=True,
    )


def example_3_documentary_custom():
    """Example 3: Custom documentary voice"""
    print("\n" + "="*70)
    print("Example 3: Custom Documentary Voice")
    print("="*70)
    
    generate_speech(
        transcript="[scene] The Arctic tundra stretches endlessly. [discovery] Beneath the ice lies ancient history. [mystery] What secrets does this frozen world hold?",
        voice_name="Pax",  # Deep, warm voice for documentary
        audio_profile="A compelling documentary voice that tells stories of nature and science.",  # Custom
        style="Informative",  # Custom: informative but engaging
        pace="Natural",
        accent="British",  # Custom: British accent for BBC-style documentary
        description="arctic-documentary",
        output_dir="./examples/documentary",
        auto_extract_description=True,
    )


def example_4_friendly_custom():
    """Example 4: Custom friendly/casual voice"""
    print("\n" + "="*70)
    print("Example 4: Custom Friendly Voice")
    print("="*70)
    
    generate_speech(
        transcript="[greeting] Hey there! [main] Let's chat about your favorite movies. [invitation] Share your thoughts in the comments below!",
        voice_name="Orus",  # Soft, friendly voice
        audio_profile="A warm, conversational voice that feels like talking to a friend.",  # Custom
        style="Conversational",  # Custom: casual and friendly
        pace="Natural",
        accent="American (Gen)",
        description="friendly-chat",
        output_dir="./examples/friendly",
        auto_extract_description=True,
    )


def example_5_custom_all_parameters():
    """Example 5: All custom parameters"""
    print("\n" + "="*70)
    print("Example 5: Custom Everything!")
    print("="*70)
    
    # Create a completely custom scenario
    custom_transcript = """[excitement] Introducing our revolutionary new product!
[benefit1] It's faster than ever before.
[benefit2] It's easier to use.
[benefit3] It's more affordable.
[call-to-action] Get yours today!"""
    
    custom_voice = "Achernar"  # Using a different voice
    custom_profile = "A sleek, modern voice perfect for tech product launches."  # Your custom profile
    custom_style = "Energetic"  # Custom high-energy style
    custom_pace = "Fast"  # Custom: fast paced for excitement
    custom_accent = "American (Gen)"
    custom_description = "product-launch-promo"
    
    print(f"\nCustom Parameters:")
    print(f"  Voice: {custom_voice}")
    print(f"  Profile: {custom_profile}")
    print(f"  Style: {custom_style}")
    print(f"  Pace: {custom_pace}")
    print(f"  Accent: {custom_accent}")
    
    try:
        generate_speech(
            transcript=custom_transcript,
            voice_name=custom_voice,
            audio_profile=custom_profile,
            style=custom_style,
            pace=custom_pace,
            accent=custom_accent,
            description=custom_description,
            output_dir="./examples/custom_product_launch",
            auto_extract_description=True,
        )
    except Exception as e:
        print(f"Note: {e}")
        print("Make sure GEMINI_API_KEY is set to generate audio.")


def main():
    print("\n" + "="*70)
    print("TTS Agent - Custom Parameter Examples")
    print("="*70)
    print("\nThis script demonstrates how to use CUSTOM values for:")
    print("  ✓ voice_name (not limited to Orus, Achernar, Pax, Sage)")
    print("  ✓ audio_profile (any custom description)")
    print("  ✓ style (any style, not just predefined)")
    print("  ✓ pace (any pace description)")
    print("  ✓ accent (any accent)")
    print("  ✓ description (any filename description)")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("\n⚠️  GEMINI_API_KEY not set.")
        print("These examples show STRUCTURE - they won't generate audio without the key.")
        print("Set it with: $env:GEMINI_API_KEY='your-key-here'")
    else:
        print("\n✓ API key found. Examples will generate audio.")
    
    print("\n" + "="*70)
    print("Example 1: Custom Commercial")
    print("="*70)
    print("  Voice: Pax (deep, authoritative)")
    print("  Profile: 'A sophisticated, luxury brand voice'")
    print("  Style: Promo/Hype")
    print("  Accent: British")
    
    print("\n" + "="*70)
    print("Example 2: Custom Educational")
    print("="*70)
    print("  Voice: Sage (professional)")
    print("  Profile: 'Clear, engaging educational voice'")
    print("  Style: Informative")
    print("  Pace: Slow")
    
    print("\n" + "="*70)
    print("Example 3: Custom Documentary")
    print("="*70)
    print("  Voice: Pax (deep, warm)")
    print("  Profile: 'Documentary voice for nature/science'")
    print("  Style: Informative")
    print("  Accent: British")
    
    print("\n" + "="*70)
    print("Example 4: Custom Friendly")
    print("="*70)
    print("  Voice: Orus (soft, friendly)")
    print("  Profile: 'Warm, conversational like a friend'")
    print("  Style: Conversational")
    print("  Pace: Natural")
    
    print("\n" + "="*70)
    print("Example 5: Custom Everything!")
    print("="*70)
    print("  Voice: Achernar (custom selection)")
    print("  Profile: 'Modern voice for tech launches'")
    print("  Style: Energetic")
    print("  Pace: Fast")
    
    print("\n" + "="*70)
    print("\nKey Points:")
    print("  ✓ ALL parameters accept CUSTOM values")
    print("  ✓ Defaults are provided but easily overridden")
    print("  ✓ No restriction to predefined lists")
    print("  ✓ Works with CLI, Python scripts, and GitHub Actions")
    print("\n" + "="*70)
    
    # Try to generate if API key is set
    if api_key:
        print("\nGenerating examples... (check ./examples/ folder)")
        try:
            example_1_custom_commercial()
            example_2_educational_custom()
            example_3_documentary_custom()
            example_4_friendly_custom()
            example_5_custom_all_parameters()
            print("\n✅ All examples completed!")
        except Exception as e:
            print(f"\n⚠️  Generation stopped: {e}")
    else:
        print("\nTo run these examples with audio generation:")
        print("1. Set your API key: $env:GEMINI_API_KEY='your-key-here'")
        print("2. Run: python examples_custom_parameters.py")


if __name__ == "__main__":
    main()
