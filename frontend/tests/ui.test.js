const fs = require('fs');
const path = require('path');

// Membaca file HTML asli yang dibuat developer
const html = fs.readFileSync(path.resolve(__dirname, '../index.html'), 'utf8');

describe('Pengujian Komponen Frontend', () => {
    beforeEach(() => {
        // Memuat HTML ke dalam Document Object Model (DOM) virtual milik CI
        document.documentElement.innerHTML = html.toString();
    });

    test('Memastikan judul H2 dirender dengan benar', () => {
        const heading = document.querySelector('h2');
        expect(heading.textContent).toBe('Frontend (Nginx)');
    });

    test('Memastikan tombol API tersedia untuk di-klik pengguna', () => {
        const button = document.querySelector('button');
        expect(button).not.toBeNull();
        expect(button.textContent).toBe('Panggil Backend API');
    });

    test('Memastikan teks notifikasi error/sukses tersembunyi saat awal dimuat', () => {
        const resultParagraph = document.getElementById('result');
        expect(resultParagraph.textContent).toBe('');
    });
});