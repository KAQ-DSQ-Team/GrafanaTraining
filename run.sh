#!/bin/bash

echo "🚀 Grafana Training Project 시작"
echo "=================================="

# 1. 데이터 생성
echo "📊 센서 데이터 생성 중..."
python3 data/sensor_data.py

# 2. Grafana 컨테이너 실행
echo "🐳 Grafana Docker 컨테이너 시작 중..."
docker compose up -d

# 3. 상태 확인
echo "⏳ Grafana 시작 대기 중..."
sleep 10

# 4. 접속 정보 출력
echo ""
echo "✅ 설정 완료!"
echo "🌐 Grafana 접속: http://localhost:3000"
echo "👤 계정: admin / admin"
echo ""
echo "📋 다음 단계:"
echo "1. Grafana에 로그인"
echo "2. SQLite 플러그인 설치 (frser-sqlite-datasource)"
echo "3. 데이터소스 연결"
echo "4. 대시보드 확인"
echo ""
echo "🛑 종료하려면: docker compose down" 