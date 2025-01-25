from scipy.io.wavfile import read, write
from IPython.display import Audio

# 오디오 파일 불러오고 오디오 데이터를 정규화하는 함수 생성
def load_audio(filename):
    rate, data = read(filename)
    return rate, data / 32768.0 if data.dtype == np.int16 else data  # Normalize if needed

# 파일 미리 로드
audio_files = {name: load_audio(name) for name in [
    "cymbal.wav", "kick.wav", "closed_hihat.wav", "snare.wav", "open_hihat.wav"
]}

## Drum Pattern A to X
# Drum pattern A (1st bar)
drum_patternA = [
    {"time": 0.0, "sounds": ["cymbal.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["closed_hihat.wav"]},
]

# Drum pattern B (2nd bar)
drum_patternB = [
    {"time": 0.0, "sounds": ["cymbal.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.6, "sounds": ["closed_hihat.wav"]},
    {"time": 1.75, "sounds": ["open_hihat.wav"]},
]

# Drum pattern C (3rd bar)
drum_patternC = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["cymbal.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["closed_hihat.wav"]},
]

# Drum pattern D (4th bar)
drum_patternD = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.1, "sounds": ["closed_hihat.wav"]},
    {"time": 1.25, "sounds": ["snare.wav"]},
    {"time": 1.5, "sounds": ["snare.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]

# Drum pattern E (5th bar)
drum_patternE = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.5, "sounds": ["cymbal.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["closed_hihat.wav"]},
]

# Drum pattern F (8th bar)
drum_patternF = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.1, "sounds": ["closed_hihat.wav"]},
    {"time": 0.25, "sounds": ["snare.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.6, "sounds": ["snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.35, "sounds": ["snare.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]

# Drum pattern G (10th bar)
drum_patternG = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["closed_hihat.wav"]},
]

# Drum pattern H (12th bar)
drum_patternH = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.1, "sounds": ["closed_hihat.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.6, "sounds": ["closed_hihat.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.1, "sounds": ["closed_hihat.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav"]},
    {"time": 1.6, "sounds": ["snare.wav"]},
]

# Drum pattern I (13th bar)
drum_patternI = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["closed_hihat.wav"]},
]

# Drum pattern J (16th bar)
drum_patternJ = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.5, "sounds": ["snare.wav"]},
    {"time": 0.6, "sounds": ["snare.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 1.1, "sounds": ["closed_hihat.wav"]},
    {"time": 1.25, "sounds": ["snare.wav"]},
    {"time": 1.5, "sounds": ["snare.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]

# Drum pattern K (18th bar)
drum_patternK = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.1, "sounds": ["closed_hihat.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.6, "sounds": ["closed_hihat.wav"]},
    {"time": 1.75, "sounds": ["open_hihat.wav"]},
]

# Drum pattern L (19th bar)
drum_patternL = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.85, "sounds": ["closed_hihat.wav"]},
]

# Drum pattern M (20th bar)
drum_patternM = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 0.85, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.85, "sounds": ["closed_hihat.wav"]},
]

# Drum pattern N (24th bar)
drum_patternN = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.5, "sounds": ["snare.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]

# Drum pattern O (26th bar)
drum_patternO = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.1, "sounds": ["closed_hihat.wav"]},
    {"time": 0.25, "sounds": ["snare.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.6, "sounds": ["snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 1.1, "sounds": ["closed_hihat.wav"]},
    {"time": 1.25, "sounds": ["snare.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]

# Drum pattern P (28th bar)
drum_patternP = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.1, "sounds": ["closed_hihat.wav"]},
    {"time": 0.25, "sounds": ["snare.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.6, "sounds": ["snare.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.35, "sounds": ["snare.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]

# Drum pattern Q (33th bar)
drum_patternQ = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.5, "sounds": ["cymbal.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["closed_hihat.wav"]},
]

# Drum pattern R (48th bar)
drum_patternR = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.1, "sounds": ["closed_hihat.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 0.6, "sounds": ["closed_hihat.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.35, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 1.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.85, "sounds": ["closed_hihat.wav"]},
]

# Drum pattern S (52th bar)
drum_patternS = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 0.85, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]

# Drum pattern T (56th bar)
drum_patternT = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.5, "sounds": ["snare.wav"]},
    {"time": 0.6, "sounds": ["snare.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.35, "sounds": ["snare.wav"]},
    {"time": 1.5, "sounds": ["snare.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]

# Drum pattern U (60th bar)
drum_patternU = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.1, "sounds": ["closed_hihat.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]

# Drum pattern V (68th bar)
drum_patternV = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.1, "sounds": ["closed_hihat.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.6, "sounds": ["closed_hihat.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.1, "sounds": ["closed_hihat.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav"]},
    {"time": 1.6, "sounds": ["snare.wav"]},
]

# Drum pattern W (72th bar)
drum_patternW = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["snare.wav"]},
    {"time": 0.6, "sounds": ["snare.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "snare.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.35, "sounds": ["snare.wav"]},
    {"time": 1.5, "sounds": ["snare.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]

# Drum pattern X (80th bar)
drum_patternX = [
    {"time": 0.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 0.25, "sounds": ["closed_hihat.wav"]},
    {"time": 0.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 0.75, "sounds": ["closed_hihat.wav"]},
    {"time": 1.0, "sounds": ["closed_hihat.wav", "kick.wav"]},
    {"time": 1.25, "sounds": ["closed_hihat.wav"]},
    {"time": 1.5, "sounds": ["closed_hihat.wav", "snare.wav"]},
    {"time": 1.75, "sounds": ["snare.wav"]},
    {"time": 1.85, "sounds": ["snare.wav"]},
]


# 곡에 나오는 모든 드럼 패턴 리스트
all_patterns = [drum_patternA, drum_patternB, drum_patternC, drum_patternD,
                drum_patternE, drum_patternF, drum_patternG, drum_patternH,
                drum_patternI, drum_patternJ, drum_patternK, drum_patternL,
                drum_patternM, drum_patternN, drum_patternO, drum_patternP,
                drum_patternQ, drum_patternR, drum_patternS, drum_patternT,
                drum_patternU, drum_patternV, drum_patternW, drum_patternX]


# BPM 구성
beat_duration = 1.0  # 한 박자(비트)는 1초
sample_rate = 44100

# 단일 드럼 패턴 기반 오디오 데이터 생성
def generate_drum_pattern(pattern, sample_rate):
    """
    Generate audio for a single drum pattern without any trailing silence.
    """
    ## 패턴 한 길이의 정확한 시간 계산
    # 패턴 전체 길이 계산
    max_time = max(note["time"] for note in pattern)
    # 한 패턴 끝에 0.25초의 여유 공간을 추가하여 샘플 길이 조정
    total_samples = int((max_time + 0.25) * sample_rate)

    # 빈 오디오의 배열을 초기화
    # 전체 샘플 길이만큼 0으로 채운 오디오 배열 생성
    audio = np.zeros(total_samples)

    ## 노트 반복 처리
    for note in pattern:
      # 각 노트의 시작 단위를 샘플 단위로 계산한다
        start_idx = int(note["time"] * sample_rate)
        # 사운드 반복 처리
        for sound in note["sounds"]:
            rate, audio_data = audio_files[sound]
            # 오디오 파일과 sample rate가 다를 경우 오류 발생시키기
            if rate != sample_rate:
                raise ValueError(f"Sample rate mismatch for {sound}. Expected {sample_rate}, got {rate}.")
            end_idx = start_idx + len(audio_data)
            # 시작 인덱스부터 소리 데이터를 배열에 더한다
            audio[start_idx:end_idx] += audio_data[:len(audio[start_idx:end_idx])]

    # 오디오 정규화
    audio = audio / np.max(np.abs(audio)) if np.max(np.abs(audio)) > 0 else audio
    return audio


## 결합
# 여러 드럼 패턴을 순서대로 결합하여 하나의 연속된 오디오로 생성
def combine_patterns(patterns, sample_rate):
    """
    Concatenate multiple drum patterns without any gaps or silence.
    """
    combined_audio = []

    # 각 패턴의 오디오 생성
    for pattern in patterns:
        # 모든 패턴의 오디오 데이터를 리스트에 추가
        pattern_audio = generate_drum_pattern(pattern, sample_rate)
        combined_audio.append(pattern_audio)

    # 패턴 오디오 데이터 리스트를 하나로 결합
    combined_audio = np.concatenate(combined_audio)

    # 오디오 정규화 & 16비트 정수 변환(wav 파일 형식으로 저장하기 위함)
    combined_audio = combined_audio / np.max(np.abs(combined_audio)) if np.max(np.abs(combined_audio)) > 0 else combined_audio
    return (combined_audio * 32767).astype(np.int16)


## 곡에 따라 92개의 마디 생성
pattern_sequence = [
    drum_patternA, drum_patternB, drum_patternC, drum_patternD, # 1~4 bars
    drum_patternE, drum_patternB, drum_patternC, drum_patternF,  # 5~8 bars
    drum_patternC, drum_patternG, drum_patternC, drum_patternH,  # 9~12 bars
    drum_patternI, drum_patternG, drum_patternC, drum_patternJ,  # 13~16 bars
    drum_patternI, drum_patternK, drum_patternL, drum_patternM,  # 17~20 bars
    drum_patternI, drum_patternK, drum_patternC, drum_patternN,  # 21~24 bars
    drum_patternE, drum_patternO, drum_patternC, drum_patternP,  # 25~28 bars
    drum_patternC, drum_patternG, drum_patternC, drum_patternH,  # 29~32 bars
    drum_patternQ, drum_patternB, drum_patternC, drum_patternP,  # 33~36 bars1
    drum_patternC, drum_patternG, drum_patternC, drum_patternH,  # 37~40 bars1
    drum_patternQ, drum_patternB, drum_patternC, drum_patternP,  # 41~44 bars1
    drum_patternC, drum_patternB, drum_patternI, drum_patternR,  # 45~48 bars1
    drum_patternA, drum_patternB, drum_patternC, drum_patternS,  # 49~52 bars1
    drum_patternE, drum_patternB, drum_patternC, drum_patternT,  # 53~56 bars1
    drum_patternI, drum_patternB, drum_patternC, drum_patternU,  # 57~60 bars1
    drum_patternE, drum_patternB, drum_patternC, drum_patternT,  # 61~64 bars1
    drum_patternC, drum_patternG, drum_patternC, drum_patternV,  # 65~68 bars1
    drum_patternI, drum_patternG, drum_patternC, drum_patternW,  # 69~72 bars1
    drum_patternQ, drum_patternB, drum_patternC, drum_patternP,  # 33~36 bars1
    drum_patternC, drum_patternG, drum_patternC, drum_patternH,  # 37~40 bars1
    drum_patternQ, drum_patternB, drum_patternC, drum_patternP,  # 41~44 bars1
    drum_patternC, drum_patternB, drum_patternI, drum_patternR,  # 45~48 bars1
    drum_patternI, drum_patternG, drum_patternC, drum_patternT,  # 73~76 bars
    drum_patternI, drum_patternB, drum_patternI, drum_patternX,  # 77~80 bars
    drum_patternI, drum_patternG, drum_patternC, drum_patternT,  # 73~76 bars
    drum_patternI, drum_patternB, drum_patternI, drum_patternX,  # 77~80 bars
    drum_patternC, drum_patternG, drum_patternC, drum_patternV,  # 81~84 bars
    drum_patternC, drum_patternG, drum_patternC, drum_patternT,  # 85~88 bars
    drum_patternI, drum_patternB, drum_patternI, drum_patternV,  # 89~92 bars
]

# 모든 패턴 시퀀스를 평탄화한다.
# all_bars = [pattern for group in pattern_sequence for pattern in group]

# 결합된 오디오 생성
combined_audio = combine_patterns(pattern_sequence, sample_rate)

# 전체 오디오 저장 후 재생
write("combined_drum_pattern.wav", sample_rate, combined_audio)
Audio("combined_drum_pattern.wav")
#from google.colab import files
#files.download("combined_drum_pattern.wav")
