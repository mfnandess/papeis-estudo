# Guia Comparativo de Arquitetura Teórica: Guidorizzi (Vol. 1, 5ª Ed.) vs. Apostol (*Cálculo I*, 2ª Ed.)
## Paper Metodológico para Estudo Cruzado sem Conflitos de Nomenclatura ou Hipóteses

---

> **Navegação Rápida entre os Papers deste Repositório (GitHub Pages):**
> - 📄 **[Paper 1 — Tratado Teórico Principal (Capítulos 1 a 17 + Apêndices)](./index.html)** | [Versão Markdown](./Paper_Calculo_1_Guidorizzi_Apostol.md)
> - 📝 **[Paper 2 — Caderno de Exercícios Resolvidos (Guidorizzi + Apostol)](./exercicios.html)** | [Versão Markdown](./Caderno_Exercicios_Calculo_1.md)
> - ⚖️ **[Paper 3 — Guia Comparativo: Guidorizzi vs. Apostol (Você está aqui)](./comparativo-guidorizzi-apostol.html)** | [Versão Markdown](./Comparativo_Guidorizzi_vs_Apostol.md)

---

## 1. Visão Geral das Duas Obras: Duas Escolas Clássicas de Cálculo 1

Estudar Cálculo Diferencial e Integral I combinando **Hamilton Luiz Guidorizzi (*Um Curso de Cálculo — Volume 1*, 5ª edição)** como **referência principal** e **Tom M. Apostol (*Cálculo I*, 2ª edição)** como **referência complementar** oferece o melhor de dois mundos — desde que o estudante compreenda claramente **onde a ordem lógica e a nomenclatura dos dois autores divergem**.

| Dimensão | 📘 **H. L. Guidorizzi (*Um Curso de Cálculo*, Vol. 1, 5ª ed.)** | 📙 **Tom M. Apostol (*Cálculo I*, Vol. 1, 2ª ed.)** |
| :--- | :--- | :--- |
| **Ordem Macro dos Pilares** | **Ordem Analítica Padrão:** Números Reais $\to$ Funções $\to$ Limite e Continuidade $\to$ Exponencial/Logaritmo $\to$ **Derivada** $\to$ **Integral de Riemann** $\to$ Aplicações $\to$ EDOs $\to$ Taylor $\to$ Arquimedes/Pascal/Fermat. | **Ordem Histórica (Arquimedes $\to$ Newton):** Axiomas de $\mathbb{R}$ e Indução $\to$ **Integral (Funções em Escada)** $\to$ Limite e Continuidade $\to$ **Derivada** $\to$ TFC $\to$ Logaritmo (via Integral) e Exponencial $\to$ Taylor e L'Hospital $\to$ EDOs. |
| **Fundamentação de $\mathbb{R}$** | **Seção 1.5:** Intervalos Encaixantes ($b_n - a_n < r$) e Arquimedes no texto; **Apêndice 1:** Propriedade do Supremo; **Apêndice 6:** Construção de $\mathbb{R}$ via **Cortes de Dedekind**. | **Parte I.3:** Apresentação **Axiomática de Hilbert** (Axiomas de Corpo, Ordem e o Axioma 10 do Extremo Superior / Completitude). |
| **Ordem em Limite e Continuidade** | **Continuidade primeiro (Seção 3.2)**, **Limite depois (Seção 3.3)**. Domínio sempre suposto intervalo ou união de intervalos. | **Limite primeiro (Seção 3.2)**, **Continuidade depois (Seção 3.3)**. |
| **Construção de $e^x$ e $\ln x$** | **Cap. 4 e 6 (Antes de Derivada e Integral):** Define $e = \lim (1+1/n)^n$ (Seção 4.5), $a^x$ por extensão contínua de $\mathbb{Q}$ a $\mathbb{R}$ (Seção 6.1 e Ap. 3), e $\log_a \beta$ via **Teorema do Valor Intermediário** (Seção 6.2). | **Cap. 6 (Depois da Integral):** Define primeiro **$\ln x = \int_1^x \frac{1}{t}\,dt$** ($x > 0$), define $e$ por $\ln e = 1$, define $e^x$ como a função inversa de $\ln x$, e define $a^x = e^{x\ln a}$. |
| **Definição da Integral Definida** | **Cap. 11:** Limite $\varepsilon$-$\delta$ das **Somas de Riemann** $\sum_{i=1}^n f(c_i)\Delta x_i$ quando $\max \Delta x_i \to 0$ (e Somas de Darboux no **Apêndice 4**). | **Cap. 1:** Integral de **Funções em Escada** e **Integrais Inferior e Superior de Darboux** ($\underline{I}(f) = \overline{I}(f)$). |
| **Nomenclatura do 1º e 2º TFC** | **1º TFC (Vol. 1, Seção 11.5):** $\int_a^b f(x)\,dx = F(b) - F(a)$ (sendo $F' = f$). <br> **2º TFC (Vol. 2, Cap. 2):** $\frac{d}{dx}\left[\int_a^x f(t)\,dt\right] = f(x)$. | **1º TFC (Vol. 1, Seção 5.1):** $\frac{d}{dx}\left[\int_a^x f(t)\,dt\right] = f(x)$. <br> **2º TFC (Vol. 1, Seção 5.3):** $\int_a^b f(x)\,dx = P(b) - P(a)$. |

---

## 2. Os 8 Pontos Críticos Onde Você Deve Redobrar a Atenção Conceitual

### Ponto Crítico 1: Propriedade do Supremo vs. Intervalos Encaixantes vs. Propriedade de Arquimedes
- 📘 **No Guidorizzi (Seção 1.5 e Apêndice 1):** A **Propriedade do Supremo** (Apêndice 1, Seção A1.2) é a propriedade mãe da completude de $\mathbb{R}$. Dela decorrem tanto a **Propriedade de Arquimedes** quanto a **Propriedade dos Intervalos Encaixantes** ($[a_0, b_0] \supset [a_1, b_1] \supset \dots$ com $\lim (b_n - a_n) = 0 \implies \exists!\, \alpha \in \bigcap_{n=0}^{\infty}[a_n, b_n]$).
- ⚠️ **O que nunca confundir:** A Propriedade de Arquimedes sozinha **não** implica completude (pois $\mathbb{Q}$ é arquimediano).

### Ponto Crítico 2: O Limite da Função Composta $\lim_{x \to p} g(f(x))$
- 📘 **No Guidorizzi (Seção 3.5, Teoremas 1 e 2):** Se $\lim_{x \to p} f(x) = a$ e $\lim_{u \to a} g(u) = L$, para concluir que $\lim_{x \to p} g(f(x)) = L$ é preciso que ocorra **pelo menos uma** de duas condições:
  1. Ou **$g$ é contínua em $a$** ($L = g(a)$, Teorema 1);
  2. Ou **existe $r > 0$ tal que $f(x) \neq a$ para todo $0 < |x - p| < r$** (Teorema 2).

### Ponto Crítico 3: O Teorema da Derivada da Função Inversa
- 📘 **No Guidorizzi (Seção 8.2):** Para provar que $g = f^{-1}$ é derivável em $p = f(q)$ (e não apenas achar uma fórmula supondo que $g'(p)$ já exista!), o teorema exige:
  1. $f$ inversível com inversa $g$;
  2. $f$ derivável em $q = g(p)$ com **$f'(q) \neq 0$**;
  3. **$g$ contínua em $p$** *(propriedade que **Apostol, Seção 3.13**, demonstra ser automática sempre que $f$ é contínua e estritamente monótona num intervalo!)*.

### Ponto Crítico 4: Concavidade e Ponto de Inflexão
- 📘 **No Guidorizzi (Seção 9.3):**
  - A **definição** de concavidade para cima (resp. para baixo) num intervalo aberto $I$ é geométrica: o gráfico de $f$ situa-se estritamente acima (resp. abaixo) da reta tangente $T(x) = f(p) + f'(p)(x-p)$ para quaisquer $x \neq p$ em $I$.
  - Um ponto $p \in D_f$ onde **$f$ é contínua** é **ponto de inflexão** se $f$ muda o sentido da concavidade ao passar por $p$ (não se exige na definição que $f$ seja duas vezes derivável em $p$: por exemplo, $f(x) = \sqrt[3]{x}$ tem ponto de inflexão em $p = 0$ mesmo sem ter derivada finita em $0$).

### Ponto Crítico 5: O Enunciado Geral do Teorema de Cauchy
- 📘 **No Guidorizzi (Seção 15.3):** Se $f$ e $g$ são contínuas em $[a, b]$ e deriváveis em $]a, b[$, existe $c \in \,]a, b[$ tal que:
  $$[f(b) - f(a)]g'(c) = [g(b) - g(a)]f'(c).$$
  Só dividimos por $g(b) - g(a)$ e $g'(c)$ quando garantimos $g'(x) \neq 0$ em $]a, b[$.

### Ponto Crítico 6: Por que $f$ Precisa Ser Integrável no Enunciado do 1º TFC de Guidorizzi?
- 📘 **No Guidorizzi (Seção 11.5):** O enunciado do 1º TFC diz: *"Se **$f$ for integrável em $[a, b]$** e se $F$ for uma primitiva de $f$ em $[a, b]$, então $\int_a^b f(x)\,dx = F(b) - F(a)$."*
- Por que não basta dizer "$F$ é primitiva de $f$"? Porque existem funções deriváveis $F$ em $[a, b]$ cuja derivada $f = F'$ **não é limitada** (ou é altamente oscilante, como $F(x) = x^2\operatorname{sen}(1/x^2)$ com $F(0)=0$) e, portanto, $f$ nem sequer é integrável segundo Riemann! Quando $f$ é contínua em $[a, b]$, ela é automaticamente integrável (Apêndice 4, Seção A4.3) e possui primitiva $G(x) = \int_a^x f(t)\,dt$ (Apostol, Seção 5.1 / Guidorizzi Vol. 2, Cap. 2).

### Ponto Crítico 7: AInversão de Nomes entre "1º TFC" e "2º TFC" (Guidorizzi vs. Apostol)
- Ao resolver uma prova na USP (Poli/IME) baseada no **Guidorizzi**, lembre-se sempre:
  - **1º TFC (Guidorizzi Vol. 1, Seção 11.5):** $\int_a^b f(x)\,dx = F(b) - F(a)$ (onde $F' = f$).
  - **2º TFC (Guidorizzi Vol. 2, Cap. 2):** $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$.
- Já ao ler o **Apostol (Cap. 5)**:
  - Apostol chama $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ de **1º TFC** (Seção 5.1) e $\int_a^b f(x)\,dx = P(b) - P(a)$ de **2º TFC** (Seção 5.3).

### Ponto Crítico 8: Soluções Constantes e Soluções Não Constantes nas EDOs Separáveis
- 📘 **No Guidorizzi (Cap. 14, Seções 14.3 e 14.4):** Ao resolver $\frac{dx}{dt} = g(t)h(x)$ (com $g$ contínua e $h'$ contínua):
  1. Primeiro ache **todas as raízes de $h(x) = 0$**: cada raiz $x_0$ fornece uma **solução constante $x(t) = x_0$**.
  2. Pelo **Teorema da Seção 14.4**, nenhuma solução não constante pode assumir valor $x_0$ onde $h(x_0) = 0$, o que legitima dividir por $h(x)$ para achar todas as soluções não constantes via $\int \frac{1}{h(x)}\,dx = \int g(t)\,dt + k$.

---

## 3. Tabela de Correspondência Direta de Capítulos (Guidorizzi 5ª Ed. $\leftrightarrow$ Apostol *Cálculo I*)

| Tópico de Cálculo 1 | 📘 Guidorizzi (Vol. 1, 5ª ed.) | 📙 Apostol (*Cálculo I*, 2ª ed.) |
| :--- | :--- | :--- |
| Números Reais, Módulo e Intervalos | Cap. 1 (1.1–1.4) e Apêndice 6 | Parte I.3 (I.3.1–I.3.8) e Parte I.4 (I.4.8) |
| Supremo, Arquimedes e Intervalos Encaixantes | Seção 1.5 e Apêndice 1 (A1.1–A1.3) | Parte I.3 (I.3.8–I.3.12) |
| Princípio de Indução Finita e Binômio de Newton | Cap. 17 (Seção 17.2) | Parte I.4 (Seções I.4.1–I.4.10) |
| Funções e Funções Trigonométricas | Cap. 2 (2.1–2.4) e Apêndice 3 (A3.2) | Cap. 1 (1.2–1.5) e Cap. 2 (2.5–2.7) |
| Continuidade e Limites Locais | Cap. 3 (3.1–3.9) | Cap. 3 (3.1–3.7) |
| Limites no Infinito, Infinitos, Sequências e $e$ | Cap. 4 (4.1–4.5) e Apêndice 1 (A1.4) | Cap. 7 (7.14–7.16) e Cap. 10 (10.2–10.4) |
| Teoremas de Bolzano, TVI e Weierstrass | Cap. 5 e Apêndice 2 (A2.1–A2.4) | Cap. 3 (3.8–3.9, 3.16–3.17) |
| Exponencial e Logaritmo | Cap. 6 (6.1–6.3) e Apêndice 3 (A3.1) | Cap. 6 (6.1–6.17) |
| Derivadas, Regra da Cadeia, Implícita e Taxas | Cap. 7 (7.1–7.17) | Cap. 4 (4.1–4.13) |
| Funções Inversas e Trigonométricas Inversas | Cap. 8 (8.1–8.2) | Cap. 3 (3.12–3.15) e Cap. 6 (6.18–6.21) |
| Rolle, TVM, Cauchy, L'Hospital, Gráficos e Extremos | Cap. 9 (9.1–9.8) e Cap. 15 (15.1–15.3) | Cap. 4 (4.14–4.21) e Cap. 7 (7.12–7.16) |
| Primitivas e Integral de Riemann / TFC | Cap. 10, Cap. 11 (11.1–11.8) e Apêndice 4 | Cap. 1 (1.8–1.27), Cap. 3 (3.18–3.19) e Cap. 5 (5.1–5.6) |
| Técnicas de Primitivação | Cap. 12 (12.1–12.11) | Cap. 5 (5.7–5.10) e Cap. 6 (6.22–6.25) |
| Aplicações da Integral (Volumes, Polares, Pappus) | Cap. 13 (13.1–13.9) e Apêndice 5 | Cap. 2 (2.1–2.18) |
| EDOs de 1ª Ordem (Separáveis e Lineares) | Cap. 14 (14.1–14.6) | Cap. 8 (8.1–8.7, 8.21–8.26) |
| Fórmula e Polinômios de Taylor | Cap. 16 (16.1–16.3) | Cap. 7 (7.1–7.11) |
| Arquimedes, Pascal e Fermat (Quadraturas) | Cap. 17 (17.1–17.3) | Parte I.1 (I.1.1–I.1.5) |
