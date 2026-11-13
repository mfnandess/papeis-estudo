#!/usr/bin/env python3
"""Gera calculo-1/claude/index.html a partir de calculo-1/claude/src/paper.html.

As figuras são desenhadas aqui (SVG inline, calculadas numericamente) para
que se adaptem ao tema claro/escuro da página. No texto-fonte, uma figura é
inserida com:   {{fig:nome|Legenda da figura}}

Uso:  python3 calculo-1/claude/build.py
"""
import math
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent


class Fig:
    def __init__(self, name, xmin, xmax, ymin, ymax, W=360, H=230):
        self.name = name
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.W, self.H = W, H
        self.l, self.r, self.t, self.b = 14, 16, 12, 20
        self.parts = []

    # coordenadas
    def X(self, x):
        return self.l + (x - self.xmin) / (self.xmax - self.xmin) * (self.W - self.l - self.r)

    def Y(self, y):
        return self.t + (self.ymax - y) / (self.ymax - self.ymin) * (self.H - self.t - self.b)

    def P(self, x, y):
        return f"{self.X(x):.1f},{self.Y(y):.1f}"

    # primitivas
    def axes(self, xl="x", yl="y"):
        mid = f"url(#ar-{self.name})"
        if self.ymin <= 0 <= self.ymax:
            self.parts.append(f'<line class="ax" x1="{self.X(self.xmin):.1f}" y1="{self.Y(0):.1f}" '
                              f'x2="{self.X(self.xmax):.1f}" y2="{self.Y(0):.1f}" marker-end="{mid}"/>')
            self.parts.append(f'<text class="lb s" x="{self.X(self.xmax) - 4:.1f}" y="{self.Y(0) + 15:.1f}" text-anchor="end">{xl}</text>')
        if self.xmin <= 0 <= self.xmax:
            self.parts.append(f'<line class="ax" x1="{self.X(0):.1f}" y1="{self.Y(self.ymin):.1f}" '
                              f'x2="{self.X(0):.1f}" y2="{self.Y(self.ymax):.1f}" marker-end="{mid}"/>')
            self.parts.append(f'<text class="lb s" x="{self.X(0) + 7:.1f}" y="{self.Y(self.ymax) + 10:.1f}">{yl}</text>')

    def curve(self, f, a, b, cls="c1", n=400):
        segs, cur = [], []
        for i in range(n + 1):
            x = a + (b - a) * i / n
            try:
                y = f(x)
            except (ValueError, ZeroDivisionError, OverflowError):
                y = None
            ok = y is not None and not math.isnan(y) and self.ymin - 0.02 * (self.ymax - self.ymin) <= y <= self.ymax + 0.02 * (self.ymax - self.ymin)
            if ok:
                cur.append(self.P(x, y))
            elif cur:
                segs.append(cur)
                cur = []
        if cur:
            segs.append(cur)
        for s in segs:
            if len(s) > 1:
                self.parts.append(f'<polyline class="{cls}" points="{" ".join(s)}"/>')

    def param(self, fx, fy, a, b, cls="c1", n=400):
        pts = [self.P(fx(a + (b - a) * i / n), fy(a + (b - a) * i / n)) for i in range(n + 1)]
        self.parts.append(f'<polyline class="{cls}" points="{" ".join(pts)}"/>')

    def line(self, x1, y1, x2, y2, cls="c2"):
        self.parts.append(f'<line class="{cls}" x1="{self.X(x1):.1f}" y1="{self.Y(y1):.1f}" x2="{self.X(x2):.1f}" y2="{self.Y(y2):.1f}"/>')

    def poly(self, pts, cls="fill"):
        self.parts.append(f'<polygon class="{cls}" points="{" ".join(self.P(x, y) for x, y in pts)}"/>')

    def region(self, top, bot, a, b, cls="fill", n=120):
        up = [(a + (b - a) * i / n, top(a + (b - a) * i / n)) for i in range(n + 1)]
        dn = [(a + (b - a) * i / n, bot(a + (b - a) * i / n)) for i in range(n, -1, -1)]
        self.poly(up + dn, cls)

    def dot(self, x, y, cls="dot", hollow=False):
        c = "hole" if hollow else cls
        self.parts.append(f'<circle class="{c}" cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="4"/>')

    def text(self, x, y, t, cls="lb", anchor="middle", dx=0, dy=0):
        self.parts.append(f'<text class="{cls}" x="{self.X(x) + dx:.1f}" y="{self.Y(y) + dy:.1f}" text-anchor="{anchor}">{t}</text>')

    def raw(self, s):
        self.parts.append(s)

    def svg(self, aria):
        defs = (f'<defs><marker id="ar-{self.name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="arw"/></marker></defs>')
        return (f'<svg viewBox="0 0 {self.W} {self.H}" role="img" aria-label="{aria}">'
                + defs + "".join(self.parts) + "</svg>")


# ---------------------------------------------------------------- figuras
def fig_limite():
    F = Fig("lim", -0.4, 4, -0.4, 3.4)
    f = lambda x: 0.3 * (x - 1) ** 2 + 1
    F.axes()
    F.curve(f, -0.3, 3.9)
    F.line(2, 0, 2, 2.6, "guide")
    F.line(0, 1.3, 2, 1.3, "guide")
    F.dot(2, 1.3, hollow=True)
    F.dot(2, 2.6, "dot2")
    F.text(2, 0, "p", dy=15)
    F.text(0, 1.3, "L", anchor="end", dx=-5, dy=4)
    F.text(2, 2.6, "f(p)", anchor="start", dx=8, dy=4, cls="lb c2t")
    F.text(3.55, f(3.55), "y = f(x)", anchor="end", dx=-6, dy=-4, cls="lb c1t")
    return F.svg("Gráfico de f com um buraco no ponto (p, L) e o valor f(p) fora da curva")


def fig_circulo():
    F = Fig("circ", -0.25, 1.55, -0.22, 1.28, W=300, H=262)
    t = 0.75
    F.param(math.cos, math.sin, 0, math.pi / 2, "c-faint")
    F.axes()
    F.param(math.cos, math.sin, 0, t, "c1 thick")
    F.line(0, 0, 1, math.tan(t), "c-faint")
    F.line(math.cos(t), 0, math.cos(t), math.sin(t), "c2 thick")
    F.line(1, 0, 1, math.tan(t), "c3 thick")
    F.dot(0, 0)
    F.dot(math.cos(t), math.sin(t))
    F.dot(1, 0)
    F.text(0, 0, "O", anchor="end", dx=-4, dy=14)
    F.text(1, 0, "A=(1,0)", anchor="start", dx=4, dy=14, cls="lb s")
    F.text(math.cos(t), 0, "sen x", anchor="end", dx=-4, dy=-40, cls="lb c2t")
    F.text(1, math.tan(t) / 2, "tg x", anchor="start", dx=6, cls="lb c3t")
    F.text(math.cos(t / 2), math.sin(t / 2), "x", anchor="end", dx=-6, cls="lb c1t")
    F.text(0.32, 0.12, "x", cls="lb s")
    return F.svg("Círculo unitário com o arco x, o segmento sen x e o segmento tg x")


def fig_senx():
    F = Fig("senx", -13, 13, -0.4, 1.3, H=190)
    F.axes()
    F.line(-13, 1, 13, 1, "guide")
    F.curve(lambda x: math.sin(x) / x if abs(x) > 1e-3 else None, -12.8, 12.8)
    F.dot(0, 1, hollow=True)
    F.text(0, 1, "1", anchor="end", dx=-8, dy=-6)
    F.text(8, 0.55, "y = sen x / x", cls="lb c1t")
    return F.svg("Gráfico de sen x sobre x, que se aproxima de 1 quando x tende a 0")


def fig_assintotas():
    F = Fig("ass", -14, 8, -6, 10)
    f = lambda x: (2 * x + 1) / (x + 3)
    F.line(-14, 2, 8, 2, "guide")
    F.line(-3, -6, -3, 10, "guide")
    F.axes()
    F.curve(f, -13.9, -3.01, n=600)
    F.curve(f, -2.99, 7.9, n=600)
    F.text(7.8, 2, "y = 2", anchor="end", dy=-6, cls="lb s")
    F.text(-3, 9.3, "x = −3", anchor="end", dx=-5, cls="lb s")
    F.text(5, 4.2, "y = (2x+1)/(x+3)", cls="lb c1t")
    return F.svg("Hipérbole com assíntota horizontal y=2 e vertical x=-3")


def fig_tvi():
    F = Fig("tvi", -0.25, 2.6, -1.5, 3.8)
    f = lambda x: 0.35 * x ** 3 + 0.3 * x - 1
    a, b = 0.2, 2.2
    lo, hi = a, b
    for _ in range(60):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if f(m) < 0 else (lo, m)
    c = lo
    F.axes()
    F.line(a, 0, a, f(a), "guide")
    F.line(b, 0, b, f(b), "guide")
    F.curve(f, a, b)
    F.dot(a, f(a))
    F.dot(b, f(b))
    F.dot(c, 0, "dot2")
    F.text(a, 0, "a", dy=-6)
    F.text(b, 0, "b", dy=15)
    F.text(c, 0, "c", dy=-8, dx=-8, cls="lb c2t")
    F.text(a, f(a), "f(a) &lt; 0", anchor="start", dx=8, dy=4, cls="lb s")
    F.text(b, f(b), "f(b) &gt; 0", anchor="end", dx=-8, cls="lb s")
    return F.svg("Função contínua que passa de negativa a positiva e corta o eixo em c")


def fig_tangente():
    F = Fig("tan", -0.4, 4.2, -0.4, 4.4)
    f = lambda x: 0.25 * x ** 2 + 0.6
    p = 1.0
    F.axes()
    for q, cls in ((3.6, "sec faint"), (2.6, "sec")):
        m = (f(q) - f(p)) / (q - p)
        F.line(-0.3, f(p) + m * (-0.3 - p), 4.1, f(p) + m * (4.1 - p), cls)
        F.dot(q, f(q), "dot3")
    F.curve(f, -0.3, 4.1)
    F.line(-0.3, f(p) + 0.5 * (-1.3), 4.1, f(p) + 0.5 * 3.1, "c2 thick")
    F.dot(p, f(p), "dot2")
    F.line(p, 0, p, f(p), "guide")
    F.line(2.6, 0, 2.6, f(2.6), "guide")
    F.text(p, 0, "p", dy=15)
    F.text(2.6, 0, "p + h", dy=15)
    F.text(p, f(p), "P", anchor="end", dx=-6, dy=-6, cls="lb c2t")
    F.text(2.6, f(2.6), "Q", anchor="end", dx=-6, dy=-4)
    F.text(3.2, f(p) + 0.5 * 2.2, "tangente", anchor="start", dy=20, cls="lb c2t")
    F.text(3.3, f(3.3), "secantes", anchor="end", dx=-20, dy=-14, cls="lb s")
    return F.svg("Retas secantes por P e Q se aproximando da reta tangente em P quando h tende a 0")


def fig_explog():
    F = Fig("exl", -3, 4.2, -3, 4.2, W=320, H=320)
    F.line(-3, -3, 4.2, 4.2, "guide")
    F.axes()
    F.curve(math.exp, -3, math.log(4.2))
    F.curve(lambda x: math.log(x) if x > 0 else None, 0.04, 4.2, "c2")
    F.dot(0, 1)
    F.dot(1, 0, "dot2")
    F.text(1.1, math.exp(1.1), "y = eˣ", anchor="start", dx=8, cls="lb c1t")
    F.text(3.5, math.log(3.5), "y = ln x", anchor="end", dy=-10, cls="lb c2t")
    F.text(3.4, 3.4, "y = x", anchor="end", dx=-8, cls="lb s")
    F.text(0, 1, "(0,1)", anchor="end", dx=-6, dy=-2, cls="lb s")
    F.text(1, 0, "(1,0)", anchor="start", dx=4, dy=14, cls="lb s")
    return F.svg("Gráficos de e elevado a x e de ln x, simétricos em relação à reta y = x")


def fig_variacao():
    F = Fig("var", -2.5, 2.5, -3.1, 3.1, H=250)
    f = lambda x: x ** 3 - 3 * x
    F.axes()
    F.curve(f, -2.2, 2.2)
    F.dot(-1, 2, "dot2")
    F.dot(1, -2, "dot2")
    F.dot(0, 0, "dot3")
    F.text(-1, 2, "máx. local", dy=-10, cls="lb c2t")
    F.text(1, -2, "mín. local", dy=18, cls="lb c2t")
    F.text(0, 0, "inflexão", anchor="start", dx=8, dy=-6, cls="lb c3t")
    F.text(-1.25, -2.5, "côncava ↓", cls="lb s")
    F.text(1.25, 2.5, "côncava ↑", cls="lb s")
    return F.svg("Gráfico de x ao cubo menos 3x com máximo local em -1, mínimo local em 1 e inflexão em 0")


def fig_tvm():
    F = Fig("tvm", -0.25, 4.6, -0.3, 4.4)
    f = lambda x: 0.5 + 1.5 * math.sqrt(x)
    a, b = 0.25, 4.0
    m = (f(b) - f(a)) / (b - a)
    c = (0.75 / m) ** 2
    F.axes()
    F.curve(f, 0, 4.5)
    F.line(a, f(a), b, f(b), "sec")
    F.line(c - 1.3, f(c) - 1.3 * m, c + 1.6, f(c) + 1.6 * m, "c2 thick")
    F.dot(a, f(a))
    F.dot(b, f(b))
    F.dot(c, f(c), "dot2")
    F.line(c, 0, c, f(c), "guide")
    F.text(a, f(a), "A", anchor="start", dx=4, dy=16)
    F.text(b, f(b), "B", anchor="start", dx=6, dy=4)
    F.text(c, 0, "c", dy=15, cls="lb c2t")
    F.text(c, f(c), "tangente // AB", anchor="end", dx=-10, dy=-12, cls="lb c2t")
    return F.svg("Teorema do valor médio: a tangente em c é paralela à secante AB")


def fig_maxmin():
    F = Fig("mm", -2.7, 3.7, -24, 10, H=250)
    f = lambda x: x ** 4 / 4 - x ** 3 - 2 * x ** 2 + 3
    F.axes()
    F.curve(f, -2.45, 3.25, "c-faint")
    F.curve(f, -2, 3)
    for x0 in (-2, 3):
        F.line(x0, 0, x0, f(x0), "guide")
    F.dot(-2, f(-2), "dot2")
    F.dot(3, f(3), "dot2")
    F.dot(-1, f(-1), "dot3")
    F.dot(0, f(0), "dot3")
    F.text(-2, f(-2), "máx. global (7)", anchor="start", dx=8, dy=-2, cls="lb c2t")
    F.text(3, f(3), "mín. global (−87/4)", anchor="end", dx=-8, dy=4, cls="lb c2t")
    F.text(-2, 0, "−2", anchor="end", dx=-3, dy=-5, cls="lb s")
    F.text(3, 0, "3", anchor="start", dx=4, dy=-5, cls="lb s")
    return F.svg("Função em intervalo fechado com máximo e mínimo globais nas extremidades")


def fig_riemann():
    F = Fig("rie", -0.3, 4.4, -0.3, 4.3)
    f = lambda x: 0.2 * x ** 2 + 0.6
    a, b, n = 0.4, 4.0, 6
    dx = (b - a) / n
    for i in range(n):
        x0 = a + i * dx
        c = x0 + dx / 2
        F.poly([(x0, 0), (x0, f(c)), (x0 + dx, f(c)), (x0 + dx, 0)], "rect")
        F.dot(c, 0, "dot3")
    F.axes()
    F.curve(f, 0, 4.2)
    F.text(a, 0, "a", dy=15)
    F.text(b, 0, "b", dy=15)
    F.text(a + 2.5 * dx, 0, "cᵢ", dy=15, cls="lb c3t")
    F.text(3.4, f(3.9), "y = f(x)", anchor="end", dx=-4, cls="lb c1t")
    return F.svg("Soma de Riemann: retângulos de base delta x e altura f nos pontos c i")


def fig_area_entre():
    F = Fig("aen", -0.25, 1.35, -0.18, 1.3, W=300, H=262)
    F.region(lambda x: x, lambda x: x * x, 0, 1)
    F.axes()
    F.curve(lambda x: x, -0.1, 1.25)
    F.curve(lambda x: x * x, -0.1, 1.13, "c2")
    F.dot(1, 1)
    F.text(0.4, 0.4, "y = x", anchor="end", dx=-14, dy=-6, cls="lb c1t")
    F.text(0.85, 0.72, "y = x²", anchor="start", dx=8, dy=12, cls="lb c2t")
    F.text(0.55, 0.42, "A", cls="lb")
    F.text(1, 0, "1", dy=15)
    return F.svg("Região entre y=x e y=x ao quadrado, de 0 a 1")


def fig_discos():
    F = Fig("dis", -0.3, 4.8, -2.5, 2.5, H=240)
    f = math.sqrt
    F.region(f, lambda x: -f(x), 0, 4, "fill faint")
    xs = 2.6
    F.axes()
    F.curve(f, 0, 4)
    F.curve(lambda x: -f(x), 0, 4, "c-faint")
    rx = 12
    for x0, cls in ((xs, "rect"), (4, "c-faint-fill")):
        F.raw(f'<ellipse class="{cls}" cx="{F.X(x0):.1f}" cy="{F.Y(0):.1f}" rx="{rx}" ry="{F.Y(0) - F.Y(f(x0)):.1f}"/>')
    F.line(xs, 0, xs, f(xs), "c2 thick")
    F.text(xs, f(xs) / 2, "r = f(x)", anchor="start", dx=16, cls="lb c2t")
    F.text(1.4, f(1.4), "y = √x", anchor="end", dx=-4, dy=-10, cls="lb c1t")
    F.text(0.5, 0, "eixo de rotação", anchor="start", dy=-6, cls="lb s")
    return F.svg("Sólido de revolução de y igual a raiz de x, fatiado em discos de raio f de x")


def fig_taylor():
    F = Fig("tay", -2.6, 2.1, -1.2, 6.2, H=260)
    F.axes()
    F.curve(lambda x: 1 + x, -2.6, 2.1, "c3")
    F.curve(lambda x: 1 + x + x * x / 2, -2.6, 2.1, "c2")
    F.curve(lambda x: 1 + x + x * x / 2 + x ** 3 / 6, -2.6, 2.1, "c4")
    F.curve(math.exp, -2.6, 1.82, "c1 thick")
    F.text(1.7, math.exp(1.7), "eˣ", anchor="end", dx=-8, cls="lb c1t")
    F.text(2.0, 3.0, "P₁", anchor="end", cls="lb c3t")
    F.text(-2.2, 1.45, "P₂", cls="lb c2t")
    F.text(-1.9, -0.6, "P₃", anchor="start", dx=6, cls="lb c4t")
    return F.svg("Exponencial e seus polinômios de Taylor de ordens 1, 2 e 3 em torno de 0")


def fig_edo():
    F = Fig("edo", -0.2, 3.2, -1, 24, H=230)
    F.line(0, 10, 3.1, 10, "guide")
    F.axes("t", "T")
    for C in (12, 6, -4, -8):
        F.curve(lambda t, C=C: 10 + C * math.exp(-2 * t), 0, 3.1, "c1" if C != 6 else "c2 thick")
    F.text(3.1, 10, "T = 10 (equilíbrio)", anchor="end", dy=-6, cls="lb s")
    F.dot(0, 16, "dot2")
    F.text(0.3, 14.3, "T(0) = 16", anchor="start", cls="lb c2t")
    return F.svg("Soluções da equação T linha igual a menos 2 vezes T menos 10 tendendo a 10")


def fig_cardioide():
    F = Fig("car", -0.7, 2.3, -1.5, 1.5, W=300, H=290)
    F.raw("")
    th = lambda s: s
    r = lambda s: 1 + math.cos(s)
    pts = [(r(s * 2 * math.pi / 200) * math.cos(s * 2 * math.pi / 200),
            r(s * 2 * math.pi / 200) * math.sin(s * 2 * math.pi / 200)) for s in range(201)]
    F.poly(pts, "fill faint")
    F.axes()
    F.param(lambda s: r(s) * math.cos(s), lambda s: r(s) * math.sin(s), 0, 2 * math.pi)
    a = 1.0
    F.line(0, 0, r(a) * math.cos(a), r(a) * math.sin(a), "c2 thick")
    F.text(r(a) * math.cos(a) / 2, r(a) * math.sin(a) / 2, "r(θ)", anchor="end", dx=-6, cls="lb c2t")
    F.text(2, 0, "2", dy=15)
    F.text(1.6, 1.25, "r = 1 + cos θ", cls="lb c1t")
    return F.svg("Cardioide r igual a 1 mais cosseno de theta")


FIGS = {
    "limite": fig_limite, "circulo": fig_circulo, "senx": fig_senx,
    "assintotas": fig_assintotas, "tvi": fig_tvi, "tangente": fig_tangente,
    "explog": fig_explog, "variacao": fig_variacao, "tvm": fig_tvm,
    "maxmin": fig_maxmin, "riemann": fig_riemann, "area_entre": fig_area_entre,
    "discos": fig_discos, "taylor": fig_taylor, "edo": fig_edo, "cardioide": fig_cardioide,
}


def main():
    src = (ROOT / "src" / "paper.html").read_text(encoding="utf-8")
    counter = {"n": 0}

    def repl(m):
        name, cap = m.group(1), m.group(2)
        counter["n"] += 1
        return (f'<figure class="fig" id="fig-{name}">{FIGS[name]()}'
                f'<figcaption><b>Figura {counter["n"]}.</b> {cap}</figcaption></figure>')

    out = re.sub(r"\{\{fig:(\w+)\|(.*?)\}\}", repl, src, flags=re.S)
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    print(f"ok: {counter['n']} figuras -> {ROOT / 'index.html'}")


if __name__ == "__main__":
    main()
