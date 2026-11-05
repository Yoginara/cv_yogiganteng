import os
import fitz
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak, Image, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

# ==========================================
# STRICT MONOCHROME / BLACK TEXT PALETTE
# ==========================================
BLACK = colors.HexColor("#000000")       # Pure Black Text
DARK_GRAY = colors.HexColor("#222222")   # Deep Charcoal for subtle emphasis
BORDER_BLACK = colors.HexColor("#333333")# Solid Dark Border
LINE_BLACK = colors.HexColor("#000000")  # Pure Black Line
BG_WHITE = colors.HexColor("#FFFFFF")    # Clean White
BG_LIGHT_GRAY = colors.HexColor("#F8F9FA")# Subtle Crisp Neutral Background
BG_ALT_GRAY = colors.HexColor("#F1F3F5")  # Clean Section Table Background

# ==========================================
# 1. GENERATE ATS CV (BLACK TEXT ONLY)
# ==========================================
def build_black_ats_cv(lang='id', pages=2):
    suffix = f"_{lang.upper()}" if pages == 2 else f"_{lang.upper()}_1Page"
    filename = f"CV_ATS_Yoginara_Pratama_Sitorus{suffix}.pdf"
    
    # Page setup
    if pages == 1:
        doc = SimpleDocTemplate(
            filename,
            pagesize=A4,
            leftMargin=28,
            rightMargin=28,
            topMargin=22,
            bottomMargin=22
        )
        fs_name = 14.5
        lead_name = 17
        fs_sec = 8.8
        lead_sec = 11
        fs_job = 8
        lead_job = 10
        fs_body = 7.7
        lead_body = 10.2
        fs_skill = 7.5
        lead_skill = 9.8
        sp_item = 0.5
        sp_sec = 2.5
    else:
        doc = SimpleDocTemplate(
            filename,
            pagesize=A4,
            leftMargin=32,
            rightMargin=32,
            topMargin=26,
            bottomMargin=26
        )
        fs_name = 16
        lead_name = 19
        fs_sec = 9.5
        lead_sec = 12
        fs_job = 8.5
        lead_job = 11
        fs_body = 8
        lead_body = 11.2
        fs_skill = 8
        lead_skill = 11
        sp_item = 1.2
        sp_sec = 3.5

    st = {
        'Name': ParagraphStyle('Name', fontName='Helvetica-Bold', fontSize=fs_name, leading=lead_name, textColor=BLACK, alignment=TA_CENTER),
        'Title': ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=fs_job, leading=lead_job+1, textColor=BLACK, alignment=TA_CENTER),
        'Contact': ParagraphStyle('Contact', fontName='Helvetica', fontSize=fs_body, leading=lead_body, textColor=BLACK, alignment=TA_CENTER),
        'Section': ParagraphStyle('Section', fontName='Helvetica-Bold', fontSize=fs_sec, leading=lead_sec, textColor=BLACK, spaceBefore=sp_sec, spaceAfter=1.5, textTransform='uppercase'),
        'JobTitle': ParagraphStyle('JobTitle', fontName='Helvetica-Bold', fontSize=fs_job, leading=lead_job, textColor=BLACK),
        'Company': ParagraphStyle('Company', fontName='Helvetica-Oblique', fontSize=fs_body, leading=lead_body, textColor=BLACK),
        'DateLoc': ParagraphStyle('DateLoc', fontName='Helvetica', fontSize=fs_body, leading=lead_body, textColor=BLACK, alignment=TA_RIGHT),
        'Bullet': ParagraphStyle('Bullet', fontName='Helvetica', fontSize=fs_body, leading=lead_body, textColor=BLACK, alignment=TA_JUSTIFY, leftIndent=8, firstLineIndent=-8),
        'Summary': ParagraphStyle('Summary', fontName='Helvetica', fontSize=fs_body, leading=lead_body, textColor=BLACK, alignment=TA_JUSTIFY),
        'SkillCat': ParagraphStyle('SkillCat', fontName='Helvetica-Bold', fontSize=fs_skill, leading=lead_skill, textColor=BLACK),
        'SkillVal': ParagraphStyle('SkillVal', fontName='Helvetica', fontSize=fs_skill, leading=lead_skill, textColor=BLACK)
    }

    def add_sec(title):
        return [
            Paragraph(title, st['Section']),
            HRFlowable(width="100%", thickness=0.8, color=LINE_BLACK, spaceBefore=1, spaceAfter=2.5)
        ]

    story = []
    col_w = [395, 140] if pages == 1 else [385, 146]

    # Header
    story.append(Paragraph("YOGINARA PRATAMA SITORUS, S.Tr.Kom", st['Name']))
    story.append(Spacer(1, 1))
    t_role = "FULLSTACK WEB DEVELOPER & SOFTWARE ENGINEER" if lang == 'id' else "FULL-STACK WEB DEVELOPER & SOFTWARE ENGINEER"
    story.append(Paragraph(t_role, st['Title']))
    story.append(Spacer(1, 1))
    story.append(Paragraph('Bandung, Indonesia &bull; +62 813-6064-0668 &bull; yoginara2004@gmail.com &bull; <a href="https://github.com/Yoginara"><font color="#000000">github.com/Yoginara</font></a> &bull; <a href="https://yoginara.github.io/cv_yogiganteng/"><font color="#000000">yoginara.github.io/cv_yogiganteng</font></a>', st['Contact']))
    story.append(Spacer(1, 2.5))

    if lang == 'id':
        # Summary
        story.extend(add_sec("Ringkasan Profil"))
        story.append(Paragraph(
            "Sarjana Terapan Teknik Informatika (IPK 3,56 / 4,00) dari Universitas Logistik & Bisnis Internasional (ULBI) dengan spesialisasi Fullstack Web Development dan arsitektur backend enterprise. Berpengalaman menangani sistem e-GRC korporat skala 116.000+ LoC di BUMD Tirta Raharja, merancang algoritma kalkulasi risiko dinamis ISO 31000:2018, serta mengoptimalkan pelaporan hingga efisiensi 85%. Menguasai Laravel 12, CodeIgniter 3, Golang Fiber, basis data relasional (MySQL, Oracle OCI8) dan NoSQL (MongoDB), TDD (PHPUnit 11), serta tersertifikasi resmi BNSP Teknisi Muda Jaringan Komputer aktif hingga 2029.",
            st['Summary']
        ))
        story.append(Spacer(1, 1.5))

        # Experience
        story.extend(add_sec("Pengalaman Kerja Rekayasa Perangkat Lunak"))
        row1 = Table([
            [Paragraph("<b>Fullstack Web Developer & Software Engineer Intern</b>", st['JobTitle']), Paragraph("Sep 2025 – Des 2025", st['DateLoc'])],
            [Paragraph("Perumda Air Minum Tirta Raharja (Kabupaten Bandung)", st['Company']), Paragraph("Bandung / Cimahi, ID", st['DateLoc'])]
        ], colWidths=col_w)
        row1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
        story.append(row1)
        story.append(Spacer(1, 1))

        bullets_exp = [
            "<b>Pemeliharaan Arsitektur Sistem Enterprise:</b> Mengembangkan dan memelihara aplikasi web Enterprise Governance, Risk, and Compliance (e-GRC) berbasis CodeIgniter 3 MVC pada basis kode <b>116.000+ LoC</b> (203 controller dan 188 model relasional).",
            "<b>Rekayasa Algoritma Risiko Residu Dinamis:</b> Merancang kalkulasi reaktif di <i>risk_analisisdetail.php</i> sesuai ISO 31000:2018: <i>nilaiPenurunan = Efektivitas &times; (% Progres / 100)</i>, mengeliminasi manipulasi data subjektif antar cabang.",
            "<b>Efisiensi Pelaporan Korporat 85%:</b> Merefaktor modul pelaporan Kertas Kerja Profil Risiko BPKP dan Satuan Pengawas Intern (SPI), memangkas siklus konsolidasi dari <b>~10 hari kerja menjadi hitungan detik</b> siap cetak.",
            "<b>Persistensi Data Dual-Database:</b> Mengelola abstraksi kustom ADODB yang menghubungkan MySQL/MariaDB dan Oracle Enterprise (OCI8) secara modular dengan proteksi <i>soft-deletes</i> terpusat.",
            "<b>Dokumentasi Standar Tim & AI Assistant:</b> Menginisiasi dan menyusun berkas arsitektur panduan pengembang <i>.github/copilot-instructions.md</i> guna menjamin kesinambungan standar kode tim pengembang."
        ]
        for b in bullets_exp:
            story.append(Paragraph(f"&bull; {b}", st['Bullet']))
            story.append(Spacer(1, 0.75 if pages == 1 else 1))

        # Projects
        story.extend(add_sec("Proyek Rekayasa Perangkat Lunak Utama"))
        p1 = Table([
            [Paragraph("<b>CMI Content Management System & Database Query Optimization</b>", st['JobTitle']), Paragraph("Nov 2026", st['DateLoc'])],
            [Paragraph("Laravel 12.0 &bull; PHP 8.2+ &bull; Tailwind CSS v3 &bull; SQLite/MySQL &bull; PHPUnit 11", st['Company']), Paragraph("Arsitektur Enterprise", st['DateLoc'])]
        ], colWidths=col_w)
        p1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
        story.append(p1)
        story.append(Spacer(1, 0.75))
        story.append(Paragraph("&bull; Membangun portal artikel dengan proteksi otorisasi kepemilikan (Laravel Policy anti-IDOR), generator slug unik otomatis, dan manajemen siklus berkas Flysystem.", st['Bullet']))
        story.append(Paragraph("&bull; Mengoptimalkan performa kueri basis data via Query Builder <b>INNER JOIN</b>, aliasing, serta paginasi 10 record dengan alokasi memori PHP terkontrol <b>&lt; 8 MB</b>.", st['Bullet']))
        story.append(Paragraph("&bull; Mencapai kelulusan <b>100% Green (39 automated unit & feature tests, 134 assertions)</b> dengan PHPUnit 11 serta mitigasi OWASP Top 10.", st['Bullet']))
        story.append(Spacer(1, 1.5))

        p2 = Table([
            [Paragraph("<b>StepUp & ManukShop Platform — High-Throughput REST API Microservices</b>", st['JobTitle']), Paragraph("2026", st['DateLoc'])],
            [Paragraph("Golang 1.22 &bull; GoFiber v2 (FastHTTP) &bull; MongoDB Atlas &bull; JWT &bull; Swagger", st['Company']), Paragraph("Mikroservis Backend", st['DateLoc'])]
        ], colWidths=col_w)
        p2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
        story.append(p2)
        story.append(Spacer(1, 0.75))
        story.append(Paragraph("&bull; Merancang microservice backend RESTful dengan konkurensi tinggi dan latensi sub-milidetik ditenagai core fasthttp GoFiber untuk katalog produk dan transaksi e-commerce.", st['Bullet']))
        story.append(Paragraph("&bull; Mengimplementasikan otentikasi JWT, hashing kata sandi Bcrypt, pola embedded snapshot NoSQL MongoDB, serta dokumentasi interaktif Swagger.", st['Bullet']))

        if pages == 2:
            story.append(PageBreak())

        # Page 2 content (or continued)
        story.extend(add_sec("Proyek Rekayasa Lanjutan & Riset" if pages == 2 else "Proyek Tambahan"))
        p3 = Table([
            [Paragraph("<b>RTConnect — Sistem Administrasi Digital & Smart Community Management</b>", st['JobTitle']), Paragraph("2026", st['DateLoc'])],
            [Paragraph("PHP Fullstack &bull; MySQL (15+ Relational Tables) &bull; Bootstrap 5 &bull; Public Validator", st['Company']), Paragraph("E-Government", st['DateLoc'])]
        ], colWidths=col_w)
        p3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
        story.append(p3)
        story.append(Spacer(1, 0.75))
        story.append(Paragraph("&bull; Mengembangkan platform tata kelola komunitas cerdas berbasis web untuk penagihan iuran warga, verifikasi kas lingkungan real-time, dan penerbitan surat pengantar resmi ber-validator publik.", st['Bullet']))
        
        if pages == 2:
            story.append(Spacer(1, 1.5))
            p4 = Table([
                [Paragraph("<b>CIT-TPRO: Convolution Interactive Transformer Deep Learning</b>", st['JobTitle']), Paragraph("2026", st['DateLoc'])],
                [Paragraph("Python &bull; PyTorch &bull; Linear Self-Attention O(N) &bull; EEG Biomedical Signal Fusion", st['Company']), Paragraph("Riset AI", st['DateLoc'])]
            ], colWidths=col_w)
            p4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
            story.append(p4)
            story.append(Spacer(1, 0.75))
            story.append(Paragraph("&bull; Riset arsitektur Transformer dengan perhatian linier O(N) dan fusi fitur PSD+DE untuk klasifikasi sinyal gelombang otak (EEG) pada benchmark dataset internasional (DEAP, DREAMER).", st['Bullet']))

        # Education
        story.extend(add_sec("Pendidikan Formal"))
        edu = Table([
            [Paragraph("<b>Universitas Logistik dan Bisnis Internasional (ULBI)</b>", st['JobTitle']), Paragraph("Lulus 2026", st['DateLoc'])],
            [Paragraph("Sarjana Terapan Komputer (S.Tr.Kom) — D4 Teknik Informatika | <b>IPK: 3,56 / 4,00</b>", st['Company']), Paragraph("Bandung, Indonesia", st['DateLoc'])],
            [Paragraph("Konsentrasi: Rekayasa Perangkat Lunak, Basis Data Korporat, Arsitektur Jaringan Komputer", st['Company']), Paragraph("Predikat Sangat Memuaskan", st['DateLoc'])]
        ], colWidths=col_w)
        edu.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
        story.append(edu)

        # Certifications
        story.extend(add_sec("Sertifikasi & Lisensi Resmi"))
        certs = [
            ("Teknisi Muda Jaringan Komputer (First-Level Computer Network Technician)", "Badan Nasional Sertifikasi Profesi (BNSP RI)", "2026 – 2029", "No. Reg: JIK.215.00004.2026 &bull; LSP ULBI (7 Unit SKKNI: Topologi, Pengalamatan IP, Switching, Cabling)"),
            ("Java Programming Certificate", "Oracle Academy", "Jun 2023", "Object-Oriented Programming, Data Structures, Polymorphism & Algorithmic Analysis"),
            ("Java Fundamentals Certificate", "Oracle Academy", "Jan 2023", "Core Java Syntax, Procedural Flow & Computational Logic"),
            ("MATLAB Onramp Course Completion (Score: 100%)", "MathWorks", "Mar 2023", "Komputasi Matriks Numerik, Visualisasi Grafis & Pemrosesan Data"),
            ("Introduction to JavaScript", "Great Learning Academy", "Mar 2024", "DOM Scripting, Modern JavaScript ES6+ & Asynchronous Handling")
        ]
        if pages == 1:
            certs = certs[:3]
        for title, org, date, detail in certs:
            c_row = Table([
                [Paragraph(f"<b>{title}</b> &bull; {org}", st['JobTitle']), Paragraph(date, st['DateLoc'])],
                [Paragraph(detail, st['Company']), Paragraph("", st['DateLoc'])]
            ], colWidths=[425, 110] if pages == 1 else [425, 106])
            c_row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
            story.append(c_row)
            story.append(Spacer(1, 0.5 if pages == 1 else 1))

        # Skills
        story.extend(add_sec("Keahlian Teknis (Technical Skills Matrix)"))
        skills = [
            ("Bahasa Pemrograman:", "PHP (8.x), Go (Golang 1.22), JavaScript (ES6+), Python, SQL, HTML5, CSS3"),
            ("Framework & Library:", "Laravel 12.x, CodeIgniter 3 MVC, GoFiber v2, Tailwind CSS v3, Bootstrap 5, jQuery, Blade"),
            ("Basis Data & Storage:", "MySQL, MariaDB, Oracle Database (OCI8), MongoDB Atlas (NoSQL), SQLite, ADODB Driver"),
            ("Pengujian & Keamanan:", "PHPUnit 11 (TDD/Automated Testing), OWASP Top 10 Mitigation, CSRF, XSS Escaping, IDOR"),
            ("Jaringan & Infrastruktur:", "BNSP Certified Network Technician, TCP/IP, IP Addressing, Switching, Structured Cabling"),
            ("Tools & Metodologi:", "Git, GitHub, RESTful API, Postman, Swagger/OpenAPI, Composer, NPM, Linux Environment")
        ]
        for cat, val in skills:
            sk_row = Table([[Paragraph(cat, st['SkillCat']), Paragraph(val, st['SkillVal'])]], colWidths=[135, 400] if pages == 1 else [135, 396])
            sk_row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
            story.append(sk_row)

    else:
        # Summary (EN)
        story.extend(add_sec("Profile Summary"))
        story.append(Paragraph(
            "Applied Bachelor of Informatics Engineering graduate (GPA: 3.56 / 4.00) from Universitas Logistik & Bisnis Internasional (ULBI), specializing in full-stack web development and scalable backend architecture. Proven production track record at regional utility BUMD maintaining a 116,000+ LoC codebase, engineering dynamic ISO 31000:2018 residual risk algorithms, and boosting reporting efficiency by 85%. Proficient in Laravel 12, CodeIgniter 3, Go (GoFiber), relational (MySQL, Oracle OCI8) and NoSQL (MongoDB) database optimization, test-driven development (PHPUnit 11), and OWASP Top 10 security. Officially certified by BNSP as a First-Level Computer Network Technician (valid 2026–2029).",
            st['Summary']
        ))
        story.append(Spacer(1, 1.5))

        # Experience (EN)
        story.extend(add_sec("Software Engineering Work Experience"))
        row1 = Table([
            [Paragraph("<b>Full-Stack Web Developer & Software Engineer Intern</b>", st['JobTitle']), Paragraph("Sep 2025 – Dec 2025", st['DateLoc'])],
            [Paragraph("Perumda Air Minum Tirta Raharja (Regional Water Utility BUMD)", st['Company']), Paragraph("Bandung / Cimahi, ID", st['DateLoc'])]
        ], colWidths=col_w)
        row1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
        story.append(row1)
        story.append(Spacer(1, 1))

        bullets_exp = [
            "<b>Enterprise Architecture Maintenance:</b> Engineered and maintained an Enterprise Governance, Risk, and Compliance (e-GRC) web suite built on CodeIgniter 3 MVC across a <b>116,000+ LoC</b> codebase (203 controllers, 188 relational models).",
            "<b>Dynamic Residual Risk Engine:</b> Implemented a reactive client-side calculation model in <i>risk_analisisdetail.php</i> compliant with ISO 31000:2018: <i>Risk Reduction = Effectiveness &times; (% Progress / 100)</i>, eliminating subjective bias.",
            "<b>85% Reporting Workflow Acceleration:</b> Refactored the corporate Risk Working Paper reporting engine, slashing compilation cycles from <b>~10 business days to automated instant generation</b>.",
            "<b>Dual-Database Abstraction:</b> Managed database persistence across MySQL/MariaDB and Oracle Enterprise (OCI8) through custom ADODB drivers with centralized soft-delete query filtration.",
            "<b>Engineering Standards & AI Documentation:</b> Authored the developer architectural guide <i>.github/copilot-instructions.md</i> to standardize code conventions and AI coding assistant workflows."
        ]
        for b in bullets_exp:
            story.append(Paragraph(f"&bull; {b}", st['Bullet']))
            story.append(Spacer(1, 0.75 if pages == 1 else 1))

        # Projects (EN)
        story.extend(add_sec("Key Software Engineering Projects"))
        p1 = Table([
            [Paragraph("<b>CMI Content Management System & Database Query Optimization</b>", st['JobTitle']), Paragraph("Nov 2026", st['DateLoc'])],
            [Paragraph("Laravel 12.0 &bull; PHP 8.2+ &bull; Tailwind CSS v3 &bull; SQLite/MySQL &bull; PHPUnit 11", st['Company']), Paragraph("Enterprise Architecture", st['DateLoc'])]
        ], colWidths=col_w)
        p1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
        story.append(p1)
        story.append(Spacer(1, 0.75))
        story.append(Paragraph("&bull; Architected an article publishing platform featuring granular ownership authorization (Laravel Policy anti-IDOR), collision-free sequential slug generation, and Flysystem media lifecycle management.", st['Bullet']))
        story.append(Paragraph("&bull; Optimized relational query throughput using Query Builder <b>INNER JOIN</b>, column aliasing, and 10-record pagination maintaining low memory footprint <b>&lt; 8 MB</b>.", st['Bullet']))
        story.append(Paragraph("&bull; Achieved <b>100% Green test suite (39 automated unit & feature tests, 134 assertions)</b> using PHPUnit 11 alongside OWASP Top 10 mitigation.", st['Bullet']))
        story.append(Spacer(1, 1.5))

        p2 = Table([
            [Paragraph("<b>StepUp & ManukShop Platform — High-Throughput REST API Microservices</b>", st['JobTitle']), Paragraph("2026", st['DateLoc'])],
            [Paragraph("Go (Golang 1.22) &bull; GoFiber v2 (FastHTTP) &bull; MongoDB Atlas &bull; JWT &bull; Swagger", st['Company']), Paragraph("Backend Microservice", st['DateLoc'])]
        ], colWidths=col_w)
        p2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
        story.append(p2)
        story.append(Spacer(1, 0.75))
        story.append(Paragraph("&bull; Constructed high-concurrency RESTful microservices with sub-millisecond response latency powered by GoFiber fasthttp core for high-throughput product catalog and transactions.", st['Bullet']))
        story.append(Paragraph("&bull; Implemented JWT authentication, Bcrypt password hashing, MongoDB embedded snapshots, and OpenAPI/Swagger documentation.", st['Bullet']))

        if pages == 2:
            story.append(PageBreak())

        # Page 2 (EN)
        story.extend(add_sec("Additional Engineering & Research Projects" if pages == 2 else "Additional Projects"))
        p3 = Table([
            [Paragraph("<b>RTConnect — Digital Community Administration & Public Validator</b>", st['JobTitle']), Paragraph("2026", st['DateLoc'])],
            [Paragraph("PHP Fullstack &bull; MySQL (15+ Relational Tables) &bull; Bootstrap 5 &bull; QR Validator", st['Company']), Paragraph("E-Government", st['DateLoc'])]
        ], colWidths=col_w)
        p3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
        story.append(p3)
        story.append(Spacer(1, 0.75))
        story.append(Paragraph("&bull; Developed a web-based smart community management system streamlining dues collection, real-time ledger auditing, and automated official resident certificates with public QR verification.", st['Bullet']))

        if pages == 2:
            story.append(Spacer(1, 1.5))
            p4 = Table([
                [Paragraph("<b>CIT-TPRO: Convolution Interactive Transformer Deep Learning</b>", st['JobTitle']), Paragraph("2026", st['DateLoc'])],
                [Paragraph("Python &bull; PyTorch &bull; Linear Self-Attention O(N) &bull; EEG Biomedical Signal Fusion", st['Company']), Paragraph("AI Research", st['DateLoc'])]
            ], colWidths=col_w)
            p4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
            story.append(p4)
            story.append(Spacer(1, 0.75))
            story.append(Paragraph("&bull; Investigated hybrid Transformer architectures with linear attention O(N) and PSD+DE feature fusion for emotion recognition on benchmark EEG datasets (DEAP, DREAMER).", st['Bullet']))

        # Education (EN)
        story.extend(add_sec("Education"))
        edu = Table([
            [Paragraph("<b>Universitas Logistik dan Bisnis Internasional (ULBI)</b>", st['JobTitle']), Paragraph("Graduated 2026", st['DateLoc'])],
            [Paragraph("Bachelor of Applied Science in Informatics Engineering (S.Tr.Kom) | <b>GPA: 3.56 / 4.00</b>", st['Company']), Paragraph("Bandung, Indonesia", st['DateLoc'])],
            [Paragraph("Focus: Software Engineering, Enterprise Database Systems, Computer Network Infrastructure", st['Company']), Paragraph("Graduated with Distinction", st['DateLoc'])]
        ], colWidths=col_w)
        edu.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
        story.append(edu)

        # Certifications (EN)
        story.extend(add_sec("Licenses & Certifications"))
        certs = [
            ("First-Level Computer Network Technician (Teknisi Muda Jaringan Komputer)", "Badan Nasional Sertifikasi Profesi (BNSP RI)", "2026 – 2029", "Reg No: JIK.215.00004.2026 &bull; LSP ULBI (7 SKKNI Units: Topology, IP Addressing, Switching, Cabling)"),
            ("Java Programming Certificate", "Oracle Academy", "Jun 2023", "Object-Oriented Programming, Data Structures, Polymorphism & Algorithmic Analysis"),
            ("Java Fundamentals Certificate", "Oracle Academy", "Jan 2023", "Core Java Syntax, Procedural Flow & Computational Logic"),
            ("MATLAB Onramp Course Completion (Score: 100%)", "MathWorks", "Mar 2023", "Numerical Matrix Computations, Graphical Visualization & Data Processing"),
            ("Introduction to JavaScript", "Great Learning Academy", "Mar 2024", "DOM Scripting, Modern JavaScript ES6+ & Asynchronous Handling")
        ]
        if pages == 1:
            certs = certs[:3]
        for title, org, date, detail in certs:
            c_row = Table([
                [Paragraph(f"<b>{title}</b> &bull; {org}", st['JobTitle']), Paragraph(date, st['DateLoc'])],
                [Paragraph(detail, st['Company']), Paragraph("", st['DateLoc'])]
            ], colWidths=[425, 110] if pages == 1 else [425, 106])
            c_row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
            story.append(c_row)
            story.append(Spacer(1, 0.5 if pages == 1 else 1))

        # Skills (EN)
        story.extend(add_sec("Technical Skills Matrix"))
        skills = [
            ("Programming Languages:", "PHP (8.x), Go (Golang 1.22), JavaScript (ES6+), Python, SQL, HTML5, CSS3"),
            ("Frameworks & Libraries:", "Laravel 12.x, CodeIgniter 3 MVC, GoFiber v2, Tailwind CSS v3, Bootstrap 5, jQuery, Blade"),
            ("Databases & Storage:", "MySQL, MariaDB, Oracle Database (OCI8), MongoDB Atlas (NoSQL), SQLite, ADODB Driver"),
            ("QA & Security Standards:", "PHPUnit 11 (TDD/Automated Testing), OWASP Top 10 Mitigation, CSRF, XSS Escaping, IDOR"),
            ("Networking & Infrastructure:", "BNSP Certified Network Technician, TCP/IP, IP Addressing, Switching, Structured Cabling"),
            ("Tools & Methodologies:", "Git, GitHub, RESTful API, Postman, Swagger/OpenAPI, Composer, NPM, Linux Environment")
        ]
        for cat, val in skills:
            sk_row = Table([[Paragraph(cat, st['SkillCat']), Paragraph(val, st['SkillVal'])]], colWidths=[135, 400] if pages == 1 else [135, 396])
            sk_row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5)]))
            story.append(sk_row)

    doc.build(story)
    doc_fitz = fitz.open(filename)
    print(f"Generated {filename}: {len(doc_fitz)} page(s) (Target: {pages})")
    assert len(doc_fitz) == pages, f"Error: {filename} has {len(doc_fitz)} pages instead of {pages}"
    return filename

# ==========================================
# 2. GENERATE MASTER TECHNICAL PORTFOLIO (10 PAGES - BLACK TEXT ONLY)
# ==========================================
def build_black_master_portfolio(lang='id'):
    filename = f"Portofolio_Lengkap_Yoginara_{lang.upper()}.pdf" if lang == 'id' else f"Portfolio_Master_Yoginara_{lang.upper()}.pdf"
    
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
    )
    
    base = getSampleStyleSheet()
    pst = {
        'CoverTitle': ParagraphStyle('CoverTitle', fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=BLACK),
        'CoverSubtitle': ParagraphStyle('CoverSubtitle', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=BLACK),
        'SectionTitle': ParagraphStyle('SectionTitle', fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=BLACK, spaceBefore=4, spaceAfter=2),
        'CardHeading': ParagraphStyle('CardHeading', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=BLACK),
        'CardSub': ParagraphStyle('CardSub', fontName='Helvetica-Bold', fontSize=8, leading=11, textColor=BLACK),
        'Body': ParagraphStyle('Body', fontName='Helvetica', fontSize=8, leading=11.5, textColor=BLACK, alignment=TA_JUSTIFY),
        'BodyBullet': ParagraphStyle('BodyBullet', fontName='Helvetica', fontSize=8, leading=11.5, textColor=BLACK, leftIndent=9, firstLineIndent=-9),
        'MetaKey': ParagraphStyle('MetaKey', fontName='Helvetica-Bold', fontSize=7.5, leading=10, textColor=BLACK),
        'MetaVal': ParagraphStyle('MetaVal', fontName='Helvetica', fontSize=7.5, leading=10, textColor=BLACK),
        'MetricBig': ParagraphStyle('MetricBig', fontName='Helvetica-Bold', fontSize=11, leading=13, textColor=BLACK, alignment=TA_CENTER),
        'MetricLbl': ParagraphStyle('MetricLbl', fontName='Helvetica', fontSize=6.8, leading=8.5, textColor=BLACK, alignment=TA_CENTER)
    }
    
    story = []

    # ----------------------------------------------------
    # HALAMAN 1: COVER & EXECUTIVE CANDIDATE DOSSIER
    # ----------------------------------------------------
    t_doc = "MASTER TECHNICAL PORTFOLIO & ARCHITECTURE DOSSIER" if lang == 'en' else "DOKUMEN MASTER PORTOFOLIO TEKNIKAL & ARSITEKTUR"
    t_cand = "YOGINARA PRATAMA SITORUS, S.Tr.Kom"
    t_sub = "Full-Stack Web Developer & Software Engineer | Applied Informatics Engineering ULBI" if lang == 'en' else "Fullstack Web Developer & Software Engineer | Sarjana Terapan Komputer ULBI"
    
    hdr = Table([
        [Paragraph(t_doc, pst['CoverSubtitle']), Paragraph('<a href="https://yoginara.github.io/cv_yogiganteng/"><font color="#000000">yoginara.github.io/cv_yogiganteng</font></a>', ParagraphStyle('HR', fontName='Helvetica-Bold', fontSize=8, textColor=BLACK, alignment=TA_RIGHT))],
        [Paragraph(t_cand, pst['CoverTitle']), Paragraph("", ParagraphStyle('ST', fontName='Helvetica-Bold', fontSize=8, textColor=BLACK, alignment=TA_RIGHT))],
        [Paragraph(t_sub, pst['CardSub']), Paragraph("Bandung, Jawa Barat, ID", ParagraphStyle('LC', fontName='Helvetica', fontSize=8, textColor=BLACK, alignment=TA_RIGHT))]
    ], colWidths=[385, 138])
    hdr.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1)]))
    story.append(hdr)
    story.append(HRFlowable(width="100%", thickness=1.5, color=LINE_BLACK, spaceBefore=3, spaceAfter=6))

    # Metric Banner (Monochrome Black Text)
    m1_lbl = "Undergraduate GPA (ULBI)" if lang == 'en' else "IPK Sarjana Terapan ULBI"
    m2_lbl = "Enterprise Codebase LoC" if lang == 'en' else "Skala Kode Enterprise BUMD"
    m3_lbl = "Automated QA Passed" if lang == 'en' else "Automated QA Tests Green"
    m4_lbl = "BNSP National License" if lang == 'en' else "Lisensi Resmi BNSP RI"
    
    mb = Table([
        [
            Paragraph("<b>3,56 / 4,00</b>", pst['MetricBig']),
            Paragraph("<b>116.000+ LoC</b>", pst['MetricBig']),
            Paragraph("<b>100% Passed</b>", pst['MetricBig']),
            Paragraph("<b>BNSP Certified</b>", pst['MetricBig']),
        ],
        [
            Paragraph(m1_lbl, pst['MetricLbl']),
            Paragraph(m2_lbl, pst['MetricLbl']),
            Paragraph(m3_lbl, pst['MetricLbl']),
            Paragraph(m4_lbl, pst['MetricLbl']),
        ]
    ], colWidths=[130, 130, 130, 133], style=[
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT_GRAY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_BLACK),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ])
    story.append(mb)
    story.append(Spacer(1, 6))

    sec1_t = "1. Profil Eksekutif & Ringkasan Kapabilitas Rekayasa" if lang == 'id' else "1. Executive Profile & Engineering Competency Summary"
    story.append(Paragraph(sec1_t, pst['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE_BLACK, spaceBefore=1, spaceAfter=4))

    p_img = []
    if os.path.exists('foto_profil.jpeg'):
        p_img.append(Image('foto_profil.jpeg', width=110, height=145))

    bio_text = (
        "Yoginara Pratama Sitorus adalah Software Engineer dan Fullstack Developer berlatar belakang Sarjana Terapan Komputer (S.Tr.Kom) dari Universitas Logistik dan Bisnis Internasional (ULBI) dengan IPK 3,56. Menguasai arsitektur backend berskala korporat (Laravel 12, CodeIgniter 3, Golang Fiber), optimasi kueri basis data relasional (MySQL, Oracle OCI8) dan NoSQL (MongoDB), pengujian mutu otomatis (TDD PHPUnit 11), kepatuhan keamanan OWASP Top 10, serta memegang lisensi resmi BNSP Teknisi Muda Jaringan Komputer."
        if lang == 'id' else
        "Yoginara Pratama Sitorus is a Software Engineer and Full-Stack Developer holding an Applied Bachelor of Informatics Engineering degree from Universitas Logistik dan Bisnis Internasional (ULBI) with a 3.56 GPA. He specializes in enterprise backend architecture (Laravel 12, CodeIgniter 3, Golang Fiber), database query optimization (MySQL, Oracle OCI8, MongoDB), automated test-driven development (PHPUnit 11), OWASP Top 10 security mitigation, and holds official BNSP Network Technician certification."
    )

    p_box = [
        Paragraph(bio_text, pst['Body']),
        Spacer(1, 4),
        Table([
            [
                Paragraph("<b>Backend Engineering:</b><br/>&bull; Laravel 12 Enterprise<br/>&bull; CodeIgniter 3 MVC<br/>&bull; Golang 1.22 & GoFiber<br/>&bull; RESTful Microservices", pst['Body']),
                Paragraph("<b>Database & Storage:</b><br/>&bull; MySQL & MariaDB (3NF)<br/>&bull; Oracle Enterprise OCI8<br/>&bull; MongoDB Atlas (NoSQL)<br/>&bull; INNER JOIN Optimization", pst['Body']),
                Paragraph("<b>QA & Infrastructure:</b><br/>&bull; PHPUnit 11 (Automated)<br/>&bull; OWASP Top 10 Mitigation<br/>&bull; BNSP Computer Network<br/>&bull; Git & GitHub CI/CD", pst['Body']),
            ]
        ], colWidths=[135, 135, 138], style=[
            ('BACKGROUND', (0,0), (-1,-1), BG_ALT_GRAY),
            ('BOX', (0,0), (-1,-1), 1, BORDER_BLACK),
            ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_BLACK),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ])
    ]

    story.append(Table([[p_img, p_box]], colWidths=[120, 403], style=[
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(Spacer(1, 6))

    story.append(Table([
        [
            Paragraph("<b>Email:</b> yoginara2004@gmail.com", pst['MetaKey']),
            Paragraph("<b>WhatsApp:</b> +62 813-6064-0668", pst['MetaKey']),
            Paragraph("<b>GitHub:</b> github.com/Yoginara", pst['MetaKey']),
            Paragraph("<b>Domisili:</b> Bandung, ID", pst['MetaKey']),
        ]
    ], colWidths=[140, 130, 130, 123], style=[
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT_GRAY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))

    # ----------------------------------------------------
    # HALAMAN 2: STUDI KASUS ENTERPRISE 1 - E-GRC (BAGIAN 1)
    # ----------------------------------------------------
    story.append(PageBreak())
    h2_title = "2. Studi Kasus Enterprise: Sistem e-GRC Perumda Tirta Raharja (Bagian 1)" if lang == 'id' else "2. Enterprise Case Study: e-GRC Suite at Perumda Tirta Raharja (Part 1)"
    story.append(Paragraph(h2_title, pst['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE_BLACK, spaceBefore=1, spaceAfter=4))

    egrc_t1 = Table([
        [Paragraph("<b>Instansi / Client:</b> Perumda Air Minum Tirta Raharja (BUMD)", pst['MetaVal']), Paragraph("<b>Peran:</b> Fullstack Web Developer Intern", pst['MetaVal'])],
        [Paragraph("<b>Skala Codebase:</b> 116.000+ LoC &bull; 203 Controllers &bull; 188 Models", pst['MetaVal']), Paragraph("<b>Lingkup:</b> ERM Risk, SPI Audit, GCG & KPI", pst['MetaVal'])],
        [Paragraph("<b>Tech Stack:</b> PHP CodeIgniter 3 MVC, MySQL, Oracle DB OCI8", pst['MetaVal']), Paragraph("<b>Standar:</b> ISO 31000:2018 ERM & Audit BPKP", pst['MetaVal'])],
    ], colWidths=[260, 263], style=[
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT_GRAY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_BLACK),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ])
    story.append(egrc_t1)
    story.append(Spacer(1, 4))

    img_egrc = []
    if os.path.exists('assets/thumb_egrc.png'):
        img_egrc.append(Image('assets/thumb_egrc.png', width=130, height=180))

    egrc_text_p1 = [
        Paragraph("<b>A. Konteks Bisnis & Masalah Operasional:</b>", pst['CardHeading']),
        Paragraph(
            "Perumda Air Minum Tirta Raharja merupakan BUMD penyedia air minum vital di Kabupaten Bandung, Cimahi, dan Bandung Barat. Sebelum sistem terpusat diimplementasikan, pendokumentasian manajemen risiko tersebar di spreadsheet masing-masing cabang (Cabang I-IV) dan divisi. Hal ini menimbulkan keterlambatan konsolidasi berbulan-bulan, ketidaksinkronan data ke Dewan Pengawas, serta lemahnya audit trail bagi Satuan Pengawas Intern (SPI)."
            if lang == 'id' else
            "Perumda Air Minum Tirta Raharja is a vital regional utility BUMD serving Bandung Regency, Cimahi, and West Bandung. Before centralized e-GRC deployment, risk management was fragmented across manual spreadsheets in branch offices and divisions, causing prolonged consolidation lags and lack of transparent audit trails for regulatory compliance."
        , pst['Body']),
        Spacer(1, 3),
        Paragraph("<b>B. Rekayasa Algoritma Risiko Residu Dinamis (ISO 31000:2018):</b>", pst['CardHeading']),
        Paragraph(
            "Yoginara mengatasi kelemahan penentuan risiko manual dengan merancang kalkulasi reaktif sisi-klien di <code>risk_analisisdetail.php</code> berbasis ISO 31000:2018. Penurunan kemungkinan dan dampak dihitung otomatis secara proporsional terhadap realisasi fisik: <i>nilaiPenurunan = Efektivitas &times; (% Progres / 100)</i>, diproteksi batas bawah level 1 (skala 1 s.d. 5). Inovasi ini menjamin akurasi matematis 100% dan mencegah manipulasi data risiko pada laporan profil risiko korporat."
            if lang == 'id' else
            "Yoginara engineered a client-side reactive calculation engine in <code>risk_analisisdetail.php</code> adhering to ISO 31000:2018: <i>Risk Reduction = Effectiveness &times; (% Progress / 100)</i> with floor level 1 protections. This mathematical model guarantees proportional risk reduction and prevents falsified corporate risk documentation."
        , pst['Body']),
        Spacer(1, 3),
        Paragraph("<b>C. Matriks Risiko 5x5 Heatmap & Kategori:</b>", pst['CardHeading']),
        Paragraph(
            "Sistem mengintegrasikan visualisasi matriks 5x5 dinamis: Sangat Tinggi (16-25, mitigasi darurat direksi), Tinggi (9-15, rencana penanganan terukur PIC manajer), Sedang (4-8, SOP monitoring rutin), dan Rendah (1-3, batas toleransi risiko)."
            if lang == 'id' else
            "The system integrates dynamic 5x5 heatmaps categorizing residual risk into Extreme (16-25), High (9-15), Moderate (4-8), and Low (1-3) with automatic Top 10 Corporate Risk escalations."
        , pst['Body'])
    ]

    story.append(Table([[img_egrc, egrc_text_p1]], colWidths=[140, 383], style=[
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))

    # ----------------------------------------------------
    # HALAMAN 3: STUDI KASUS ENTERPRISE 1 - E-GRC (BAGIAN 2)
    # ----------------------------------------------------
    story.append(PageBreak())
    h3_title = "2. Studi Kasus Enterprise: Sistem e-GRC Perumda Tirta Raharja (Bagian 2)" if lang == 'id' else "2. Enterprise Case Study: e-GRC Suite at Perumda Tirta Raharja (Part 2)"
    story.append(Paragraph(h3_title, pst['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE_BLACK, spaceBefore=1, spaceAfter=4))

    story.append(Paragraph("<b>D. Restrukturisasi Laporan Kertas Kerja Profil Risiko (Commit 5d6c824):</b>", pst['CardHeading']))
    story.append(Paragraph(
        "Kertas Kerja Profil Risiko merupakan dokumen inti yang dituntut auditor eksternal (BPKP dan KAP). Yoginara merefaktor <code>Laporan_kertas_kerja.php</code> dan view cetak, mengganti label ambigu dengan standarisasi modern UC/C (Uncontrollable / Controllable), memetakan relasi hierarki (Sasaran Strategis &bull; Sasaran Unit &bull; Kegiatan &bull; Risiko), dan menambahkan kolom output mitigasi terukur beserta tanggal pelaksanaan."
        if lang == 'id' else
        "The Risk Working Paper is the primary formal document audited by government inspectors (BPKP). Yoginara refactored <code>Laporan_kertas_kerja.php</code>, standardizing UC/C taxonomies, establishing strategic objective hierarchies, and mapping mitigation completion milestones."
    , pst['Body']))
    story.append(Spacer(1, 4))

    refact_data = [
        [Paragraph("<b>Elemen Kolom</b>", pst['MetaKey']), Paragraph("<b>Kondisi Sebelum Refactoring</b>", pst['MetaKey']), Paragraph("<b>Penyempurnaan oleh Yoginara</b>", pst['MetaKey'])],
        [Paragraph("Konteks Operasional", pst['MetaVal']), Paragraph("Label membingungkan ('Operasional N, Ab, E')", pst['Body']), Paragraph("Standardisasi UC/C (Uncontrollable / Controllable)", pst['Body'])],
        [Paragraph("Konteks Sasaran", pst['MetaVal']), Paragraph("Hanya sasaran umum perusahaan", pst['Body']), Paragraph("Pemisahan Sasaran Strategis Korporat & Sasaran Unit", pst['Body'])],
        [Paragraph("Kegiatan Kerja", pst['MetaVal']), Paragraph("Kolom kegiatan tidak terpetakan", pst['Body']), Paragraph("Pemetaan relasional otomatis dari model Risk_kegiatanModel", pst['Body'])],
        [Paragraph("Output Mitigasi", pst['MetaVal']), Paragraph("Deskripsi singkat tanpa jadwal pasti", pst['Body']), Paragraph("Ditambahkan kolom Output Penurunan & Jadwal Mulai-Selesai", pst['Body'])],
    ]
    story.append(Table(refact_data, colWidths=[120, 200, 203], style=[
        ('BACKGROUND', (0,0), (-1,0), BG_LIGHT_GRAY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_BLACK),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>E. Arsitektur Dual-Database & Standar AI Coding Assistant:</b>", pst['CardHeading']))
    egrc_p2_bullets = [
        "<b>Abstraksi ADODB Modular:</b> Menghubungkan MySQL/MariaDB dan Oracle Enterprise (OCI8) via driver kustom (<code>_DB_mysqli_driver</code> & <code>_DB_oci8_driver</code>), memungkinkan replikasi dan query silang tanpa mengubah logika aplikasi.",
        "<b>Eliminasi Null Pointers:</b> Menambahkan filter integritas <code>deleted_date IS NULL</code> pada seluruh subquery relasi bertingkat, mencegah crash data kosong.",
        "<b>Efisiensi Bisnis Nyata 85%:</b> Memangkas waktu kompilasi dokumen profil risiko dari <b>~10 hari kerja menjadi hitungan detik</b> siap cetak.",
        "<b>Pedoman Tim (.github/copilot-instructions.md):</b> Menginisiasi dokumentasi standar arsitektur kelas inti (<code>_adminController</code>, <code>_Model</code>) dan aturan integrasi asisten AI demi kontinuitas kualitas kode."
    ] if lang == 'id' else [
        "<b>Modular ADODB Abstraction:</b> Orchestrated transparent persistence across MySQL/MariaDB and Oracle Enterprise OCI8 via custom drivers without altering business logic.",
        "<b>Null Pointer Elimination:</b> Enforced strict <code>deleted_date IS NULL</code> filtration across multi-tiered subqueries, ensuring zero empty-pointer exceptions.",
        "<b>85% Reporting Acceleration:</b> Slashed quarterly report compilation cycles from <b>~10 business days to automated instantaneous generation</b>.",
        "<b>Copilot Architecture Guide:</b> Authored <code>.github/copilot-instructions.md</code> codifying base controller conventions and AI programming standards."
    ]
    for b in egrc_p2_bullets:
        story.append(Paragraph(f"&bull; {b}", pst['BodyBullet']))
        story.append(Spacer(1, 1.5))

    # ----------------------------------------------------
    # HALAMAN 4: STUDI KASUS FRAMEWORK MODERN - CMI PORTAL (BAGIAN 1)
    # ----------------------------------------------------
    story.append(PageBreak())
    h4_title = "3. Studi Kasus Framework Modern: CMI Portal Laravel 12 Engine (Bagian 1)" if lang == 'id' else "3. Modern Architecture Case Study: CMI Portal Laravel 12 Engine (Part 1)"
    story.append(Paragraph(h4_title, pst['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE_BLACK, spaceBefore=1, spaceAfter=4))

    cmi_meta = Table([
        [Paragraph("<b>Proyek:</b> CMI Content Management System (CMI Artikel)", pst['MetaVal']), Paragraph("<b>Framework:</b> Laravel 12.0 &bull; PHP 8.2+ &bull; Tailwind CSS v3", pst['MetaVal'])],
        [Paragraph("<b>Status Mutu:</b> 100% Passed (39 Tests &bull; 134 Assertions)", pst['MetaVal']), Paragraph("<b>Keamanan:</b> OWASP Top 10 &bull; Gate Policy Authorization", pst['MetaVal'])],
        [Paragraph("<b>Query Builder:</b> INNER JOIN Indexed &bull; Paginasi 10 Record", pst['MetaVal']), Paragraph("<b>Alokasi Memori PHP:</b> Terkontrol Stabil di < 8 MB", pst['MetaVal'])],
    ], colWidths=[260, 263], style=[
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT_GRAY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_BLACK),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ])
    story.append(cmi_meta)
    story.append(Spacer(1, 4))

    img_cmi = []
    if os.path.exists('assets/thumb_cmi.png'):
        img_cmi.append(Image('assets/thumb_cmi.png', width=130, height=180))

    cmi_text_p1 = [
        Paragraph("<b>A. Arsitektur Presentasi & Pemisahan Dependensi:</b>", pst['CardHeading']),
        Paragraph(
            "Sistem dibangun dengan pola Model-View-Controller (MVC) modular dan pemisahan layout yang tegas antara antarmuka publik (<code>PublicLayout</code>) dan dasbor terproteksi admin (<code>AppLayout</code>). Seluruh mutasi data diverifikasi oleh Form Request terisolasi dengan otentikasi berbasis Laravel Breeze dan proteksi CSRF otomatis."
            if lang == 'id' else
            "Architected on modular Laravel 12 MVC patterns with strict separation between public presentation layouts and authenticated administrative dashboards, enforced through isolated Form Requests and CSRF middleware."
        , pst['Body']),
        Spacer(1, 3),
        Paragraph("<b>B. Algoritma Pembuatan Slug Unik Otomatis (Anti-Kolisi):</b>", pst['CardHeading']),
        Paragraph(
            "Mengatasi crash database unik saat artikel memiliki judul identik, Yoginara membangun algoritma penomoran berurut otomatis: <code>generateUniqueSlug($judul, $ignoreId)</code>. Algoritma memastikan judul pertama menghasilkan slug bersih (misal: <code>belajar-laravel</code>), dan artikel berikutnya otomatis bertransformasi menjadi <code>belajar-laravel-1</code>, <code>belajar-laravel-2</code> tanpa error database."
            if lang == 'id' else
            "Implemented an automated collision-free slug generation algorithm handling duplicate article titles via sequential indexing, preserving clean SEO URLs without unique constraint violations."
        , pst['Body']),
        Spacer(1, 3),
        Paragraph("<b>C. Manajemen Siklus Hidup Berkas Media (Flysystem):</b>", pst['CardHeading']),
        Paragraph(
            "Unggahan berkas gambar divalidasi biner MIME-type asli (maks 2MB), diberi nama hash acak, dan disimpan di storage publik terabstraksi. Saat artikel diperbarui atau dihapus, sistem secara proaktif menghapus berkas fisik lama dari disk via <code>Storage::disk('public')->delete()</code>, mengeliminasi sampah penyimpanan (orphaned files) secara permanen."
            if lang == 'id' else
            "Integrated automated media lifecycle management using Flysystem, enforcing binary MIME inspection and proactively purging obsolete storage files upon article modification or deletion."
        , pst['Body'])
    ]

    story.append(Table([[img_cmi, cmi_text_p1]], colWidths=[140, 383], style=[
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))

    # ----------------------------------------------------
    # HALAMAN 5: STUDI KASUS CMI (BAGIAN 2) - QUERY OPTIMIZATION & QA
    # ----------------------------------------------------
    story.append(PageBreak())
    h5_title = "3. Studi Kasus Framework Modern: CMI Portal Laravel 12 Engine (Bagian 2)" if lang == 'id' else "3. Modern Architecture Case Study: CMI Portal Laravel 12 Engine (Part 2)"
    story.append(Paragraph(h5_title, pst['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE_BLACK, spaceBefore=1, spaceAfter=4))

    story.append(Paragraph("<b>D. Optimasi Kueri Basis Data (Query Builder INNER JOIN):</b>", pst['CardHeading']))
    story.append(Paragraph(
        "Menjawab spesifikasi teknis penggabungan entitas artikel dan pengguna dengan performa tinggi, sistem mengimplementasikan Laravel Query Builder dengan klausul <code>INNER JOIN</code> terindeks B-Tree, aliasing kolom (<code>articles.judul AS title</code>), penyaringan status publikasi (status = 1), pengurutan kronologis terbalik (<code>created_at DESC</code>), serta paginasi 10 baris dengan preservasi kata kunci pencarian (<code>withQueryString()</code>). Alokasi memori PHP tetap stabil di &lt; 8 MB."
        if lang == 'id' else
        "Engineered relational article-author reporting using Laravel Query Builder with indexed <code>INNER JOIN</code> clauses, column aliasing, publication status filtering, and 10-row pagination with query string preservation, maintaining RAM consumption strictly under 8 MB."
    , pst['Body']))
    story.append(Spacer(1, 3))

    q_eval = [
        [Paragraph("<b>Metode Eksekusi</b>", pst['MetaKey']), Paragraph("<b>Performa Kueri</b>", pst['MetaKey']), Paragraph("<b>Integritas Relasi</b>", pst['MetaKey']), Paragraph("<b>Kesesuaian Spesifikasi</b>", pst['MetaKey'])],
        [Paragraph("INNER JOIN (Terpilih)", pst['MetaVal']), Paragraph("Tinggi (B-Tree Index)", pst['Body']), Paragraph("Sangat Baik: Menghilangkan orphaned record", pst['Body']), Paragraph("100% Sesuai Spesifikasi Soal 2", pst['Body'])],
        [Paragraph("LEFT JOIN", pst['MetaVal']), Paragraph("Sedang", pst['Body']), Paragraph("Berpotensi NULL jika foreign key putus", pst['Body']), Paragraph("Kurang tepat untuk data wajib relasi", pst['Body'])],
        [Paragraph("Subquery / Eloquent N+1", pst['MetaVal']), Paragraph("Rendah (Overhead I/O)", pst['Body']), Paragraph("Tergantung eager loading relasi ORM", pst['Body']), Paragraph("Rawan bottleneck N+1 query", pst['Body'])],
    ]
    story.append(Table(q_eval, colWidths=[120, 110, 160, 133], style=[
        ('BACKGROUND', (0,0), (-1,0), BG_LIGHT_GRAY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_BLACK),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>E. Audit Keamanan OWASP Top 10 & Pengujian Mutu Otomatis (PHPUnit 11):</b>", pst['CardHeading']))
    cmi_qa_bullets = [
        "<b>SQL Injection Prevention (A03:2021):</b> Seluruh interaksi database dieksekusi via Parameterized PDO Prepared Statements bebas concantenation query mentah.",
        "<b>Cross-Site Scripting / XSS (A03:2021):</b> Template Blade mengeksekusi <code>htmlspecialchars()</code> secara otomatis pada kurung kurawal ganda.",
        "<b>Cross-Site Request Forgery / CSRF (A01:2021):</b> Dilindungi token kriptografis <code>@csrf</code> dan verifikasi Synchronizer Token Pattern oleh kernel middleware.",
        "<b>IDOR Broken Access Control (A01:2021):</b> Otorisasi kepemilikan ketat via <code>ArticlePolicy</code> (modifikasi langsung ID artikel menghasilkan respon 403 Forbidden).",
        "<b>Verifikasi Mutu 100% Green:</b> Sebanyak <b>39 pengujian unit & fitur (134 assertions)</b> berhasil lulus sempurna menggunakan PHPUnit 11 pada SQLite in-memory."
    ] if lang == 'id' else [
        "<b>SQL Injection Prevention:</b> 100% database interactions executed via Parameterized PDO Prepared Statements.",
        "<b>Cross-Site Scripting (XSS):</b> Blade template engine executes automated <code>htmlspecialchars()</code> sanitization.",
        "<b>CSRF Protection:</b> Cryptographic tokens and Synchronizer Token Pattern middleware defend all state-mutating requests.",
        "<b>IDOR Prevention:</b> Strict ownership validation in <code>ArticlePolicy</code> restricts modifications to legitimate resource creators.",
        "<b>100% Green Automated QA:</b> 39 automated unit and feature tests with 134 assertions completely passed using PHPUnit 11."
    ]
    for b in cmi_qa_bullets:
        story.append(Paragraph(f"&bull; {b}", pst['BodyBullet']))
        story.append(Spacer(1, 1))

    # ----------------------------------------------------
    # HALAMAN 6: STUDI KASUS MIKROSERVIS GOLANG (STEPUP & MANUKSHOP)
    # ----------------------------------------------------
    story.append(PageBreak())
    h6_title = "4. Portofolio High-Performance Backend: Mikroservis Golang 1.22" if lang == 'id' else "4. High-Performance Backend Portfolio: Go (Golang 1.22) Microservices"
    story.append(Paragraph(h6_title, pst['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE_BLACK, spaceBefore=1, spaceAfter=4))

    img_stepup = []
    if os.path.exists('assets/thumb_stepup.png'):
        img_stepup.append(Image('assets/thumb_stepup.png', width=130, height=180))

    go_desc = [
        Paragraph("<b>A. StepUp Footwear E-Commerce Platform & High-Concurrency REST API:</b>", pst['CardHeading']),
        Paragraph(
            "StepUp dirancang untuk menangani beban transaksi e-commerce dan katalog produk alas kaki dengan volume tinggi. Ditenagai oleh engine <b>Go (Golang 1.22)</b> dan framework <b>GoFiber v2 (FastHTTP)</b> yang memiliki performa alokasi memori mendekati nol dan latensi sub-milidetik. Basis data memanfaatkan <b>MongoDB Atlas NoSQL</b> dengan pola indexing teroptimasi, autentikasi berbasis JWT token stateless, enkripsi sandi Bcrypt, serta proteksi CORS ketat."
            if lang == 'id' else
            "StepUp is an e-commerce backend built to sustain high transactional concurrency. Powered by Go 1.22 and GoFiber v2 (FastHTTP core), it delivers sub-millisecond response latencies, zero-allocation routing, MongoDB Atlas cloud storage, stateless JWT authentication, and Bcrypt security."
        , pst['Body']),
        Spacer(1, 3),
        Paragraph("<b>B. ManukShop Livestock Management & OpenAPI Documentation:</b>", pst['CardHeading']),
        Paragraph(
            "Platform manajemen peternakan dan e-commerce komoditas unggas terintegrasi. Mengimplementasikan arsitektur mikroservis Golang dengan basis data MongoDB Cloud berbasis pola <i>embedded snapshot pattern</i> untuk preservasi riwayat transaksi. Dilengkapi dokumentasi interaktif <b>OpenAPI / Swagger 3.0</b> untuk pengujian endpoint dan antarmuka responsif berbasis Tailwind CSS."
            if lang == 'id' else
            "Integrated livestock management and trading microservice platform in Golang, utilizing embedded NoSQL snapshot modeling, interactive OpenAPI/Swagger 3.0 documentation, and responsive Tailwind CSS interfaces."
        , pst['Body']),
        Spacer(1, 3),
        Paragraph("<b>C. Benchmarking & Metrik Kecepatan Engine Go:</b>", pst['CardHeading']),
        Paragraph(
            "Ditenagai core FastHTTP, pipeline routing GoFiber menangani konkurensi koneksi hingga 10x lebih tinggi dibanding server PHP konvensional, dengan alokasi heap memori yang sangat stabil di bawah 20 MB saat melayani lonjakan request."
            if lang == 'id' else
            "Driven by FastHTTP core architecture, the GoFiber pipeline achieves 10x higher connection concurrency than standard PHP servers while maintaining stable memory consumption below 20 MB under traffic spikes."
        , pst['Body'])
    ]

    story.append(Table([[img_stepup, go_desc]], colWidths=[140, 383], style=[
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))

    # ----------------------------------------------------
    # HALAMAN 7: SISTEM E-GOVERNMENT & KOMUNITAS (RTCONNECT & UD ABANG ADIK)
    # ----------------------------------------------------
    story.append(PageBreak())
    h7_title = "5. Portofolio E-Government & Komunitas: RTConnect & UD Abang Adik" if lang == 'id' else "5. Community Tech & E-Government Systems: RTConnect & UD Abang Adik"
    story.append(Paragraph(h7_title, pst['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE_BLACK, spaceBefore=1, spaceAfter=4))

    img_rt = []
    if os.path.exists('assets/thumb_rtconnect.png'):
        img_rt.append(Image('assets/thumb_rtconnect.png', width=130, height=180))

    comm_desc = [
        Paragraph("<b>A. RTConnect — Platform Administrasi & Transparansi Lingkungan RT:</b>", pst['CardHeading']),
        Paragraph(
            "RTConnect adalah platform digital tata kelola komunitas cerdas (Smart Community Management) berbasis web yang mengotomasi penagihan iuran bulanan warga, pencatatan kas lingkungan transparan, dan penerbitan surat pengantar resmi ber-validator QR publik. Arsitektur dibangun di atas 15+ tabel database relasional ternormalisasi (3NF) dengan multi-role access (Ketua RT, Bendahara, Warga)."
            if lang == 'id' else
            "RTConnect is a digital smart community governance platform automating neighborhood dues billing, real-time fiscal accounting, and official resident certificate issuance with public QR verification, structured across 15+ normalized relational tables."
        , pst['Body']),
        Spacer(1, 3),
        Paragraph("<b>B. Fitur Kunci & Dampak Sosial RTConnect:</b>", pst['CardHeading']),
        Paragraph(
            "&bull; <b>Validasi Dokumen Publik:</b> Setiap surat pengantar memiliki kode QR unik yang dapat dipindai oleh kelurahan/instansi tanpa perlu login ke sistem.<br/>&bull; <b>Audit Kas Lingkungan Real-time:</b> Saldo kas warga tercatat secara transparan dengan bukti nota digital, meniadakan konflik pencatatan manual."
            if lang == 'id' else
            "&bull; <b>Public QR Validation:</b> Official certificates carry unique QR codes verifiable by administrative officers without requiring account logins.<br/>&bull; <b>Real-Time Ledger Auditing:</b> Dues and expenditure balances are transparently logged with digital invoice receipts."
        , pst['Body']),
        Spacer(1, 3),
        Paragraph("<b>C. UD Abang Adik — Arsitektur E-Commerce Zero-Cost:</b>", pst['CardHeading']),
        Paragraph(
            "Mengimplementasikan katalog e-commerce dengan strategi biaya operasional $0/bulan (Zero-Cost Infrastructure). Menerapkan caching cerdas dan mekanisme fallback toleran terhadap kegagalan (fault-tolerant) yang menghasilkan latensi API super cepat &lt; 200 ms dan uptime 100%."
            if lang == 'id' else
            "Implemented an e-commerce product catalog with zero operating costs ($0/month infrastructure), leveraging intelligent caching and fault-tolerant fallbacks achieving sub-200ms API latency."
        , pst['Body'])
    ]

    story.append(Table([[img_rt, comm_desc]], colWidths=[140, 383], style=[
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))

    # ----------------------------------------------------
    # HALAMAN 8: RISET DEEP LEARNING & SISTEM IOT (CIT-TPRO & CO2 AIRBOARD)
    # ----------------------------------------------------
    story.append(PageBreak())
    h8_title = "6. Riset Kecerdasan Buatan & Sistem IoT: CIT-TPRO & CO2 AirBoard" if lang == 'id' else "6. Deep Learning AI Research & IoT Systems: CIT-TPRO & CO2 AirBoard"
    story.append(Paragraph(h8_title, pst['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE_BLACK, spaceBefore=1, spaceAfter=4))

    ai_t = Table([
        [Paragraph("<b>CIT-TPRO: Convolution Interactive Transformer (Riset AI)</b>", pst['CardHeading']), Paragraph("<b>CO2 AirBoard: Sistem Telemetri Kualitas Udara (IoT)</b>", pst['CardHeading'])],
        [
            Paragraph(
                "<b>Laboratorium:</b> AI & Biomedis ULBI (2026)<br/>"
                "<b>Teknologi:</b> Python, PyTorch, Linear Self-Attention O(N)<br/>"
                "<b>Inovasi:</b> Riset arsitektur model hibrida menggabungkan Convolutional Feature Extraction dan Linear Transformer untuk pengenalan emosi berbasis sinyal elektroensefalogram (EEG). Mengintegrasikan fusi fitur PSD (Power Spectral Density) dan DE (Differential Entropy) serta pengujian multi-dataset benchmark internasional (DEAP, DREAMER, SEED-IV) dengan skenario LOSO cross-subject."
                if lang == 'id' else
                "<b>Laboratory:</b> AI & Biomedical Lab ULBI (2026)<br/>"
                "<b>Technology:</b> Python, PyTorch, Linear Attention O(N)<br/>"
                "<b>Innovation:</b> Investigated hybrid Convolutional Transformer architectures with linear attention O(N) and PSD+DE feature fusion for emotion recognition on benchmark EEG datasets (DEAP, DREAMER, SEED-IV)."
            , pst['Body']),
            Paragraph(
                "<b>Domain:</b> Internet of Things (IoT) & Telemetri Lingkungan<br/>"
                "<b>Hardware:</b> Mikrokontroler ESP32, Sensor Gas NDIR CO2<br/>"
                "<b>Sistem:</b> Perancangan perangkat keras pemantau konsentrasi gas CO2 dan parameter lingkungan real-time. Data dikirimkan secara telemetri ke server dan dirender pada dashboard visual interaktif dengan mekanisme batas ambang peringatan otomatis untuk keselamatan ruangan tertutup."
                if lang == 'id' else
                "<b>Domain:</b> IoT & Environmental Telemetry<br/>"
                "<b>Hardware:</b> ESP32 Microcontroller, NDIR CO2 Sensor<br/>"
                "<b>System:</b> Engineered real-time environmental telemetry monitoring ambient CO2 gas concentrations with interactive web dashboards and automated threshold alert systems."
            , pst['Body'])
        ]
    ], colWidths=[261, 262], style=[
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT_GRAY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('INNERGRID', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ])
    story.append(ai_t)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Portofolio Rekayasa Perangkat Lunak Tambahan:</b>", pst['CardHeading']))
    more_sys = Table([
        [
            Paragraph("<b>Sistem RS Online (Healthcare):</b> Manajemen antrean pasien, rekam medis poliklinik, jadwal dokter spesialis, dan sistem penomoran otomatis berbasis role-based access.", pst['Body']),
            Paragraph("<b>Betta Store (E-Commerce):</b> Perancangan front-end toko daring responsif dengan validasi form ketat, widget tree modular, dan antarmuka transaksi modern.", pst['Body'])
        ],
        [
            Paragraph("<b>View of Indonesia (Tourism E-Ticketing):</b> Portal pariwisata terintegrasi dengan pemesanan tiket interaktif dan perbaikan kualitas kode front-end standar industri.", pst['Body']),
            Paragraph("<b>Algoritma & Pemrograman II (Academic Honors):</b> Penguasaan algoritma sorting, searching, binary tree, graph traversal, dan analisis kompleksitas Big-O.", pst['Body'])
        ]
    ], colWidths=[261, 262], style=[
        ('BACKGROUND', (0,0), (-1,-1), BG_ALT_GRAY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('INNERGRID', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ])
    story.append(more_sys)

    # ----------------------------------------------------
    # HALAMAN 9: SERTIFIKASI PROFESI NASIONAL (BNSP RI)
    # ----------------------------------------------------
    story.append(PageBreak())
    h9_title = "7. Lisensi Resmi & Sertifikasi Kompetensi Nasional (BNSP RI)" if lang == 'id' else "7. Official National Competency Certification (BNSP RI)"
    story.append(Paragraph(h9_title, pst['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE_BLACK, spaceBefore=1, spaceAfter=4))

    img_bnsp = []
    if os.path.exists('assets/thumb_bnsp.png'):
        img_bnsp.append(Image('assets/thumb_bnsp.png', width=130, height=180))

    bnsp_desc = [
        Paragraph("<b>BADAN NASIONAL SERTIFIKASI PROFESI (BNSP REPUBLIK INDONESIA)</b>", pst['CardHeading']),
        Paragraph(
            "<b>Kualifikasi Kompetensi:</b> Teknisi Muda Jaringan Komputer (First-Level Computer Network Technician)<br/>"
            "<b>Lembaga Sertifikasi:</b> LSP Universitas Logistik dan Bisnis Internasional (ULBI)<br/>"
            "<b>No. Sertifikat:</b> 62090 3513 5 0000004 2026<br/>"
            "<b>No. Registrasi:</b> JIK.215.00004.2026<br/>"
            "<b>Tanggal Terbit:</b> 29 Oktober 2026 &bull; <b>Masa Berlaku:</b> 3 Tahun (s/d 29 Oktober 2029)"
            if lang == 'id' else
            "<b>Qualification:</b> First-Level Computer Network Technician (Teknisi Muda Jaringan Komputer)<br/>"
            "<b>Certification Body:</b> Lembaga Sertifikasi Profesi (LSP) ULBI<br/>"
            "<b>Certificate No:</b> 62090 3513 5 0000004 2026<br/>"
            "<b>Registration No:</b> JIK.215.00004.2026<br/>"
            "<b>Issue Date:</b> October 29, 2026 &bull; <b>Validity:</b> 3 Years (Through October 29, 2029)"
        , pst['Body']),
        Spacer(1, 3),
        Paragraph("<b>Nilai Tambah bagi Tim Rekayasa Perangkat Lunak:</b>", pst['CardHeading']),
        Paragraph(
            "Memiliki pemahaman mendalam tentang transmisi data paket TCP/IP, perancangan subnetting IP yang efisien, isolasi traffic switch VLAN, serta pengkabelan terstruktur. Keahlian ini memastikan aplikasi web yang dibangun tidak hanya handal di level kode aplikasi, melainkan juga optimal saat beroperasi di atas infrastruktur server dan topologi jaringan riil."
            if lang == 'id' else
            "Provides comprehensive knowledge of TCP/IP packet transmission, network subnetting, VLAN switch configurations, and physical cabling, ensuring software applications perform optimally across underlying network architectures."
        , pst['Body'])
    ]

    story.append(Table([[img_bnsp, bnsp_desc]], colWidths=[140, 383], style=[
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(Spacer(1, 4))

    u_h1 = "<b>Kode Unit</b>" if lang == 'id' else "<b>Unit Code</b>"
    u_h2 = "<b>Judul Unit Kompetensi SKKNI Teruji (Standar Kompetensi Kerja Nasional Indonesia)</b>" if lang == 'id' else "<b>SKKNI National Competency Standard Title</b>"
    
    u_rows = [
        [Paragraph(u_h1, pst['MetaKey']), Paragraph(u_h2, pst['MetaKey'])],
        [Paragraph("J.611000.001.01", pst['MetaVal']), Paragraph("Mengumpulkan Kebutuhan Teknis Pengguna yang Menggunakan Jaringan (Technical Requirements)" if lang == 'id' else "Collecting Technical Requirements of Network Users", pst['MetaVal'])],
        [Paragraph("J.611000.002.01", pst['MetaVal']), Paragraph("Mengumpulkan Data Peralatan Jaringan dengan Teknologi yang Sesuai (Equipment Inventory)" if lang == 'id' else "Collecting Network Equipment Data with Appropriate Technology", pst['MetaVal'])],
        [Paragraph("J.611000.003.02", pst['MetaVal']), Paragraph("Merancang Topologi Jaringan Komputer (Network Topology Design)" if lang == 'id' else "Designing Computer Network Topology", pst['MetaVal'])],
        [Paragraph("J.611000.004.01", pst['MetaVal']), Paragraph("Merancang Pengalamatan Jaringan (IP Addressing, VLSM, Subnetting)" if lang == 'id' else "Designing Network IP Addressing and Subnetting", pst['MetaVal'])],
        [Paragraph("J.611000.005.02", pst['MetaVal']), Paragraph("Menentukan Spesifikasi Perangkat Jaringan (Hardware Specifications)" if lang == 'id' else "Determining Network Device Specifications", pst['MetaVal'])],
        [Paragraph("J.611000.009.02", pst['MetaVal']), Paragraph("Memasang Kabel Jaringan Terstruktur (Structured Cabling UTP/STP/Fiber)" if lang == 'id' else "Installing Structured Network Cabling", pst['MetaVal'])],
        [Paragraph("J.611000.012.02", pst['MetaVal']), Paragraph("Mengkonfigurasi Switch pada Jaringan Komputer (Managed Switch Configuration)" if lang == 'id' else "Configuring Switches on Computer Networks", pst['MetaVal'])],
    ]
    story.append(Table(u_rows, colWidths=[120, 403], style=[
        ('BACKGROUND', (0,0), (-1,0), BG_LIGHT_GRAY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_BLACK),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_BLACK),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))

    # ----------------------------------------------------
    # HALAMAN 10: SERTIFIKASI GLOBAL, MATRIKS LENGKAP & KESIMPULAN
    # ----------------------------------------------------
    story.append(PageBreak())
    h10_title = "8. Kredensial Global, Matriks Keahlian Lengkap & Kesiapan Kerja" if lang == 'id' else "8. Global Credentials, Complete Skills Matrix & Career Readiness"
    story.append(Paragraph(h10_title, pst['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE_BLACK, spaceBefore=1, spaceAfter=4))

    g_certs = [
        ("Oracle Academy", "Java Programming Certificate", "Juni 2023", "Object-Oriented Programming (OOP), Data Structures, Polymorphism & Algorithm Design"),
        ("Oracle Academy", "Java Fundamentals Certificate", "Januari 2023", "Java Core, Data Types, Control Structures & Computational Logic"),
        ("MathWorks", "MATLAB Onramp Course Completion (Score: 100%)", "Maret 2023", "Komputasi Matriks Numerik, Visualisasi Grafis & Analisis Data Matematis"),
        ("Great Learning", "Introduction to JavaScript", "Maret 2024", "DOM Scripting, Modern JavaScript ES6+ & Asynchronous Handling")
    ] if lang == 'id' else [
        ("Oracle Academy", "Java Programming Certificate", "June 2023", "Object-Oriented Programming (OOP), Data Structures, Polymorphism & Algorithm Design"),
        ("Oracle Academy", "Java Fundamentals Certificate", "January 2023", "Java Core, Data Types, Control Structures & Computational Logic"),
        ("MathWorks", "MATLAB Onramp Course Completion (Score: 100%)", "March 2023", "Numerical Matrix Computations, Visualization & Mathematical Processing"),
        ("Great Learning", "Introduction to JavaScript", "March 2024", "DOM Scripting, Modern JavaScript ES6+ & Asynchronous Handling")
    ]
    for org, name, date, desc in g_certs:
        sc_t = Table([
            [Paragraph(f"&bull; <b>{name}</b> &mdash; {org} ({date})", pst['Body']), Paragraph(desc, pst['Body'])]
        ], colWidths=[290, 233], style=[
            ('TOPPADDING', (0,0), (-1,-1), 1),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0)
        ])
        story.append(sc_t)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Matriks Keahlian Komprehensif (Technical Competency Matrix):</b>", pst['CardHeading']))
    full_skills = [
        ("Bahasa Pemrograman:", "PHP 8.2+ (Expert), Go / Golang 1.22, JavaScript (ES6+), Python 3.12, SQL, HTML5, CSS3"),
        ("Framework Backend:", "Laravel 12.x Engine, CodeIgniter 3 MVC, GoFiber v2 (FastHTTP), Blade Templating"),
        ("Basis Data & Storage:", "MySQL, MariaDB (3NF Normalization), Oracle Database (OCI8), MongoDB Atlas (NoSQL), Flysystem"),
        ("Frontend & UI/UX:", "Tailwind CSS v3, Bootstrap 5 Responsive, jQuery, DataTables, Select2, Responsive Web Design"),
        ("Security & Governance:", "OWASP Top 10 Mitigation (CSRF, XSS, SQLi, IDOR), ISO 31000:2018 ERM, SPI Audit Compliance"),
        ("Testing & Quality Assurance:", "PHPUnit 11 (TDD & Automated Unit/Feature Tests), Postman API Testing, Swagger OpenAPI"),
        ("Infrastruktur & Jaringan:", "BNSP Certified Network Technician, TCP/IP, IP Addressing, VLAN Switch, Cabling, Linux Server"),
        ("Tools & Metodologi:", "Git, GitHub CI/CD Workflow, Composer, NPM, Vite, RESTful API Microservices, Scrum/Agile")
    ] if lang == 'id' else [
        ("Programming Languages:", "PHP 8.2+ (Expert), Go / Golang 1.22, JavaScript (ES6+), Python 3.12, SQL, HTML5, CSS3"),
        ("Backend Frameworks:", "Laravel 12.x Engine, CodeIgniter 3 MVC, GoFiber v2 (FastHTTP), Blade Templating"),
        ("Databases & Storage:", "MySQL, MariaDB (3NF Normalization), Oracle Database (OCI8), MongoDB Atlas (NoSQL), Flysystem"),
        ("Frontend & UI/UX:", "Tailwind CSS v3, Bootstrap 5 Responsive, jQuery, DataTables, Select2, Responsive Web Design"),
        ("Security & Governance:", "OWASP Top 10 Mitigation (CSRF, XSS, SQLi, IDOR), ISO 31000:2018 ERM, SPI Audit Compliance"),
        ("Testing & QA:", "PHPUnit 11 (TDD & Automated Unit/Feature Tests), Postman API Testing, Swagger OpenAPI"),
        ("Infrastructure & Network:", "BNSP Certified Network Technician, TCP/IP, IP Addressing, VLAN Switch, Cabling, Linux Server"),
        ("Tools & Methodologies:", "Git, GitHub CI/CD Workflow, Composer, NPM, Vite, RESTful API Microservices, Scrum/Agile")
    ]
    for c, v in full_skills:
        row_s = Table([[Paragraph(c, pst['MetaKey']), Paragraph(v, pst['MetaVal'])]], colWidths=[140, 383], style=[
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0.5),
        ])
        story.append(row_s)
    story.append(Spacer(1, 4))

    final_text = (
        "<b>Pernyataan Kesiapan Karier & Integritas Data:</b><br/>"
        "Seluruh rincian teknis, metrik efisiensi, dan sertifikasi yang tercantum dalam dokumen ini didasarkan pada berkas repositori kode sumber nyata dan sertifikat resmi pemerintah Republik Indonesia. "
        "Yoginara Pratama Sitorus, S.Tr.Kom siap berkontribusi secara langsung sebagai <b>Fullstack Web Developer / Software Engineer</b> baik secara onsite di Bandung, Jakarta, maupun secara hybrid/remote."
        if lang == 'id' else
        "<b>Career Readiness & Data Integrity Statement:</b><br/>"
        "All engineering specifications, efficiency benchmarks, and certifications detailed in this master dossier are fully substantiated by active production repositories and official credentials. "
        "Yoginara Pratama Sitorus, S.Tr.Kom is prepared for immediate deployment as a <b>Full-Stack Web Developer / Software Engineer</b> across onsite, hybrid, and remote engineering environments."
    )
    story.append(Table([[Paragraph(final_text, pst['Body'])]], colWidths=[523], style=[
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT_GRAY),
        ('BOX', (0,0), (-1,-1), 1.5, BORDER_BLACK),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))

    doc.build(story)
    doc_fitz = fitz.open(filename)
    print(f"Generated {filename}: {len(doc_fitz)} page(s) (Target: 10)")
    assert len(doc_fitz) == 10, f"Error: {filename} has {len(doc_fitz)} pages instead of 10"
    return filename

# ==========================================
# 3. GENERATE COVER LETTERS (BLACK TEXT ONLY)
# ==========================================
def build_black_cover_letters():
    base = getSampleStyleSheet()
    st = {
        'Name': ParagraphStyle('Name', fontName='Helvetica-Bold', fontSize=16, leading=20, textColor=BLACK),
        'Title': ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=BLACK),
        'Contact': ParagraphStyle('Contact', fontName='Helvetica', fontSize=8.2, leading=11.5, textColor=BLACK),
        'Date': ParagraphStyle('Date', fontName='Helvetica', fontSize=8.5, leading=12, textColor=BLACK),
        'Recipient': ParagraphStyle('Recipient', fontName='Helvetica', fontSize=8.5, leading=12, textColor=BLACK),
        'Subject': ParagraphStyle('Subject', fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=BLACK),
        'Salutation': ParagraphStyle('Salutation', fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=BLACK),
        'Body': ParagraphStyle('Body', fontName='Helvetica', fontSize=8.5, leading=12.5, textColor=BLACK, alignment=TA_JUSTIFY),
        'Bullet': ParagraphStyle('Bullet', fontName='Helvetica', fontSize=8.5, leading=12, textColor=BLACK, leftIndent=12, firstLineIndent=-12),
        'Sign': ParagraphStyle('Sign', fontName='Helvetica', fontSize=8.5, leading=12, textColor=BLACK),
        'SignName': ParagraphStyle('SignName', fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=BLACK)
    }

    # 1. Indonesian Cover Letter
    doc_id = SimpleDocTemplate("Surat_Lamaran_Yoginara_ID.pdf", pagesize=A4, leftMargin=40, rightMargin=40, topMargin=36, bottomMargin=36)
    story_id = [
        Paragraph("YOGINARA PRATAMA SITORUS, S.Tr.Kom", st['Name']),
        Spacer(1, 2),
        Paragraph("Fullstack Web Developer & Software Engineer", st['Title']),
        Spacer(1, 2),
        Paragraph("Bandung, Jawa Barat, Indonesia &bull; +62 813-6064-0668 &bull; yoginara2004@gmail.com &bull; github.com/Yoginara", st['Contact']),
        HRFlowable(width="100%", thickness=1.2, color=LINE_BLACK, spaceBefore=4, spaceAfter=10),
        Paragraph("Bandung, 04 November 2026", st['Date']),
        Spacer(1, 8),
        Paragraph("<b>Kepada Yth.</b><br/><b>Tim Rekrutmen / Talent Acquisition</b><br/>Perusahaan / Institusi Teknologi Terkemuka<br/>Di Tempat", st['Recipient']),
        Spacer(1, 8),
        Paragraph("<b>Perihal: Lamaran Pekerjaan — Fullstack Web Developer / Software Engineer</b>", st['Subject']),
        Spacer(1, 8),
        Paragraph("Dengan hormat,", st['Salutation']),
        Spacer(1, 4),
        Paragraph("Sehubungan dengan informasi lowongan pekerjaan yang dibuka oleh perusahaan Bapak/Ibu, melalui surat ini saya bermaksud mengajukan diri untuk posisi <b>Fullstack Web Developer / Software Engineer</b>. Saya merupakan lulusan Sarjana Terapan Komputer (S.Tr.Kom) program studi D4 Teknik Informatika dari Universitas Logistik dan Bisnis Internasional (ULBI) dengan predikat Sangat Memuaskan (<b>IPK 3,56 / 4,00</b>), serta memiliki lisensi resmi kompetensi nasional <b>BNSP Republik Indonesia</b> sebagai Teknisi Muda Jaringan Komputer.", st['Body']),
        Spacer(1, 6),
        Paragraph("Selama masa studi dan pengalaman kerja magang di <b>Perumda Air Minum Tirta Raharja (BUMD)</b>, saya terbiasa mengelola sistem perangkat lunak skala enterprise dengan basis kode <b>116.000+ baris kode (LoC)</b>. Beberapa kontribusi kunci yang berhasil saya berikan antara lain:", st['Body']),
        Spacer(1, 4),
        Paragraph("&bull; <b>Rekayasa Algoritma ISO 31000:2018:</b> Mengembangkan model kalkulasi risiko residu dinamis reaktif sisi-klien di <i>risk_analisisdetail.php</i> yang meniadakan manipulasi pelaporan risiko subjektif antar cabang.", st['Bullet']),
        Spacer(1, 2),
        Paragraph("&bull; <b>Akselerasi Pelaporan 85%:</b> Merefaktor mesin Kertas Kerja Profil Risiko BPKP dan audit SPI, memangkas siklus konsolidasi dari ~10 hari kerja menjadi hitungan detik siap cetak.", st['Bullet']),
        Spacer(1, 2),
        Paragraph("&bull; <b>Dual-Database Architecture:</b> Mengelola abstraksi kustom ADODB yang menjembatani persistensi data MySQL/MariaDB dan Oracle Enterprise (OCI8) secara transparan.", st['Bullet']),
        Spacer(1, 2),
        Paragraph("&bull; <b>Penguasaan Framework Modern (Laravel 12 & Golang 1.22):</b> Membangun arsitektur portal CMI dengan Query Builder <i>INNER JOIN</i> terindeks (alokasi memori &lt; 8 MB), mitigasi OWASP Top 10, 39 pengujian otomatis PHPUnit 11 (100% Green), serta mikroservis GoFiber v2 bervolume tinggi.", st['Bullet']),
        Spacer(1, 6),
        Paragraph("Saya memiliki dedikasi tinggi terhadap prinsip <i>Clean Code</i>, <i>Security-by-Design</i>, serta otomasi pengujian mutu perangkat lunak. Kombinasi antara keahlian arsitektur web modern, optimasi basis data, dan fondasi infrastruktur jaringan bersertifikasi BNSP memungkinkan saya untuk segera memberikan dampak nyata dan beradaptasi cepat dengan alur kerja tim rekayasa perangkat lunak di perusahaan Bapak/Ibu.", st['Body']),
        Spacer(1, 6),
        Paragraph("Bersama surat ini, saya lampirkan berkas CV ATS, dokumen Master Portofolio teknikal, dan sertifikat resmi pendukung. Besar harapan saya untuk diberikan kesempatan wawancara guna memaparkan kualifikasi dan kontribusi yang dapat saya berikan secara lebih mendalam. Atas perhatian dan kesempatan yang Bapak/Ibu berikan, saya ucapkan terima kasih.", st['Body']),
        Spacer(1, 10),
        Paragraph("Hormat saya,", st['Sign']),
        Spacer(1, 24),
        Paragraph("<b>Yoginara Pratama Sitorus, S.Tr.Kom</b>", st['SignName']),
        Paragraph("Kontak: +62 813-6064-0668 &bull; yoginara2004@gmail.com", st['Contact'])
    ]
    doc_id.build(story_id)
    doc_fitz_id = fitz.open("Surat_Lamaran_Yoginara_ID.pdf")
    print(f"Generated Surat_Lamaran_Yoginara_ID.pdf: {len(doc_fitz_id)} page(s) (Target: 1)")

    # 2. English Cover Letter
    doc_en = SimpleDocTemplate("Cover_Letter_Yoginara_EN.pdf", pagesize=A4, leftMargin=40, rightMargin=40, topMargin=36, bottomMargin=36)
    story_en = [
        Paragraph("YOGINARA PRATAMA SITORUS, S.Tr.Kom", st['Name']),
        Spacer(1, 2),
        Paragraph("Full-Stack Web Developer & Software Engineer", st['Title']),
        Spacer(1, 2),
        Paragraph("Bandung, Indonesia &bull; +62 813-6064-0668 &bull; yoginara2004@gmail.com &bull; github.com/Yoginara", st['Contact']),
        HRFlowable(width="100%", thickness=1.2, color=LINE_BLACK, spaceBefore=4, spaceAfter=10),
        Paragraph("November 04, 2026", st['Date']),
        Spacer(1, 8),
        Paragraph("<b>To:</b><br/><b>Hiring Manager / Engineering Talent Acquisition</b><br/>Technology Enterprise / Innovation Organization<br/>", st['Recipient']),
        Spacer(1, 8),
        Paragraph("<b>Subject: Application for Full-Stack Web Developer / Software Engineer</b>", st['Subject']),
        Spacer(1, 8),
        Paragraph("Dear Hiring Team,", st['Salutation']),
        Spacer(1, 4),
        Paragraph("I am writing to enthusiastically express my interest in the <b>Full-Stack Web Developer / Software Engineer</b> position at your organization. I hold an Applied Bachelor of Informatics Engineering degree (S.Tr.Kom) from Universitas Logistik dan Bisnis Internasional (ULBI), graduating with distinction (<b>GPA: 3.56 / 4.00</b>), and hold official national accreditation as a <b>First-Level Computer Network Technician certified by BNSP Republic of Indonesia</b>.", st['Body']),
        Spacer(1, 6),
        Paragraph("During my software engineering internship at regional utility <b>Perumda Air Minum Tirta Raharja (BUMD)</b>, I actively maintained and engineered mission-critical modules within an enterprise suite spanning over <b>116,000+ Lines of Code (LoC)</b>. My tangible accomplishments include:", st['Body']),
        Spacer(1, 4),
        Paragraph("&bull; <b>ISO 31000:2018 Algorithmic Modeling:</b> Engineered a reactive client-side residual risk engine in <i>risk_analisisdetail.php</i>, mathematically preventing subjective bias across multi-branch corporate reporting.", st['Bullet']),
        Spacer(1, 2),
        Paragraph("&bull; <b>85% Reporting Workflow Acceleration:</b> Overhauled the formal Risk Working Paper reporting engine, slashing compilation cycles from ~10 business days to instant generation for state regulatory BPKP audits.", st['Bullet']),
        Spacer(1, 2),
        Paragraph("&bull; <b>Dual-Database Architecture:</b> Orchestrated transparent persistence across MySQL/MariaDB and Oracle Enterprise (OCI8) via custom modular ADODB abstractions.", st['Bullet']),
        Spacer(1, 2),
        Paragraph("&bull; <b>Modern Framework & High-Concurrency Systems:</b> Built high-throughput Laravel 12 platforms optimized with indexed <i>INNER JOIN</i> query builder logic (RAM footprint &lt; 8 MB), strict OWASP Top 10 mitigation, 39 automated tests (100% Green), and Go (Golang 1.22) Fiber microservices.", st['Bullet']),
        Spacer(1, 6),
        Paragraph("I am deeply committed to Clean Code, Test-Driven Development (TDD), and Security-by-Design. Combining advanced web framework capabilities with database optimization and certified networking infrastructure, I am prepared to deliver immediate engineering value and seamlessly integrate into your development team.", st['Body']),
        Spacer(1, 6),
        Paragraph("Attached are my ATS-compliant CV, comprehensive Master Technical Portfolio dossier, and official certification proofs. I welcome the opportunity to discuss how my technical qualifications align with your company's mission. Thank you for your time and consideration.", st['Body']),
        Spacer(1, 10),
        Paragraph("Sincerely,", st['Sign']),
        Spacer(1, 24),
        Paragraph("<b>Yoginara Pratama Sitorus, S.Tr.Kom</b>", st['SignName']),
        Paragraph("Contact: +62 813-6064-0668 &bull; yoginara2004@gmail.com", st['Contact'])
    ]
    doc_en.build(story_en)
    doc_fitz_en = fitz.open("Cover_Letter_Yoginara_EN.pdf")
    print(f"Generated Cover_Letter_Yoginara_EN.pdf: {len(doc_fitz_en)} page(s) (Target: 1)")

if __name__ == '__main__':
    print("Building Core Official Documents with PURE BLACK TEXT ONLY...")
    # 2-Page ATS CVs
    build_black_ats_cv('id', pages=2)
    build_black_ats_cv('en', pages=2)

    # Master Portfolios (10 Pages)
    build_black_master_portfolio('id')
    build_black_master_portfolio('en')
    print("\nALL OFFICIAL DOCUMENTS SUCCESSFULLY GENERATED WITH BLACK TEXT ONLY!")
