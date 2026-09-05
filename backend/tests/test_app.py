import json
import pytest
import sys
import os

# Menambahkan path agar pytest bisa menemukan file app.py di folder luar
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

@pytest.fixture
def client():
    # Menyalakan mode testing bawaan Flask
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_status_berhasil(client):
    """Skenario: Robot CI memanggil /api/status dan mengecek respons"""
    response = client.get('/api/status')
    
    # 1. Pastikan server merespons dengan HTTP 200 OK
    assert response.status_code == 200
    
    # 2. Pastikan respons berupa JSON yang bisa dibaca
    data = json.loads(response.data)
    
    # 3. Pastikan isi datanya sesuai ekspektasi dari developer
    assert data['status'] == 'success'
    assert 'version' in data