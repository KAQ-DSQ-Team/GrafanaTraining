# Grafana Training Project

## 📋 프로젝트 개요

실측 센서 시계열 데이터를 SQLite에 저장하고 Grafana로 시각화하는 실습 프로젝트입니다.

### 🎯 목표
- **주요 목표**: 실측 센서 데이터의 시계열 시각화 학습
- **시간**: 총 2시간 이내 완료
- **수준**: 랩 테스트 수준, 향후 품질관리/공정실험 시각화 확장 기반 마련

### 🔄 학습 플로우
```
센서 or 가상센서 → SQLite (time-series) → Grafana Docker → 시각화 패널 구성
```

## 🚀 시작하기

### 사전 요구사항
- Docker & Docker Compose
- Python 3.7+
- Git

### 설치 및 실행

1. **프로젝트 클론**
```bash
git clone <repository-url>
cd GrafanaTraining
```

2. **Grafana Docker 실행**
```bash
docker compose up -d
```

3. **Grafana 접속**
- URL: http://localhost:3000
- 기본 계정: admin / admin

## 📊 실습 단계

### Step 1: Grafana Docker 구성 (15분)
- Docker Compose를 통한 Grafana 컨테이너 실행
- 기본 설정 및 접속 확인

### Step 2: SQLite 데이터 입력 (20분)
- Python 스크립트를 통한 가상 센서 데이터 생성
- SQLite 데이터베이스에 시계열 데이터 저장

### Step 3: 기본 시각화 실습 (30~45분)
- Stat Panel: 평균 온도, 평균 압력
- Time-series Panel: 시간대별 추이 시각화
- Threshold 구성: x̄ ± 3σ 기준선
- Treemap, Bar/Line Chart: 공정 흐름 표현

### Step 4: 확장 설계 회고 (15~20분)
- 향후 확장 계획 수립
- 커스텀 패널 개발 방향 검토

## 🔧 기술 스택

- **데이터베이스**: SQLite
- **시각화**: Grafana
- **컨테이너**: Docker & Docker Compose
- **데이터 생성**: Python

## 📈 3단계 확장 전략

| 단계 | 목표 | 방법 |
|------|------|------|
| Step 1 | 시계열 시각화 기본 학습 | Grafana + SQLite |
| Step 2 | 커스텀 패널 실험 | React 패널 템플릿 |
| Step 3 | 공정실험 시각화 확장 | 품질지표 통합 시각화 |

## 📁 프로젝트 구조

```
GrafanaTraining/
├── docker-compose.yml          # Grafana Docker 설정
├── data/                       # 데이터 파일들
│   ├── metrics.db             # SQLite 데이터베이스
│   └── sensor_data.py         # 센서 데이터 생성 스크립트
├── grafana/                    # Grafana 설정 파일들
│   └── provisioning/          # 대시보드 및 데이터소스 설정
└── README.md                  # 프로젝트 문서
```

## 🔗 유용한 링크

- [Grafana 공식 문서](https://grafana.com/docs/)
- [SQLite 플러그인](https://grafana.com/grafana/plugins/fr-ser-sqlite-datasource/)
- [Docker Compose 문서](https://docs.docker.com/compose/)

## 📝 라이센스

이 프로젝트는 학습 목적으로 제작되었습니다.

---

**작성일**: 2025-01-15  
**버전**: 1.0.0 