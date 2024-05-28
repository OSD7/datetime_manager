# datetime_manager

`datetime_manager`는 파이썬에서 날짜와 시간 관련 작업을 쉽게 처리할 수 있도록 도와주는 모듈입니다. 날짜 및 시간의 형식 변환, 산술 연산, 시간대 관리를 포함한 다양한 기능을 제공합니다.

## 기능

- 날짜 문자열을 다양한 형식으로 파싱 및 변환 (format_converter)
- 날짜 및 시간 산술 연산 (arithmetic_operations)
- 시간대 관리 (timezone_manager)

## 설치

`datetime_manager` 모듈을 설치하려면 다음과 같이 합니다:

```
pip install pytz
```

# 모듈 설명


## 형식 변환 (Format Conversion)


### 날짜 문자열을 datetime 객체로 파싱합니다.
parse_date(date_string, yearfirst=True, monthfirst=False)

date_string: 파싱할 날짜 문자열
yearfirst: 연도가 먼저 오는 형식 여부 (기본값: True)
monthfirst: 월이 먼저 오는 형식 여부 (기본값: False)

### datetime 객체를 지정된 형식의 문자열로 변환합니다.
format_date(date_obj, yearfirst=True, monthfirst=False)

date_obj: 변환할 datetime 객체
yearfirst: 연도가 먼저 오는 형식 여부 (기본값: True)
monthfirst: 월이 먼저 오는 형식 여부 (기본값: False)


## 산술 연산 (Arithmetic Operations)


### datetime 객체에 시간 간격을 더합니다.
add_time(date_obj, days=0, hours=0, minutes=0, seconds=0)

date_obj: 기준이 되는 datetime 객체
days: 더할 일 수 (기본값: 0)
hours: 더할 시간 수 (기본값: 0)
minutes: 더할 분 수 (기본값: 0)
seconds: 더할 초 수 (기본값: 0)

### datetime 객체에서 시간 간격을 뺍니다.
subtract_time(date_obj, days=0, hours=0, minutes=0, seconds=0)

date_obj: 기준이 되는 datetime 객체
days: 뺄 일 수 (기본값: 0)
hours: 뺄 시간 수 (기본값: 0)
minutes: 뺄 분 수 (기본값: 0)
seconds: 뺄 초 수 (기본값: 0)

### 두 datetime 객체 간의 시간 차이를 계산합니다.
time_difference(date_obj1, date_obj2)

date_obj1: 첫 번째 datetime 객체
date_obj2: 두 번째 datetime 객체


## 시간대 관리 (Timezone Management)


### 날짜 문자열을 주어진 시간대의 datetime 객체로 파싱합니다.
parse_date_with_timezone(date_string, timezone, yearfirst=True, monthfirst=False)

date_string: 파싱할 날짜 문자열
timezone: 적용할 시간대 (pytz.timezone 객체)
yearfirst: 연도가 먼저 오는 형식 여부 (기본값: True)
monthfirst: 월이 먼저 오는 형식 여부 (기본값: False)

### datetime 객체를 주어진 시간대와 형식의 문자열로 변환합니다.
format_date_with_timezone(date_obj, timezone, format="%Y-%m-%d")

date_obj: 변환할 datetime 객체
timezone: 적용할 시간대 (pytz.timezone 객체)
format: 출력할 날짜 형식 (기본값: "%Y-%m-%d")

이 README 파일은 `datetime_manager` 모듈의 주요 기능, 설치 방법, 사용 예제 및 함수 설명을 포함합니다. 이를 통해 사용자는 모듈의 세부 기능인 형식 변환, 산술 연산 및 시간대 관리를 쉽게 이해하고 사용할 수 있습니다.