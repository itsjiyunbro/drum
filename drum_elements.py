!pip install simpleaudio

import numpy as np
import matplotlib.pyplot as plt
import simpleaudio as sa
from scipy.io.wavfile import write  # write 함수 임포트
from scipy.signal import butter, lfilter
from IPython.display import Audio


# 샘플링 주파수 44.1Hz(초당 샘플 개수)
sample_rate = 44100

# 기본 지속시간
duration = 1

# 주파수
frequency = 80;
# 시간 배열
t = np.linspace(0, duration, int(sample_rate * duration), False)

# 그래프 그리기 함수
def graph(wave, title):
  plt.figure(figsize=(10, 4))
  plt.plot(t[:1000], wave[:1000])  # 첫 1000개 샘플만 표시(for 시간 축소하여 보여주기 위해)
  plt.title(title)
  plt.xlabel("Time [s]")
  plt.ylabel("Amplitude")
  plt.show()


# Basic settings
sample_rate = 44100
duration = 1.0  # Kick sound is short but has a bit of tail for depth
t = np.linspace(0, duration, int(sample_rate * duration), False)


## 킥 사운드 정의
def generate_kick():
    # 빠르게 감쇠하는 고주파 트랜지어트 생성
    attack_freq = 100  # 트랜지어트 초기 고주파수 100Hz
    transient = np.sin(2 * np.pi * attack_freq * t) * np.exp(-30 * t)
    # sin함수: 100Hz의 사인파 생성 & exp함수: 지수 감쇠 함수

    # 공명감(body) 사운드 생성(저주파)
    frequency = 50  # 저주파의 기본 주파수를 50Hz로 설정
    body = np.sin(2 * np.pi * frequency * t) * np.exp(-5 * t)
    # sin함수: 50Hz의 저주파 사인파 생성 & exp함수: 점차 소리가 사라지도록

    # 트랜지어트 + 몸통 (결합)
    kick_wave = transient + body
    kick_wave *= 0.8  # 볼륨 조정
    return kick_wave

## 킥 그래프 그리기
kick_wave = generate_kick()
#graph(kick_wave, "Kick Waveform (80Hz with Exponential Decay)")


## 스네어 사운드 정의
def generate_snare(sample_rate=44100, duration=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # 1. 날카로운 '크랙("딱" 소리)' 사운드 생성(짧은 고주파)
    crack_freq = 3000  # 기본 주파수 3000Hz
    crack = np.sin(2 * np.pi * crack_freq * t) * np.exp(-80 * t)
    # sin함수: 3000Hz 고주파 사인파 생성 & exp함수: 빠르게 감쇠하도록

    # 2.공명감(body) 사운드 생성(저음역대)
    body_freq = 200  # 기본주파수 200Hz
    body = np.sin(2 * np.pi * body_freq * t) * np.exp(-8 * t)
    # sin함수: 200Hz 저주파 사인파 생성 & exp: 점차 소리가 사라지도록

    # 3. 와이어 사운드(Rattle) 생성(특유의 질감을 위해 3개의 화이트노이즈 layers)
    # Layer 1: 초반 날카로운 Rattle
    # 평균 0, 표준편차 0.4의 화이트노이즈 & 소리 빠르게 감소
    rattle1 = np.random.normal(0, 0.4, t.shape) * np.exp(-30 * t)
    # Layer 2: 중간 강도의 Rattle
    # 평균 0, 표준편차 0.3의 화이트노이즈 & 감쇠 속도 완화
    rattle2 = np.random.normal(0, 0.3, t.shape) * np.exp(-15 * t)
    # Layer 3: 끝부분의 잔향과 같은 미세한 Rattle
    # 평균 0, 표준편차 0.2의 화이트노이즈
    rattle3 = np.random.normal(0, 0.2, t.shape) * np.exp(-7 * t)
    rattle = rattle1 + rattle2 + rattle3

    # 결합
    snare_wave = crack + body + rattle

    # 전체 소리 정규화(소리 크기가 1을 넘지 않도록 조정)
    snare_wave = snare_wave / np.max(np.abs(snare_wave))
    snare_wave *= 0.8  # 볼륨 조정

    return snare_wave

## 스네어 그래프
snare_wave = generate_snare()
#graph(snare_wave, "Snare Waveform (80Hz with Exponential Decay)")


# 하이패스 필터 정의
# 저주파 제거, 고주파 강조: 심벌 소리의 고음 구현을 위함
# 입력변수: data(필터링할 입력 신호), cutoff(4000Hz이상의 고주파만 통과하도록), fs(sampling rate 44100), order(필터의 차수(강도))
def highpass_filter(data, cutoff=4000, fs=44100, order=3):
    # 나이퀴스트 주파수: 샘플링 주파수의 절반
    nyquist = 0.5 * fs
    # 컷오프 주파수: 나이퀴스트 주파수로 정규화
    normal_cutoff = cutoff / nyquist
    # Butterworth 필터 생성
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    # 필터를 신호(data)에 적용
    y = lfilter(b, a, data)
    return y

# 심벌 사운드 정의
def generate_cymbal():
    # 화이트 노이즈 생성: 무작위적이고 복잡한 음색 구현을 위함
    # 평균 0, 표준편차 0.5
    noise = np.random.normal(0, 0.5, t.shape)

    # 지수 감쇠 함수
    decay = np.exp(-1.5 * t)

    # HPF 적용
    filtered_noise = highpass_filter(noise, cutoff=4000, fs=sample_rate, order=3)

    # 결합
    cymbal_wave = filtered_noise * decay

    # 정규화
    cymbal_wave *= 0.8 / np.max(np.abs(cymbal_wave))
    return cymbal_wave

# 그래프 그리기
cymbal_wave = generate_cymbal()
#graph(cymbal_wave, "Cymbal Waveform")


## 클로즈드 하이햇 사운드 정의
def generate_closed_hihat():
  # 화이트 노이즈 생성
  closed_hihat_wave = np.random.normal(0, 1, t.shape)
  closed_hihat_wave *= 0.5
  # 지수 감쇠 함수
  closed_hihat_wave *= np.exp(-50 * t)
  return closed_hihat_wave

## 클로즈드 하이햇 그래프 그리기
closed_hihat_wave = generate_closed_hihat()
#graph(closed_hihat_wave, "Closed-hihat Waveform")


## 오픈 하이햇 사운드 정의
def generate_open_hihat():
    # 화이트 노이즈 생성 for metallic shimmer
    # 메인 바디 노이즈
    noise1 = np.random.normal(0, 0.3, t.shape) * np.exp(-4 * t)
    # 질감을 위한 빠른 감쇠
    noise2 = np.random.normal(0, 0.2, t.shape) * np.exp(-5 * t)

    # 화이트 노이즈의 결합
    open_hihat_wave = noise1 + noise2

    # HPF
    open_hihat_wave = highpass_filter(open_hihat_wave, cutoff=4000, fs=sample_rate, order=3)

    # 정규화
    open_hihat_wave *= 0.5 / np.max(np.abs(open_hihat_wave))
    return open_hihat_wave

## 오픈 하이햇 그래프 그리기
open_hihat_wave = generate_open_hihat()
#graph(open_hihat_wave, "Open-Hihat Waveform")


## 라이드 사운드 정의
def generate_ride():
    # 공명감(base) 생성 (저주파)
    base_freq = 300 # 기본 주파수 300Hz 설정
    base_tone = np.sin(2 * np.pi * base_freq * t) * np.exp(-1.5 * t)

    # 중고역대 overtones 생성(금속성 질감과 다채로운 울림을 위함)
    overtone1 = np.sin(2 * np.pi * 1200 * t) * np.exp(-2 * t)
    overtone2 = np.sin(2 * np.pi * 1500 * t) * np.exp(-2.2 * t)
    overtone3 = np.sin(2 * np.pi * 1800 * t) * np.exp(-2.5 * t)
    overtone4 = np.sin(2 * np.pi * 2200 * t) * np.exp(-3 * t)

    # 요소 결합
    ride_wave = base_tone + overtone1 + overtone2 + overtone3 + overtone4

    # HPF
    ride_wave = highpass_filter(ride_wave, cutoff=800, fs=sample_rate, order=2)

    # 정규화
    ride_wave *= 0.1 / np.max(np.abs(ride_wave))
    return ride_wave

ride_wave = generate_ride()
#graph(ride_wave, "Ride Waveform")


### 사운드 재생 함수
# WAV 파일로 저장하는 함수
def save_wave(wave, filename="output.wav"):
    audio = np.int16(wave * 32767)  # 16-bit 변환
    write(filename, sample_rate, audio)

print("cymbal")
# 심벌 소리를 WAV 파일로 저장하고 재생
save_wave(cymbal_wave, "cymbal.wav")
display(Audio("cymbal.wav"))

print("kick")
# 킥 소리를 WAV 파일로 저장하고 재생
save_wave(kick_wave, "kick.wav")
display(Audio("kick.wav"))

print("snare")
# 스네어 소리를 WAV 파일로 저장하고 재생
save_wave(snare_wave, "snare.wav")
display(Audio("snare.wav"))

print("closed-hihat")
# 클로즈드 하이햇 소리를 WAV 파일로 저장하고 재생
save_wave(closed_hihat_wave, "closed_hihat.wav")
display(Audio("closed_hihat.wav"))

print("open-hihat")
# 오픈 하이햇 소리를 WAV 파일로 저장하고 재생
save_wave(open_hihat_wave, "open_hihat.wav")
display(Audio("open_hihat.wav"))

print("ride")
# 라이드 소리를 WAV 파일로 저장하고 재생
save_wave(ride_wave, "ride.wav")
display(Audio("ride.wav"))
