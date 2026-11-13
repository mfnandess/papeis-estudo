# Caderno de Exercícios, Problemas Clássicos e Demonstrações de Cálculo I
## Paper Prático Acoplado ao Tratado de Cálculo 1: *Um Curso de Cálculo — Vol. 1* (H. L. Guidorizzi, 5ª Edição) + Complementos de *Cálculo I* (Tom M. Apostol)

---

> **Navegação Rápida entre os Papers deste Repositório (GitHub Pages):**
> - 📄 **[Paper 1 — Tratado Teórico Principal (Capítulos 1 a 17 + Apêndices)](./index.html)** | [Versão Markdown](./Paper_Calculo_1_Guidorizzi_Apostol.md)
> - 📝 **[Paper 2 — Caderno de Exercícios Resolvidos (Você está aqui)](./exercicios.html)** | [Versão Markdown](./Caderno_Exercicios_Calculo_1.md)
> - ⚖️ **[Paper 3 — Guia Comparativo: Guidorizzi (5ª ed.) vs. Apostol (Cálculo I)](./comparativo-guidorizzi-apostol.html)** | [Versão Markdown](./Comparativo_Guidorizzi_vs_Apostol.md)

---

> **Sobre este Paper de Exercícios**  
> Este caderno reúne **45 problemas fundamentais e demonstrações selecionadas**, organizados na sequência exata dos **17 capítulos de *Um Curso de Cálculo — Volume 1* (5ª edição), de Hamilton Luiz Guidorizzi**, acrescidos de exercícios teóricos clássicos de ***Cálculo I*, de Tom M. Apostol**.  
> Cada exercício traz:
> 1. **Selo de Referência Explícito:** `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção X.Y]` ou `📙 [Mudança de Referência — Apostol, Cálculo I, Seção Y.Z]`;
> 2. **Classificação de Nível:** 🟢 *Fixação e Técnica*, 🟡 *Clássico de Prova (Poli/IME-USP)*, 🔴 *Desafio Teórico / Demonstração*;
> 3. **Dica Estratégica** (para você tentar resolver antes de abrir a resposta);
> 4. **Resolução Completa Passo a Passo** (expansível).

---

## Sumário por Blocos Temáticos
1. [Bloco 1 — Números Reais, Módulo, Desigualdades, Indução e Funções (Cap. 1 e 2)](#cap-1-2)
2. [Bloco 2 — Limite, Continuidade, $\varepsilon$-$\delta$, Confronto e 1º Limite Fundamental (Cap. 3)](#cap-3)
3. [Bloco 3 — Limites no Infinito, Limites Infinitos, Sequências e o Número $e$ (Cap. 4)](#cap-4)
4. [Bloco 4 — Teoremas Globais: Anulamento (Bolzano), TVI e Weierstrass (Cap. 5)](#cap-5)
5. [Bloco 5 — Funções Exponencial e Logarítmica (Cap. 6)](#cap-6)
6. [Bloco 6 — Derivadas, Regra da Cadeia, Implícita, Diferencial e Taxas (Cap. 7)](#cap-7)
7. [Bloco 7 — Funções Inversas e Trigonométricas Inversas (Cap. 8)](#cap-8)
8. [Bloco 8 — Rolle, TVM, Cauchy, L'Hospital, Concavidade, Gráficos e Otimização (Cap. 9 e 15)](#cap-9-15)
9. [Bloco 9 — Primitivas, Integral de Riemann, 1º e 2º TFC, Áreas e Trabalho (Cap. 10 e 11)](#cap-10-11)
10. [Bloco 10 — Técnicas de Primitivação: Partes, Substituição Trigonométrica e Frações Parciais (Cap. 12)](#cap-12)
11. [Bloco 11 — Volumes, Comprimento de Arco, Área de Superfície, Polares e Pappus (Cap. 13)](#cap-13)
12. [Bloco 12 — Equações Diferenciais de 1ª Ordem Separáveis e Lineares (Cap. 14)](#cap-14)
13. [Bloco 13 — Polinômios e Fórmula de Taylor com Restos de Peano e Lagrange (Cap. 16)](#cap-16)
14. [Bloco 14 — Quadraturas Históricas de Arquimedes, Pascal e Fermat (Cap. 17)](#cap-17)

---

<a id="cap-1-2"></a>
## Bloco 1 — Números Reais, Módulo, Supremo e Funções (Capítulos 1 e 2)

### Exercício B1.1 🟢 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 1.3, Ex. 3 e 5]`
Elimine o módulo na expressão $f(x) = |x - 1| + |x + 2|$ e resolva a inequação $|2x - 1| < |x + 1|$.
- **Dica:** Para a função com dois módulos, estude o sinal nos intervalos determinados pelas raízes $-2$ e $1$. Para a inequação entre módulos, como ambos os lados são $\ge 0$, eleve ao quadrado usando $|A| < |B| \iff A^2 < B^2 \iff (A-B)(A+B) < 0$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Eliminação do módulo em $f(x) = |x - 1| + |x + 2|$ (Exemplo 10, Seção 1.3):**  
   As mudanças de sinal ocorrem em $x = -2$ e $x = 1$:
   - Para $x < -2$: $x - 1 < 0$ e $x + 2 < 0 \implies f(x) = -(x - 1) - (x + 2) = -2x - 1$.
   - Para $-2 \le x < 1$: $x - 1 < 0$ e $x + 2 \ge 0 \implies f(x) = -(x - 1) + (x + 2) = 3$.
   - Para $x \ge 1$: $x - 1 \ge 0$ e $x + 2 \ge 0 \implies f(x) = (x - 1) + (x + 2) = 2x + 1$.
   Logo:
   $$|x - 1| + |x + 2| = \begin{cases} -2x - 1, & \text{se } x < -2 \\ 3, & \text{se } -2 \le x < 1 \\ 2x + 1, & \text{se } x \ge 1. \end{cases}$$
2. **Resolução de $|2x - 1| < |x + 1|$:**  
   Como $|u|^2 = u^2$ e ambos os membros são não negativos:
   $$|2x - 1| < |x + 1| \iff (2x - 1)^2 < (x + 1)^2 \iff (2x - 1)^2 - (x + 1)^2 < 0.$$
   Pela diferença de quadrados $A^2 - B^2 = (A - B)(A + B)$:
   $$[(2x - 1) - (x + 1)][(2x - 1) + (x + 1)] < 0 \iff (x - 2)(3x) < 0 \iff \mathbf{0 < x < 2 \;\; (x \in \,]0, 2[)}. \quad \blacksquare$$
</details>

---

### Exercício B1.2 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 1.3, Ex. 6 e 7]`
Prove que, quaisquer que sejam $x, y \in \mathbb{R}$:
(a) $|x + y| = |x| + |y| \iff xy \ge 0$;  
(b) $\big||x| - |y|\big| \le |x - y|$.
- **Dica:** Em (a), eleve ambos os membros não negativos ao quadrado e use $|x|^2 = x^2$ e $|xy| = xy \iff xy \ge 0$. Em (b), aplique a desigualdade triangular a $x = (x - y) + y$ e a $y = (y - x) + x$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Como $|x + y| \ge 0$ e $|x| + |y| \ge 0$:
   $$|x + y| = |x| + |y| \iff |x + y|^2 = (|x| + |y|)^2 \iff (x + y)^2 = |x|^2 + 2|x||y| + |y|^2.$$
   Como $(x + y)^2 = x^2 + 2xy + y^2$, $|x|^2 = x^2$, $|y|^2 = y^2$ e $|x||y| = |xy|$, a igualdade equivale a:
   $$x^2 + 2xy + y^2 = x^2 + 2|xy| + y^2 \iff xy = |xy| \iff \mathbf{xy \ge 0}.$$
2. **Item (b):** Pela desigualdade triangular:
   $$|x| = |(x - y) + y| \le |x - y| + |y| \implies |x| - |y| \le |x - y|.$$
   Trocando os papéis de $x$ e $y$:
   $$|y| = |(y - x) + x| \le |y - x| + |x| = |x - y| + |x| \implies |y| - |x| = -(|x| - |y|) \le |x - y|.$$
   Logo, $-|x - y| \le |x| - |y| \le |x - y| \iff \mathbf{\big||x| - |y|\big| \le |x - y|}$. $\blacksquare$
</details>

---

### Exercício B1.3 🔴 `📙 [Mudança de Referência — Apostol, Cálculo I, Parte I.3, Seção I.3.12, Ex. 5 e Guidorizzi, Apêndice 1, Seção A1.2]`
Sejam $A$ e $B$ dois subconjuntos não vazios de $\mathbb{R}$, limitados superiormente, e seja $C = \{x + y \mid x \in A, y \in B\}$. Prove que $C$ é limitado superiormente e que:
$$\sup C = \sup A + \sup B.$$
- **Dica:** Mostre primeiro que $\sup A + \sup B$ é cota superior de $C$ (logo $\sup C \le \sup A + \sup B$). Depois, dado $\varepsilon > 0$ arbitrário, use a caracterização do supremo para escolher $x \in A$ com $x > \sup A - \frac{\varepsilon}{2}$ e $y \in B$ com $y > \sup B - \frac{\varepsilon}{2}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. Sejam $a = \sup A$ e $b = \sup B$. Para todo $x \in A$ e todo $y \in B$, temos $x \le a$ e $y \le b$, logo $x + y \le a + b$. Assim, $a + b$ é uma cota superior de $C$, o que garante que $C$ admite supremo $c = \sup C$ e que **$c \le a + b$**.
2. Para provar que $c = a + b$, suponhamos, ou mostremos diretamente: dado qualquer $\varepsilon > 0$, como $a = \sup A$, $a - \frac{\varepsilon}{2}$ não é cota superior de $A$, logo existe $x_0 \in A$ tal que $a - \frac{\varepsilon}{2} < x_0$. Analogamente, existe $y_0 \in B$ tal que $b - \frac{\varepsilon}{2} < y_0$.
3. Somando as duas desigualdades, obtemos um elemento $x_0 + y_0 \in C$ tal que:
   $$(a + b) - \varepsilon < x_0 + y_0 \le \sup C = c.$$
   Como $(a + b) - \varepsilon < c$ vale para todo $\varepsilon > 0$, concluímos que $a + b \le c$. Combinando com $c \le a + b$, segue **$\sup C = \sup A + \sup B$**. $\blacksquare$
</details>

---

<a id="cap-3"></a>
## Bloco 2 — Limite e Continuidade (Capítulo 3)

### Exercício B2.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 3.2, Ex. 21 e Seção 3.3]`
(a) Prove, diretamente pela definição $\varepsilon$-$\delta$, que $\lim_{x \to 2} x^2 = 4$.  
(b) (**Densidade de $\mathbb{Q}$ e Funções Contínuas — Ex. 21 da Seção 3.2:**) Sejam $f, g: \mathbb{R} \to \mathbb{R}$ duas funções contínuas em $\mathbb{R}$ tais que $f(r) = g(r)$ para todo número racional $r \in \mathbb{Q}$. Prove que $f(x) = g(x)$ para todo real $x \in \mathbb{R}$.
- **Dica:** Em (a), escreva $|x^2 - 4| = |x - 2||x + 2|$ e restrinja inicialmente $|x - 2| < 1$ para limitar $|x + 2| < 5$, tomando $\delta = \min\left\{1, \frac{\varepsilon}{5}\right\}$. Em (b), considere $h(x) = f(x) - g(x)$ e use o Teorema da Conservação do Sinal caso existisse $p \in \mathbb{R}$ com $h(p) \neq 0$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Dado $\varepsilon > 0$, queremos achar $\delta > 0$ tal que $0 < |x - 2| < \delta \implies |x^2 - 4| = |x - 2||x + 2| < \varepsilon$.  
   Se exigirmos primeiramente $|x - 2| < 1$, teremos $1 < x < 3 \implies 3 < x + 2 < 5 \implies |x + 2| < 5$. Assim, para $|x - 2| < 1$, vale $|x - 2||x + 2| < 5|x - 2|$.  
   Tomando então **$\delta = \min\left\{1, \frac{\varepsilon}{5}\right\} > 0$**, sempre que $0 < |x - 2| < \delta$ temos simultaneamente $|x - 2| < 1$ (donde $|x+2| < 5$) e $|x - 2| < \frac{\varepsilon}{5}$, logo:
   $$|x^2 - 4| = |x - 2||x + 2| < 5|x - 2| < 5\left(\frac{\varepsilon}{5}\right) = \varepsilon. \quad \blacksquare$$
2. **Item (b):** Seja $h(x) = f(x) - g(x)$. Como $f$ e $g$ são contínuas em $\mathbb{R}$, $h$ é contínua em $\mathbb{R}$ e $h(r) = 0$ para todo $r \in \mathbb{Q}$. Suponha, por absurdo, que exista $p \in \mathbb{R}$ tal que $h(p) \neq 0$. Pela continuidade de $h$ em $p$, $\lim_{x \to p} h(x) = h(p) \neq 0$. Pelo **Teorema da Conservação do Sinal**, existe $\delta > 0$ tal que para todo $x \in \,]p - \delta, p + \delta[$, $h(x)$ tem o mesmo sinal de $h(p)$ (em particular, $h(x) \neq 0$ em todo o intervalo $]p-\delta, p+\delta[$). Mas entre dois reais quaisquer $p - \delta < p + \delta$ sempre existe pelo menos um número racional $r \in \mathbb{Q}$, para o qual $h(r) = 0$ — contradição! Logo, $h(p) = 0 \iff f(p) = g(p)$ para todo $p \in \mathbb{R}$. $\blacksquare$
</details>

---

### Exercício B2.2 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 3.3 e Seção 3.8]`
Calcule os seguintes limites sem usar a Regra de L'Hospital (usando fatoração, conjugado de raízes e o 1º Limite Fundamental):
(a) $\displaystyle \lim_{x \to 1} \frac{\sqrt[3]{x} - 1}{\sqrt{x} - 1}$; $\qquad$ (b) $\displaystyle \lim_{x \to 0} \frac{\cos(2x) - \cos(3x)}{x^2}$; $\qquad$ (c) $\displaystyle \lim_{x \to p} \frac{\operatorname{sen} x - \operatorname{sen} p}{x - p}$.
- **Dica:** Em (a), faça a mudança de variável $x = u^6$ ($u \to 1$). Em (b), use prostaférese $\cos A - \cos B = -2\operatorname{sen}\left(\frac{A+B}{2}\right)\operatorname{sen}\left(\frac{A-B}{2}\right)$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Fazendo $x = u^6$ ($u = \sqrt[6]{x}$), quando $x \to 1$ temos $u \to 1$ ($u \neq 1$). Então $\sqrt[3]{x} = u^2$ e $\sqrt{x} = u^3$:
   $$\lim_{x \to 1} \frac{\sqrt[3]{x} - 1}{\sqrt{x} - 1} = \lim_{u \to 1} \frac{u^2 - 1}{u^3 - 1} = \lim_{u \to 1} \frac{(u - 1)(u + 1)}{(u - 1)(u^2 + u + 1)} = \frac{1 + 1}{1 + 1 + 1} = \mathbf{\frac{2}{3}}.$$
2. **Item (b):** Pela fórmula de transformação em produto $\cos(2x) - \cos(3x) = -2\operatorname{sen}\left(\frac{5x}{2}\right)\operatorname{sen}\left(-\frac{x}{2}\right) = 2\operatorname{sen}\left(\frac{5x}{2}\right)\operatorname{sen}\left(\frac{x}{2}\right)$:
   $$\lim_{x \to 0} \frac{\cos(2x) - \cos(3x)}{x^2} = \lim_{x \to 0} 2 \cdot \frac{\operatorname{sen}(5x/2)}{(5x/2)} \cdot \frac{5}{2} \cdot \frac{\operatorname{sen}(x/2)}{(x/2)} \cdot \frac{1}{2} = 2 \cdot 1 \cdot \frac{5}{2} \cdot 1 \cdot \frac{1}{2} = \mathbf{\frac{5}{2}}.$$
3. **Item (c):** Como $\operatorname{sen} x - \operatorname{sen} p = 2\operatorname{sen}\left(\frac{x - p}{2}\right)\cos\left(\frac{x + p}{2}\right)$:
   $$\lim_{x \to p} \frac{\operatorname{sen} x - \operatorname{sen} p}{x - p} = \lim_{x \to p} \frac{\operatorname{sen}\left(\frac{x - p}{2}\right)}{\frac{x - p}{2}} \cdot \cos\left(\frac{x + p}{2}\right) = 1 \cdot \cos p = \mathbf{\cos p}. \quad \blacksquare$$
</details>

---

<a id="cap-4"></a>
## Bloco 3 — Extensões do Limite, Sequências e o Número $e$ (Capítulo 4)

### Exercício B3.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 4.1 e Seção 4.3]`
Calcule os limites no infinito:
(a) $\displaystyle \lim_{x \to -\infty} \frac{\sqrt{9x^2 + x + 1}}{2x - 5}$; $\qquad$ (b) $\displaystyle \lim_{x \to +\infty} \left(\sqrt{x^2 + 3x} - x\right)$; $\qquad$ (c) $\displaystyle \lim_{n \to \infty} \sqrt[n]{3^n + 5^n}$.
- **Dica:** Em (a), lembre-se de que para $x < 0$, $\sqrt{x^2} = |x| = -x$! Em (b), multiplique pelo conjugado $\sqrt{x^2 + 3x} + x$. Em (c), coloque $5^n$ em evidência dentro da raiz $n$-ésima e use o Teorema do Confronto ($5 \le \sqrt[n]{3^n + 5^n} \le 5\sqrt[n]{2}$).

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Para $x < 0$, temos $\sqrt{x^2} = |x| = -x$. Colocando $x^2$ em evidência dentro do radical:
   $$\lim_{x \to -\infty} \frac{\sqrt{9x^2 + x + 1}}{2x - 5} = \lim_{x \to -\infty} \frac{|x|\sqrt{9 + \frac{1}{x} + \frac{1}{x^2}}}{x\left(2 - \frac{5}{x}\right)} = \lim_{x \to -\infty} \frac{-x\sqrt{9 + \frac{1}{x} + \frac{1}{x^2}}}{x\left(2 - \frac{5}{x}\right)} = \frac{-\sqrt{9}}{2} = \mathbf{-\frac{3}{2}}.$$
2. **Item (b):** Multiplicando e dividindo pelo conjugado $\sqrt{x^2 + 3x} + x$ (com $x > 0$):
   $$\lim_{x \to +\infty} \left(\sqrt{x^2 + 3x} - x\right) = \lim_{x \to +\infty} \frac{(x^2 + 3x) - x^2}{\sqrt{x^2 + 3x} + x} = \lim_{x \to +\infty} \frac{3x}{x\left(\sqrt{1 + \frac{3}{x}} + 1\right)} = \frac{3}{1 + 1} = \mathbf{\frac{3}{2}}.$$
3. **Item (c):** Como $5^n < 3^n + 5^n < 5^n + 5^n = 2 \cdot 5^n$, extraindo a raiz $n$-ésima:
   $$5 < \sqrt[n]{3^n + 5^n} < 5 \cdot \sqrt[n]{2}.$$
   Como $\lim_{n \to \infty} \sqrt[n]{2} = 1$, pelo Teorema do Confronto obtemos $\lim_{n \to \infty} \sqrt[n]{3^n + 5^n} = \mathbf{5}$. $\blacksquare$
</details>

---

<a id="cap-5"></a>
## Bloco 4 — Teoremas Globais em $[a, b]$: Anulamento, TVI e Weierstrass (Capítulo 5)

### Exercício B4.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Cap. 5, Ex. 2, 7 e 11]`
(a) (**Teorema do Ponto Fixo em $[0, 1]$ — Ex. 11, Cap. 5:**) Seja $f: [0, 1] \to \mathbb{R}$ uma função contínua tal que, para todo $x \in [0, 1]$, tem-se $0 \le f(x) \le 1$. Prove que existe pelo menos um $c \in [0, 1]$ tal que **$f(c) = c$**.  
(b) (**Ex. 2, Cap. 5:**) Prove que a equação $x^3 - 4x + 2 = 0$ admite exatamente **três raízes reais distintas** e localize cada uma num intervalo de amplitude $1$.
- **Dica:** Em (a), aplique o Teorema do Anulamento à função auxiliar $g(x) = f(x) - x$ em $[0, 1]$. Em (b), calcule $f(-3), f(-2), f(0), f(1), f(2)$ e observe as mudanças de sinal!

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Se $f(0) = 0$ ou $f(1) = 1$, basta tomar $c = 0$ ou $c = 1$. Suponhamos então que $f(0) \neq 0$ e $f(1) \neq 1$. Como $0 \le f(x) \le 1$ para todo $x \in [0, 1]$, temos $f(0) > 0$ e $f(1) < 1$.  
   Considere a função auxiliar $g(x) = f(x) - x$, que é contínua em $[0, 1]$. Temos:
   $$g(0) = f(0) - 0 > 0 \qquad \text{e} \qquad g(1) = f(1) - 1 < 0.$$
   Pelo **Teorema do Anulamento (Bolzano)**, existe $c \in \,]0, 1[$ tal que $g(c) = 0 \iff \mathbf{f(c) = c}$. $\blacksquare$
2. **Item (b):** Seja $f(x) = x^3 - 4x + 2$, contínua em $\mathbb{R}$. Avaliando nos inteiros:
   - $f(-3) = -27 + 12 + 2 = -13 < 0$;
   - $f(-2) = -8 + 8 + 2 = 2 > 0$;
   - $f(0) = 2 > 0$;
   - $f(1) = 1 - 4 + 2 = -1 < 0$;
   - $f(2) = 8 - 8 + 2 = 2 > 0$.
   Pelo Teorema do Anulamento, $f$ possui pelo menos uma raiz real $r_1 \in \,]-3, -2[$, uma raiz $r_2 \in \,]0, 1[$ e uma raiz $r_3 \in \,]1, 2[$. Como um polinômio de grau $3$ tem no máximo $3$ raízes reais, essas são as três únicas raízes reais da equação! $\blacksquare$
</details>

---

### Exercício B4.2 🔴 `📘 [Guidorizzi, Vol. 1, 5ª ed., Cap. 5, Ex. 10 e Ex. 12]`
(a) Suponha que $f: [0, 1] \to \mathbb{R}$ seja contínua, $f(0) = 1$ e que **$f(x)$ seja um número racional para todo $x \in [0, 1]$**. Prove que $f(x) = 1$ para todo $x \in [0, 1]$.  
(b) Seja $f$ contínua e injetora em $[a, b]$ com $f(a) < f(b)$. Prove, usando apenas o TVI, que $f$ é **estritamente crescente** em $[a, b]$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Suponha, por absurdo, que exista $x_0 \in [0, 1]$ tal que $f(x_0) \neq 1$. Como $f$ é contínua em $[0, x_0]$, pelo **Teorema do Valor Intermediário (TVI)** $f$ deveria assumir todos os valores reais compreendidos entre $f(0) = 1$ e $f(x_0)$. Mas entre dois números reais distintos existem infinitos números **irracionais**, contradizendo a hipótese de que $f(x) \in \mathbb{Q}$ para todo $x \in [0, 1]$! Logo, $f(x) = 1$ para todo $x \in [0, 1]$. $\blacksquare$
2. **Item (b):** Dados $s, t \in [a, b]$ com $s < t$, precisamos provar que $f(s) < f(t)$.  
   Primeiro mostremos que para todo $x \in \,]a, b[$, tem-se $f(a) < f(x) < f(b)$:
   - Se fosse $f(x) < f(a) < f(b)$, pelo TVI aplicado em $[x, b]$ existiria $c \in \,]x, b[$ tal que $f(c) = f(a)$, contradizendo a injetividade de $f$ ($c \neq a$)!
   - Se fosse $f(a) < f(b) < f(x)$, pelo TVI aplicado em $[a, x]$ existiria $c \in \,]a, x[$ tal que $f(c) = f(b)$, novamente contradizendo a injetividade!
   Logo, $f(a) < f(x) < f(b)$ para todo $x \in \,]a, b[$. Aplicando esse mesmo raciocínio ao subintervalo $[s, b]$ (já que $f(s) < f(b)$), para todo $t \in \,]s, b]$ resulta **$f(s) < f(t)$**! $\blacksquare$
</details>

---

<a id="cap-6"></a>
## Bloco 5 — Funções Exponencial e Logarítmica (Capítulo 6)

### Exercício B5.1 🟢 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 6.3, Ex. 1 a 3]`
Calcule os limites exponenciais e logarítmicos usando os limites fundamentais da Seção 6.3:
(a) $\displaystyle \lim_{x \to +\infty} \left(\frac{2x + 3}{2x - 1}\right)^{x + 1}$; $\qquad$ (b) $\displaystyle \lim_{x \to 0} \frac{a^x - b^x}{x}$ ($a > 0, b > 0$); $\qquad$ (c) $\displaystyle \lim_{x \to 0} \frac{\ln(\cos x)}{x^2}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Dividindo numerador e denominador por $2x$ ou somando e subtraindo no numerador:
   $$\frac{2x + 3}{2x - 1} = \frac{(2x - 1) + 4}{2x - 1} = 1 + \frac{4}{2x - 1}.$$
   Fazendo $u = \frac{2x - 1}{4} \iff 2x - 1 = 4u \iff x = 2u + \frac{1}{2}$ ($x \to +\infty \iff u \to +\infty$):
   $$\left(\frac{2x + 3}{2x - 1}\right)^{x + 1} = \left(1 + \frac{1}{u}\right)^{2u + 3/2} = \left[\left(1 + \frac{1}{u}\right)^u\right]^2 \cdot \left(1 + \frac{1}{u}\right)^{3/2} \xrightarrow{u \to +\infty} e^2 \cdot 1^{3/2} = \mathbf{e^2}.$$
2. **Item (b):** Somando e subtraindo $1$ no numerador e usando $\lim_{x \to 0} \frac{a^x - 1}{x} = \ln a$ (Ex. 2, Seção 6.3):
   $$\lim_{x \to 0} \frac{a^x - b^x}{x} = \lim_{x \to 0} \left(\frac{a^x - 1}{x} - \frac{b^x - 1}{x}\right) = \ln a - \ln b = \mathbf{\ln\left(\frac{a}{b}\right)}.$$
3. **Item (c):** Escrevendo $\cos x = 1 + (\cos x - 1)$ e multiplicando e dividindo por $\cos x - 1$:
   $$\lim_{x \to 0} \frac{\ln(\cos x)}{x^2} = \lim_{x \to 0} \frac{\ln\big(1 + (\cos x - 1)\big)}{\cos x - 1} \cdot \frac{\cos x - 1}{x^2} = 1 \cdot \left(-\frac{1}{2}\right) = \mathbf{-\frac{1}{2}}. \quad \blacksquare$$
</details>

---

<a id="cap-7"></a>
## Bloco 6 — Derivadas, Regra da Cadeia, Implícita e Taxas Relacionadas (Capítulo 7)

### Exercício B6.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seções 7.13, 7.15 e 7.16]`
(a) (**Derivação Implícita — Fólio de Descartes, Seção 7.13:**) Sendo $y = f(x)$ definida implicitamente pela equação $x^3 + y^3 - 3xy = 0$, determine $\frac{dy}{dx}$ e a equação da reta tangente no ponto $\left(\frac{3}{2}, \frac{3}{2}\right)$.  
(b) (**Taxas Relacionadas — Seção 7.15:**) Uma escada de $5\text{ m}$ de comprimento está apoiada numa parede vertical. Se a base da escada desliza horizontalmente afastando-se da parede à velocidade constante de $1{,}2\text{ m/s}$, com que velocidade o topo da escada escorrega para baixo no instante em que a base está a $3\text{ m}$ da parede?

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Derivando ambos os membros de $x^3 + y^3 - 3xy = 0$ em relação a $x$ (usando a Regra da Cadeia em $y^3$ e a Regra do Produto em $3xy$):
   $$3x^2 + 3y^2 y' - 3(1 \cdot y + x y') = 0 \implies (y^2 - x)y' = y - x^2 \implies \mathbf{y' = \frac{y - x^2}{y^2 - x}}.$$
   No ponto $\left(\frac{3}{2}, \frac{3}{2}\right)$:
   $$y'\left(\frac{3}{2}\right) = \frac{\frac{3}{2} - \frac{9}{4}}{\frac{9}{4} - \frac{3}{2}} = -1.$$
   Logo, a equação da reta tangente é $y - \frac{3}{2} = -1\left(x - \frac{3}{2}\right) \iff \mathbf{x + y - 3 = 0}$.
2. **Item (b):** Sejam $x(t)$ a distância da base à parede e $y(t)$ a altura do topo. Pelo Teorema de Pitágoras:
   $$x^2(t) + y^2(t) = 5^2 = 25.$$
   Derivando ambos os membros em relação ao tempo $t$:
   $$2x(t)\frac{dx}{dt} + 2y(t)\frac{dy}{dt} = 0 \implies \frac{dy}{dt} = -\frac{x(t)}{y(t)}\frac{dx}{dt}.$$
   Quando $x = 3\text{ m}$, temos $y = \sqrt{25 - 9} = 4\text{ m}$ e $\frac{dx}{dt} = 1{,}2\text{ m/s}$. Portanto:
   $$\frac{dy}{dt} = -\frac{3}{4} \cdot 1{,}2 = \mathbf{-0{,}9\text{ m/s}} \quad (\text{desce à razão de } 0{,}9\text{ m/s}). \quad \blacksquare$$
</details>

---

<a id="cap-8"></a>
## Bloco 7 — Funções Inversas e suas Derivadas (Capítulo 8)

### Exercício B7.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 8.2, Ex. 1 a 5]`
(a) Seja $f(x) = x^5 + 2x^3 + x - 1$. Mostre que $f$ é inversível com inversa $g = f^{-1}$ derivável em $\mathbb{R}$, e calcule **$g'(3)$** e **$g''(3)$**.  
(b) Simplifique a derivada de $h(x) = \operatorname{arctg}\left(\frac{1 + x}{1 - x}\right)$ para $x \neq 1$, e interprete o resultado.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Temos $f'(x) = 5x^4 + 6x^2 + 1 \ge 1 > 0$ para todo $x \in \mathbb{R}$, logo $f$ é estritamente crescente, sobrejetora em $\mathbb{R}$ e sua inversa $g = f^{-1}$ é derivável em todo $\mathbb{R}$.  
   Por inspeção, $f(1) = 1 + 2 + 1 - 1 = 3 \iff g(3) = 1$ (e como $f$ é injetora, $q = 1$ é o único ponto tal que $f(q) = 3$).  
   Pelo Teorema da Derivada da Inversa:
   $$g'(3) = \frac{1}{f'(g(3))} = \frac{1}{f'(1)} = \frac{1}{5(1)^4 + 6(1)^2 + 1} = \mathbf{\frac{1}{12}}.$$
   Para calcular $g''(3)$, derivamos $g'(y) = \frac{1}{f'(g(y))}$ pela Regra da Cadeia:
   $$g''(y) = -\frac{f''(g(y)) \cdot g'(y)}{[f'(g(y))]^2} = -\frac{f''(g(y))}{[f'(g(y))]^3}.$$
   Como $f''(x) = 20x^3 + 12x \implies f''(1) = 32$, resulta:
   $$g''(3) = -\frac{f''(1)}{[f'(1)]^3} = -\frac{32}{12^3} = -\frac{32}{1728} = \mathbf{-\frac{1}{54}}.$$
2. **Item (b):** Pela Regra da Cadeia e Regra do Quociente:
   $$h'(x) = \frac{1}{1 + \left(\frac{1+x}{1-x}\right)^2} \cdot \frac{1(1-x) - (1+x)(-1)}{(1-x)^2} = \frac{(1-x)^2}{(1-x)^2 + (1+x)^2} \cdot \frac{2}{(1-x)^2} = \frac{2}{2 + 2x^2} = \mathbf{\frac{1}{1 + x^2}}.$$
   Observe que $h'(x) = (\operatorname{arctg} x)'$ em cada um dos intervalos $]-\infty, 1[$ e $]1, +\infty[$! Pelo Corolário da Seção 10.1, em cada um desses dois intervalos separadamente, $h(x) - \operatorname{arctg} x$ é constante (valendo $\frac{\pi}{4}$ para $x < 1$ e $-\frac{3\pi}{4}$ para $x > 1$). $\blacksquare$
</details>

---

<a id="cap-9-15"></a>
## Bloco 8 — TVM, Rolle, Cauchy, Variação de Funções e Otimização (Capítulos 9 e 15)

### Exercício B8.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 9.2, Ex. 6 e 9]`
Utilizando o Teorema do Valor Médio (ou o estudo de crescimento da Seção 9.2), demonstre as desigualdades clássicas:
(a) **Desigualdade de Bernoulli Generalizada:** $(1 + x)^\alpha > 1 + \alpha x$ para todo $x > 0$ e $\alpha > 1$;  
(b) $\dfrac{x}{1 + x^2} < \operatorname{arctg} x < x$ para todo $x > 0$;  
(c) $|\operatorname{sen} b - \operatorname{sen} a| \le |b - a|$ para todos $a, b \in \mathbb{R}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Seja $f(x) = (1 + x)^\alpha - (1 + \alpha x)$ para $x \ge 0$ ($\alpha > 1$). Temos $f(0) = 0$ e, para $x > 0$:
   $$f'(x) = \alpha(1 + x)^{\alpha - 1} - \alpha = \alpha\big[(1 + x)^{\alpha - 1} - 1\big] > 0$$
   pois $1 + x > 1$ e $\alpha - 1 > 0 \implies (1+x)^{\alpha-1} > 1$. Logo, $f$ é estritamente crescente em $[0, +\infty[$, donde para todo $x > 0$ vale $f(x) > f(0) = 0 \iff \mathbf{(1 + x)^\alpha > 1 + \alpha x}$.
2. **Item (b):** Para $x > 0$, aplicamos o **TVM** à função $g(t) = \operatorname{arctg} t$ no intervalo $[0, x]$: existe $c \in \,]0, x[$ tal que:
   $$\frac{\operatorname{arctg} x - \operatorname{arctg} 0}{x - 0} = g'(c) = \frac{1}{1 + c^2} \implies \operatorname{arctg} x = \frac{x}{1 + c^2}.$$
   Como $0 < c < x \implies 1 < 1 + c^2 < 1 + x^2 \implies \frac{1}{1 + x^2} < \frac{1}{1 + c^2} < 1$, multiplicando por $x > 0$ obtemos imediatamente:
   $$\mathbf{\frac{x}{1 + x^2} < \operatorname{arctg} x < x} \quad (\forall x > 0).$$
3. **Item (c):** Se $a = b$, a igualdade $0 \le 0$ é óbvia. Se $a \neq b$, pelo TVM aplicado a $f(x) = \operatorname{sen} x$ no intervalo fechado de extremos $a$ e $b$, existe $c$ entre $a$ e $b$ tal que $\operatorname{sen} b - \operatorname{sen} a = (\cos c)(b - a)$. Tomando módulos e usando $|\cos c| \le 1$, segue $|\operatorname{sen} b - \operatorname{sen} a| = |\cos c||b - a| \le |b - a|$. $\blacksquare$
</details>

---

### Exercício B8.2 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 9.6 e Seção 9.8]`
Determine as dimensões (raio da base $r$ e altura $h$) do cilindro circular reto de **volume máximo** que pode ser inscrito numa esfera de raio fixo $R > 0$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Modelagem Geométrica:** Num corte meridiano da esfera de raio $R$, o retângulo gerador do cilindro tem base $2r$ e altura $h$, inscrito num círculo de raio $R$. Pelo Teorema de Pitágoras:
   $$r^2 + \left(\frac{h}{2}\right)^2 = R^2 \implies r^2 = R^2 - \frac{h^2}{4}, \quad \text{com } h \in [0, 2R].$$
2. **Função Volume em uma variável $h \in [0, 2R]$:**
   $$V(h) = \pi r^2 h = \pi\left(R^2 - \frac{h^2}{4}\right)h = \pi\left(R^2 h - \frac{h^3}{4}\right), \quad h \in [0, 2R].$$
3. **Maximização em $[0, 2R]$:** Como $V(0) = 0$ e $V(2R) = 0$, e $V(h) > 0$ em $]0, 2R[$, o máximo global ocorre no interior $]0, 2R[$. Derivando em relação a $h$:
   $$V'(h) = \pi\left(R^2 - \frac{3h^2}{4}\right) = 0 \implies h^2 = \frac{4R^2}{3} \implies \mathbf{h = \frac{2R}{\sqrt{3}} = \frac{2\sqrt{3}}{3}R}.$$
   Como $V''(h) = -\frac{3\pi}{2}h < 0$ para $h > 0$, este é o ponto de máximo global! O raio correspondente é:
   $$r = \sqrt{R^2 - \frac{h^2}{4}} = \sqrt{R^2 - \frac{R^2}{3}} = \mathbf{R\sqrt{\frac{2}{3}}}, \qquad \text{com } V_{\max} = \mathbf{\frac{4\pi\sqrt{3}}{9}R^3}. \quad \blacksquare$$
</details>

---

### Exercício B8.3 🔴 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 9.7, Ex. 8 — Teorema de Darboux para a Derivada]`
(**Teorema de Darboux:**) Suponha que $g$ seja derivável no intervalo fechado $[a, b]$, com **$g'(a) < 0$ e $g'(b) > 0$**. Prove (mesmo sem supor que $g'$ seja contínua!) que existe pelo menos um $c \in \,]a, b[$ tal que **$g'(c) = 0$**.
- **Dica (Sugestão do Guidorizzi):** Como $g$ é derivável em $[a, b]$, $g$ é contínua em $[a, b]$ e, pelo Teorema de Weierstrass, assume valor mínimo global num ponto $c \in [a, b]$. Mostre que $g'(a) < 0 \implies c \neq a$ e $g'(b) > 0 \implies c \neq b$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. Como $g$ é derivável em $[a, b]$, $g$ é contínua em $[a, b]$ (Teorema da Seção 7.6). Pelo **Teorema de Weierstrass**, existe $c \in [a, b]$ tal que $g(c) \le g(x)$ para todo $x \in [a, b]$ ($c$ é ponto de mínimo de $g$ em $[a, b]$).
2. Provemos que $c \neq a$: como $g'(a) = \lim_{x \to a^+} \frac{g(x) - g(a)}{x - a} < 0$, pelo Teorema da Conservação do Sinal existe $\delta_1 > 0$ tal que para $a < x < a + \delta_1$ tem-se $\frac{g(x) - g(a)}{x - a} < 0 \implies g(x) < g(a)$. Logo, $g(a)$ não é o valor mínimo de $g$ em $[a, b]$, ou seja, **$c \neq a$**.
3. Provemos que $c \neq b$: como $g'(b) = \lim_{x \to b^-} \frac{g(x) - g(b)}{x - b} > 0$, pela Conservação do Sinal existe $\delta_2 > 0$ tal que para $b - \delta_2 < x < b$ (onde $x - b < 0$) tem-se $\frac{g(x) - g(b)}{x - b} > 0 \implies g(x) - g(b) < 0 \implies g(x) < g(b)$. Logo, $g(b)$ também não é o valor mínimo, ou seja, **$c \neq b$**.
4. Portanto, $c$ pertence ao intervalo aberto $]a, b[$ ($c$ é ponto interior!). Pelo Teorema 1 da Seção 9.7 (Condição Necessária de Fermat), como $c \in \,]a, b[$ é ponto de mínimo local de $g$, segue obrigatoriamente **$g'(c) = 0$**! $\blacksquare$
</details>

---

<a id="cap-10-11"></a>
## Bloco 9 — Primitivas, Integral de Riemann, 1º e 2º TFC e Áreas (Capítulos 10 e 11)

### Exercício B9.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 11.6 e Seção 11.7]`
(a) Calcule a área da região plana limitada pelas curvas $y = x^2 - 2x$ e $y = 4 - x^2$.  
(b) Seja $f: [-a, a] \to \mathbb{R}$ contínua. Prove, usando o Teorema de Mudança de Variável na Integral (Seção 11.7), que se $f$ é **ímpar** ($f(-x) = -f(x)$), então $\int_{-a}^{a} f(x)\,dx = 0$; e use isso para calcular num segundo $\displaystyle \int_{-\pi/2}^{\pi/2} \left(x^3 \cos x + \frac{\operatorname{sen}^5 x}{1 + x^4} + \cos x\right)dx$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Achamos primeiro as abscissas de interseção igualando as ordenadas:
   $$x^2 - 2x = 4 - x^2 \iff 2x^2 - 2x - 4 = 0 \iff x^2 - x - 2 = 0 \iff (x + 1)(x - 2) = 0 \implies x = -1 \text{ ou } x = 2.$$
   Para $x \in [-1, 2]$, temos $4 - x^2 \ge x^2 - 2x$. Portanto:
   $$\text{Área} = \int_{-1}^{2} \big[(4 - x^2) - (x^2 - 2x)\big]\,dx = \int_{-1}^{2} (-2x^2 + 2x + 4)\,dx = \left[-\frac{2x^3}{3} + x^2 + 4x\right]_{-1}^{2} = \left(-\frac{16}{3} + 4 + 8\right) - \left(\frac{2}{3} + 1 - 4\right) = \mathbf{9}.$$
2. **Item (b):** Pela aditividade da integral, $\int_{-a}^{a} f(x)\,dx = \int_{-a}^{0} f(x)\,dx + \int_{0}^{a} f(x)\,dx$. Na primeira integral, fazemos a substituição $x = -u \implies dx = -du$ (para $x = -a \implies u = a$; para $x = 0 \implies u = 0$):
   $$\int_{-a}^{0} f(x)\,dx = \int_{a}^{0} f(-u)(-du) = \int_{0}^{a} f(-u)\,du = -\int_{0}^{a} f(u)\,du \implies \int_{-a}^{a} f(x)\,dx = 0.$$
   Aplicando à integral dada em $[-\pi/2, \pi/2]$: as funções $g_1(x) = x^3 \cos x$ e $g_2(x) = \frac{\operatorname{sen}^5 x}{1 + x^4}$ são **ímpares** (logo suas integrais em $[-\pi/2, \pi/2]$ valem $0$), enquanto $\cos x$ é **par**:
   $$\int_{-\pi/2}^{\pi/2} \left(x^3 \cos x + \frac{\operatorname{sen}^5 x}{1 + x^4} + \cos x\right)dx = 0 + 0 + 2\int_{0}^{\pi/2} \cos x\,dx = 2\big[\operatorname{sen} x\big]_{0}^{\pi/2} = \mathbf{2}. \quad \blacksquare$$
</details>

---

### Exercício B9.2 🟡 `📙 [Mudança de Referência — Apostol, Cálculo I, Cap. 5, Seção 5.1 (e Guidorizzi Vol. 2, Cap. 2)]`
Seja $F(x) = \displaystyle \int_{\operatorname{sen} x}^{x^2} e^{-t^2}\,dt$. Calcule $F'(x)$ para todo $x \in \mathbb{R}$, e calcule o limite:
$$\lim_{x \to 0} \frac{\displaystyle \int_{0}^{x^2} \operatorname{sen}(\sqrt{t})\,dt}{x^3} \quad (x > 0).$$

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Derivada de $F(x)$:** Pelo Teorema da Derivada da Integral (Apostol, Seção 5.1) combinado com a Regra da Cadeia:
   $$F'(x) = \frac{d}{dx}\left[\int_{\operatorname{sen} x}^{x^2} e^{-t^2}\,dt\right] = e^{-(x^2)^2}\cdot (x^2)' - e^{-(\operatorname{sen} x)^2}\cdot (\operatorname{sen} x)' = \mathbf{2x e^{-x^4} - (\cos x) e^{-\operatorname{sen}^2 x}}.$$
2. **Cálculo do limite:** Quando $x \to 0^+$, tanto o numerador $\int_0^{x^2} \operatorname{sen}(\sqrt{t})\,dt$ quanto o denominador $x^3$ tendem a $0$ (indeterminação $\frac{0}{0}$). Aplicando a Regra de L'Hospital e derivando o numerador pelo TFC:
   $$\lim_{x \to 0^+} \frac{\int_{0}^{x^2} \operatorname{sen}(\sqrt{t})\,dt}{x^3} \stackrel{\text{L'H}}{=} \lim_{x \to 0^+} \frac{\operatorname{sen}\left(\sqrt{x^2}\right) \cdot 2x}{3x^2} = \lim_{x \to 0^+} \frac{2}{3} \cdot \frac{\operatorname{sen} x}{x} = \mathbf{\frac{2}{3}}. \quad \blacksquare$$
</details>

---

<a id="cap-12"></a>
## Bloco 10 — Técnicas de Primitivação (Capítulo 12)

### Exercício B10.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seções 12.3, 12.5 e 12.9]`
Calcule as seguintes integrais:
(a) $\displaystyle \int x^2 \operatorname{arctg} x\,dx$; $\qquad$ (b) $\displaystyle \int \frac{\sqrt{4 - x^2}}{x^2}\,dx$ ($0 < x < 2$); $\qquad$ (c) (**Integrais de Wallis — Ex. da Seção 12.9:**) Deduzir que para todo natural $n \ge 2$, $I_n = \int_{0}^{\pi/2} \operatorname{sen}^n x\,dx$ satisfaz $I_n = \frac{n-1}{n}I_{n-2}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Integração por Partes (Seção 12.3):** Escolhendo $u = \operatorname{arctg} x \implies du = \frac{1}{1+x^2}\,dx$ e $dv = x^2\,dx \implies v = \frac{x^3}{3}$:
   $$\int x^2 \operatorname{arctg} x\,dx = \frac{x^3}{3}\operatorname{arctg} x - \frac{1}{3}\int \frac{x^3}{x^2 + 1}\,dx.$$
   Efetuando a divisão de polinômios $\frac{x^3}{x^2 + 1} = \frac{x(x^2 + 1) - x}{x^2 + 1} = x - \frac{x}{x^2 + 1}$:
   $$\int x^2 \operatorname{arctg} x\,dx = \frac{x^3}{3}\operatorname{arctg} x - \frac{1}{3}\int \left(x - \frac{x}{x^2 + 1}\right)dx = \mathbf{\frac{x^3}{3}\operatorname{arctg} x - \frac{x^2}{6} + \frac{1}{6}\ln(x^2 + 1) + k}.$$
2. **Item (b) — Substituição Trigonométrica (Seção 12.5):** Fazendo $x = 2\operatorname{sen}\theta$ ($\theta \in \,]0, \pi/2[$), temos $dx = 2\cos\theta\,d\theta$ e $\sqrt{4 - x^2} = 2\cos\theta$:
   $$\int \frac{\sqrt{4 - x^2}}{x^2}\,dx = \int \frac{(2\cos\theta)(2\cos\theta\,d\theta)}{4\operatorname{sen}^2\theta} = \int \operatorname{cotg}^2\theta\,d\theta = \int (\operatorname{cossec}^2\theta - 1)\,d\theta = -\operatorname{cotg}\theta - \theta + k.$$
   Como $\operatorname{sen}\theta = \frac{x}{2}$, no triângulo retângulo de hipotenusa $2$ e cateto oposto $x$, o cateto adjacente é $\sqrt{4 - x^2}$, logo $\operatorname{cotg}\theta = \frac{\sqrt{4 - x^2}}{x}$ e $\theta = \operatorname{arcsen}\left(\frac{x}{2}\right)$:
   $$\int \frac{\sqrt{4 - x^2}}{x^2}\,dx = \mathbf{-\frac{\sqrt{4 - x^2}}{x} - \operatorname{arcsen}\left(\frac{x}{2}\right) + k}.$$
3. **Item (c) — Fórmula de Wallis (Seção 12.9):** Aplicando a fórmula de recorrência da Seção 12.9 no intervalo $[0, \pi/2]$:
   $$I_n = \int_{0}^{\pi/2} \operatorname{sen}^n x\,dx = \underbrace{\left[-\frac{1}{n}\operatorname{sen}^{n-1} x \cos x\right]_{0}^{\pi/2}}_{0 - 0 = 0} + \frac{n - 1}{n}\int_{0}^{\pi/2} \operatorname{sen}^{n-2} x\,dx = \mathbf{\frac{n - 1}{n}I_{n-2}}. \quad \blacksquare$$
</details>

---

<a id="cap-13"></a>
## Bloco 11 — Volumes, Comprimento de Arco, Polares e Pappus (Capítulo 13)

### Exercício B11.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seções 13.1, 13.2 e 13.9, Ex. 5]`
Considere o disco circular $A = \{(x, y) \in \mathbb{R}^2 \mid x^2 + (y - b)^2 \le a^2\}$, com $0 < a < b$. Calcule o volume do **Toro (pneu / rosquinha)** obtido pela rotação de $A$ em torno do eixo $x$, tanto pela integral direta quanto pelo **Teorema de Pappus**!

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Método 1 (Integral Direta por Anéis / Substituição Trigonométrica — Seção 13.1):**  
   Isolando $y$ na equação $(y - b)^2 \le a^2 - x^2$ para $x \in [-a, a]$, o bordo superior é $f(x) = b + \sqrt{a^2 - x^2}$ e o bordo inferior é $g(x) = b - \sqrt{a^2 - x^2}$. Logo:
   $$[f(x)]^2 - [g(x)]^2 = \left(b + \sqrt{a^2 - x^2}\right)^2 - \left(b - \sqrt{a^2 - x^2}\right)^2 = 4b\sqrt{a^2 - x^2}.$$
   Integrando de $-a$ a $a$:
   $$V_x = \pi \int_{-a}^{a} 4b\sqrt{a^2 - x^2}\,dx = 4\pi b \underbrace{\int_{-a}^{a} \sqrt{a^2 - x^2}\,dx}_{\text{área do semicírculo } = \frac{\pi a^2}{2}} = 4\pi b \left(\frac{\pi a^2}{2}\right) = \mathbf{2\pi^2 a^2 b}.$$
2. **Método 2 (Em 1 linha pelo Teorema de Pappus — Seção 13.9):**  
   O disco $A$ tem área $\text{Área}(A) = \pi a^2$ e seu centro de massa (por simetria) é o centro do círculo $(x_c, y_c) = (0, b)$. Na rotação em torno do eixo $x$, o centro de massa descreve uma circunferência de raio $b$ e comprimento $2\pi b$. Pelo Teorema de Pappus:
   $$V_x = (2\pi y_c) \cdot \text{Área}(A) = (2\pi b)(\pi a^2) = \mathbf{2\pi^2 a^2 b}. \quad \blacksquare$$
</details>

---

<a id="cap-14"></a>
## Bloco 12 — Equações Diferenciais de 1ª Ordem (Capítulo 14)

### Exercício B12.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seções 14.3–14.6]`
(a) Determine **todas** as soluções (constantes e não constantes) da EDO de variáveis separáveis $\dfrac{dx}{dt} = x^2 - 1$.  
(b) Resolva o problema de valor inicial (PVI) linear de 1ª ordem:
$$\frac{dy}{dx} + (\operatorname{tg} x)y = \cos^2 x, \qquad y(0) = 2, \quad x \in \left]-\frac{\pi}{2}, \frac{\pi}{2}\right[.$$

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — EDO Separável (Seções 14.3–14.5):**
   - **Soluções constantes ($h(x) = x^2 - 1 = 0$):** As funções constantes **$x(t) = 1$** ($\forall t \in \mathbb{R}$) e **$x(t) = -1$** ($\forall t \in \mathbb{R}$) são soluções.
   - **Soluções não constantes ($x^2 - 1 \neq 0$):** Separando as variáveis e usando frações parciais $\frac{1}{x^2 - 1} = \frac{1}{2}\left(\frac{1}{x - 1} - \frac{1}{x + 1}\right)$:
     $$\int \frac{1}{x^2 - 1}\,dx = \int 1\,dt \implies \frac{1}{2}\ln\left|\frac{x - 1}{x + 1}\right| = t + c \implies \left|\frac{x - 1}{x + 1}\right| = e^{2c} e^{2t} \implies \frac{x - 1}{x + 1} = k e^{2t} \quad (k \in \mathbb{R}^*).$$
     Isolando $x(t)$: $x - 1 = k e^{2t}(x + 1) \implies x(1 - k e^{2t}) = 1 + k e^{2t} \implies \mathbf{x(t) = \frac{1 + k e^{2t}}{1 - k e^{2t}}}$ (e note que tomando $k = 0$ recuperamos a solução constante $x(t) = 1$, enquanto $x(t) = -1$ fica destacada à parte!).
2. **Item (b) — EDO Linear via Fator Integrante (Seção 14.6):**  
   Para $x \in \,]-\frac{\pi}{2}, \frac{\pi}{2}[$, temos $\cos x > 0$ e $a(x) = \operatorname{tg} x \implies A(x) = \int \operatorname{tg} x\,dx = -\ln(\cos x) = \ln(\sec x)$.  
   Logo, o fator integrante é $\mu(x) = e^{A(x)} = \sec x = \frac{1}{\cos x}$. Multiplicando a EDO por $\sec x$:
   $$(\sec x)y' + (\sec x \operatorname{tg} x)y = \sec x \cos^2 x \iff \frac{d}{dx}\Big[(\sec x)y\Big] = \cos x.$$
   Integrando em relação a $x$:
   $$(\sec x)y = \int \cos x\,dx = \operatorname{sen} x + k \implies y(x) = \operatorname{sen} x \cos x + k\cos x.$$
   Impondo $y(0) = 2 \implies 0 + k \cdot 1 = 2 \implies k = 2$. Portanto:
   $$\mathbf{y(x) = \operatorname{sen} x \cos x + 2\cos x}. \quad \blacksquare$$
</details>

---

<a id="cap-16"></a>
## Bloco 13 — Fórmula e Polinômios de Taylor (Capítulo 16)

### Exercício B13.1 🟡 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 16.2, Ex. 2 e Seção 16.3, Ex. 6 e 10]`
(a) Utilizando um polinômio de Taylor de ordem $2$ em volta de $x_0 = 8$, calcule um valor aproximado para **$\sqrt[3]{8{,}12}$**, avalie o erro cometido pelo Resto de Lagrange e diga se a aproximação é por falta ou por excesso.  
(b) Usando os polinômios de Maclaurin com resto de Peano $o(x^n)$, calcule o limite:
$$\lim_{x \to 0} \frac{\cos x - e^{-x^2/2}}{x^4}.$$

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Seja $f(x) = x^{1/3}$ em torno de $x_0 = 8$. Calculando as derivadas até a 3ª ordem:
   - $f(x) = x^{1/3} \implies f(8) = 2$;
   - $f'(x) = \frac{1}{3}x^{-2/3} \implies f'(8) = \frac{1}{3 \cdot 4} = \frac{1}{12}$;
   - $f''(x) = -\frac{2}{9}x^{-5/3} \implies f''(8) = -\frac{2}{9 \cdot 32} = -\frac{1}{144}$;
   - $f'''(x) = \frac{10}{27}x^{-8/3}$.
   O polinômio de Taylor de ordem $2$ em volta de $x_0 = 8$ é:
   $$P_2(x) = 2 + \frac{1}{12}(x - 8) - \frac{1}{288}(x - 8)^2.$$
   Para $x = 8{,}12$ ($x - 8 = 0{,}12$):
   $$\sqrt[3]{8{,}12} \approx P_2(8{,}12) = 2 + \frac{0{,}12}{12} - \frac{(0{,}12)^2}{288} = 2 + 0{,}01 - \frac{0{,}0144}{288} = 2 + 0{,}01 - 0{,}00005 = \mathbf{2{,}00995}.$$
   **Estimativa do Erro:** Pelo Teorema de Lagrange, existe $\bar{x} \in \,]8;\, 8{,}12[$ tal que:
   $$E_2(8{,}12) = \frac{f'''(\bar{x})}{3!}(0{,}12)^3 = \frac{10}{27 \cdot 6 \cdot \bar{x}^{8/3}}(0{,}12)^3 = \frac{5}{81 \cdot \bar{x}^{8/3}}(0{,}12)^3.$$
   Como $\bar{x} > 8 \implies \bar{x}^{8/3} > 8^{8/3} = 2^8 = 256$ e $E_2(8{,}12) > 0$, a aproximação é **por falta** e o erro satisfaz:
   $$0 < E_2(8{,}12) < \frac{5}{81 \cdot 256}(1{,}728 \times 10^{-3}) < \mathbf{5 \times 10^{-7}}.$$
2. **Item (b):** Pela expansão de Maclaurin de ordem $4$ em torno de $x_0 = 0$:
   $$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + o(x^4) = 1 - \frac{x^2}{2} + \frac{x^4}{24} + o(x^4)$$
   e substituindo $u = -\frac{x^2}{2}$ em $e^u = 1 + u + \frac{u^2}{2!} + o(u^2)$:
   $$e^{-x^2/2} = 1 - \frac{x^2}{2} + \frac{(-x^2/2)^2}{2} + o(x^4) = 1 - \frac{x^2}{2} + \frac{x^4}{8} + o(x^4).$$
   Subtraindo as duas expansões:
   $$\lim_{x \to 0} \frac{\cos x - e^{-x^2/2}}{x^4} = \lim_{x \to 0} \frac{\left(\frac{1}{24} - \frac{1}{8}\right)x^4 + o(x^4)}{x^4} = \frac{1}{24} - \frac{3}{24} = \mathbf{-\frac{1}{12}}. \quad \blacksquare$$
</details>

---

<a id="cap-17"></a>
## Bloco 14 — Arquimedes, Pascal e Fermat (Capítulo 17)

### Exercício B14.1 🔴 `📘 [Guidorizzi, Vol. 1, 5ª ed., Seção 17.3 — Desafio Final de Fermat]`
Utilizando a progressão geométrica ilimitada $1, E, E^2, E^3, \dots$ com **$E > 1$** (proposta por Guidorizzi ao final da Seção 17.3), mostre pelo método de Fermat que, para todo natural $k \ge 2$, a área da região ilimitada compreendida entre o gráfico de $y = \dfrac{1}{x^k}$, o eixo $Ox$ e à direita da reta $x = 1$ ($x \ge 1$) é dada exatamente por:
$$\text{Área} = \frac{1}{k - 1}.$$

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. Tomamos $E > 1$ e subdividimos a semirreta $[1, +\infty[$ nos subintervalos $[1, E], [E, E^2], [E^2, E^3], \dots, [E^{i-1}, E^i], \dots$
2. Como $f(x) = \frac{1}{x^k}$ é decrescente para $x \ge 1$, o retângulo circunscrito (por excesso) sobre o $i$-ésimo subintervalo $[E^{i-1}, E^i]$ tem base $E^i - E^{i-1} = E^{i-1}(E - 1)$ e altura $f(E^{i-1}) = \frac{1}{(E^{i-1})^k} = (E^{-k})^{i-1}$. Logo, sua área é:
   $$\text{área}(R_i) = (E - 1) \cdot \left(\frac{1}{E^{k-1}}\right)^{i-1}, \qquad i = 1, 2, 3, \dots$$
3. Como $E > 1$ e $k \ge 2 \implies k - 1 \ge 1$, a razão da progressão geométrica é $q = \frac{1}{E^{k-1}} \in \,]0, 1[$. Somando a PG infinita:
   $$\sum_{i=1}^{\infty} \text{área}(R_i) = \frac{E - 1}{1 - \dfrac{1}{E^{k-1}}} = \frac{E^{k-1}(E - 1)}{E^{k-1} - 1} = \frac{E^{k-1}}{E^{k-2} + E^{k-3} + \dots + E + 1}.$$
4. Fazendo $E \to 1^+$ (para que a amplitude de cada subintervalo tenda a zero), o numerador tende a $1^{k-1} = 1$ e o denominador possui $(k - 1)$ parcelas que tendem a $1$, resultando em:
   $$\lim_{E \to 1^+} \frac{E^{k-1}}{E^{k-2} + \dots + E + 1} = \mathbf{\frac{1}{k - 1}}. \quad \blacksquare$$
</details>
