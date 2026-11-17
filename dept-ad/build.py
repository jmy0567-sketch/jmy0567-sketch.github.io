# 드림애드컴 백화점 광고(갤러리아 홍보부스·매체) 사이트 생성기
# 사용: python build.py  → index.html, cheonan.html, jinju.html, booth.html, sitemap.xml
# 사실만 넣는다. 확인 안 된 값(가격, 센터시티 부스 조건, 대전 매체)은 넣지 않는다.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = 'https://jmy0567-sketch.github.io/dept-ad/'
TEL, TEL_LINK = '1599-3611', 'tel:15993611'
SMS = 'sms:15993611?&body=' + '%5B%EB%B0%B1%ED%99%94%EC%A0%90%20%EA%B4%91%EA%B3%A0%20%EB%AC%B8%EC%9D%98%5D%0A%EC%A7%80%EC%A0%90%3A%20%0A%EA%B4%80%EC%8B%AC%20%EB%A7%A4%EC%B2%B4%3A%20%0A%ED%9D%AC%EB%A7%9D%20%EC%8B%9C%EA%B8%B0%3A%20'
LASTMOD = '2026-11-17'

CSS = r"""
:root{--ink:#14213d;--ink2:#2a3555;--cream:#f7f3ec;--paper:#fffdf9;--gold:#b8925a;--gold2:#8a6a3c;--line:#e6dfd2;--muted:#6b6f7b}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:Pretendard,-apple-system,'Apple SD Gothic Neo','Malgun Gothic',sans-serif;color:var(--ink);background:var(--paper);line-height:1.65;word-break:keep-all;padding-bottom:72px}
img{max-width:100%;display:block}a{color:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:0 18px}
header{position:sticky;top:0;z-index:20;background:rgba(255,253,249,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;gap:14px;height:60px}
.brand{text-decoration:none;font-weight:800;letter-spacing:-.02em;line-height:1.15}
.brand small{display:block;font-size:11px;font-weight:500;color:var(--muted);letter-spacing:0}
nav{margin-left:auto;display:flex;gap:4px;overflow-x:auto;scrollbar-width:none}nav::-webkit-scrollbar{display:none}
nav a{white-space:nowrap;text-decoration:none;font-size:14px;font-weight:600;padding:8px 10px;border-radius:8px}
nav a.on,nav a:hover{background:var(--cream);color:var(--gold2)}
@media(max-width:720px){header .wrap{flex-wrap:wrap;height:auto;padding-top:8px;padding-bottom:6px}nav{margin-left:0;width:100%}}
.hero{position:relative;color:#fff;background:var(--ink);overflow:hidden}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.38}
.hero .wrap{position:relative;padding:72px 18px 64px}
.eyebrow{display:inline-block;font-size:13px;font-weight:700;letter-spacing:.08em;color:var(--gold);text-transform:uppercase}
.hero h1{font-size:clamp(30px,6vw,52px);line-height:1.2;margin:10px 0 14px;letter-spacing:-.03em}
.hero h1 em{font-style:normal;color:#f3d9a8}
.hero p{font-size:17px;max-width:620px;color:#e9e6df;margin:0 0 24px}
.kw{display:block;font-size:14px;font-weight:600;color:#d8cdb8;margin-bottom:8px;letter-spacing:0}
.btns{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;text-decoration:none;font-weight:800;padding:14px 22px;border-radius:999px;font-size:16px}
.btn.gold{background:var(--gold);color:#fff}.btn.line{border:1.5px solid rgba(255,255,255,.6);color:#fff}
.btn.ink{background:var(--ink);color:#fff}
.notice{font-size:13px;color:#cfc8ba;margin-top:22px;max-width:640px}
section{padding:64px 0}section.cream{background:var(--cream)}section.dark{background:var(--ink);color:#fff}
.head{margin-bottom:26px}.head h2{font-size:clamp(24px,4vw,34px);line-height:1.3;margin:6px 0 8px;letter-spacing:-.02em}.head p{margin:0;color:var(--muted);max-width:680px}
section.dark .head p{color:#c9c6bf}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.stat{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:16px;padding:20px}
.stat b{display:block;font-size:28px;color:#f3d9a8;letter-spacing:-.02em}.stat span{font-size:14px;color:#ddd8cd}
.src{font-size:12px;color:#a9a59c;margin-top:12px}
.split{display:grid;grid-template-columns:1.05fr 1fr;gap:34px;align-items:center}
@media(max-width:820px){.split{grid-template-columns:1fr}}
.split img,.card img,.media img{border-radius:16px;width:100%;object-fit:cover}
.checks{list-style:none;padding:0;margin:16px 0 22px}.checks li{padding:9px 0 9px 28px;position:relative;border-bottom:1px solid var(--line)}
.checks li:before{content:"";position:absolute;left:4px;top:17px;width:12px;height:7px;border-left:2.5px solid var(--gold);border-bottom:2.5px solid var(--gold);transform:rotate(-45deg)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;text-decoration:none;display:flex;flex-direction:column}
.card img{border-radius:0;aspect-ratio:16/10}
.card .ph{aspect-ratio:16/10;background:linear-gradient(135deg,var(--ink),var(--ink2));color:#f3d9a8;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:22px;letter-spacing:-.02em;text-align:center;padding:12px}
.card .in{padding:18px}.card h3{margin:0 0 6px;font-size:20px}.card p{margin:0;color:var(--muted);font-size:15px}
.tag{display:inline-block;font-size:12px;font-weight:700;background:var(--cream);color:var(--gold2);border-radius:999px;padding:3px 10px;margin-bottom:8px}
.tag.soon{background:#eef0f4;color:#596079}
.media{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.mcard{background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px}
.mcard img{border-radius:12px;aspect-ratio:4/3;object-fit:cover;margin-bottom:12px}
.mcard h3{margin:0 0 8px;font-size:18px}
.mcard dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:14px}.mcard dt{color:var(--muted)}.mcard dd{margin:0;font-weight:600}
.tbl{overflow-x:auto;border-radius:14px;border:1px solid var(--line);background:#fff}
table{border-collapse:collapse;width:100%;min-width:540px;font-size:15px}
th,td{padding:12px 14px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
thead th{background:var(--ink);color:#fff;font-weight:700}tbody th{white-space:nowrap}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;counter-reset:s}
.step{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px}
.step:before{counter-increment:s;content:counter(s);display:inline-flex;width:30px;height:30px;border-radius:50%;background:var(--gold);color:#fff;font-weight:800;align-items:center;justify-content:center;margin-bottom:8px}
.step h3{margin:0 0 4px;font-size:17px}.step p{margin:0;font-size:14px;color:var(--muted)}
details{background:#fff;border:1px solid var(--line);border-radius:14px;margin-bottom:10px}
summary{cursor:pointer;padding:16px 18px;font-weight:700;list-style:none}summary::-webkit-details-marker{display:none}
summary:after{content:"+";float:right;color:var(--gold);font-weight:800}details[open] summary:after{content:"−"}
details p{margin:0;padding:0 18px 16px;color:var(--ink2)}
.cta{background:var(--ink);color:#fff;border-radius:22px;padding:34px 26px;text-align:center}
.cta h2{margin:0 0 8px;font-size:clamp(24px,4vw,32px)}.cta .big{display:block;font-size:clamp(34px,8vw,52px);font-weight:900;color:#f3d9a8;text-decoration:none;margin:10px 0 16px;letter-spacing:-.02em}
.cta p{color:#cfcabe;margin:0 0 18px}
footer{background:#0e1730;color:#b9b7b0;font-size:13px;padding:34px 0 40px}
footer b{color:#fff}footer a{color:#f3d9a8}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:30;display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:10px 12px calc(10px + env(safe-area-inset-bottom));background:rgba(255,253,249,.96);border-top:1px solid var(--line)}
.bar a{display:flex;align-items:center;justify-content:center;text-decoration:none;font-weight:800;border-radius:12px;padding:13px 6px;font-size:16px}
.bar .t{background:var(--ink);color:#fff}.bar .m{background:var(--gold);color:#fff}
@media(min-width:900px){.bar{left:auto;right:18px;bottom:18px;width:360px;border-radius:16px;border:1px solid var(--line);box-shadow:0 10px 30px rgba(0,0,0,.12)}body{padding-bottom:0}}
.crumb{font-size:13px;color:#d8cdb8;margin-bottom:6px}.crumb a{color:#d8cdb8}
.note{font-size:13px;color:var(--muted);margin-top:10px}
"""

NAV = [('index.html', '홈', 'home'), ('booth.html', '홍보부스', 'booth'), ('cheonan.html', '천안 센터시티', 'cheonan'),
       ('jinju.html', '진주점', 'jinju'), ('index.html#cases', '집행 사례', 'cases'), ('index.html#contact', '문의', 'contact')]

DISCLAIMER = ('드림애드컴은 갤러리아 백화점 천안 센터시티점·진주점의 광고 매체와 홍보부스를 대행하는 광고 회사입니다. '
              '이 사이트는 한화갤러리아의 공식 홈페이지가 아닙니다.')


def page(fn, key, title, desc, img, body, faq=None, crumb=None):
    url = BASE + ('' if fn == 'index.html' else fn)
    graph = [
        {"@type": "LocalBusiness", "@id": BASE + "#biz", "name": "주식회사 드림애드컴", "url": BASE,
         "telephone": "+82-1599-3611", "email": "ad3611@naver.com",
         "address": {"@type": "PostalAddress", "streetAddress": "불당34길 3-16", "addressLocality": "천안시 서북구",
                     "addressRegion": "충청남도", "addressCountry": "KR"}},
        {"@type": "WebPage", "@id": url + "#page", "url": url, "name": title, "description": desc,
         "inLanguage": "ko-KR", "about": {"@id": BASE + "#biz"}, "primaryImageOfPage": BASE + img},
    ]
    if crumb:
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "홈", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]})
    if faq:
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    nav = ''.join(f'<a href="{h}"' + (' class="on"' if k == key else '') + f'>{t}</a>' for h, t, k in NAV)
    faq_html = ''
    if faq:
        faq_html = ('<section class="cream"><div class="wrap"><div class="head"><span class="eyebrow">FAQ</span><h2>자주 묻는 질문</h2></div>'
                    + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq) + '</div></section>')
    html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#14213d">
<meta property="og:type" content="website">
<meta property="og:site_name" content="드림애드컴 백화점 광고">
<meta property="og:locale" content="ko_KR">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE + img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%2314213d'/%3E%3Ctext x='32' y='44' font-size='34' font-weight='900' text-anchor='middle' font-family='Arial' fill='%23f3d9a8'%3ED%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>{CSS}</style>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header><div class="wrap"><a class="brand" href="index.html">드림애드컴<small>백화점 홍보부스 · 광고 대행</small></a><nav aria-label="메뉴">{nav}</nav></div></header>
<main>
{body}
{faq_html}
</main>
<footer><div class="wrap">
<p><b>주식회사 드림애드컴</b> · 백화점 홍보부스·광고 대행<br>대표전화 <a href="{TEL_LINK}">{TEL}</a> · 이메일 <a href="mailto:ad3611@naver.com">ad3611@naver.com</a><br>본사 충남 천안시 서북구 불당34길 3-16</p>
<p>{DISCLAIMER} 갤러리아는 ㈜한화갤러리아의 상표입니다. 광고·부스 문의는 백화점 매장이 아닌 드림애드컴으로 해 주세요.</p>
<p>LED 홍보차·전광판 차량은 <a href="https://jmy0567-sketch.github.io/dreamadcom/" target="_blank" rel="noopener">드림애드컴 LED 홍보차 홈페이지</a> · <a href="https://blog.naver.com/dreamadcom_" target="_blank" rel="noopener">네이버 블로그</a></p>
<p>© 2026 DreamAdcom</p>
</div></footer>
<div class="bar"><a class="t" href="{TEL_LINK}">전화 {TEL}</a><a class="m" href="{SMS}">문자 문의</a></div>
</body>
</html>
"""
    open(os.path.join(HERE, fn), 'w', encoding='utf-8', newline='\n').write(html)
    return fn


CONTACT = f"""<section id="contact"><div class="wrap"><div class="cta">
<h2>원하시는 지점과 시기만 알려 주세요</h2>
<p>비어 있는 자리와 일정을 확인해 바로 안내해 드립니다.</p>
<a class="big" href="{TEL_LINK}">{TEL}</a>
<div class="btns" style="justify-content:center"><a class="btn gold" href="{TEL_LINK}">전화 상담</a><a class="btn line" href="{SMS}">문자로 문의</a></div>
<p class="notice" style="margin:18px auto 0">{DISCLAIMER}</p>
</div></div></section>"""

CASES = [
    ('더샵 천안라크원', '아파트 분양', '천안 센터시티', '1층 서편 엘리베이터홀 벽면', '3,000 × 2,000'),
    ('김이태안과', '병원', '천안 센터시티', '주차장 출구', '3,000 × 2,000'),
    ('천안자생한방병원', '병원', '천안 센터시티', '주차장 입구', '3,000 × 2,000'),
    ('삼성미라클안과의원', '병원', '천안 센터시티', '지하 2층 주차장 입구', '3,000 × 2,000'),
    ('삼성유바디외과', '병원', '천안 센터시티', '지하 1층 서편 엘리베이터홀 벽면', '3,000 × 2,000'),
    ('신불당아트센터', '문화시설', '천안 센터시티', '1층·지하 1층 북편 엘리베이터홀 벽면 / 엘리베이터홀 디지털 포스터', '1,500 × 2,000 / 570 × 1,000'),
]
CASES_TABLE = ('<div class="tbl"><table><thead><tr><th>광고주</th><th>업종</th><th>지점</th><th>자리</th><th>크기 (mm)</th></tr></thead><tbody>'
               + ''.join(f'<tr><th>{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a, b, c, d, e in CASES)
               + '</tbody></table></div><p class="note">광고가 걸리면 전경·근경 사진으로 집행 보고서를 드립니다.</p>')

STEPS = """<div class="steps">
<div class="step"><h3>문의</h3><p>지점, 원하는 자리(부스·벽면·화면), 시기를 알려 주세요</p></div>
<div class="step"><h3>자리·일정 확인</h3><p>비어 있는 매체와 부스 일정을 확인해 제안합니다</p></div>
<div class="step"><h3>계약·디자인</h3><p>매체 크기에 맞춰 디자인하고 백화점 기준에 맞게 준비합니다</p></div>
<div class="step"><h3>게시·사진 보고</h3><p>광고가 걸리면 전경·근경 사진으로 보고드립니다</p></div>
</div>"""

# ---------- 홈 ----------
home_faq = [
    ('백화점 홍보부스는 어떻게 빌리나요?', '원하시는 지점과 날짜를 알려 주시면 비어 있는 일정을 확인해 드립니다. 진주점은 1층 또는 12층 엘리베이터홀에서 10일 단위로 운영합니다. 천안 센터시티점 부스 조건은 상담 때 안내해 드립니다. 1599-3611'),
    ('어느 지점에서 광고할 수 있나요?', '지금은 갤러리아 천안 센터시티점과 진주점 광고를 진행합니다. 대전 타임월드점은 준비 중입니다.'),
    ('디자인도 해 주나요?', '네. 매체 크기에 맞춰 디자인부터 게시, 사진 보고까지 진행합니다.'),
    ('영상 광고도 되나요?', '매체마다 다릅니다. 진주점 LCD 화면은 이미지 광고만 됩니다. 상담 때 정확히 안내해 드립니다.'),
    ('광고비는 얼마인가요?', '지점, 매체, 기간에 따라 다릅니다. 원하시는 자리와 기간을 알려 주시면 견적을 드립니다.'),
]
page('index.html', 'home',
     '드림애드컴 | 갤러리아 백화점 홍보부스·광고 대행 (천안 센터시티·진주)',
     '분양 홍보부스부터 엘리베이터홀·주차장·디지털 포스터 광고까지. 드림애드컴이 갤러리아 백화점 천안 센터시티점·진주점 광고를 대행합니다. 실제 집행 사례, 매체 크기, 진행 순서. 1599-3611',
     'img/booth-apt.jpg', f"""
<section class="hero"><img src="img/booth-apt.jpg" alt="백화점 엘리베이터홀 앞 아파트 분양 홍보부스">
<div class="wrap"><span class="eyebrow">천안 센터시티 · 진주 · 대전 준비 중</span>
<h1><span class="kw">갤러리아 백화점 홍보부스 · 백화점 광고 대행</span>견본주택 열기 전,<br><em>백화점에서 먼저 상담하세요</em></h1>
<p>백화점 안에 분양 홍보부스를 차리고, 엘리베이터홀·주차장·디지털 화면에 광고를 겁니다. 드림애드컴이 자리 확인부터 디자인, 게시, 사진 보고까지 맡습니다.</p>
<div class="btns"><a class="btn gold" href="booth.html">홍보부스 보기</a><a class="btn line" href="#branches">지점 보기</a></div>
<p class="notice">{DISCLAIMER}</p></div></section>

<section class="dark"><div class="wrap"><div class="head"><span class="eyebrow">NUMBERS</span><h2>숫자로 보는 백화점 광고</h2></div>
<div class="stats">
<div class="stat"><b>하루 3.3만 명</b><span>천안 센터시티 주차장 출입구 이용</span></div>
<div class="stat"><b>18기</b><span>천안 센터시티 엘리베이터홀 디지털 포스터</span></div>
<div class="stat"><b>약 5만 명</b><span>진주점 정기 고객 문자(LMS) 발송</span></div>
</div><p class="src">출처: 갤러리아 센터시티·진주점 광고 매체 자료. 날짜·요일에 따라 달라질 수 있습니다.</p></div></section>

<section><div class="wrap split">
<img src="img/booth-apt.jpg" alt="백화점 매장 안 분양 홍보부스와 상담 테이블" loading="lazy">
<div><span class="eyebrow">PROMOTION BOOTH</span><div class="head" style="margin-bottom:0"><h2>요즘 분양 광고는<br>백화점 홍보부스입니다</h2></div>
<ul class="checks">
<li>현수막·전단은 지나치지만, 부스는 <b>손님과 마주 앉아 상담</b>합니다</li>
<li>백화점을 찾는 <b>구매력 있는 지역 손님</b>을 매장 안에서 만납니다</li>
<li>부스와 함께 <b>엘리베이터홀·주차장 광고</b>를 묶으면 같은 손님이 여러 번 봅니다</li>
</ul><a class="btn ink" href="booth.html">홍보부스 자세히</a></div></div></section>

<section class="cream" id="branches"><div class="wrap"><div class="head"><span class="eyebrow">BRANCHES</span><h2>지점별 광고 안내</h2></div>
<div class="cards">
<a class="card" href="cheonan.html"><div class="ph">천안 센터시티점</div><div class="in"><span class="tag">진행 중</span><h3>천안 센터시티</h3><p>주차장 입·출구, 엘리베이터홀 벽면, 디지털 포스터 18기, 홍보부스</p></div></a>
<a class="card" href="jinju.html"><img src="img/jinju-building.jpg" alt="갤러리아 진주점 건물" loading="lazy"><div class="in"><span class="tag">진행 중</span><h3>진주점</h3><p>서문 LED, 에스컬레이터 LCD 10기, 엘리베이터 LCD 4기, 고객 문자, 홍보부스</p></div></a>
<div class="card"><div class="ph">대전 타임월드점</div><div class="in"><span class="tag soon">준비 중</span><h3>대전 타임월드</h3><p>매체·부스 안내를 준비하고 있습니다. 미리 문의 주시면 먼저 안내해 드립니다.</p></div></div>
</div></div></section>

<section id="cases"><div class="wrap"><div class="head"><span class="eyebrow">CASES</span><h2>드림애드컴이 진행한 광고</h2><p>병원·분양·문화시설 광고주가 갤러리아 센터시티를 선택했습니다.</p></div>{CASES_TABLE}</div></section>

<section class="cream"><div class="wrap"><div class="head"><span class="eyebrow">PROCESS</span><h2>진행 순서</h2></div>{STEPS}</div></section>
{CONTACT}""", home_faq)

# ---------- 홍보부스 ----------
booth_faq = [
    ('부스는 며칠 단위로 빌리나요?', '진주점은 10일 단위로 운영합니다. 천안 센터시티점 부스 기간은 상담 때 안내해 드립니다.'),
    ('부스 위치는 어디인가요?', '진주점은 1층 또는 12층 엘리베이터홀입니다. 천안 센터시티점 위치는 상담 때 비어 있는 자리를 확인해 안내해 드립니다.'),
    ('분양 말고 다른 업종도 되나요?', '병원·뷰티·지역 브랜드 등도 상담해 드립니다. 백화점 기준에 따라 가능 여부를 먼저 확인해 드립니다.'),
    ('부스와 광고를 같이 할 수 있나요?', '네. 부스와 엘리베이터홀 벽면·디지털 포스터·주차장 광고를 함께 하면 같은 손님에게 여러 번 보입니다.'),
]
page('booth.html', 'booth',
     '백화점 홍보부스 · 분양 홍보부스 대행 | 갤러리아 천안 센터시티·진주 · 드림애드컴',
     '견본주택 열기 전, 백화점에서 먼저 상담하세요. 갤러리아 진주점 1층·12층 엘리베이터홀 10일 단위 홍보부스, 천안 센터시티 홍보부스 상담. 엘리베이터홀·주차장 광고와 함께. 1599-3611',
     'img/booth-apt.jpg', f"""
<section class="hero"><img src="img/booth-apt.jpg" alt="백화점 분양 홍보부스">
<div class="wrap"><div class="crumb"><a href="index.html">홈</a> / 홍보부스</div><span class="eyebrow">PROMOTION BOOTH</span>
<h1><span class="kw">백화점 홍보부스 · 분양 홍보부스</span>손님이 오는 곳에<br><em>상담 테이블을 놓습니다</em></h1>
<p>아파트 분양 홍보에서 요즘 가장 많이 찾는 방법입니다. 백화점 엘리베이터홀 앞에서 지역 손님과 직접 상담합니다.</p>
<div class="btns"><a class="btn gold" href="{TEL_LINK}">부스 일정 문의 {TEL}</a></div></div></section>

<section><div class="wrap split"><img src="img/booth-apt.jpg" alt="분양 홍보부스 상담 테이블과 안내 배너" loading="lazy">
<div><div class="head" style="margin-bottom:0"><span class="eyebrow">WHY</span><h2>왜 백화점 부스일까요</h2></div>
<ul class="checks">
<li>견본주택 오픈 전부터 <b>관심 고객 상담</b>을 받을 수 있습니다</li>
<li>백화점에 오는 <b>지역 손님</b>을 매장 안에서 만납니다</li>
<li>현수막·전단과 달리 <b>마주 앉아 설명</b>합니다</li>
<li>엘리베이터홀·주차장 광고와 묶으면 <b>부스까지 안내</b>가 이어집니다</li>
</ul></div></div></section>

<section class="cream"><div class="wrap"><div class="head"><span class="eyebrow">BY BRANCH</span><h2>지점별 홍보부스</h2></div>
<div class="tbl"><table><thead><tr><th>지점</th><th>위치</th><th>기간 단위</th><th>함께 쓰면 좋은 매체</th></tr></thead><tbody>
<tr><th>진주점</th><td>1층 또는 12층 엘리베이터홀</td><td>10일 단위</td><td>서문 LED, 에스컬레이터 LCD, 엘리베이터 LCD, 고객 문자</td></tr>
<tr><th>천안 센터시티</th><td>상담 때 안내</td><td>상담 때 안내</td><td>엘리베이터홀 벽면, 디지털 포스터 18기, 주차장 입·출구</td></tr>
<tr><th>대전 타임월드</th><td colspan="3">준비 중 · 미리 문의 주시면 먼저 안내해 드립니다</td></tr>
</tbody></table></div></div></section>

<section><div class="wrap"><div class="head"><span class="eyebrow">FOR</span><h2>이런 곳이 씁니다</h2></div>
<div class="cards">
<div class="card"><div class="in"><h3>아파트 분양</h3><p>견본주택 오픈 전후 관심 고객 상담·방문 예약</p></div></div>
<div class="card"><div class="in"><h3>병원·의원</h3><p>상담 → 진료 예약으로 이어지는 지역 병원 홍보</p></div></div>
<div class="card"><div class="in"><h3>뷰티·지역 브랜드</h3><p>백화점 손님층과 잘 맞는 업종의 체험·상담</p></div></div>
</div></div></section>

<section class="cream"><div class="wrap"><div class="head"><span class="eyebrow">PROCESS</span><h2>진행 순서</h2></div>{STEPS}</div></section>
{CONTACT}""", booth_faq, '홍보부스')

# ---------- 천안 ----------
cheonan_faq = [
    ('천안 센터시티점에는 어떤 광고 자리가 있나요?', '주차장 입구·출구(3,000×2,000mm), 엘리베이터홀 벽면(3,000×2,000 / 1,500×2,000mm), 엘리베이터홀 디지털 포스터 18기(570×1,000mm), 홍보부스가 있습니다.'),
    ('어떤 업종이 많이 하나요?', '안과·한방병원·외과 같은 병원과 아파트 분양, 문화시설 광고를 진행했습니다.'),
    ('광고가 걸린 걸 어떻게 확인하나요?', '게시 후 전경·근경 사진으로 집행 보고서를 드립니다.'),
]
page('cheonan.html', 'cheonan',
     '갤러리아 센터시티 광고 · 천안 백화점 홍보부스 | 드림애드컴',
     '천안 불당동 갤러리아 센터시티 광고: 주차장 출입구 하루 3.3만 명, 엘리베이터홀 디지털 포스터 18기, 주차장·엘리베이터홀 벽면, 분양 홍보부스. 더샵 천안라크원·김이태안과 등 집행 사례. 1599-3611',
     'img/booth-apt.jpg', f"""
<section class="hero"><img src="img/wall-lcd.jpg" alt="백화점 벽면 디지털 포스터">
<div class="wrap"><div class="crumb"><a href="index.html">홈</a> / 천안 센터시티</div><span class="eyebrow">CHEONAN CENTERCITY</span>
<h1><span class="kw">갤러리아 센터시티 광고 · 천안 백화점 광고</span>주차장부터 엘리베이터홀까지,<br><em>손님 동선마다 광고</em></h1>
<p>천안 불당동 생활권 한가운데 백화점입니다. 차로 들어오는 순간부터 엘리베이터를 기다리는 시간까지 광고가 보입니다.</p>
<div class="btns"><a class="btn gold" href="{TEL_LINK}">센터시티 광고 문의 {TEL}</a></div></div></section>

<section class="dark"><div class="wrap"><div class="head"><span class="eyebrow">NUMBERS</span><h2>센터시티 숫자</h2></div>
<div class="stats">
<div class="stat"><b>하루 3.3만 명</b><span>주차장 출입구 이용</span></div>
<div class="stat"><b>평균 42분</b><span>지하 1층 엘리베이터홀 머무는 시간</span></div>
<div class="stat"><b>18기</b><span>엘리베이터홀 디지털 포스터</span></div>
<div class="stat"><b>4.2회</b><span>1층 명품관 엘리베이터홀 1인당 노출</span></div>
</div><p class="src">출처: 갤러리아 센터시티 광고 매체 자료. 날짜·요일에 따라 달라질 수 있습니다.</p></div></section>

<section><div class="wrap"><div class="head"><span class="eyebrow">MEDIA</span><h2>광고 자리</h2></div>
<div class="media">
<div class="mcard"><h3>주차장 입구·출구</h3><dl><dt>크기</dt><dd>3,000 × 2,000mm</dd><dt>위치</dt><dd>주차장 입구·출구, 지하 2층 주차장 입구</dd><dt>특징</dt><dd>차로 오는 손님 정면</dd></dl></div>
<div class="mcard"><h3>엘리베이터홀 벽면</h3><dl><dt>크기</dt><dd>3,000 × 2,000 / 1,500 × 2,000mm</dd><dt>위치</dt><dd>1층·지하 1층 엘리베이터홀</dd><dt>특징</dt><dd>기다리는 동안 눈앞에</dd></dl></div>
<div class="mcard"><img src="img/wall-lcd.jpg" alt="벽면 디지털 포스터 예시" loading="lazy"><h3>디지털 포스터</h3><dl><dt>크기</dt><dd>570 × 1,000mm</dd><dt>수량</dt><dd>18기</dd><dt>위치</dt><dd>엘리베이터홀</dd></dl></div>
<div class="mcard"><img src="img/booth-apt.jpg" alt="홍보부스 예시" loading="lazy"><h3>홍보부스</h3><dl><dt>용도</dt><dd>분양·병원 상담</dd><dt>위치·기간</dt><dd>상담 때 안내</dd></dl></div>
</div><p class="note">사진은 매체 종류를 보여 주는 예시입니다.</p></div></section>

<section class="cream"><div class="wrap"><div class="head"><span class="eyebrow">CASES</span><h2>센터시티 집행 사례</h2></div>{CASES_TABLE}</div></section>
{CONTACT}""", cheonan_faq, '천안 센터시티')

# ---------- 진주 ----------
jinju_faq = [
    ('진주점 홍보부스는 어디에 있나요?', '1층 또는 12층 엘리베이터홀에서 10일 단위로 운영합니다.'),
    ('진주점 LCD에 영상을 틀 수 있나요?', '에스컬레이터·엘리베이터 LCD는 이미지 광고만 됩니다.'),
    ('고객 문자 광고는 어떻게 나가나요?', '백화점 정기 고객 약 5만 명에게 매주 금요일 나가는 문자 하단에 광고가 들어갑니다.'),
]
page('jinju.html', 'jinju',
     '갤러리아 진주점 광고 · 진주 백화점 홍보부스 | 드림애드컴',
     '갤러리아 진주점 광고: 1층·12층 엘리베이터홀 홍보부스(10일 단위), 서문 출입구 LED 1,500×2,400, 에스컬레이터 LCD 10기, 엘리베이터 LCD 4기, 정기 고객 문자 약 5만 명. 1599-3611',
     'img/jinju-building.jpg', f"""
<section class="hero"><img src="img/jinju-building.jpg" alt="갤러리아 진주점 건물">
<div class="wrap"><div class="crumb"><a href="index.html">홈</a> / 진주점</div><span class="eyebrow">JINJU</span>
<h1><span class="kw">갤러리아 진주점 광고 · 진주 백화점 홍보부스</span>정문 LED부터 고객 문자까지,<br><em>한 번에</em></h1>
<p>서부 경남의 백화점. 출입구 LED, 에스컬레이터·엘리베이터 화면, 정기 고객 문자, 홍보부스를 함께 진행할 수 있습니다.</p>
<div class="btns"><a class="btn gold" href="{TEL_LINK}">진주점 광고 문의 {TEL}</a></div></div></section>

<section><div class="wrap"><div class="head"><span class="eyebrow">MEDIA</span><h2>광고 자리</h2></div>
<div class="media">
<div class="mcard"><img src="img/booth-apt.jpg" alt="엘리베이터홀 홍보부스" loading="lazy"><h3>홍보부스</h3><dl><dt>위치</dt><dd>1층 또는 12층 엘리베이터홀</dd><dt>기간</dt><dd>10일 단위</dd></dl></div>
<div class="mcard"><img src="img/jinju-west-led.jpg" alt="진주점 서문 출입구 LED" loading="lazy"><h3>서문 출입구 LED</h3><dl><dt>크기</dt><dd>1,500 × 2,400mm · 1기</dd><dt>기간</dt><dd>1개월 기준</dd><dt>송출</dt><dd>1구좌 10초</dd></dl></div>
<div class="mcard"><img src="img/wall-lcd.jpg" alt="에스컬레이터 LCD 포스터" loading="lazy"><h3>에스컬레이터 LCD</h3><dl><dt>크기</dt><dd>900 × 500mm</dd><dt>수량</dt><dd>10기 · 모두 같은 광고</dd><dt>기간</dt><dd>1개월 기준 · 이미지</dd></dl></div>
<div class="mcard"><img src="img/ev-lcd.jpg" alt="엘리베이터 안 LCD" loading="lazy"><h3>엘리베이터 LCD</h3><dl><dt>크기</dt><dd>300 × 540mm</dd><dt>수량</dt><dd>4기 (1~4호기)</dd><dt>기간</dt><dd>1개월 기준 · 이미지</dd></dl></div>
<div class="mcard"><img src="img/lms-phone.jpg" alt="휴대폰으로 받는 백화점 문자" loading="lazy"><h3>고객 문자 (LMS)</h3><dl><dt>대상</dt><dd>정기 고객 약 5만 명</dd><dt>발송</dt><dd>매주 금요일 백화점 문자 하단</dd></dl></div>
</div><p class="note">출처: 갤러리아 진주점 광고 제안서. 사진은 매체 예시입니다.</p></div></section>

<section class="cream"><div class="wrap"><div class="head"><span class="eyebrow">FOR</span><h2>진주점이 잘 맞는 광고주</h2></div>
<div class="cards">
<div class="card"><div class="in"><h3>병원·의원</h3><p>부스 상담 → 진료 예약 → 내원으로</p></div></div>
<div class="card"><div class="in"><h3>뷰티·피부</h3><p>백화점 손님층과 잘 맞는 업종</p></div></div>
<div class="card"><div class="in"><h3>아파트 분양</h3><p>부스 + LED + 고객 문자로 지역에 한 번에</p></div></div>
</div></div></section>
{CONTACT}""", jinju_faq, '진주점')

# ---------- sitemap ----------
urls = ['', 'booth.html', 'cheonan.html', 'jinju.html']
open(os.path.join(HERE, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{BASE}{u}</loc><lastmod>{LASTMOD}</lastmod></url>\n' for u in urls) + '</urlset>\n')
print('built', urls)
