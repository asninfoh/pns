import os, random
from datetime import datetime

# ================= AUTO BASE URL =================
def get_base_url():
    url = open("domain.txt").read().strip()
    if not url.startswith("http"):
        url = "https://" + url
    return url.rstrip("/")

BASE_URL = get_base_url()

print("BASE_URL =", BASE_URL)

# ================= CONFIG =================
BATCH_SIZE = 12

keywords = [k.strip() for k in open("keyword.txt").readlines() if k.strip()]
os.makedirs("posts", exist_ok=True)

# ================= PROGRESS =================
start = 0
if os.path.exists("last_index.txt"):
    start = int(open("last_index.txt").read().strip())

end = start + BATCH_SIZE
selected = keywords[start:end]

open("last_index.txt","w").write(str(end))

# ================= CONTENT =================
def paragraph():
    base = [
# ================= KEPRIBADIAN & IMAGE =================
"Menjadi PNS cantik bukan hanya soal penampilan, tapi juga sikap dan profesionalisme.",
"Kepercayaan diri dan pembawaan yang elegan mencerminkan karakter yang kuat.",
"Kecantikan dalam seragam terlihat dari cara membawa diri dengan penuh percaya diri.",
"Penampilan yang rapi dan sikap yang sopan selalu memberi kesan positif.",
"Kecantikan dari dalam sangat berpengaruh terhadap citra seorang wanita karier.",
"Sikap tenang dan ramah membuat aura seseorang semakin menarik.",
"Keanggunan sejati terlihat dari perilaku, bukan hanya dari wajah.",
"Kepribadian yang kuat membuat wanita terlihat lebih menarik dan berkelas.",

# ================= GAYA HIDUP =================
"Gaya hidup seimbang membantu menjaga kecantikan dan produktivitas.",
"Merawat kesehatan fisik dan mental penting untuk menjaga kepercayaan diri.",
"Pikiran positif membuat seseorang terlihat lebih menarik secara alami.",
"Perawatan diri sederhana sudah cukup untuk menjaga kecantikan alami.",
"Rutinitas sehat mendukung kesuksesan karier dan kebahagiaan pribadi.",
"Rasa percaya diri tumbuh dari kenyamanan terhadap diri sendiri.",

# ================= KEHIDUPAN PROFESIONAL =================
"Penampilan profesional membantu membangun kepercayaan di tempat kerja.",
"Disiplin dan tanggung jawab adalah ciri utama PNS yang sukses.",
"Etos kerja yang baik meningkatkan citra diri dan karier.",
"Konsistensi dalam bekerja menciptakan identitas profesional yang kuat.",
"Integritas membuat seseorang lebih dihargai daripada sekadar penampilan.",
"Profesionalisme adalah daya tarik utama dalam dunia kerja.",

# ================= EMOSI & PERCAYA DIRI =================
"Percaya diri adalah bentuk kecantikan paling kuat yang dimiliki wanita.",
"Perasaan bahagia akan terpancar melalui penampilan sehari-hari.",
"Mencintai diri sendiri adalah dasar dari kecantikan sejati.",
"Ketika nyaman dengan diri sendiri, aura positif akan terlihat.",
"Keseimbangan emosi menciptakan kepribadian yang menenangkan.",
"Sikap positif membuat seseorang terlihat lebih bersinar alami.",

# ================= GAYA SOSIAL MEDIA / SEO =================
"Konten tentang PNS cantik semakin populer di media sosial.",
"Audiens modern lebih menyukai keaslian dan kesederhanaan.",
"Berbagi rutinitas harian bisa menjadi inspirasi bagi banyak orang.",
"Kecantikan alami dan profesionalisme menciptakan personal branding yang kuat.",
"Konten sederhana dan jujur sering lebih menarik perhatian.",
"Konsistensi dalam membuat konten membantu membangun audiens.",
"Menjadi diri sendiri lebih menarik daripada terlihat sempurna.",
"Citra diri yang kuat membuka peluang baru di dunia digital.",

# ================= SENTUHAN LEMBUT & ROMANTIS =================
"Wanita kuat dengan hati lembut memiliki pesona yang berbeda.",
"Kecantikan akan terasa lebih bermakna jika disertai kebaikan.",
"Senyuman tulus bisa membuat suasana menjadi lebih hangat.",
"Percaya diri yang dibarengi kelembutan menciptakan daya tarik alami.",
"Wanita yang menghargai dirinya akan lebih dihargai orang lain.",
"Pesona sejati datang dari ketulusan hati.",

# ================= KEHIDUPAN SEHARI-HARI =================
"Momen sederhana dalam hidup sering mencerminkan kebahagiaan sejati.",
"Produktif tanpa melupakan perawatan diri adalah kunci keseimbangan.",
"Rutinitas yang rapi membantu menjaga fokus dan kenyamanan.",
"Kebiasaan kecil yang positif bisa membawa perubahan besar.",
"Menikmati hal sederhana membuat hidup terasa lebih berarti.",
"Konsistensi dalam keseharian membangun kepercayaan diri jangka panjang.",
    ]
    sentence = random.choice(base)
    if random.random() > 0.5:
        sentence += ". " + random.choice(base)
    return "<p>" + sentence + "</p>"

def long_content():
    return "".join(paragraph() for _ in range(random.randint(3, 6)))

# ================= RELATED POSTS =================
def related(current):
    items = random.sample([k for k in keywords if k != current], 6)

    html = """
    <h6 class='fw-bold text-uppercase mb-3'>
        <span class='text-danger'>/</span> RELATED POSTS <span class='text-danger'>/</span>
    </h6>
    <div class="row g-3">
    """

    for i in items:
        slug = i.replace(" ", "-")
        url = f"{BASE_URL}/posts/{slug}.html"
        img = f"https://tse1.mm.bing.net/th?q={i}&w=400"

        html += f"""
        <div class='col-md-4 col-6 mb-3'>
            <div class='card post h-100 shadow-sm'>
                <a href='{url}'>
                    <img src='{img}' class='card-img-top' loading="lazy" alt="{i}">
                </a>
                <div class='card-body'>
                    <a href='{url}' class='text-dark text-decoration-none'>
                        <b>{i.title()}</b>
                    </a>
                </div>
            </div>
        </div>
        """

    html += "</div>"
    return html

# ================= HEADER (GLOBAL TEMPLATE) =================

def get_site_title():
    if os.path.exists("title.txt"):
        return open("title.txt").read().strip()
    return "Aridjaya"

def build_header(title):
    site_title = get_site_title()

    # auto image fallback
    og_image = f"https://tse1.mm.bing.net/th?q={title}"

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta content='width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no' name='viewport'/>

<title>{title} | {site_title}</title>
<meta name="description" content="{title} ideas and inspiration for modern home decor.">

<!-- OG META -->
<meta property="og:type" content="article">
<meta property="og:title" content="{title} | {site_title}">
<meta property="og:description" content="{title} ideas and inspiration for modern interior design.">
<meta property="og:url" content="{BASE_URL}/posts/{slug}.html">
<meta property="og:image" content="{og_image}">

<!-- TWITTER CARD -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} | {site_title}">
<meta name="twitter:description" content="{title} ideas and inspiration for modern home decor.">
<meta name="twitter:image" content="{og_image}">

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="{BASE_URL}/style.css" rel="stylesheet">
<script type='text/javascript' src='https://adsterrah.github.io/banner/popunder.js'></script>
</head>

<body>

<!-- NAVBAR -->
<nav class="navbar navbar-expand-lg border-bottom bg-light shadow-sm sticky-top">
<div class="container">
    <a class="navbar-brand fw-bold text-danger text-uppercase fs-4" href="{BASE_URL}/index.html">{get_site_title()}</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="nav">
        <ul class="navbar-nav me-auto">
            <li class="nav-item"><a class="nav-link" href="{BASE_URL}/galeri.html">Galeri</a></li>
            <li class="nav-item"><a class="nav-link" href="{BASE_URL}/inspirasi.html">Inspirasi</a></li>
            <li class="nav-item"><a class="nav-link" href="{BASE_URL}/karir.html">Karir</a></li>
            <li class="nav-item"><a class="nav-link" href="https://aridjaya.com" target='_blank'>Partner</a></li>
            <li class="nav-item"><a class="nav-link" href="{BASE_URL}/kontak.html">Kontak</a></li>
        </ul>
        <form class="d-flex">
            <input class="form-control me-2" placeholder="Search...">
        </form>
    </div>
</div>
</nav>

"""

# ================= FOOTER =================
def build_footer():
    return """
<footer class="bg-dark text-white text-center p-3 mt-4 border-top">
    Supported by <a class='text-danger fw-bold text-decoration-none' href='https://aridjaya.com/'>Aridjaya</a>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script type='text/javascript' src='https://adsterrah.github.io/banner/socialbar.js'></script>
<script type='text/javascript'>
// Set the overflow property on the body element to prevent scrolling
document.body.style.overflow = "hidden";
// Use a timer to enable scrolling after 5 seconds
setTimeout(function () {
    document.body.style.overflow = "auto";
}, 3000); // 3000 milliseconds = 3 seconds
</script>
</body>
</html>
"""

# ================= GENERATE POSTS =================
for kw in selected:
    slug = kw.replace(" ", "-")
    title = kw.title()
    url = f"{BASE_URL}/posts/{slug}.html"
    image = f"https://tse1.mm.bing.net/th?q={kw}"

    html = build_header(title)

    html += f"""
<div class="container mt-4">
    <!-- ad1 -->
    <div class="text-center p-3 my-3">
        <script type='text/javascript' src='https://adsterrah.github.io/banner/ad1.js'></script>
    </div>
    <div class="row">
        <!-- MAIN CONTENT -->
        <main class="col-md-8">
            <article>
                <h1 class="post-title fw-bold pb-4 mb-4">{title}</h1>
                <a href="https://indonesiya.com" target="_blank" rel="noopener noreferrer">
                    <img alt="{title} - gambar utama" title="{title}" src="{image}" loading="lazy"
                        class="w-100 img-fluid rounded mb-3">
                </a>
                <p class="text-center text-black-50">
                    <small>{title}</small>
                </p>
                <!-- ad2 -->
                <div class="text-center p-3 mb-3">
                    <script type='text/javascript' src='https://adsterrah.github.io/banner/ad2.js'></script>
                </div>
                <section>
                    {long_content()}
                </section>
                <h2 class="fw-bold my-4">{kw.title()}</h2>
                <section>
                    {long_content()}
                </section>
                <!-- ad3 -->
                <div class="text-center p-3 my-3">
                    <script type='text/javascript' src='https://adsterrah.github.io/banner/ad3.js'></script>
                </div>
                <!-- RELATED -->
                <section>
                    {related(kw)}
                </section>
            </article>
        </main>
        <!-- SIDEBAR -->
        <aside class="col-md-4">
            <!-- ABOUT -->
            <div class="card mb-3">
                <div class="card-body bg-light rounded">
                    <h6 class="fw-bold text-uppercase mb-3">
                        <span class="text-danger">/</span> TENTANG KAMI <span class="text-danger">/</span>
                    </h6>
                    <p>Inspirasi seputar PNS cantik, mulai dari gaya kerja, kehidupan wanita karir, hingga pesona alami yang elegan dan profesional.</p>
                    <!-- ad2 -->
                    <div class="text-center my-4">
                        <script type='text/javascript' src='https://adsterrah.github.io/banner/ad1.js'></script>
                    </div>
                </div>
            </div>
            <!-- CATEGORIES -->
            <div class="card mb-4">
                <div class="card-body bg-light rounded">
                    <h6 class="fw-bold text-uppercase mb-3">
                        <span class="text-danger">/</span> KATEGORI <span class="text-danger">/</span>
                    </h6>
                    <ul class="list-unstyled">
                        <li><a href="{BASE_URL}/pns-cantik">PNS Cantik</a></li>
                        <li><a href="{BASE_URL}/pns-berhijab">PNS Berhijab</a></li>
                        <li><a href="{BASE_URL}/gaya-kerja">Gaya Kerja</a></li>
                        <li><a href="{BASE_URL}/outfit-kantor">Outfit Kantor</a></li>
                        <li><a href="{BASE_URL}/wanita-karir">Wanita Karir</a></li>
                        <li><a href="{BASE_URL}/inspirasi">Inspirasi</a></li>
                        <li><a href="{BASE_URL}/kehidupan-pns">Kehidupan PNS</a></li>
                        <li><a href="{BASE_URL}/tips-cantik">Tips Cantik</a></li>
                    </ul>
                </div>
            </div>
            <!-- POPULAR POSTS -->
            <div class="card mb-4">
                <div class="card-body bg-light rounded">
                    <h6 class="fw-bold text-uppercase mb-3">
                        <span class="text-danger">/</span> POPULER <span class="text-danger">/</span>
                    </h6>
                    <ul class="list-unstyled">
                        <li><a href="{BASE_URL}/pns-cantik-indonesia">PNS Cantik Indonesia</a></li>
                        <li><a href="{BASE_URL}/pns-cantik-berhijab">PNS Cantik Berhijab</a></li>
                        <li><a href="{BASE_URL}/gaya-pns-modern">Gaya PNS Modern</a></li>
                        <li><a href="{BASE_URL}/outfit-kantor-elegan">Outfit Kantor Elegan</a></li>
                        <li><a href="{BASE_URL}/wanita-karir-inspiratif">Wanita Karir Inspiratif</a></li>
                    </ul>
                </div>
            </div>
            <!-- TAG CLOUD -->
            <div class="card mb-4">
                <div class="card-body bg-light rounded">
                    <h6 class="fw-bold text-uppercase mb-3">
                        <span class="text-danger">/</span> TAGS <span class="text-danger">/</span>
                    </h6>
                    <a href="{BASE_URL}/pns-cantik" class="badge bg-dark text-white">PNS Cantik</a>
                    <a href="{BASE_URL}/wanita-karir" class="badge bg-secondary text-white">Wanita Karir</a>
                    <a href="{BASE_URL}/outfit-kantor" class="badge bg-dark text-white">Outfit Kantor</a>
                    <a href="{BASE_URL}/hijab-style" class="badge bg-secondary text-white">Hijab Style</a>
                </div>
            </div>
            <!-- NEWSLETTER -->
            <div class="card mb-4">
                <div class="card-body bg-light rounded">
                    <h6 class="fw-bold text-uppercase mb-3">
                        <span class="text-danger">/</span> UPDATE HARIAN <span class="text-danger">/</span>
                    </h6>
                    <p>Dapatkan inspirasi PNS cantik dan wanita karir setiap hari.</p>
                    <input type="email" class="form-control mb-2" placeholder="Masukkan email">
                    <a href="https://aridjaya.com" target="_blank" rel="noopener">
                        <button class="btn btn-success btn-sm w-100">Daftar</button>
                    </a>
                </div>
            </div>
        </aside>
    </div>
</div>


"""

    html += build_footer()

    open(f"posts/{slug}.html", "w", encoding="utf-8").write(html)

# ================= HOMEPAGE =================

# post terbaru di atas (lebih akurat dari reverse)
posts = sorted(
    os.listdir("posts"),
    key=lambda x: os.path.getmtime(f"posts/{x}"),
    reverse=True
)

home = build_header(get_site_title())

home += """
<div class="container mt-4">

<!-- ad1 -->
<div class="text-center p-3 my-3">
    <script type='text/javascript' src='https://adsterrah.github.io/banner/ad1.js'></script>
</div>

<div class="row" id="post-container">
"""

# tampilkan awal (12 post pertama)
for p in posts[:12]:
    t = p.replace(".html","").replace("-"," ").title()
    img = f"https://tse1.mm.bing.net/th?q={t}&w=400"

    home += f"""
    <div class="col-md-3 mb-4">
        <div class="card post h-100 shadow-sm">
            <a href="posts/{p}">
                <img src="{img}" class="card-img-top" loading="lazy">
            </a>
            <div class="card-body">
                <a href="posts/{p}" class="text-dark text-capitalize text-decoration-none">
                    <h6 class="fw-bold">{t}</h6>
                </a>
            </div>
        </div>
    </div>
    """

# ================= INFINITE SCROLL SCRIPT =================
home += f"""
</div>

<div id="loading" class="text-center my-3" style="display:none;">
    <small>Loading...</small>
</div>

<script>
let posts = {posts};   // semua data post
let perPage = 12;
let current = {len(posts[:12])};
let loading = false;

window.onscroll = function() {{
    if (loading) return;

    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 300) {{
        if (current >= posts.length) return;

        loading = true;
        document.getElementById("loading").style.display = "block";

        setTimeout(() => {{
            let container = document.getElementById("post-container");

            for (let i = current; i < current + perPage && i < posts.length; i++) {{
                let p = posts[i];
                let t = p.replace(".html","").replaceAll("-"," ");

                let html = `
                <div class="col-md-3 mb-4">
                    <div class="card post h-100 shadow-sm">
                        <a href="posts/${{p}}">
                            <img src="https://tse1.mm.bing.net/th?q=${{t}}&w=400" class="card-img-top" loading="lazy">
                        </a>
                        <div class="card-body">
                            <a href="posts/${{p}}" class="text-dark text-decoration-none">
                                <h6 class="fw-bold">${{t}}</h6>
                            </a>
                        </div>
                    </div>
                </div>
                `;

                container.insertAdjacentHTML("beforeend", html);
            }}

            current += perPage;
            loading = false;
            document.getElementById("loading").style.display = "none";
        }}, 500);
    }}
}};
</script>

<!-- adnativ -->
<script type='text/javascript' src='https://adsterrah.github.io/banner/nativ.js'></script>

</div>
"""

home += build_footer()

open("index.html", "w", encoding="utf-8").write(home)

# ================= SITEMAP =================
sitemap = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for p in posts:
    url = f"{BASE_URL}/posts/{p}"

    sitemap.append("<url>")
    sitemap.append(f"<loc>{url}</loc>")
    sitemap.append(f"<lastmod>{datetime.utcnow().date()}</lastmod>")
    sitemap.append("<changefreq>weekly</changefreq>")
    sitemap.append("<priority>0.8</priority>")
    sitemap.append("</url>")

sitemap.append("</urlset>")

open("sitemap.xml", "w", encoding="utf-8").write("\n".join(sitemap))


# ================= IMAGE SITEMAP =================
import urllib.parse
from xml.sax.saxutils import escape

image_sitemap = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
    'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
]

for p in posts:
    title = p.replace(".html", "").replace("-", " ").title()

    page_url = f"{BASE_URL}/posts/{p}"
    image_url = "https://tse1.mm.bing.net/th?q=" + urllib.parse.quote(title)

    image_sitemap.append("<url>")
    image_sitemap.append(f"<loc>{escape(page_url)}</loc>")

    image_sitemap.append("<image:image>")
    image_sitemap.append(f"<image:loc>{escape(image_url)}</image:loc>")
    image_sitemap.append(f"<image:title>{escape(title)}</image:title>")
    image_sitemap.append("</image:image>")

    image_sitemap.append("</url>")

image_sitemap.append("</urlset>")

open("sitemap-images.xml", "w", encoding="utf-8").write("\n".join(image_sitemap))

# ================= RSS =================
rss = [
"<?xml version='1.0' encoding='UTF-8'?>",
"<rss version='2.0'><channel>",
f"<title>{get_site_title()}</title>",
f"<link>{BASE_URL}</link>",
"<description>Home decor inspiration</description>"
]

for p in posts[:30]:
    title = p.replace(".html","").replace("-"," ").title()
    link = f"{BASE_URL}/posts/{p}"

    rss.append("<item>")
    rss.append(f"<title>{title}</title>")
    rss.append(f"<link>{link}</link>")
    rss.append("</item>")

rss.append("</channel></rss>")

open("feed.xml", "w").write("\n".join(rss))

print("✅ DONE:", len(selected), "posts generated")