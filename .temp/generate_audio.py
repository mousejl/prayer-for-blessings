#!/usr/bin/env python3
"""
Generate chanting audio for the Zen Blessing app.
Uses macOS 'say' TTS + Python post-processing to create
temple-style chanting audio with reverb and resonance.

3 tracks:
1. Heart Sutra (心经) - slow, meditative
2. Great Compassion Mantra (大悲咒) - medium tempo  
3. Six-Syllable Mantra (六字大明咒) - repetitive, rhythmic

Output: WAV files in audio/ directory
"""

import os
import wave
import struct
import math
import subprocess
import tempfile
import array

SAMPLE_RATE = 22050
AUDIO_DIR = os.path.dirname(os.path.abspath(__file__))

# === Chanting texts (split into phrases for natural rhythm) ===

HEART_SUTRA = [
    "观自在菩萨",
    "行深般若波罗蜜多时",
    "照见五蕴皆空",
    "度一切苦厄",
    "舍利子",
    "色不异空",
    "空不异色",
    "色即是空",
    "空即是色",
    "受想行识",
    "亦复如是",
    "舍利子",
    "是诸法空相",
    "不生不灭",
    "不垢不净",
    "不增不减",
    "是故空中无色",
    "无受想行识",
    "无眼耳鼻舌身意",
    "无色声香味触法",
    "无眼界",
    "乃至无意识界",
    "无无明",
    "亦无无明尽",
    "乃至无老死",
    "亦无老死尽",
    "无苦集灭道",
    "无智亦无得",
    "以无所得故",
    "菩提萨埵",
    "依般若波罗蜜多故",
    "心无罣碍",
    "无罣碍故",
    "无有恐怖",
    "远离颠倒梦想",
    "究竟涅槃",
    "三世诸佛",
    "依般若波罗蜜多故",
    "得阿耨多罗三藐三菩提",
    "故知般若波罗蜜多",
    "是大神咒",
    "是大明咒",
    "是无上咒",
    "是无等等咒",
    "能除一切苦",
    "真实不虚",
    "故说般若波罗蜜多咒",
    "即说咒曰",
    "揭谛揭谛",
    "波罗揭谛",
    "波罗僧揭谛",
    "菩提萨婆诃",
]

COMPASSION_MANTRA = [
    "南无大悲观世音菩萨",
    "南无大悲观世音菩萨",
    "千手千眼无量大悲心",
    "宣化上人",
    "大悲咒",
    "南无喝啰怛那",
    "哆啰夜耶",
    "南无阿唎耶",
    "婆卢羯帝",
    "烁钵啰耶",
    "菩提萨埵婆耶",
    "摩诃萨埵婆耶",
    "摩诃迦卢尼迦耶",
    "唵",
    "萨皤啰罚曳",
    "数怛那怛写",
    "南无悉吉栗埵",
    "伊蒙阿唎耶",
    "婆卢吉帝",
    "室佛啰愣驮婆",
    "南无那啰谨墀",
    "醯利摩诃",
    "皤哆沙咩",
    "萨婆阿他",
    "豆输朋",
    "阿逝孕",
    "萨婆萨哆",
    "那摩婆萨哆",
    "那摩婆伽",
    "摩罚特豆",
    "怛侄他",
    "唵",
    "阿婆卢醯",
    "卢迦帝",
    "迦罗帝",
    "夷醯唎",
    "摩诃菩提萨埵",
    "悉陀耶",
    "堕婆迦",
    "摩罚特豆",
    "娑婆诃",
]

SIX_SYLLABLE_MANTRA = [
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
    "嗡嘛呢呗咪吽",
]


def generate_tts_wav(text, voice="Grandpa (中文（中国大陆）)", rate=120, out_path=None):
    """Generate a single TTS WAV file using macOS 'say' command."""
    if out_path is None:
        fd, out_path = tempfile.mkstemp(suffix='.aiff')
        os.close(fd)
    
    # Generate AIFF with say
    subprocess.run(
        ['say', '-v', voice, '-r', str(rate), '-o', out_path, text],
        check=True, capture_output=True
    )
    
    # Convert to WAV
    wav_path = out_path.replace('.aiff', '.wav') if out_path.endswith('.aiff') else out_path + '.wav'
    subprocess.run(
        ['afconvert', out_path, wav_path, '-f', 'WAVE', '-d', f'LEI16@{SAMPLE_RATE}'],
        check=True, capture_output=True
    )
    
    # Clean up AIFF
    if out_path.endswith('.aiff') and os.path.exists(out_path):
        os.unlink(out_path)
    
    return wav_path


def read_wav(path):
    """Read WAV file and return samples as float list."""
    with wave.open(path, 'r') as w:
        n = w.getnframes()
        raw = w.readframes(n)
        samples = array.array('h')
        samples.frombytes(raw)
        return list(samples), w.getframerate(), w.getnchannels()


def write_wav(path, samples, sample_rate=SAMPLE_RATE, channels=1):
    """Write samples (int16 values) to WAV file."""
    data = array.array('h')
    for s in samples:
        # Clamp to int16 range
        data.append(max(-32767, min(32767, int(s))))
    
    with wave.open(path, 'w') as w:
        w.setnchannels(channels)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        w.writeframes(data.tobytes())


def add_reverb(samples, decay=0.3, delay_ms=80, wet=0.25):
    """Add simple reverb effect (multiple echo taps)."""
    delay_samples = int(SAMPLE_RATE * delay_ms / 1000)
    output = list(samples)
    
    for tap in range(1, 5):
        gain = wet * (decay ** tap)
        offset = delay_samples * tap
        for i in range(len(output)):
            if i + offset < len(samples):
                output[i + offset] += int(samples[i] * gain)
    
    return output


def add_low_boost(samples, boost_db=6):
    """Simple low-frequency emphasis by averaging adjacent samples (crude low-pass + boost)."""
    output = list(samples)
    # Simple 3-sample moving average for low-freq emphasis
    smoothed = []
    for i in range(len(output)):
        s = output[i]
        if i > 0:
            s += output[i-1]
        if i < len(output) - 1:
            s += output[i+1]
        smoothed.append(s // 3)
    
    # Mix original with boosted low-freq
    boost = 10 ** (boost_db / 20)
    for i in range(len(output)):
        output[i] = int(output[i] * 0.7 + smoothed[i] * boost * 0.3)
    
    return output


def add_om_drone(duration_sec, sample_rate=SAMPLE_RATE, freq=65, vol=0.15):
    """Generate Om drone as background layer."""
    n = int(duration_sec * sample_rate)
    samples = []
    for i in range(n):
        t = i / sample_rate
        # Fundamental
        s = math.sin(2 * math.pi * freq * t) * vol
        # Fifth
        s += math.sin(2 * math.pi * freq * 1.5 * t) * vol * 0.4
        # Slow LFO modulation
        lfo = 1.0 + 0.02 * math.sin(2 * math.pi * 0.07 * t)
        s *= lfo
        # Fade in/out
        fade = min(i / (sample_rate * 0.5), 1.0)
        if i > n - sample_rate:
            fade = min(fade, (n - i) / sample_rate)
        samples.append(int(s * fade * 32767))
    return samples


def add_wood_fish_hits(samples, interval_sec=2.5, vol=0.12):
    """Add wood fish (percussion) hits at regular intervals."""
    output = list(samples)
    interval_samples = int(SAMPLE_RATE * interval_sec)
    hit_dur = int(SAMPLE_RATE * 0.04)  # 40ms
    
    pos = int(SAMPLE_RATE * 1.0)  # Start after 1 second
    while pos < len(output) - hit_dur:
        for i in range(hit_dur):
            # Decaying square wave at ~800Hz
            t = i / SAMPLE_RATE
            decay = math.exp(-t * 50)
            hit = int(32767 * vol * decay * (1 if math.sin(2 * math.pi * 800 * t) > 0 else -1))
            output[pos + i] = max(-32767, min(32767, output[pos + i] + hit))
        pos += interval_samples + int(SAMPLE_RATE * (0.3 * (pos % 3 / 3.0)))  # Slight variation
    
    return output


def mix_tracks(track1, track2, vol1=0.8, vol2=0.2):
    """Mix two audio tracks."""
    length = max(len(track1), len(track2))
    output = []
    for i in range(length):
        s1 = track1[i] * vol1 if i < len(track1) else 0
        s2 = track2[i] * vol2 if i < len(track2) else 0
        output.append(int(s1 + s2))
    return output


def generate_track(phrases, voice, rate, output_name, 
                   reverb_decay=0.3, reverb_delay=80,
                   om_vol=0.12, wood_fish_interval=2.5,
                   pause_between=0.8):
    """Generate a complete track from phrases."""
    print(f"Generating {output_name}...")
    
    all_samples = []
    silence_gap = int(SAMPLE_RATE * pause_between)
    
    for i, phrase in enumerate(phrases):
        print(f"  Phrase {i+1}/{len(phrases)}: {phrase[:20]}...")
        
        # Generate TTS for this phrase
        wav_path = generate_tts_wav(phrase, voice=voice, rate=rate)
        
        try:
            samples, sr, ch = read_wav(wav_path)
        except Exception as e:
            print(f"  Warning: failed to read {wav_path}: {e}")
            continue
        
        # Add reverb to phrase
        samples = add_reverb(samples, decay=reverb_decay, delay_ms=reverb_delay, wet=0.3)
        
        # Add to output
        all_samples.extend(samples)
        all_samples.extend([0] * silence_gap)  # Pause between phrases
        
        # Clean up temp file
        os.unlink(wav_path)
    
    if not all_samples:
        print(f"  No samples generated for {output_name}!")
        return None
    
    # Add Om drone
    duration = len(all_samples) / SAMPLE_RATE
    print(f"  Adding Om drone ({duration:.1f}s)...")
    drone = add_om_drone(duration, vol=om_vol)
    
    # Mix voice + drone
    print("  Mixing tracks...")
    mixed = mix_tracks(all_samples, drone, vol1=0.85, vol2=0.2)
    
    # Add wood fish
    print("  Adding wood fish hits...")
    mixed = add_wood_fish_hits(mixed, interval_sec=wood_fish_interval, vol=0.1)
    
    # Low-freq boost
    print("  Applying low-frequency boost...")
    mixed = add_low_boost(mixed, boost_db=4)
    
    # Final reverb pass
    print("  Final reverb pass...")
    mixed = add_reverb(mixed, decay=0.4, delay_ms=120, wet=0.15)
    
    # Write output
    out_path = os.path.join(AUDIO_DIR, output_name)
    print(f"  Writing {out_path}...")
    write_wav(out_path, mixed)
    print(f"  Done! Size: {os.path.getsize(out_path)/1024:.0f}KB")
    
    return out_path


def main():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    
    # Track 1: Heart Sutra - slow, meditative
    generate_track(
        HEART_SUTRA,
        voice="Grandpa (中文（中国大陆）)",
        rate=100,  # Slow pace
        output_name="heart_sutra.wav",
        reverb_decay=0.4,
        reverb_delay=100,
        om_vol=0.12,
        wood_fish_interval=3.0,
        pause_between=1.2
    )
    
    # Track 2: Great Compassion Mantra - medium tempo
    generate_track(
        COMPASSION_MANTRA,
        voice="Grandpa (中文（中国大陆）)",
        rate=130,  # Medium pace
        output_name="compassion_mantra.wav",
        reverb_decay=0.3,
        reverb_delay=80,
        om_vol=0.10,
        wood_fish_interval=2.0,
        pause_between=0.6
    )
    
    # Track 3: Six-Syllable Mantra - repetitive, rhythmic
    generate_track(
        SIX_SYLLABLE_MANTRA,
        voice="Grandpa (中文（中国大陆）)",
        rate=90,  # Slow and deliberate
        output_name="six_syllable_mantra.wav",
        reverb_decay=0.5,
        reverb_delay=150,
        om_vol=0.15,
        wood_fish_interval=1.8,
        pause_between=0.4
    )
    
    print("\nAll tracks generated!")
    
    # Clean up test file
    test_files = [os.path.join(AUDIO_DIR, f) for f in ['test.aiff', 'test.wav', 'test.m4a', 'test.caf']]
    for f in test_files:
        if os.path.exists(f):
            os.unlink(f)


if __name__ == '__main__':
    main()
