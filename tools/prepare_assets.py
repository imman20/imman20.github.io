"""Saya mengambil grafik hasil nyata dan mengecilkannya untuk halaman statis."""

from io import BytesIO
from pathlib import Path
from urllib.request import urlopen

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "kurs.webp": "https://raw.githubusercontent.com/imman20/forecast-kurs-rupiah-arima-svr/main/assets/08_perbandingan_testing.png",
    "retail.webp": "https://raw.githubusercontent.com/imman20/analisis-penjualan-retail-sql-powerbi/main/assets/dashboard_overview.png",
    "survei.webp": "https://raw.githubusercontent.com/imman20/analisis-survei-dan-eksperimen-r/main/assets/hero.png",
    "excel.webp": "https://raw.githubusercontent.com/imman20/portofolio-excel-hr-administrasi/main/proyek/01_sales_profitability/assets/report.png",
    "hr.webp": "https://raw.githubusercontent.com/imman20/hr-attrition-analytics/penyempurnaan/analitik-hr/assets/evaluation.png",
}


def main():
    (ROOT / "assets").mkdir(exist_ok=True)
    for name, url in SOURCES.items():
        with urlopen(url, timeout=60) as response:
            picture = Image.open(BytesIO(response.read())).convert("RGB")
        if picture.width > 800:
            picture = picture.resize(
                (800, round(picture.height * 800 / picture.width)),
                Image.Resampling.LANCZOS,
            )
        picture.save(ROOT / "assets" / name, "WEBP", quality=94, method=6)
        if name == "hr.webp":
            picture.save(ROOT / "assets/social.png", optimize=True)
        print(name, picture.size, (ROOT / "assets" / name).stat().st_size)


if __name__ == "__main__":
    main()
