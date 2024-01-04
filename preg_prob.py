from datetime import datetime, timedelta

def estimate_ovulation(cycle_length, last_period_start):
    return last_period_start + timedelta(days=(cycle_length - 14))

def calculate_fertile_window(ovulation_date):
    start = ovulation_date - timedelta(days=5)
    end = ovulation_date + timedelta(days=1)
    return start, end

def calculate_probability(cycle_length, last_period_start, contraceptive_method, symptoms):
    # Estimate the ovulation and fertile window
    ovulation_date = estimate_ovulation(cycle_length, last_period_start)
    fertile_window_start, fertile_window_end = calculate_fertile_window(ovulation_date)

    # Base probability on fertile window
    probability = 0.30 if fertile_window_start <= datetime.today() <= fertile_window_end else 0.05

    # Adjust probability based on contraceptive method
    contraceptive_effects = {
        '안함': 1.0,
        '남성콘돔': 0.85,
        '여성콘돔': 0.8,
        '질외사정': 0.78,
        '피임약': 0.01,
        'Depo-Provera': 0.03,
        '자궁내장치': 0.02,
        '임플란트': 0.01
    }
    probability *= contraceptive_effects.get(contraceptive_method, 1.0)

    # Adjust probability based on symptoms
    symptom_effects = {
        '미열': 1.05,
        '피로': 1.03,
        '유방통': 1.07,
        '두통': 1.02,
        '입덧': 1.08,
        '질분비물 증가': 1.04,
        '변비': 1.01,
        '기분 변화': 1.06
    }
    for symptom in symptoms:
        probability *= symptom_effects.get(symptom, 1.0)

    return probability

# User input
cycle_length = int(input("마지막 생리 주기를 입력하세요 (예 : 28): "))
last_period_start_str = input("마지막 생리 시작일을 입력하세요 (YYYY-MM-DD): ")
last_period_start = datetime.strptime(last_period_start_str, "%Y-%m-%d")

# Get contraceptive method used
contraceptive_method = input("피임 방법을 선택하세요: ")

# Get any symptoms experienced
symptoms = []
print("다음 중 경험한 증상을 모두 선택하세요:")
symptom_options = ['미열', '피로', '유방통', '두통', '입덧', '질분비물 증가', '변비', '기분 변화']
for option in symptom_options:
    response = input(f"{option} (Y/N): ").strip().lower()
    if response == 'y':
        symptoms.append(option)

# Calculate probability
probability = calculate_probability(cycle_length, last_period_start, contraceptive_method, symptoms)
print(f"임신 가능성은 {probability:.2%}입니다.")
