#!/usr/bin/env python3
"""
가상 센서 데이터 생성 및 SQLite 저장 스크립트
Grafana 학습용 실습 데이터 생성
"""

import sqlite3
import time
import random
from datetime import datetime, timedelta
import os

class SensorDataGenerator:
    def __init__(self, db_path='data/metrics.db'):
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        
    def connect_db(self):
        """SQLite 데이터베이스 연결"""
        # 디렉토리가 없으면 생성
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        
    def create_table(self):
        """센서 데이터 테이블 생성"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sensor_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                temperature REAL NOT NULL,
                pressure REAL NOT NULL,
                humidity REAL NOT NULL,
                flow_rate REAL NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
        print("✅ 센서 데이터 테이블이 생성되었습니다.")
        
    def generate_sample_data(self, num_samples=100, interval_seconds=2):
        """샘플 센서 데이터 생성"""
        print(f"🔄 {num_samples}개의 센서 데이터를 생성합니다...")
        
        base_time = datetime.utcnow()
        
        for i in range(num_samples):
            # 시간 계산 (2초 간격)
            current_time = base_time + timedelta(seconds=i * interval_seconds)
            timestamp = current_time.isoformat()
            
            # 가상 센서 데이터 생성 (현실적인 범위)
            temperature = round(25.0 + random.uniform(-2.0, 2.0) + 0.1 * i, 2)  # 온도: 23-27°C
            pressure = round(1.013 + random.uniform(-0.05, 0.05) + 0.001 * i, 3)  # 압력: 0.96-1.07 bar
            humidity = round(45.0 + random.uniform(-5.0, 5.0) + 0.05 * i, 1)  # 습도: 40-50%
            flow_rate = round(10.0 + random.uniform(-1.0, 1.0) + 0.02 * i, 2)  # 유량: 9-11 L/min
            
            # 데이터베이스에 저장
            self.cursor.execute('''
                INSERT INTO sensor_data (timestamp, temperature, pressure, humidity, flow_rate)
                VALUES (?, ?, ?, ?, ?)
            ''', (timestamp, temperature, pressure, humidity, flow_rate))
            
            # 진행상황 출력
            if (i + 1) % 10 == 0:
                print(f"📊 {i + 1}/{num_samples} 데이터 생성 완료")
                
        self.conn.commit()
        print("✅ 모든 센서 데이터가 생성되었습니다.")
        
    def show_data_summary(self):
        """생성된 데이터 요약 정보 출력"""
        self.cursor.execute('''
            SELECT 
                COUNT(*) as total_count,
                MIN(timestamp) as first_record,
                MAX(timestamp) as last_record,
                AVG(temperature) as avg_temp,
                AVG(pressure) as avg_pressure,
                AVG(humidity) as avg_humidity,
                AVG(flow_rate) as avg_flow_rate
            FROM sensor_data
        ''')
        
        result = self.cursor.fetchone()
        print("\n📈 데이터 생성 요약:")
        print(f"   총 레코드 수: {result[0]}")
        print(f"   시작 시간: {result[1]}")
        print(f"   종료 시간: {result[2]}")
        print(f"   평균 온도: {result[3]:.2f}°C")
        print(f"   평균 압력: {result[4]:.3f} bar")
        print(f"   평균 습도: {result[5]:.1f}%")
        print(f"   평균 유량: {result[6]:.2f} L/min")
        
    def close_db(self):
        """데이터베이스 연결 종료"""
        if self.conn:
            self.conn.close()
            print("✅ 데이터베이스 연결이 종료되었습니다.")

def main():
    """메인 실행 함수"""
    print("🚀 Grafana 학습용 센서 데이터 생성기 시작")
    print("=" * 50)
    
    # 데이터 생성기 초기화
    generator = SensorDataGenerator()
    
    try:
        # 데이터베이스 연결
        generator.connect_db()
        
        # 테이블 생성
        generator.create_table()
        
        # 샘플 데이터 생성 (100개, 2초 간격)
        generator.generate_sample_data(num_samples=100, interval_seconds=2)
        
        # 데이터 요약 출력
        generator.show_data_summary()
        
        print("\n🎉 데이터 생성이 완료되었습니다!")
        print("💡 Grafana에서 SQLite 데이터소스를 연결하여 시각화를 시작하세요.")
        
    except Exception as e:
        print(f"❌ 오류가 발생했습니다: {e}")
        
    finally:
        generator.close_db()

if __name__ == "__main__":
    main() 