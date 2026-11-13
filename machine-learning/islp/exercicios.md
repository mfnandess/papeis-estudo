# Caderno de Exercícios e Demonstrações Resolvidas de Machine Learning
## Material Prático Baseado em *An Introduction to Statistical Learning — with Applications in Python* (James, Witten, Hastie, Tibshirani & Taylor, 2023), com Complementos de *Machine Learning with PyTorch and Scikit-Learn* (Raschka, Liu & Mirjalili, 2022)

---

> **Sobre este Caderno**  
> Este documento reúne **45 problemas fundamentais e demonstrações algébricas selecionadas**, organizados na sequência dos **13 capítulos de *An Introduction to Statistical Learning — with Applications in Python (ISLP)***, acrescidos de exercícios teóricos e de engenharia prática de ***Machine Learning with PyTorch and Scikit-Learn*, de Sebastian Raschka, Yuxi Liu & Vahid Mirjalili** (sempre identificados por `[Complemento — Raschka et al., ML with PyTorch and Scikit-Learn, Cap. X]`). Cada problema apresenta uma dica estratégica seguida da resolução passo a passo.

---

## Sumário por Blocos Temáticos
1. [Bloco 1 — Aprendizado Estatístico, Decomposição Viés-Variância, KNN e Pré-Processamento (Cap. 2 + Raschka Cap. 4)](#bloco-1)
2. [Bloco 2 — Regressão Linear Simples e Múltipla, Teoria OLS, $R^2$ e Interações (Cap. 3)](#bloco-2)
3. [Bloco 3 — Classificação: Logística, LDA, QDA, Naive Bayes, Softmax e Perceptron/Adaline (Cap. 4 + Raschka Cap. 2)](#bloco-3)
4. [Bloco 4 — Reamostragem: Validação Cruzada $k$-Fold, LOOCV, Atalho $h_i$ e Bootstrap (Cap. 5)](#bloco-4)
5. [Bloco 5 — Seleção de Variáveis, Regressão Ridge, Lasso, *Soft-Thresholding* e Priori Bayesiano (Cap. 6)](#bloco-5)
6. [Bloco 6 — Além da Linearidade: Splines Cúbicas, *Smoothing Splines*, Base Polinomial e GAMs (Cap. 7)](#bloco-6)
7. [Bloco 7 — Árvores de Decisão, Impureza de Gini/Entropia, Bagging, Random Forests e Boosting (Cap. 8 + Raschka Cap. 7)](#bloco-7)
8. [Bloco 8 — Máquinas de Vetores de Suporte (SVM), Margem Máxima, Kernels e *Hinge Loss* (Cap. 9)](#bloco-8)
9. [Bloco 9 — Deep Learning: MLPs, CNNs, Otimização não Convexa, Self-Attention, GANs e Q-Learning (Cap. 10 + Raschka Cap. 11–19)](#bloco-9)
10. [Bloco 10 — Análise de Sobrevivência e Dados Censurados: Kaplan-Meier, Log-Rank e Cox (Cap. 11)](#bloco-10)
11. [Bloco 11 — Aprendizado Não Supervisionado: PCA, Cargas via Regressão, *K-Means* e Hierárquico (Cap. 12)](#bloco-11)
12. [Bloco 12 — Testes Múltiplos de Hipóteses: FWER, Bonferroni, Holm e Benjamini-Hochberg / FDR (Cap. 13)](#bloco-12)

---

<a id="bloco-1"></a>
## Bloco 1 — Aprendizado Estatístico, Decomposição Viés-Variância, KNN e Pré-Processamento (Capítulo 2 + Raschka Cap. 4)

### Exercício B1.1 *[ISLP, Seção 2.4, Ex. 3 e Equação 2.7]*
Seja $Y = f(X) + \varepsilon$ o modelo gerador verdadeiro, em que $\mathbb{E}[\varepsilon] = 0$, $\operatorname{Var}(\varepsilon) = \sigma_\varepsilon^2$ e $\varepsilon$ é independente de $X$ e da amostra de treinamento $\mathcal{T}$.
(a) Prove algebricamente que, para um ponto de teste fixo $x_0$, o Erro Quadrático Médio esperado sobre todas as amostras de treinamento $\mathcal{T}$ e sobre o ruído de teste $\varepsilon$ decompõe-se em:
$$\mathbb{E}\!\left[\big(y_0 - \hat{f}(x_0)\big)^2\right] = \operatorname{Var}\!\big(\hat{f}(x_0)\big) + \left[\operatorname{Bias}\!\big(\hat{f}(x_0)\big)\right]^2 + \operatorname{Var}(\varepsilon).$$
(b) Explique por que o **MSE de treino** decresce monotonicamente com a flexibilidade, enquanto o **MSE de teste** apresenta formato em U.
- **Dica:** Em (a), some e subtraia $f(x_0)$ e $\mu = \mathbb{E}[\hat{f}(x_0)]$ dentro dos parênteses, expanda o quadrado e use a independência entre $\varepsilon$ e $\hat{f}(x_0)$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Prova da Decomposição Viés-Variância:**  
   Como $y_0 = f(x_0) + \varepsilon$, escrevemos:
   $$y_0 - \hat{f}(x_0) = \big(f(x_0) - \hat{f}(x_0)\big) + \varepsilon.$$
   Elevando ao quadrado e tomando a esperança $\mathbb{E}[\cdot]$ sobre o conjunto de treino $\mathcal{T}$ e sobre $\varepsilon$:
   $$\mathbb{E}\!\left[\big(y_0 - \hat{f}(x_0)\big)^2\right] = \mathbb{E}\!\left[\big(f(x_0) - \hat{f}(x_0)\big)^2\right] + 2\,\mathbb{E}\!\left[\big(f(x_0) - \hat{f}(x_0)\big)\varepsilon\right] + \mathbb{E}[\varepsilon^2].$$
   Como $\varepsilon$ é independente de $\hat{f}(x_0)$ e tem média zero ($\mathbb{E}[\varepsilon] = 0$):
   $$\mathbb{E}\!\left[\big(f(x_0) - \hat{f}(x_0)\big)\varepsilon\right] = \mathbb{E}\!\left[f(x_0) - \hat{f}(x_0)\right]\mathbb{E}[\varepsilon] = 0, \qquad \mathbb{E}[\varepsilon^2] = \operatorname{Var}(\varepsilon) + (\mathbb{E}[\varepsilon])^2 = \operatorname{Var}(\varepsilon).$$
   Agora, seja $\mu = \mathbb{E}\!\left[\hat{f}(x_0)\right]$. Somando e subtraindo $\mu$ no primeiro termo:
   $$f(x_0) - \hat{f}(x_0) = \big(f(x_0) - \mu\big) - \big(\hat{f}(x_0) - \mu\big).$$
   Como $f(x_0) - \mu$ é uma constante determinística e $\mathbb{E}\!\left[\hat{f}(x_0) - \mu\right] = 0$, o termo cruzado se anula:
   $$\mathbb{E}\!\left[\big(f(x_0) - \hat{f}(x_0)\big)^2\right] = \big(f(x_0) - \mu\big)^2 + \mathbb{E}\!\left[\big(\hat{f}(x_0) - \mu\big)^2\right] = \left[\operatorname{Bias}\!\big(\hat{f}(x_0)\big)\right]^2 + \operatorname{Var}\!\big(\hat{f}(x_0)\big).$$
   Somando $\operatorname{Var}(\varepsilon)$, concluímos a identidade fundamental:
   $$\mathbf{\mathbb{E}\!\left[\big(y_0 - \hat{f}(x_0)\big)^2\right] = \operatorname{Var}\!\big(\hat{f}(x_0)\big) + \left[\operatorname{Bias}\!\big(\hat{f}(x_0)\big)\right]^2 + \operatorname{Var}(\varepsilon)}. \quad \blacksquare$$

2. **Item (b) — Comportamento das 5 Curvas (Ex. 2.4.3):**
   - **Erro irredutível $\operatorname{Var}(\varepsilon)$:** linha horizontal constante (independe do modelo $\hat{f}$), situando-se como cota inferior para o MSE esperado de teste.
   - **Viés ao quadrado $[\operatorname{Bias}(\hat{f}(x_0))]^2$:** decresce monotonicamente à medida que a flexibilidade aumenta, pois famílias funcionais mais ricas aproximam melhor a verdadeira $f$.
   - **Variância $\operatorname{Var}(\hat{f}(x_0))$:** cresce monotonicamente com a flexibilidade, pois modelos muito flexíveis ajustam flutuações aleatórias específicas de cada amostra $\mathcal{T}$.
   - **MSE de teste:** sendo a soma de uma função decrescente (viés$^2$), uma crescente (variância) e uma constante ($\sigma_\varepsilon^2$), decresce inicialmente até atingir um mínimo no ponto ótimo de complexidade e volta a subir quando a variância explode (*overfitting*), formando um **U**.
   - **MSE de treino:** decresce monotonicamente com a flexibilidade porque toda liberdade adicional permite que $\hat{f}$ se aproxime ainda mais dos pontos observados $(x_i, y_i)$ usados na própria otimização. $\blacksquare$
</details>

---

### Exercício B1.2 *[ISLP, Seção 2.4, Ex. 1 e Ex. 2]*
Para cada um dos quatro cenários abaixo, indique se um método de aprendizado estatístico **flexível** ou **inflexível** deve apresentar melhor desempenho preditivo, justificando em termos de viés e variância:
(a) O tamanho amostral $n$ é extremamente grande e o número de preditores $p$ é pequeno.  
(b) O número de preditores $p$ é extremamente grande e o número de observações $n$ é pequeno ($p \gg n$).  
(c) A relação verdadeira entre os preditores e a resposta é altamente não linear.  
(d) A variância dos termos de erro, $\sigma_\varepsilon^2 = \operatorname{Var}(\varepsilon)$, é extremamente alta.
- **Dica:** Avalie em cada caso se o risco dominante é o *underfitting* (alto viés) ou o *overfitting* (alta variância).

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **(a) $n$ muito grande e $p$ pequeno $\implies$ Método Flexível é melhor:**  
   Com uma amostra massiva em baixa dimensão, a variância do estimador é naturalmente reduzida pelo grande $n$, permitindo reduzir o viés e capturar nuances sutis de $f$ sem sobreajustar.
2. **(b) $p$ muito grande e $n$ pequeno ($p \gg n$) $\implies$ Método Inflexível é melhor:**  
   Em alta dimensão com poucas amostras, um método flexível tem graus de liberdade excessivos e memoriza o ruído amostral (variância altíssima). Modelos restritos (como regressão linear regularizada) controlam a variância.
3. **(c) Relação verdadeira altamente não linear $\implies$ Método Flexível é melhor:**  
   Modelos rígidos (como regressão linear simples) sofrerão de um viés estrutural enorme (*underfitting*), enquanto modelos flexíveis (splines, árvores com boosting, redes neurais) possuem capacidade de representação para reduzir o viés.
4. **(d) $\sigma_\varepsilon^2 = \operatorname{Var}(\varepsilon)$ extremamente alta $\implies$ Método Inflexível é melhor:**  
   Quando os dados estão contaminados por ruído muito intenso, um método flexível perseguirá as oscilações espúrias de $\varepsilon_i$, inflando drasticamente $\operatorname{Var}(\hat{f}(x_0))$. Um modelo inflexível suaviza o ruído. $\blacksquare$
</details>

---

### Exercício B1.3 *[ISLP, Seção 2.4, Ex. 7]*
A tabela abaixo apresenta um conjunto de treinamento com $n = 6$ observações em $p = 3$ variáveis preditoras ($X_1, X_2, X_3$) e uma variável resposta qualitativa $Y \in \{\text{Vermelho}, \text{Verde}\}$:

| Obs. $i$ | $X_1$ | $X_2$ | $X_3$ | $Y$ |
| :---: | :---: | :---: | :---: | :---: |
| 1 | $0$ | $3$ | $0$ | Vermelho |
| 2 | $2$ | $0$ | $0$ | Vermelho |
| 3 | $0$ | $1$ | $3$ | Vermelho |
| 4 | $0$ | $1$ | $2$ | Verde |
| 5 | $-1$ | $0$ | $1$ | Verde |
| 6 | $1$ | $1$ | $1$ | Vermelho |

Deseja-se classificar o ponto de teste $x_0 = (0, 0, 0)^T$ usando o algoritmo *$K$-Nearest Neighbors* (KNN).
(a) Calcule a distância euclidiana entre cada observação $i \in \{1,\dots,6\}$ e o ponto de teste $x_0 = (0,0,0)^T$.  
(b) Qual é a predição do KNN para $K = 1$? E para $K = 3$? Por quê?  
(c) Se a fronteira de decisão de Bayes neste problema for altamente não linear, esperamos que o melhor valor de $K$ seja grande ou pequeno?
- **Dica:** A distância euclidiana até a origem é simplesmente a norma $\|x_i\|_2 = \sqrt{x_{i1}^2 + x_{i2}^2 + x_{i3}^2}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Distâncias Euclidianas $d(x_i, x_0) = \sqrt{X_{i1}^2 + X_{i2}^2 + X_{i3}^2}$:**
   - Obs. 1 $(0,3,0)$: $d_1 = \sqrt{0^2 + 3^2 + 0^2} = \sqrt{9} = \mathbf{3{,}00}$ (Vermelho)
   - Obs. 2 $(2,0,0)$: $d_2 = \sqrt{2^2 + 0^2 + 0^2} = \sqrt{4} = \mathbf{2{,}00}$ (Vermelho)
   - Obs. 3 $(0,1,3)$: $d_3 = \sqrt{0^2 + 1^2 + 3^2} = \sqrt{10} \approx \mathbf{3{,}16}$ (Vermelho)
   - Obs. 4 $(0,1,2)$: $d_4 = \sqrt{0^2 + 1^2 + 2^2} = \sqrt{5} \approx \mathbf{2{,}24}$ (Verde)
   - Obs. 5 $(-1,0,1)$: $d_5 = \sqrt{(-1)^2 + 0^2 + 1^2} = \sqrt{2} \approx \mathbf{1{,}41}$ (Verde)
   - Obs. 6 $(1,1,1)$: $d_6 = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3} \approx \mathbf{1{,}73}$ (Vermelho)

2. **Item (b) — Predições para $K=1$ e $K=3$:**
   - **Para $K = 1$:** O vizinho mais próximo de $(0,0,0)$ é a **Obs. 5** ($d_5 = \sqrt{2} \approx 1{,}41$), cuja classe é **Verde**. Assim, $\hat{P}(Y = \text{Verde} \mid X = x_0) = 1/1 = 100\% \implies \mathbf{\hat{Y}(x_0) = \text{Verde}}$.
   - **Para $K = 3$:** Os 3 vizinhos mais próximos são a **Obs. 5** ($d_5 = \sqrt{2}$, Verde), a **Obs. 6** ($d_6 = \sqrt{3}$, Vermelho) e a **Obs. 2** ($d_2 = 2$, Vermelho). Logo:
     $$\hat{P}(Y = \text{Vermelho} \mid X = x_0) = \frac{2}{3}, \qquad \hat{P}(Y = \text{Verde} \mid X = x_0) = \frac{1}{3} \implies \mathbf{\hat{Y}(x_0) = \text{Vermelho}}.$$

3. **Item (c) — Escolha ótima de $K$ sob fronteira de Bayes altamente não linear:**  
   Esperamos que o melhor valor de $K$ seja **pequeno**. No KNN, a flexibilidade é proporcional a $1/K$: valores pequenos de $K$ produzem fronteiras de decisão localmente adaptáveis e altamente não lineares (baixo viés), ao passo que um $K$ grande faz a média sobre grandes vizinhanças e achata a fronteira de decisão (alto viés). $\blacksquare$
</details>

---

### Exercício B1.4 *[Complemento — Raschka et al., ML with PyTorch and Scikit-Learn, Cap. 4 e Cap. 6]*
Considere um atributo contínuo $x = (10, 20, 30, 40, 500)^T$, onde $x_5 = 500$ é um *outlier* severo.
(a) Compare a transformação de **Normalização Min-Max** $x^{\text{norm}}_i = \frac{x_i - x_{\min}}{x_{\max} - x_{\min}}$ com a **Padronização (*Standardization*)** $x^{\text{std}}_i = \frac{x_i - \bar{x}}{s_x}$ neste vetor e explique o impacto sobre algoritmos baseados em distância ou gradiente.  
(b) Suponha que dividimos um conjunto de dados em treino ($\mathcal{T}$) e teste ($\mathcal{V}$). Demonstre por que calcular $\bar{x}$ e $s_x$ sobre $\mathcal{T} \cup \mathcal{V}$ antes da divisão constitui **vazamento de dados (*data leakage*)** e qual é a fórmula correta para padronizar um ponto de teste $x_{\text{test}}$.
- **Dica:** Em (a), verifique em qual intervalo ficam confinadas as 4 observações normais $(10, 20, 30, 40)$ após a compressão pelo *outlier* $500$ na escala Min-Max.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Min-Max vs. Padronização na presença de *Outliers*:**
   - **Normalização Min-Max:** Temos $x_{\min} = 10$ e $x_{\max} = 500$ (amplitude $490$). Logo:
     $$x^{\text{norm}} = \left(0,\; \frac{10}{490},\; \frac{20}{490},\; \frac{30}{490},\; 1\right)^T \approx \mathbf{(0{,}000,\; 0{,}020,\; 0{,}041,\; 0{,}061,\; 1{,}000)^T}.$$
     Note que $80\%$ dos dados legítimos foram esmagados no minúsculo subintervalo $[0;\; 0{,}061]$, destruindo a resolução das distâncias entre observações normais!
   - **Padronização (*Z-score*):** A média é $\bar{x} = \frac{10+20+30+40+500}{5} = 120$, e o desvio-padrão amostral é $s_x = \sqrt{\frac{1}{4}\sum_{i=1}^5 (x_i - 120)^2} = \sqrt{\frac{12100+10000+8100+6400+144400}{4}} = \sqrt{45250} \approx 212{,}72$. Assim:
     $$x^{\text{std}} \approx \mathbf{(-0{,}517,\; -0{,}470,\; -0{,}423,\; -0{,}376,\; +1{,}786)^T}.$$
     Além de centrar os dados em média zero (essencial para otimizadores como SGD/Adam evitarem atualizações em zigue-zague e para a PCA), a padronização preserva um espaçamento relativo quase dez vezes maior ($\Delta \approx 0{,}047$ por passo) e não força os valores a um intervalo fechado rígido.

2. **Item (b) — Prevenção de *Data Leakage* em Pipelines:**  
   Se $\bar{x}_{\text{global}}$ e $s_{\text{global}}$ forem calculados usando $\mathcal{T} \cup \mathcal{V}$, informações da distribuição futura (como a presença do *outlier* ou a média do conjunto de teste $\mathcal{V}$) alteram as coordenadas de treino, violando a independência entre treino e avaliação e produzindo estimativas de erro artificialmente otimistas.  
   A regra estrita (implementada via `Pipeline` no Scikit-Learn) exige estimar $\hat{\mu}_{\mathcal{T}}$ e $\hat{\sigma}_{\mathcal{T}}$ **exclusivamente no conjunto de treino** $\mathcal{T}$ e aplicar a mesma transformação afim ao teste:
   $$\mathbf{x_{\text{train}}^{\text{std}} = \frac{x_{\text{train}} - \hat{\mu}_{\mathcal{T}}}{\hat{\sigma}_{\mathcal{T}}}, \qquad x_{\text{test}}^{\text{std}} = \frac{x_{\text{test}} - \hat{\mu}_{\mathcal{T}}}{\hat{\sigma}_{\mathcal{T}}}}. \quad \blacksquare$$
</details>

---

<a id="bloco-2"></a>
## Bloco 2 — Regressão Linear Simples e Múltipla, Teoria OLS, $R^2$ e Interações (Capítulo 3)

### Exercício B2.1 *[ISLP, Seção 3.7, Ex. 5 e Ex. 6]*
Considere a regressão linear simples de $Y$ sobre $X$ por Mínimos Quadrados Ordinários (OLS).
(a) Partindo da minimização de $\operatorname{RSS}(\beta_0, \beta_1) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$, derive as equações normais e prove que a reta de mínimos quadrados $y = \hat{\beta}_0 + \hat{\beta}_1 x$ **sempre passa pelo centro de gravidade amostral** $(\bar{x}, \bar{y})$ (Ex. 3.7.6).  
(b) Na regressão linear simples **sem intercepto**, $\hat{y}_i = x_i \hat{\beta}$, onde $\hat{\beta} = \frac{\sum_{i=1}^n x_i y_i}{\sum_{i'=1}^n x_{i'}^2}$, mostre que cada valor ajustado é uma combinação linear das respostas observadas, $\hat{y}_i = \sum_{i'=1}^n a_{i'} y_{i'}$, e explicite a expressão de $a_{i'}$ (Ex. 3.7.5).
- **Dica:** Em (a), iguale $\frac{\partial \operatorname{RSS}}{\partial \beta_0} = 0$ e $\frac{\partial \operatorname{RSS}}{\partial \beta_1} = 0$. Em (b), substitua $\hat{\beta}$ em $\hat{y}_i = x_i \hat{\beta}$ trocando o índice mudo do numerador para $i'$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Derivação de $\hat{\beta}_0, \hat{\beta}_1$ e passagem por $(\bar{x}, \bar{y})$:**  
   Derivando $\operatorname{RSS}(\beta_0, \beta_1) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$ em relação a $\beta_0$ e $\beta_1$:
   $$\frac{\partial \operatorname{RSS}}{\partial \beta_0} = -2 \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0 \implies \sum_{i=1}^n y_i - n\hat{\beta}_0 - \hat{\beta}_1 \sum_{i=1}^n x_i = 0.$$
   Dividindo por $n$ e lembrando que $\bar{x} = \frac{1}{n}\sum x_i$ e $\bar{y} = \frac{1}{n}\sum y_i$:
   $$\bar{y} - \hat{\beta}_0 - \hat{\beta}_1 \bar{x} = 0 \iff \mathbf{\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}}.$$
   Avaliando a reta ajustada $\hat{y}(x) = \hat{\beta}_0 + \hat{\beta}_1 x$ no ponto $x = \bar{x}$:
   $$\hat{y}(\bar{x}) = (\bar{y} - \hat{\beta}_1 \bar{x}) + \hat{\beta}_1 \bar{x} = \mathbf{\bar{y}},$$
   o que prova que $(\bar{x}, \bar{y})$ pertence sempre à reta de mínimos quadrados!  
   Substituindo $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$ na segunda condição de primeira ordem $\frac{\partial \operatorname{RSS}}{\partial \beta_1} = -2\sum_{i=1}^n x_i(y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0$:
   $$\sum_{i=1}^n x_i\big[(y_i - \bar{y}) - \hat{\beta}_1(x_i - \bar{x})\big] = 0.$$
   Como $\sum_{i=1}^n \bar{x}(y_i - \bar{y}) = 0$ e $\sum_{i=1}^n \bar{x}(x_i - \bar{x}) = 0$, podemos subtrair $\bar{x}$ do primeiro fator:
   $$\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) = \hat{\beta}_1 \sum_{i=1}^n (x_i - \bar{x})^2 \implies \mathbf{\hat{\beta}_1 = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}}.$$

2. **Item (b) — Combinação linear na regressão sem intercepto (Ex. 3.7.5):**  
   Trocando o índice mudo do numerador de $\hat{\beta}$ para $i'$:
   $$\hat{y}_i = x_i \hat{\beta} = x_i \left(\frac{\sum_{i'=1}^n x_{i'} y_{i'}}{\sum_{k=1}^n x_k^2}\right) = \sum_{i'=1}^n \underbrace{\left(\frac{x_i x_{i'}}{\sum_{k=1}^n x_k^2}\right)}_{a_{i'}} y_{i'} \implies \mathbf{a_{i'} = \frac{x_i x_{i'}}{\sum_{k=1}^n x_k^2}}. \quad \blacksquare$$
</details>

---

### Exercício B2.2 *[ISLP, Seção 3.7, Ex. 7]*
Prove que, na regressão linear simples com intercepto ($\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$), a estatística $R^2$ é exatamente igual ao quadrado do coeficiente de correlação amostral de Pearson entre $X$ e $Y$:
$$R^2 = \frac{\operatorname{TSS} - \operatorname{RSS}}{\operatorname{TSS}} = \big[\operatorname{Cor}(X, Y)\big]^2.$$
- **Dica:** Escreva $y_i - \bar{y} = (\hat{y}_i - \bar{y}) + (y_i - \hat{y}_i)$, mostre que o termo cruzado $\sum (\hat{y}_i - \bar{y})(y_i - \hat{y}_i) = 0$ pelas equações normais e substitua $\hat{y}_i - \bar{y} = \hat{\beta}_1(x_i - \bar{x})$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. Pela relação $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$, temos para cada observação $i$:
   $$\hat{y}_i - \bar{y} = (\hat{\beta}_0 + \hat{\beta}_1 x_i) - \bar{y} = \hat{\beta}_1(x_i - \bar{x}).$$
2. Decompondo o desvio total $y_i - \bar{y} = (\hat{y}_i - \bar{y}) + (y_i - \hat{y}_i)$ e elevando ao quadrado:
   $$\operatorname{TSS} = \sum_{i=1}^n (y_i - \bar{y})^2 = \sum_{i=1}^n (\hat{y}_i - \bar{y})^2 + 2\sum_{i=1}^n (\hat{y}_i - \bar{y})(y_i - \hat{y}_i) + \underbrace{\sum_{i=1}^n (y_i - \hat{y}_i)^2}_{\operatorname{RSS}}.$$
3. O termo cruzado é identicamente nulo pelas equações normais do OLS ($\sum e_i = 0$ e $\sum x_i e_i = 0$, onde $e_i = y_i - \hat{y}_i$):
   $$\sum_{i=1}^n (\hat{y}_i - \bar{y})e_i = \hat{\beta}_1 \sum_{i=1}^n (x_i - \bar{x})e_i = \hat{\beta}_1\left(\sum_{i=1}^n x_i e_i - \bar{x}\sum_{i=1}^n e_i\right) = 0.$$
4. Logo, $\operatorname{TSS} - \operatorname{RSS} = \sum_{i=1}^n (\hat{y}_i - \bar{y})^2 = \hat{\beta}_1^2 \sum_{i=1}^n (x_i - \bar{x})^2$. Substituindo a expressão de $\hat{\beta}_1$:
   $$\operatorname{TSS} - \operatorname{RSS} = \left[\frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}\right]^2 \sum_{i=1}^n (x_i - \bar{x})^2 = \frac{\left[\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right]^2}{\sum_{i=1}^n (x_i - \bar{x})^2}.$$
5. Dividindo por $\operatorname{TSS} = \sum_{i=1}^n (y_i - \bar{y})^2$:
   $$R^2 = \frac{\operatorname{TSS} - \operatorname{RSS}}{\operatorname{TSS}} = \frac{\left[\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right]^2}{\left[\sum_{i=1}^n (x_i - \bar{x})^2\right]\left[\sum_{i=1}^n (y_i - \bar{y})^2\right]} = \mathbf{\big[\operatorname{Cor}(X, Y)\big]^2}. \quad \blacksquare$$
</details>

---

### Exercício B2.3 *[ISLP, Seção 3.7, Ex. 3]*
Suponha que ajustamos um modelo de regressão linear múltipla para predizer o salário inicial após a formatura ($Y$, em milhares de dólares) a partir de $X_1 = \text{GPA}$ (média acadêmica), $X_2 = \text{IQ}$, $X_3 = \text{Level}$ ($1$ para Ensino Superior/*College* e $0$ para Ensino Médio/*High School*), $X_4 = X_1 \cdot X_2$ (interação GPA $\times$ IQ) e $X_5 = X_1 \cdot X_3$ (interação GPA $\times$ Level), obtendo os coeficientes estimados:
$$\hat{\beta}_0 = 50, \quad \hat{\beta}_1 = 20, \quad \hat{\beta}_2 = 0{,}07, \quad \hat{\beta}_3 = 35, \quad \hat{\beta}_4 = 0{,}01, \quad \hat{\beta}_5 = -10.$$
(a) Escreva as equações de regressão ajustadas separadamente para graduados do Ensino Médio ($X_3 = 0$) e do Ensino Superior ($X_3 = 1$), e determine para quais valores de GPA os graduados do Ensino Superior ganham mais, em média, para um mesmo IQ.  
(b) Qual é o salário predito para um graduado do Ensino Superior com $\text{IQ} = 110$ e $\text{GPA} = 4{,}0$?  
(c) Avalie a afirmação: *"Como o coeficiente da interação GPA $\times$ IQ é muito pequeno ($\hat{\beta}_4 = 0{,}01$), não há evidência de que esse efeito de interação exista."*
- **Dica:** Em (a), compare $\hat{Y}(X_3=1) - \hat{Y}(X_3=0)$ em função de $X_1 = \text{GPA}$. Em (c), distinga a magnitude numérica de $\hat{\beta}_4$ (que depende da escala de IQ $\approx 100$) de sua significância estatística ($p$-valor do teste $t$).

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Equações por nível educacional e comparação salarial:**  
   O modelo completo é:
   $$\hat{Y} = 50 + 20\,\text{GPA} + 0{,}07\,\text{IQ} + 35\,\text{Level} + 0{,}01(\text{GPA}\cdot\text{IQ}) - 10(\text{GPA}\cdot\text{Level}).$$
   - **Para Ensino Médio ($\text{Level} = 0$):**
     $$\hat{Y}_{\text{HS}} = 50 + 20\,\text{GPA} + 0{,}07\,\text{IQ} + 0{,}01(\text{GPA}\cdot\text{IQ}).$$
   - **Para Ensino Superior ($\text{Level} = 1$):**
     $$\hat{Y}_{\text{College}} = (50 + 35) + (20 - 10)\,\text{GPA} + 0{,}07\,\text{IQ} + 0{,}01(\text{GPA}\cdot\text{IQ}) = 85 + 10\,\text{GPA} + 0{,}07\,\text{IQ} + 0{,}01(\text{GPA}\cdot\text{IQ}).$$
   A diferença salarial esperada para IQ e GPA fixos é:
   $$\hat{Y}_{\text{College}} - \hat{Y}_{\text{HS}} = 35 - 10\,\text{GPA}.$$
   Portanto, graduados do Ensino Superior ganham mais se $35 - 10\,\text{GPA} > 0 \iff \text{GPA} < 3{,}5$, mas **para GPA suficientemente alto ($\text{GPA} > 3{,}5$), graduados do Ensino Médio ganham mais em média** segundo este modelo.

2. **Item (b) — Predição para $\text{Level}=1$, $\text{IQ}=110$, $\text{GPA}=4{,}0$:**
   $$\hat{Y} = 85 + 10(4{,}0) + 0{,}07(110) + 0{,}01(4{,}0 \times 110) = 85 + 40 + 7{,}7 + 4{,}4 = \mathbf{137{,}1 \text{ mil dólares } (\text{US\$ } 137.100)}.$$

3. **Item (c) — Magnitude do coeficiente vs. Significância estatística:**  
   A afirmação é **FALSA**. Primeiro, a magnitude numérica de um coeficiente de regressão depende da escala das variáveis preditoras (como $\text{GPA}\cdot\text{IQ} \approx 400$, um coeficiente $\hat{\beta}_4 = 0{,}01$ contribui com $4{,}4$ mil dólares para o salário). Segundo, para testar a existência do efeito de interação ($H_0: \beta_4 = 0$), é indispensável examinar o **erro-padrão $\operatorname{SE}(\hat{\beta}_4)$** e o **$p$-valor da estatística $t = \hat{\beta}_4 / \operatorname{SE}(\hat{\beta}_4)$**, e não apenas o valor absoluto de $\hat{\beta}_4$. $\blacksquare$
</details>

---

### Exercício B2.4 *[ISLP, Seção 3.7, Ex. 11d–e]*
Considere a regressão linear simples **sem intercepto** de $Y$ sobre $X$ ($Y_i = \beta X_i + \varepsilon_i$) e a regressão inversa de $X$ sobre $Y$ ($X_i = \gamma Y_i + \eta_i$). Sabendo que o erro-padrão de $\hat{\beta}$ é dado por:
$$\operatorname{SE}(\hat{\beta}) = \sqrt{\frac{\sum_{i=1}^n (y_i - x_i \hat{\beta})^2}{(n - 1)\sum_{i'=1}^n x_{i'}^2}},$$
prove algebricamente que a estatística $t = \hat{\beta} / \operatorname{SE}(\hat{\beta})$ para testar $H_0: \beta = 0$ é escrita como:
$$t = \frac{(\sqrt{n - 1})\sum_{i=1}^n x_i y_i}{\sqrt{\left(\sum_{i=1}^n x_i^2\right)\left(\sum_{i'=1}^n y_{i'}^2\right) - \left(\sum_{i'=1}^n x_{i'} y_{i'}\right)^2}},$$
e conclua que a estatística $t$ da regressão de $Y$ sobre $X$ é **identicamente igual** à estatística $t$ da regressão de $X$ sobre $Y$.
- **Dica:** Expanda $\sum_{i=1}^n (y_i - x_i \hat{\beta})^2$ substituindo $\hat{\beta} = \frac{\sum x_i y_i}{\sum x_i^2}$ e simplifique o denominador de $t = \hat{\beta} / \operatorname{SE}(\hat{\beta})$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. Sejam $S_{xx} = \sum_{i=1}^n x_i^2$, $S_{yy} = \sum_{i=1}^n y_i^2$ e $S_{xy} = \sum_{i=1}^n x_i y_i$. Então $\hat{\beta} = \frac{S_{xy}}{S_{xx}}$.
2. Calculemos a soma dos quadrados dos resíduos no numerador de $\operatorname{SE}(\hat{\beta})$:
   $$\sum_{i=1}^n (y_i - x_i \hat{\beta})^2 = \sum_{i=1}^n y_i^2 - 2\hat{\beta}\sum_{i=1}^n x_i y_i + \hat{\beta}^2 \sum_{i=1}^n x_i^2 = S_{yy} - 2\left(\frac{S_{xy}}{S_{xx}}\right)S_{xy} + \left(\frac{S_{xy}}{S_{xx}}\right)^2 S_{xx} = S_{yy} - \frac{S_{xy}^2}{S_{xx}} = \frac{S_{xx}S_{yy} - S_{xy}^2}{S_{xx}}.$$
3. Substituindo na fórmula de $\operatorname{SE}(\hat{\beta})$:
   $$\operatorname{SE}(\hat{\beta}) = \sqrt{\frac{S_{xx}S_{yy} - S_{xy}^2}{(n - 1)S_{xx}^2}} = \frac{\sqrt{S_{xx}S_{yy} - S_{xy}^2}}{S_{xx}\sqrt{n - 1}}.$$
4. Dividindo $\hat{\beta} = \frac{S_{xy}}{S_{xx}}$ por $\operatorname{SE}(\hat{\beta})$, o fator $S_{xx}$ se cancela:
   $$t = \frac{\hat{\beta}}{\operatorname{SE}(\hat{\beta})} = \frac{S_{xy} / S_{xx}}{\frac{\sqrt{S_{xx}S_{yy} - S_{xy}^2}}{S_{xx}\sqrt{n - 1}}} = \frac{\sqrt{n - 1}\,S_{xy}}{\sqrt{S_{xx}S_{yy} - S_{xy}^2}} = \mathbf{\frac{(\sqrt{n - 1})\sum_{i=1}^n x_i y_i}{\sqrt{\left(\sum_{i=1}^n x_i^2\right)\left(\sum_{i'=1}^n y_{i'}^2\right) - \left(\sum_{i'=1}^n x_{i'} y_{i'}\right)^2}}}.$$
5. Como essa expressão algébrica é **totalmente simétrica** sob a permutação $x_i \leftrightarrow y_i$, segue imediatamente que a estatística $t$ da regressão de $X$ sobre $Y$ é exatamente a mesma que a da regressão de $Y$ sobre $X$. $\blacksquare$
</details>

---

<a id="bloco-3"></a>
## Bloco 3 — Classificação: Logística, LDA, QDA, Naive Bayes, Softmax e Perceptron/Adaline (Capítulo 4 + Raschka Cap. 2)

### Exercício B3.1 *[ISLP, Seção 4.8, Ex. 1, Ex. 6 e Ex. 9]*
(a) Prove que a função logística $p(X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}}$ é algebricamente equivalente à representação *odds* (*chance*) $\frac{p(X)}{1 - p(X)} = e^{\beta_0 + \beta_1 X}$ e à forma *logit* $\ln\left(\frac{p(X)}{1 - p(X)}\right) = \beta_0 + \beta_1 X$ (Ex. 4.8.1).  
(b) Suponha que coletamos dados de estudantes de uma turma de estatística com $X_1 = \text{ horas de estudo semanais}$, $X_2 = \text{ GPA na graduação}$ e $Y = \text{ receber conceito A}$, ajustando uma regressão logística com $\hat{\beta}_0 = -6$, $\hat{\beta}_1 = 0{,}05$ e $\hat{\beta}_2 = 1$. Calcule a probabilidade estimada de um estudante que estuda $40\text{ h}$ e tem $\text{GPA} = 3{,}5$ obter conceito A, e determine quantas horas esse estudante precisa estudar para ter $50\%$ de probabilidade de obter conceito A (Ex. 4.8.6).
- **Dica:** Em (a), calcule $1 - p(X)$ colocando no mesmo denominador $1 + e^{\beta_0 + \beta_1 X}$. Em (b), lembre que $p(X) = 0{,}5 \iff \text{logit}(p(X)) = \ln(1) = 0$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Equivalência Logística $\iff$ Odds $\iff$ Logit:**  
   Partindo de $p(X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}}$, a probabilidade complementar é:
   $$1 - p(X) = 1 - \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}} = \frac{1 + e^{\beta_0 + \beta_1 X} - e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}} = \frac{1}{1 + e^{\beta_0 + \beta_1 X}}.$$
   Dividindo $p(X)$ por $1 - p(X)$, os denominadores $1 + e^{\beta_0 + \beta_1 X}$ cancelam-se:
   $$\frac{p(X)}{1 - p(X)} = \frac{\frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}}}{\frac{1}{1 + e^{\beta_0 + \beta_1 X}}} = \mathbf{e^{\beta_0 + \beta_1 X}} \iff \mathbf{\ln\!\left(\frac{p(X)}{1 - p(X)}\right) = \beta_0 + \beta_1 X}. \quad \blacksquare$$

2. **Item (b) — Probabilidade de conceito A e limiar de $50\%$ (Ex. 4.8.6):**  
   - Para $X_1 = 40$ e $X_2 = 3{,}5$, o preditor linear (*logit*) vale:
     $$\hat{\eta} = \hat{\beta}_0 + \hat{\beta}_1 X_1 + \hat{\beta}_2 X_2 = -6 + 0{,}05(40) + 1(3{,}5) = -6 + 2 + 3{,}5 = -0{,}5.$$
     Logo, a probabilidade estimada é:
     $$\hat{p}(X) = \frac{e^{-0{,}5}}{1 + e^{-0{,}5}} = \frac{1}{1 + e^{0{,}5}} \approx \frac{1}{1 + 1{,}6487} \approx \mathbf{0{,}3775 \;\; (37{,}75\%)}.$$
   - Para que $\hat{p}(X) = 0{,}50$ com $X_2 = 3{,}5$, precisamos que o *logit* seja nulo ($\hat{\eta} = 0$):
     $$-6 + 0{,}05 X_1 + 1(3{,}5) = 0 \iff 0{,}05 X_1 = 2{,}5 \iff \mathbf{X_1 = 50\text{ horas}}. \quad \blacksquare$$
</details>

---

### Exercício B3.2 *[ISLP, Seção 4.8, Ex. 2, Ex. 3 e Ex. 7]*
Considere um problema de classificação em $K$ classes com um preditor $X \in \mathbb{R}$, em que a densidade condicional na classe $k$ é normal $f_k(x) = \frac{1}{\sqrt{2\pi}\sigma_k}\exp\!\left(-\frac{(x - \mu_k)^2}{2\sigma_k^2}\right)$ e a probabilidade a priori da classe $k$ é $\pi_k$.
(a) Assumindo homocedasticidade ($\sigma_1^2 = \dots = \sigma_K^2 = \sigma^2$), prove que o classificador de Bayes atribui a observação $x$ à classe $k$ que maximiza a função discriminante **linear** do LDA (Ex. 4.8.2):
$$\delta_k(x) = x\cdot\frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} + \ln(\pi_k).$$
(b) Se a hipótese de variâncias iguais for removida ($\sigma_1^2 \neq \dots \neq \sigma_K^2$), prove que o classificador de Bayes (QDA) é **quadrático** em $x$ (Ex. 4.8.3).  
(c) Suponha que queremos prever se uma empresa pagará dividendos ($Y = \text{Sim}$ ou $\text{Não}$) com base no retorno percentual $X$ do último ano. Sabemos que $X \mid (Y=\text{Sim}) \sim \mathcal{N}(10, 36)$, $X \mid (Y=\text{Não}) \sim \mathcal{N}(0, 36)$ e que $80\%$ das empresas pagam dividendos ($\pi_{\text{Sim}} = 0{,}8$). Calcule a probabilidade de uma empresa com $X = 4$ pagar dividendos (Ex. 4.8.7).
- **Dica:** Em (a) e (b), tome o logaritmo natural do numerador da regra de Bayes $\pi_k f_k(x)$ e descarte aditivas que não dependem de $k$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Derivação de $\delta_k(x)$ no LDA ($\sigma_k = \sigma$):**  
   Pelo Teorema de Bayes, $p_k(x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^K \pi_l f_l(x)}$. Como o denominador é idêntico para todas as classes $k$ e $\ln(\cdot)$ é estritamente crescente, maximizar $p_k(x)$ equivale a maximizar $\ln\big(\pi_k f_k(x)\big)$:
   $$\ln\big(\pi_k f_k(x)\big) = \ln(\pi_k) - \ln(\sqrt{2\pi}\sigma) - \frac{(x - \mu_k)^2}{2\sigma^2} = \ln(\pi_k) - \ln(\sqrt{2\pi}\sigma) - \frac{x^2}{2\sigma^2} + x\cdot\frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2}.$$
   Como $-\ln(\sqrt{2\pi}\sigma) - \frac{x^2}{2\sigma^2}$ não depende do índice de classe $k$, descartamos esses termos e obtemos exatamente a função discriminante linear em $x$:
   $$\mathbf{\delta_k(x) = x\cdot\frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} + \ln(\pi_k)}. \quad \blacksquare$$

2. **Item (b) — Fronteira Quadrática quando $\sigma_k^2$ varia com $k$ (QDA, Ex. 4.8.3):**  
   Se $\sigma_k$ depende de $k$, os termos $-\ln(\sigma_k)$ e $-\frac{x^2}{2\sigma_k^2}$ **não são mais constantes entre as classes** e não podem ser descartados na comparação entre $k$ e $l$:
   $$\mathbf{\delta_k^{\text{QDA}}(x) = -\left(\frac{1}{2\sigma_k^2}\right)x^2 + \left(\frac{\mu_k}{\sigma_k^2}\right)x - \frac{\mu_k^2}{2\sigma_k^2} - \ln(\sigma_k) + \ln(\pi_k)},$$
   que é um polinômio de **2º grau** em $x$ (coeficiente quadrático $-\frac{1}{2\sigma_k^2} \neq -\frac{1}{2\sigma_l^2}$).

3. **Item (c) — Cálculo numérico para $X = 4$ (Ex. 4.8.7):**  
   Temos $\mu_1 = 10$, $\mu_0 = 0$, $\sigma^2 = 36$ ($\sigma = 6$), $\pi_1 = 0{,}80$ e $\pi_0 = 0{,}20$. Para $x = 4$:
   $$\pi_1 f_1(4) = 0{,}80 \cdot \frac{1}{6\sqrt{2\pi}}\exp\!\left(-\frac{(4 - 10)^2}{2 \times 36}\right) = \frac{1}{6\sqrt{2\pi}} \cdot 0{,}80\,e^{-36/72} = \frac{1}{6\sqrt{2\pi}} \cdot 0{,}80\,e^{-0{,}5},$$
   $$\pi_0 f_0(4) = 0{,}20 \cdot \frac{1}{6\sqrt{2\pi}}\exp\!\left(-\frac{(4 - 0)^2}{2 \times 36}\right) = \frac{1}{6\sqrt{2\pi}} \cdot 0{,}20\,e^{-16/72} = \frac{1}{6\sqrt{2\pi}} \cdot 0{,}20\,e^{-2/9}.$$
   Cancelando o fator comum $\frac{1}{6\sqrt{2\pi}}$:
   $$P(Y = \text{Sim} \mid X = 4) = \frac{0{,}80\,e^{-0{,}5}}{0{,}80\,e^{-0{,}5} + 0{,}20\,e^{-2/9}} = \frac{1}{1 + 0{,}25\,e^{0{,}5 - 2/9}} = \frac{1}{1 + 0{,}25\,e^{5/18}} \approx \frac{1}{1 + 0{,}25(1{,}3202)} \approx \mathbf{0{,}7518 \;\; (75{,}2\%)}. \quad \blacksquare$$
</details>

---

### Exercício B3.3 *[ISLP, Seção 4.8, Ex. 4 — A Maldição da Dimensionalidade no KNN]*
Suponha que as observações de treinamento estejam uniformemente distribuídas no hipercubo unitário $p$-dimensional $[0, 1]^p$. Para predizer a resposta de uma observação de teste $X = (x_1, \dots, x_p)^T$, decidimos usar todas as observações de treino contidas em uma vizinhança local centrada em $X$ que abrange uma fração $r = 0{,}10$ ($10\%$) da amplitude de cada variável preditora individual.
(a) Qual é a fração esperada de observações disponíveis que será usada na predição para $p = 1$, $p = 2$ e $p = 100$?  
(b) Se, em vez disso, quisermos um sub-hipercubo centrado em $X$ que contenha exatamente $10\%$ do volume total dos dados de treinamento em $[0, 1]^p$, qual deve ser o comprimento da aresta $\ell_p$ desse hipercubo ao longo de cada coordenada para $p = 1$, $p = 2$, $p = 10$ e $p = 100$? Que conclusão isso impõe sobre métodos puramente locais em alta dimensão?
- **Dica:** O volume de um sub-hipercubo de aresta $\ell$ em $[0,1]^p$ é $\ell^p$. Iguale $\ell_p^p = 0{,}10 \implies \ell_p = (0{,}10)^{1/p}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Fração de observações capturadas com aresta fixa $r = 0{,}10$ por coordenada:**  
   Por independência e distribuição uniforme em $[0,1]^p$, a probabilidade de uma observação cair simultaneamente nos intervalos de comprimento $0{,}10$ em todas as $p$ coordenadas é o volume $(0{,}10)^p$:
   - Para $p = 1$: fração $= 0{,}10^1 = \mathbf{10\%}$;
   - Para $p = 2$: fração $= 0{,}10^2 = 0{,}01 = \mathbf{1\%}$;
   - Para $p = 100$: fração $= \mathbf{10^{-100}}$ (essencialmente zero — nenhuma observação do universo estará nessa vizinhança!).

2. **Item (b) — Comprimento necessário da aresta $\ell_p$ para conter $10\%$ dos dados ($\ell_p^p = 0{,}10$):**  
   Resolvendo $\ell_p = (0{,}10)^{1/p}$:
   - Para $p = 1$: $\ell_1 = 0{,}10^{1} = \mathbf{0{,}10}$ ($10\%$ do domínio);
   - Para $p = 2$: $\ell_2 = 0{,}10^{1/2} \approx \mathbf{0{,}316}$ ($31{,}6\%$ de cada eixo);
   - Para $p = 10$: $\ell_{10} = 0{,}10^{1/10} \approx \mathbf{0{,}794}$ ($79{,}4\%$ de cada eixo);
   - Para $p = 100$: $\ell_{100} = 0{,}10^{1/100} \approx \mathbf{0{,}977}$ ($97{,}7\%$ de cada eixo!).
   **Conclusão (Maldição da Dimensionalidade):** Em alta dimensão ($p \gg 1$), para capturar apenas $10\%$ dos pontos mais próximos, somos obrigados a estender a caixa por quase todo o intervalo $[0,1]$ em cada coordenada ($97{,}7\%$ em $p=100$). Portanto, **os "vizinhos mais próximos" deixam de ser locais**, fazendo com que estimadores não paramétricos puramente baseados em distância (como KNN) sofram degradação severa sem hipóteses estruturais ou redução de dimensionalidade. $\blacksquare$
</details>

---

### Exercício B3.4 *[ISLP, Seção 4.8, Ex. 12 e Complemento — Raschka et al., Cap. 2 e Cap. 3]*
(a) (**Equivalência Logística vs. Softmax — Ex. 4.8.12:**) Para $K = 2$ classes, compare a parametrização logística padrão $\Pr(Y = 1 \mid X = x) = \frac{e^{\beta_0 + \beta_1 x}}{1 + e^{\beta_0 + \beta_1 x}}$ com a parametrização **Softmax** simétrica $\Pr(Y = 1 \mid X = x) = \frac{e^{\alpha_{10} + \alpha_{11}x}}{e^{\alpha_{10} + \alpha_{11}x} + e^{\alpha_{20} + \alpha_{21}x}}$ e mostre que ambas representam exatamente a mesma família de probabilidades condicionais.  
(b) **[Complemento — Raschka et al., Cap. 2]** Escreva e compare a regra de atualização de pesos $\Delta w_j$ do **Perceptron de Rosenblatt** com a do **Adaline (*Adaptive Linear Neuron*)** treinado por Gradiente Descendente em lote sobre $L(w,b) = \frac{1}{2n}\sum_{i=1}^n (y_i - z_i)^2$, onde $z_i = w^T x_i + b$.
- **Dica:** Em (a), divida numerador e denominador da Softmax por $e^{\alpha_{20} + \alpha_{21}x}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Equivalência entre Softmax ($K=2$) e Regressão Logística (Ex. 4.8.12):**  
   Dividindo o numerador e o denominador da parametrização Softmax por $e^{\alpha_{20} + \alpha_{21}x} > 0$:
   $$\Pr(Y = 1 \mid X = x) = \frac{e^{(\alpha_{10} - \alpha_{20}) + (\alpha_{11} - \alpha_{21})x}}{1 + e^{(\alpha_{10} - \alpha_{20}) + (\alpha_{11} - \alpha_{21})x}}.$$
   Definindo $\beta_0 = \alpha_{10} - \alpha_{20}$ e $\beta_1 = \alpha_{11} - \alpha_{21}$ (e multiplicando numerador e denominador por $e^{-\beta_0 - \beta_1 x}$ caso se deseje a forma com $1$ no numerador para a classe de referência), recupera-se exatamente o modelo logístico binário. A parametrização Softmax possui um par de parâmetros redundante (invariância por translação $\alpha_{k} \mapsto \alpha_{k} + c$), razão pela qual a regressão logística fixa uma classe base com coeficientes nulos ($\alpha_{20} = \alpha_{21} = 0$).

2. **Item (b) — Perceptron vs. Adaline (Raschka Cap. 2):**
   - **Perceptron de Rosenblatt:** Atualiza os pesos **apenas quando o rótulo discreto $\hat{y}_i = \mathbb{I}(w^T x_i + b \ge 0)$ erra**:
     $$\Delta w_j^{\text{Perceptron}} = \eta(y_i - \hat{y}_i)x_{ij},$$
     onde $y_i - \hat{y}_i \in \{-1, 0, +1\}$. Se as classes não forem linearmente separáveis, o algoritmo jamais converge.
   - **Adaline (Widrow-Hoff):** Calcula o gradiente de uma função de perda diferenciável sobre a **ativação linear contínua** $\phi(z_i) = z_i = w^T x_i + b$ antes do limiar de decisão:
     $$\frac{\partial L}{\partial w_j} = -\frac{1}{n}\sum_{i=1}^n (y_i - z_i)x_{ij} \implies \mathbf{\Delta w_j^{\text{Adaline}} = \eta \cdot \frac{1}{n}\sum_{i=1}^n (y_i - z_i)x_{ij}}.$$
     Como $L(w,b)$ é quadrática e convexa, o Adaline converge para o mínimo global mesmo quando os dados não são linearmente separáveis. $\blacksquare$
</details>

---

<a id="bloco-4"></a>
## Bloco 4 — Reamostragem: Validação Cruzada $k$-Fold, LOOCV, Atalho $h_i$ e Bootstrap (Capítulo 5)

### Exercício B4.1 *[ISLP, Seção 5.4, Ex. 1]*
Seja $X$ o retorno de um ativo financeiro e $Y$ o retorno de um segundo ativo. Deseja-se investir uma fração $\alpha \in \mathbb{R}$ do capital em $X$ e a fração restante $1 - \alpha$ em $Y$, de modo a minimizar o risco (variância) total da carteira $\operatorname{Var}\big(\alpha X + (1 - \alpha)Y\big)$. Prove que o valor ótimo de $\alpha$ é dado por:
$$\alpha^* = \frac{\sigma_Y^2 - \sigma_{XY}}{\sigma_X^2 + \sigma_Y^2 - 2\sigma_{XY}},$$
onde $\sigma_X^2 = \operatorname{Var}(X)$, $\sigma_Y^2 = \operatorname{Var}(Y)$ e $\sigma_{XY} = \operatorname{Cov}(X, Y)$.
- **Dica:** Expanda $f(\alpha) = \operatorname{Var}(\alpha X + (1-\alpha)Y) = \alpha^2\sigma_X^2 + (1-\alpha)^2\sigma_Y^2 + 2\alpha(1-\alpha)\sigma_{XY}$ e resolva $f'(\alpha) = 0$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. Pela propriedade bilinear da variância $\operatorname{Var}(aX + bY) = a^2\operatorname{Var}(X) + b^2\operatorname{Var}(Y) + 2ab\operatorname{Cov}(X,Y)$ com $a = \alpha$ e $b = 1 - \alpha$:
   $$f(\alpha) = \operatorname{Var}\big(\alpha X + (1 - \alpha)Y\big) = \alpha^2\sigma_X^2 + (1 - \alpha)^2\sigma_Y^2 + 2\alpha(1 - \alpha)\sigma_{XY}.$$
2. Derivando $f(\alpha)$ em relação a $\alpha$ e igualando a zero:
   $$f'(\alpha) = 2\alpha\sigma_X^2 - 2(1 - \alpha)\sigma_Y^2 + 2(1 - 2\alpha)\sigma_{XY} = 0.$$
3. Dividindo por $2$ e agrupando os termos que multiplicam $\alpha$:
   $$\alpha\sigma_X^2 - \sigma_Y^2 + \alpha\sigma_Y^2 + \sigma_{XY} - 2\alpha\sigma_{XY} = 0 \iff \alpha\big(\sigma_X^2 + \sigma_Y^2 - 2\sigma_{XY}\big) = \sigma_Y^2 - \sigma_{XY}.$$
4. Como $f''(\alpha) = 2(\sigma_X^2 + \sigma_Y^2 - 2\sigma_{XY}) = 2\operatorname{Var}(X - Y) > 0$ (desde que $X - Y$ não seja constante quase certamente), o ponto crítico é o mínimo global único:
   $$\mathbf{\alpha^* = \frac{\sigma_Y^2 - \sigma_{XY}}{\sigma_X^2 + \sigma_Y^2 - 2\sigma_{XY}}}. \quad \blacksquare$$
</details>

---

### Exercício B4.2 *[ISLP, Seção 5.4, Ex. 2]*
Considere uma amostra de *bootstrap* $Z^*$ de tamanho $n$, obtida por amostragem aleatória simples **com reposição** a partir de um conjunto original de $n$ observações distintas $\{z_1, \dots, z_n\}$.
(a) Qual é a probabilidade de que a primeira observação sorteada no *bootstrap* **não** seja a $j$-ésima observação original $z_j$?  
(b) Qual é a probabilidade de que a $j$-ésima observação original **não pertença** à amostra de *bootstrap* $Z^*$ após os $n$ sorteios independentes?  
(c) Deduza a probabilidade de que $z_j$ **esteja presente** na amostra de *bootstrap* e calcule seu valor para $n = 5$, $n = 100$, $n = 10.000$ e no limite $n \to \infty$.
- **Dica:** Em (c), use o limite fundamental exponencial $\lim_{n \to \infty}\left(1 - \frac{1}{n}\right)^n = e^{-1}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a):** Como cada uma das $n$ observações tem probabilidade $1/n$ de ser sorteada na 1ª extração, a probabilidade de a 1ª extração não ser $z_j$ é:
   $$P(\text{1ª extração} \neq z_j) = \mathbf{1 - \frac{1}{n}}.$$
2. **Item (b):** Como as $n$ extrações do *bootstrap* são independentes e com reposição, a probabilidade de $z_j$ não ser sorteada em **nenhuma** das $n$ extrações é o produto:
   $$P(z_j \notin Z^*) = \prod_{i=1}^n \left(1 - \frac{1}{n}\right) = \mathbf{\left(1 - \frac{1}{n}\right)^n}.$$
3. **Item (c):** A probabilidade complementar de $z_j$ estar presente pelo menos uma vez na amostra de *bootstrap* é:
   $$P(z_j \in Z^*) = 1 - \left(1 - \frac{1}{n}\right)^n.$$
   Calculando numericamente e tomando o limite assintótico:
   - Para $n = 5$: $1 - (1 - 1/5)^5 = 1 - 0{,}8^5 = 1 - 0{,}32768 = \mathbf{0{,}6723 \;\; (67{,}2\%)}$;
   - Para $n = 100$: $1 - (1 - 1/100)^{100} = 1 - 0{,}99^{100} \approx \mathbf{0{,}6340 \;\; (63{,}4\%)}$;
   - Para $n = 10.000$: $1 - (1 - 1/10000)^{10000} \approx \mathbf{0{,}6321 \;\; (63{,}2\%)}$;
   - No limite $n \to \infty$:
     $$\lim_{n \to \infty}\left[1 - \left(1 - \frac{1}{n}\right)^n\right] = \mathbf{1 - e^{-1} \approx 0{,}63212 \;\; (63{,}2\%)}.$$
   Consequentemente, cerca de $e^{-1} \approx 36{,}8\%$ das observações originais ficam fora de cada árvore ou amostra de *bootstrap* (constituindo as observações *Out-of-Bag* — OOB). $\blacksquare$
</details>

---

### Exercício B4.3 *[ISLP, Seção 5.4, Ex. 3 e Equação 5.2]*
(a) Compare a **Validação Cruzada $k$-Fold** ($k = 5$ ou $10$) com a **Abordagem do Conjunto de Validação Simples (*Holdout*)** e com o **LOOCV (*Leave-One-Out Cross-Validation*)**, indicando vantagens e desvantagens em termos de custo computacional, viés e variância da estimativa do erro de teste.  
(b) Em um modelo linear ou polinomial ajustado por Mínimos Quadrados Ordinários ($\hat{y} = H y$, onde $H = X(X^T X)^{-1}X^T$ é a matriz de projeção chapéu e $h_i = H_{ii}$ é a alavancagem da $i$-ésima observação), prove que o resíduo *leave-one-out* $y_i - \hat{y}_{(-i)}$ satisfaz:
$$y_i - \hat{y}_{(-i)} = \frac{y_i - \hat{y}_i}{1 - h_i} \implies \operatorname{CV}_{(n)} = \frac{1}{n}\sum_{i=1}^n \left(\frac{y_i - \hat{y}_i}{1 - h_i}\right)^2.$$
- **Dica:** Em (b), use a propriedade de que $\hat{y}_{(-i)}$ é também a predição obtida quando substituímos a resposta $y_i$ pelo próprio valor predito $\hat{y}_{(-i)}$ no ajuste completo: $\hat{y}_i^{\text{mod}} = \sum_{j \neq i} H_{ij} y_j + H_{ii}\hat{y}_{(-i)} = \hat{y}_{(-i)}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Comparação entre Holdout, LOOCV e $k$-Fold CV:**
   - **$k$-Fold CV vs. Conjunto de Validação Simples (*Holdout*):** O *Holdout* treina apenas em metade (ou $70\%$) dos dados (superestimando o erro de teste, alto viés) e sua estimativa varia fortemente conforme a partição aleatória escolhida (alta variância). O $k$-Fold CV usa $(k-1)/k$ dos dados em cada treino (menor viés) e tira a média sobre todos os $k$ blocos (menor variância).
   - **$k$-Fold CV ($k=5, 10$) vs. LOOCV ($k=n$):**
     1. *Custo computacional:* O $k$-Fold requer apenas $5$ ou $10$ ajustes do modelo, enquanto o LOOCV requer $n$ ajustes (proibitivo para redes neurais, SVMs ou árvores em grandes bancos de dados).
     2. *Trade-off Viés-Variância:* O LOOCV tem viés quase nulo (treina com $n-1$ pontos), mas **maior variância** do que o $k$-Fold com $k=5$ ou $10$, porque os $n$ modelos do LOOCV são ajustados sobre amostras quase idênticas (compartilhando $n-2$ observações), gerando erros quadráticos altamente correlacionados cuja média não reduz tanto a variância quanto a média de $k$ blocos disjuntos menos correlacionados.

2. **Item (b) — Prova elegante da Fórmula Mágica do LOOCV Linear ($\frac{y_i - \hat{y}_i}{1 - h_i}$):**  
   Seja $\hat{\beta}_{(-i)}$ o vetor de coeficientes OLS ajustado sem a $i$-ésima observação, e $\hat{y}_{(-i)} = x_i^T \hat{\beta}_{(-i)}$. Se substituirmos o valor observado $y_i$ por $y_i^* = \hat{y}_{(-i)}$ no conjunto completo de $n$ pontos, a $i$-ésima observação tem resíduo zero em relação a $\hat{\beta}_{(-i)}$, logo o ajuste OLS nos $n$ pontos com $y_i^* = \hat{y}_{(-i)}$ continua sendo exatamente $\hat{\beta}_{(-i)}$!  
   Pela linearidade da matriz de projeção $H = X(X^T X)^{-1}X^T$ (que depende apenas de $X$, e não de $y$), a $i$-ésima predição nesse conjunto modificado é:
   $$\hat{y}_{(-i)} = \sum_{j \neq i} H_{ij} y_j + H_{ii} \hat{y}_{(-i)}.$$
   Mas, no ajuste original completo, $\hat{y}_i = \sum_{j \neq i} H_{ij} y_j + H_{ii} y_i \implies \sum_{j \neq i} H_{ij} y_j = \hat{y}_i - h_i y_i$ (onde $h_i = H_{ii}$). Substituindo:
   $$\hat{y}_{(-i)} = \hat{y}_i - h_i y_i + h_i \hat{y}_{(-i)} \implies (1 - h_i)\hat{y}_{(-i)} = \hat{y}_i - h_i y_i.$$
   Subtraindo $(1 - h_i)y_i$ de ambos os lados (ou isolando $y_i - \hat{y}_{(-i)}$):
   $$(1 - h_i)\big(y_i - \hat{y}_{(-i)}\big) = (1 - h_i)y_i - (\hat{y}_i - h_i y_i) = y_i - \hat{y}_i \iff \mathbf{y_i - \hat{y}_{(-i)} = \frac{y_i - \hat{y}_i}{1 - h_i}}. \quad \blacksquare$$
</details>

---

### Exercício B4.4 *[ISLP, Seção 5.4, Ex. 8 e Seção 5.1.5 — A Regra Prática Errada de Pré-Seleção antes da Validação Cruzada]*
Considere um cenário de alta dimensão com $n = 50$ observações e $p = 5.000$ preditores totalmente independentes do rótulo binário $Y \in \{0, 1\}$ (erro de teste verdadeiro $= 50\%$). Um pesquisador realiza o seguinte procedimento em duas etapas:
1. Usando todas as $n = 50$ observações, calcula a correlação de cada um dos $5.000$ preditores com $Y$ e seleciona os $100$ preditores mais fortemente correlacionados com $Y$.
2. Aplica Validação Cruzada $5$-Fold apenas à regressão logística ajustada sobre esses $100$ preditores pré-selecionados, obtendo uma taxa de erro de validação cruzada de apenas $3\%$.

Explique matematicamente por que a estimativa de $3\%$ é drasticamente enviesada e descreva o protocolo correto de validação cruzada.
- **Dica:** Os $100$ preditores já "viram" os rótulos $Y$ dos blocos de validação durante a Etapa 1.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Por que ocorre o viés severo (*Selection Bias / Data Leakage*):**  
   Na Etapa 1, os $100$ preditores foram escolhidos entre $5.000$ candidatos justamente por apresentarem, por puro acaso amostral nas $n = 50$ observações completas, alta correlação empírica com $Y$. Quando dividimos essas mesmas $50$ observações em $5$ blocos na Etapa 2, os pontos do bloco de validação **já foram utilizados para escolher os preditores**. Assim, esses $100$ preditores têm correlação espúria garantida com $Y$ também dentro do bloco de validação, derrubando artificialmente o erro de CV para $\sim 3\%$, embora o erro verdadeiro em novas amostras independentes seja de **$50\%$**!
2. **Protocolo Correto:**  
   Toda etapa supervisionada de pré-processamento, triagem de atributos (*feature selection*) ou redução de dimensionalidade supervisionada **deve ser executada exclusivamente dentro dos $k - 1$ blocos de treinamento de cada iteração da validação cruzada**. Ao selecionar os $100$ preditores usando apenas as $40$ observações de treino de cada *fold*, esses preditores serão totalmente independentes das $10$ observações retidas para validação, e a Validação Cruzada reportará corretamente um erro próximo de $50\%$. $\blacksquare$
</details>

---

<a id="bloco-5"></a>
## Bloco 5 — Seleção de Variáveis, Regressão Ridge, Lasso, *Soft-Thresholding* e Priori Bayesiano (Capítulo 6)

### Exercício B5.1 *[ISLP, Seção 6.6, Ex. 1, Ex. 2 e Ex. 3]*
(a) Considere os três procedimentos de seleção de subconjuntos (*Best Subset*, *Forward Stepwise* e *Backward Stepwise*) para um valor fixo de $k$ preditores ($1 \le k \le p$). Qual dos três métodos produz o **menor RSS de treino**? Qual produz o **menor RSS de teste**? E para quais métodos o modelo $\mathcal{M}_k$ com $k$ variáveis é garantidamente um subconjunto do modelo $\mathcal{M}_{k+1}$ com $k+1$ variáveis? (Ex. 6.6.1)  
(b) No Lasso, à medida que aumentamos o orçamento de norma $\ell_1$, $s \ge 0$, na restrição $\sum_{j=1}^p |\beta_j| \le s$ a partir de $s = 0$, descreva o comportamento de: (i) RSS de treino; (ii) RSS de teste; (iii) Variância; (iv) Viés ao quadrado; (v) Erro irredutível (Ex. 6.6.3).
- **Dica:** Em (a), lembre que *Best Subset* otimiza globalmente sobre todos os $\binom{p}{k}$ subconjuntos de tamanho $k$. Em (b), note que $s = 0$ força $\hat{\beta} = 0$ (máxima restrição) e $s \ge \sum |\hat{\beta}_j^{\text{OLS}}|$ recupera o OLS sem restrição.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — *Best Subset* vs. *Forward* vs. *Backward Stepwise* (Ex. 6.6.1):**
   - **Menor RSS de treino para $k$ fixo:** **Best Subset Selection**, pois avalia exaustivamente todos os $\binom{p}{k}$ modelos possíveis com $k$ preditores e escolhe aquele com menor RSS de treino, enquanto *Forward* e *Backward* fazem buscas gulosas restritas.
   - **Menor RSS de teste:** **Não há resposta determinística geral** (qualquer um dos três pode ter menor erro de teste em uma amostra específica; se $p$ for grande, *Best Subset* pode sofrer maior sobreajuste por buscar entre $\binom{p}{k}$ candidatos).
   - **Aninhamento $\mathcal{M}_k \subset \mathcal{M}_{k+1}$:** É **Verdadeiro** para **Forward Stepwise** (que adiciona 1 variável a $\mathcal{M}_k$ para formar $\mathcal{M}_{k+1}$) e para **Backward Stepwise** (que remove 1 variável de $\mathcal{M}_{k+1}$ para formar $\mathcal{M}_k$), mas **Falso** para **Best Subset** (o melhor subconjunto de 2 variáveis pode não conter a variável do melhor modelo de 1 variável).

2. **Item (b) — Evolução das grandezas no Lasso quando $s$ cresce a partir de $0$ (Ex. 6.6.3):**  
   Aumentar $s$ amplia a região viável $\{\beta : \|\beta\|_1 \le s\}$, aumentando monotonicamente a flexibilidade do modelo:
   - **(i) RSS de treino:** **Decresce monotonicamente** (pois para $s_1 < s_2$, o espaço viável para $s_1$ está contido no de $s_2$, logo o mínimo sobre um conjunto maior nunca pode aumentar), estabilizando no $\operatorname{RSS}_{\text{OLS}}$ quando $s \ge \|\hat{\beta}^{\text{OLS}}\|_1$.
   - **(ii) RSS de teste:** **Decresce inicialmente e depois cresce** (formato em **U**), atingindo o mínimo em um $s^*$ intermediário onde a redução de variância supera o viés introduzido.
   - **(iii) Variância:** **Cresce monotonicamente** com $s$, pois os coeficientes têm maior liberdade para variar com o conjunto de treinamento.
   - **(iv) Viés ao quadrado:** **Decresce monotonicamente** com $s$, pois a restrição de encolhimento em direção a zero vai sendo relaxada.
   - **(v) Erro irredutível $\operatorname{Var}(\varepsilon)$:** **Permanece constante**, pois independe de $\hat{\beta}$ e de $s$. $\blacksquare$
</details>

---

### Exercício B5.2 *[ISLP, Seção 6.6, Ex. 5 — Colinearidade Exata: Ridge vs. Lasso]*
Suponha que $n = 2$, $p = 2$, $x_{11} = x_{12}$ e $x_{21} = x_{22}$ (isto é, os dois preditores $X_1$ e $X_2$ são **idênticos**), e que $y_1 + y_2 = 0$ e $x_{11} + x_{21} = 0$, de modo que o intercepto estimado é $\hat{\beta}_0 = 0$.
(a) Escreva o problema de otimização da **Regressão Ridge** neste caso e prove que a solução ótima sempre atribui pesos idênticos aos preditores colineares: $\hat{\beta}_1^{\text{Ridge}} = \hat{\beta}_2^{\text{Ridge}}$.  
(b) Escreva o problema de otimização do **Lasso** neste caso e demonstre que a solução **não é única**, descrevendo geometricamente o conjunto de todas as soluções ótimas $(\hat{\beta}_1^{\text{Lasso}}, \hat{\beta}_2^{\text{Lasso}})$.
- **Dica:** Como $x_{i1} = x_{i2} = x_i$, o termo de ajuste aos dados depende apenas da soma $S = \beta_1 + \beta_2$. Minimize a penalidade $\beta_1^2 + \beta_2^2$ (Ridge) e $|\beta_1| + |\beta_2|$ (Lasso) para $S = \beta_1 + \beta_2$ fixo.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Regressão Ridge sob Colinearidade Exata ($\hat{\beta}_1 = \hat{\beta}_2$):**  
   Denotando $x_1 = x_{11} = x_{12}$ e $x_2 = x_{21} = x_{22}$, a função objetivo do Ridge com $\hat{\beta}_0 = 0$ é:
   $$Q_{\text{Ridge}}(\beta_1, \beta_2) = \big(y_1 - (\beta_1 + \beta_2)x_1\big)^2 + \big(y_2 - (\beta_1 + \beta_2)x_2\big)^2 + \lambda(\beta_1^2 + \beta_2^2).$$
   Derivando em relação a $\beta_1$ e a $\beta_2$ e igualando a zero:
   $$\frac{\partial Q_{\text{Ridge}}}{\partial \beta_1} = -2\sum_{i=1}^2 x_i\big(y_i - (\hat{\beta}_1 + \hat{\beta}_2)x_i\big) + 2\lambda\hat{\beta}_1 = 0,$$
   $$\frac{\partial Q_{\text{Ridge}}}{\partial \beta_2} = -2\sum_{i=1}^2 x_i\big(y_i - (\hat{\beta}_1 + \hat{\beta}_2)x_i\big) + 2\lambda\hat{\beta}_2 = 0.$$
   Subtraindo a segunda equação da primeira (para $\lambda > 0$):
   $$2\lambda(\hat{\beta}_1 - \hat{\beta}_2) = 0 \implies \mathbf{\hat{\beta}_1^{\text{Ridge}} = \hat{\beta}_2^{\text{Ridge}} = \frac{x_1 y_1 + x_2 y_2}{2(x_1^2 + x_2^2) + \lambda}}.$$
   Geometricamente, para uma soma fixa $\beta_1 + \beta_2 = S$, a norma $\ell_2^2 = \beta_1^2 + \beta_2^2 = \frac{1}{2}(\beta_1 + \beta_2)^2 + \frac{1}{2}(\beta_1 - \beta_2)^2$ é estritamente convexa e atinge seu mínimo único quando $\beta_1 = \beta_2 = S/2$.

2. **Item (b) — Não Unicidade do Lasso sob Colinearidade Exata:**  
   A função objetivo do Lasso é:
   $$Q_{\text{Lasso}}(\beta_1, \beta_2) = \big(y_1 - (\beta_1 + \beta_2)x_1\big)^2 + \big(y_2 - (\beta_1 + \beta_2)x_2\big)^2 + \lambda\big(|\beta_1| + |\beta_2|\big).$$
   Note que o termo de RSS depende exclusivamente da soma $S = \beta_1 + \beta_2$. Para qualquer par $(\beta_1, \beta_2)$ no mesmo quadrante ($\beta_1 \beta_2 \ge 0$), vale a igualdade na desigualdade triangular:
   $$|\beta_1| + |\beta_2| = |\beta_1 + \beta_2| = |S|!$$
   Portanto, se $S^* = \hat{\beta}_1 + \hat{\beta}_2$ é a soma ótima que minimiza $\sum_{i=1}^2 (y_i - S x_i)^2 + \lambda|S|$, então **qualquer ponto $(\hat{\beta}_1, \hat{\beta}_2)$ sobre o segmento de reta**:
   $$\mathbf{\big\{(\hat{\beta}_1, \hat{\beta}_2) \in \mathbb{R}^2 : \hat{\beta}_1 + \hat{\beta}_2 = S^* \text{ e } \hat{\beta}_1\hat{\beta}_2 \ge 0\big\}}$$
   possui exatamente o mesmo RSS e exatamente a mesma norma $\ell_1 = |S^*|$, sendo todas soluções ótimas globais do Lasso! $\blacksquare$
</details>

---

### Exercício B5.3 *[ISLP, Seção 6.6, Ex. 6 e Seção 6.2.2 — Equações 6.14 e 6.15]*
Considere o caso ortonormal simplificado em que $n = p$ e a matriz de desenho $X = I_p$ é a matriz identidade (sem intercepto, de modo que $\hat{\beta}_j^{\text{OLS}} = y_j$).
(a) Para a **Regressão Ridge**, minimize $\sum_{j=1}^p (y_j - \beta_j)^2 + \lambda\sum_{j=1}^p \beta_j^2$ e prove que $\hat{\beta}_j^{\text{Ridge}} = \frac{y_j}{1 + \lambda}$.  
(b) Para o **Lasso**, minimize $\sum_{j=1}^p (y_j - \beta_j)^2 + \lambda\sum_{j=1}^p |\beta_j|$ e derive rigorosamente o operador de **Limiarização Suave (*Soft-Thresholding*)**:
$$\hat{\beta}_j^{\text{Lasso}} = \operatorname{sign}(y_j)\max\!\left(|y_j| - \frac{\lambda}{2},\; 0\right) = \begin{cases} y_j - \lambda/2, & \text{se } y_j > \lambda/2; \\ y_j + \lambda/2, & \text{se } y_j < -\lambda/2; \\ 0, & \text{se } |y_j| \le \lambda/2. \end{cases}$$
- **Dica:** Como a função objetivo se separa em $p$ problemas univariados independentes $g_j(\beta_j)$, minimize $g_j(\beta_j) = (y_j - \beta_j)^2 + \lambda|\beta_j|$ analisando os casos $\beta_j > 0$, $\beta_j < 0$ e $\beta_j = 0$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Encolhimento Proporcional do Ridge:**  
   Cada coordenada $j$ minimiza independentemente $f_j(\beta_j) = (y_j - \beta_j)^2 + \lambda\beta_j^2$. Derivando:
   $$f_j'(\beta_j) = -2(y_j - \beta_j) + 2\lambda\beta_j = 0 \iff 2(1 + \lambda)\beta_j = 2y_j \iff \mathbf{\hat{\beta}_j^{\text{Ridge}} = \frac{y_j}{1 + \lambda}}.$$
   Todo coeficiente é encolhido pelo mesmo fator multiplicativo $\frac{1}{1+\lambda} \in (0, 1)$, nunca atingindo exatamente zero se $y_j \neq 0$.

2. **Item (b) — Derivação do Operador *Soft-Thresholding* do Lasso:**  
   Queremos minimizar $g_j(\beta_j) = (y_j - \beta_j)^2 + \lambda|\beta_j|$ para $\lambda > 0$. Analisemos o sinal de $\beta_j$:
   - **Caso 1 ($y_j > \lambda / 2$):** Se $\beta_j \le 0$, $g_j(\beta_j) \ge y_j^2 = g_j(0)$, logo o ótimo deve estar em $\beta_j \ge 0$. Para $\beta_j > 0$, $|\beta_j| = \beta_j$ e:
     $$g_j'(\beta_j) = -2(y_j - \beta_j) + \lambda = 0 \iff \mathbf{\hat{\beta}_j = y_j - \frac{\lambda}{2} > 0}.$$
   - **Caso 2 ($y_j < -\lambda / 2$):** Por simetria, o ótimo ocorre em $\beta_j < 0$, onde $|\beta_j| = -\beta_j$:
     $$g_j'(\beta_j) = -2(y_j - \beta_j) - \lambda = 0 \iff \mathbf{\hat{\beta}_j = y_j + \frac{\lambda}{2} < 0}.$$
   - **Caso 3 ($|y_j| \le \lambda / 2$):** Para qualquer $\beta_j \neq 0$, temos:
     $$g_j(\beta_j) - g_j(0) = (\beta_j^2 - 2y_j\beta_j + y_j^2 + \lambda|\beta_j|) - y_j^2 = \beta_j^2 + |\beta_j|\big(\lambda - 2y_j\operatorname{sign}(\beta_j)\big).$$
     Como $|y_j| \le \lambda / 2 \implies 2y_j\operatorname{sign}(\beta_j) \le 2|y_j| \le \lambda$, segue que $\lambda - 2y_j\operatorname{sign}(\beta_j) \ge 0$, logo $g_j(\beta_j) - g_j(0) \ge \beta_j^2 > 0$ para todo $\beta_j \neq 0$. Assim, o mínimo único ocorre exatamente na quina não diferenciável **$\hat{\beta}_j = 0$**, realizando **seleção exata de variáveis (esparsidade)**! $\blacksquare$
</details>

---

### Exercício B5.4 *[ISLP, Seção 6.6, Ex. 7 — Interpretação Bayesiana do Ridge e do Lasso]*
Considere o modelo linear $Y = X\beta + \varepsilon$ com erros normais independentes $\varepsilon_i \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)$.
(a) Suponha que os coeficientes $\beta_1, \dots, \beta_p$ possuem distribuição a priori i.i.d. **Laplace (dupla exponencial)** com média zero e parâmetro de escala $b > 0$, $p(\beta_j) = \frac{1}{2b}\exp\!\left(-\frac{|\beta_j|}{b}\right)$. Derive a distribuição a posteriori $p(\beta \mid X, Y)$ e prove que a moda a posteriori (**estimador MAP**) coincide exatamente com o estimador **Lasso** para $\lambda = \frac{2\sigma^2}{b}$.  
(b) Suponha agora que a priori sobre $\beta_1, \dots, \beta_p$ é **Normal** i.i.d. $\beta_j \sim \mathcal{N}(0, c^2)$. Prove que tan­to a moda (**MAP**) quanto a média a posteriori coincidem com o estimador **Ridge** para $\lambda = \frac{\sigma^2}{c^2}$.
- **Dica:** Escreva $\ln p(\beta \mid X, Y) = \ln f(Y \mid X, \beta) + \ln p(\beta) + \text{const.}$ e maximize em relação a $\beta$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Verossimilhança Gaussiana:**  
   Como $Y_i \mid X, \beta \stackrel{\text{ind.}}{\sim} \mathcal{N}(x_i^T\beta, \sigma^2)$, a função de verossimilhança conjunta é:
   $$f(Y \mid X, \beta) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma}\exp\!\left(-\frac{(y_i - x_i^T\beta)^2}{2\sigma^2}\right) = (2\pi\sigma^2)^{-n/2}\exp\!\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - x_i^T\beta)^2\right).$$

2. **Item (a) — Priori Laplace $\implies$ MAP é o Lasso:**  
   Com a priori $p(\beta) = \prod_{j=1}^p \frac{1}{2b}\exp(-|\beta_j|/b) = (2b)^{-p}\exp\!\left(-\frac{1}{b}\sum_{j=1}^p |\beta_j|\right)$, a log-posteriori (a menos de constantes aditivas que não dependem de $\beta$) é:
   $$\ln p(\beta \mid X, Y) = \ln f(Y \mid X, \beta) + \ln p(\beta) + C_1 = -\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - x_i^T\beta)^2 - \frac{1}{b}\sum_{j=1}^p |\beta_j| + C_2.$$
   Maximizar $\ln p(\beta \mid X, Y)$ equivale a minimizar $-2\sigma^2 \ln p(\beta \mid X, Y)$, ou seja:
   $$\hat{\beta}_{\text{MAP}} = \arg\min_{\beta} \left\{\sum_{i=1}^n (y_i - x_i^T\beta)^2 + \underbrace{\left(\frac{2\sigma^2}{b}\right)}_{\lambda}\sum_{j=1}^p |\beta_j|\right\},$$
   que é exatamente o estimador **Lasso** com $\mathbf{\lambda = \frac{2\sigma^2}{b}}$!

3. **Item (b) — Priori Normal $\implies$ MAP e Média a Posteriori são o Ridge:**  
   Com a priori $p(\beta) = \prod_{j=1}^p \frac{1}{\sqrt{2\pi}c}\exp\!\left(-\frac{\beta_j^2}{2c^2}\right)$, a log-posteriori é:
   $$\ln p(\beta \mid X, Y) = -\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - x_i^T\beta)^2 - \frac{1}{2c^2}\sum_{j=1}^p \beta_j^2 + C_3.$$
   Multiplicando por $-2\sigma^2$, maximizar a posteriori equivale a minimizar:
   $$\sum_{i=1}^n (y_i - x_i^T\beta)^2 + \underbrace{\left(\frac{\sigma^2}{c^2}\right)}_{\lambda}\sum_{j=1}^p \beta_j^2,$$
   que é exatamente a **Regressão Ridge** com $\mathbf{\lambda = \frac{\sigma^2}{c^2}}$. Como a log-posteriori é uma forma quadrática côncava em $\beta$, a distribuição a posteriori $p(\beta \mid X, Y)$ é uma Normal Multivariada, na qual a moda (MAP) e a esperança condicional (média a posteriori) coincidem. $\blacksquare$
</details>

---

<a id="bloco-6"></a>
## Bloco 6 — Além da Linearidade: Splines Cúbicas, *Smoothing Splines*, Base Polinomial e GAMs (Capítulo 7)

### Exercício B6.1 *[ISLP, Seção 7.9, Ex. 1 — Demonstração Completa da Base de Potência Truncada]*
Seja $\xi \in \mathbb{R}$ um nó único fixado. Considere uma função definida pela combinação linear da base de potência truncada cúbica:
$$f(x) = \beta_0 + \beta_1 x + \beta_2 x^2 + \beta_3 x^3 + \beta_4(x - \xi)_+^3, \quad \text{onde } (x - \xi)_+^3 = \begin{cases} (x - \xi)^3, & \text{se } x > \xi; \\ 0, & \text{se } x \le \xi. \end{cases}$$
(a) Encontre um polinômio cúbico $f_1(x) = a_1 + b_1 x + c_1 x^2 + d_1 x^3$ tal que $f(x) = f_1(x)$ para todo $x \le \xi$, expressando $a_1, b_1, c_1, d_1$ em termos de $\beta_0, \dots, \beta_4$ e $\xi$.  
(b) Encontre um polinômio cúbico $f_2(x) = a_2 + b_2 x + c_2 x^2 + d_2 x^3$ tal que $f(x) = f_2(x)$ para todo $x > \xi$.  
(c) Prove algebricamente que $f_1(\xi) = f_2(\xi)$, $f_1'(\xi) = f_2'(\xi)$ e $f_1''(\xi) = f_2''(\xi)$, concluindo que $f(x)$ é um **spline cúbico** (suave até a 2ª derivada no nó $\xi$, com salto $\beta_4 \cdot 6$ apenas na 3ª derivada).
- **Dica:** Em (b), expanda $(x - \xi)^3 = x^3 - 3\xi x^2 + 3\xi^2 x - \xi^3$ pelo Binômio de Newton e agrupe as potências de $x$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Polinômio à esquerda ($x \le \xi$):**  
   Para $x \le \xi$, $(x - \xi)_+^3 = 0$, logo:
   $$f_1(x) = \beta_0 + \beta_1 x + \beta_2 x^2 + \beta_3 x^3 \implies \mathbf{a_1 = \beta_0,\;\; b_1 = \beta_1,\;\; c_1 = \beta_2,\;\; d_1 = \beta_3}.$$

2. **Item (b) — Polinômio à direita ($x > \xi$):**  
   Para $x > \xi$, $(x - \xi)_+^3 = (x - \xi)^3 = x^3 - 3\xi x^2 + 3\xi^2 x - \xi^3$. Substituindo em $f(x)$ e agrupando as potências de $x$:
   $$f_2(x) = (\beta_0 - \beta_4 \xi^3) + (\beta_1 + 3\beta_4 \xi^2)x + (\beta_2 - 3\beta_4 \xi)x^2 + (\beta_3 + \beta_4)x^3,$$
   donde:
   $$\mathbf{a_2 = \beta_0 - \beta_4\xi^3, \quad b_2 = \beta_1 + 3\beta_4\xi^2, \quad c_2 = \beta_2 - 3\beta_4\xi, \quad d_2 = \beta_3 + \beta_4}.$$

3. **Item (c) — Verificação da continuidade de $f$, $f'$ e $f''$ em $x = \xi$:**  
   Notando que $f_2(x) - f_1(x) = \beta_4(x - \xi)^3$, temos imediatamente:
   - **Continuidade de $f$ ($C^0$):**
     $$f_2(\xi) - f_1(\xi) = \beta_4(\xi - \xi)^3 = 0 \implies \mathbf{f_1(\xi) = f_2(\xi) = \beta_0 + \beta_1\xi + \beta_2\xi^2 + \beta_3\xi^3}.$$
   - **Continuidade da 1ª derivada $f'$ ($C^1$):**  
     Como $f_2'(x) - f_1'(x) = \frac{d}{dx}\big[\beta_4(x - \xi)^3\big] = 3\beta_4(x - \xi)^2$:
     $$f_2'(\xi) - f_1'(\xi) = 3\beta_4(\xi - \xi)^2 = 0 \implies \mathbf{f_1'(\xi) = f_2'(\xi) = \beta_1 + 2\beta_2\xi + 3\beta_3\xi^2}.$$
   - **Continuidade da 2ª derivada $f''$ ($C^2$):**  
     Como $f_2''(x) - f_1''(x) = 6\beta_4(x - \xi)$:
     $$f_2''(\xi) - f_1''(\xi) = 6\beta_4(\xi - \xi) = 0 \implies \mathbf{f_1''(\xi) = f_2''(\xi) = 2\beta_2 + 6\beta_3\xi}.$$
   Apenas a 3ª derivada sofre um salto de $f_2'''(\xi) - f_1'''(\xi) = 6\beta_4$, provando que $f(x)$ é um spline cúbico genuíno. $\blacksquare$
</details>

---

### Exercício B6.2 *[ISLP, Seção 7.9, Ex. 2 e Ex. 5 — Limites Assintóticos de Smoothing Splines Generalizadas]*
Considere uma curva $\hat{g}$ escolhida para minimizar o funcional de suavização generalizado de ordem $m$:
$$\hat{g} = \arg\min_{g} \left\{\sum_{i=1}^n \big(y_i - g(x_i)\big)^2 + \lambda \int \left[g^{(m)}(x)\right]^2 dx\right\},$$
onde $g^{(m)}$ denota a $m$-ésima derivada de $g$ ($g^{(0)} = g$).
(a) Determine a forma analítica exata da curva ótima $\hat{g}(x)$ nos seguintes casos extremos (Ex. 7.9.2):
   (i) $\lambda = \infty, \; m = 0$; $\quad$ (ii) $\lambda = \infty, \; m = 1$; $\quad$ (iii) $\lambda = \infty, \; m = 2$; $\quad$ (iv) $\lambda = \infty, \; m = 3$; $\quad$ (v) $\lambda = 0, \; m = 3$.  
(b) Considere duas curvas $\hat{g}_1$ (obtida com $m = 3$, penalidade $\int [g^{(3)}(x)]^2 dx$) e $\hat{g}_2$ (obtida com $m = 4$, penalidade $\int [g^{(4)}(x)]^2 dx$) para o mesmo $\lambda$. Qual delas terá menor RSS de treino se $\lambda \to \infty$? (Ex. 7.9.5)
- **Dica:** Para $\lambda \to \infty$, a integral de penalidade deve anular-se identicamente, forçando $g^{(m)}(x) = 0$ para todo $x$, o que implica que $\hat{g}(x)$ é um polinômio de grau no máximo $m - 1$ ajustado por mínimos quadrados ordinários.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Caracterização de $\hat{g}$ nos cinco regimes (Ex. 7.9.2):**  
   Quando $\lambda \to \infty$, qualquer função com $\int [g^{(m)}(x)]^2 dx > 0$ teria custo infinito, logo a solução fica restrita ao núcleo do operador diferencial $g^{(m)}(x) \equiv 0$, dentro do qual minimiza-se o $\operatorname{RSS} = \sum_{i=1}^n (y_i - g(x_i))^2$:
   - **(i) $\lambda = \infty, \; m = 0$:** A penalidade $\int [g(x)]^2 dx = 0$ força **$\hat{g}(x) \equiv 0$** (eixo horizontal constante em zero).
   - **(ii) $\lambda = \infty, \; m = 1$:** A penalidade $\int [g'(x)]^2 dx = 0$ força $g'(x) \equiv 0 \implies g(x) = c$ (constante). Minimizando $\sum (y_i - c)^2$, obtemos a **reta horizontal na média amostral $\hat{g}(x) = \bar{y}$**.
   - **(iii) $\lambda = \infty, \; m = 2$:** A penalidade $\int [g''(x)]^2 dx = 0$ força $g''(x) \equiv 0 \implies g(x) = \beta_0 + \beta_1 x$. Minimizando o RSS, $\hat{g}(x)$ é a **reta de regressão linear simples de Mínimos Quadrados Ordinários (OLS)**.
   - **(iv) $\lambda = \infty, \; m = 3$:** A penalidade $\int [g'''(x)]^2 dx = 0$ força $g'''(x) \equiv 0 \implies g(x) = \beta_0 + \beta_1 x + \beta_2 x^2$. Minimizando o RSS, $\hat{g}(x)$ é a **parábola de regressão polinomial quadrática OLS**.
   - **(v) $\lambda = 0, \; m = 3$:** Com $\lambda = 0$, a penalidade desaparece por completo e o problema reduz-se a minimizar $\sum (y_i - g(x_i))^2$: $\hat{g}(x)$ é qualquer **curva interpoladora** que passe exatamente por todos os pontos $(x_i, y_i)$, atingindo $\operatorname{RSS} = 0$ (no caso de $x_i$ distintos).

2. **Item (b) — Comparação entre $\hat{g}_1$ ($m=3$) e $\hat{g}_2$ ($m=4$) quando $\lambda \to \infty$ (Ex. 7.9.5):**  
   Quando $\lambda \to \infty$, $\hat{g}_1$ restringe-se a um polinômio de grau $m - 1 = 2$ (quadrático, $\beta_0 + \beta_1 x + \beta_2 x^2$), enquanto $\hat{g}_2$ restringe-se a um polinômio de grau $m - 1 = 3$ (cúbico, $\beta_0 + \beta_1 x + \beta_2 x^2 + \beta_3 x^3$). Como a família de polinômios cúbicos contém estritamente a família quadrática (basta tomar $\beta_3 = 0$), **$\hat{g}_2$ é mais flexível e terá menor (ou igual) RSS de treino** que $\hat{g}_1$, embora possa apresentar maior ou menor RSS de teste dependendo da verdadeira curvatura de $f$. $\blacksquare$
</details>

---

### Exercício B6.3 *[ISLP, Seção 7.9, Ex. 3, Ex. 4 e Ex. 11]*
(a) Suponha que ajustamos uma curva $Y = \beta_0 + \beta_1 b_1(X) + \beta_2 b_2(X) + \varepsilon$ com funções de base $b_1(X) = X$ e $b_2(X) = (X - 1)^2 \mathbb{I}(X \ge 1)$, obtendo $\hat{\beta}_0 = 1$, $\hat{\beta}_1 = 1$ e $\hat{\beta}_2 = -2$ (Ex. 7.9.3). Escreva a expressão explícita de $\hat{Y}(X)$ nos intervalos $X < 1$ e $X \ge 1$, determine o intercepto, a inclinação em $X < 1$ e o ponto de máximo global em $[-2, 2]$.  
(b) Descreva matematicamente o algoritmo de **Backfitting** para ajustar um Modelo Aditivo Generalizado (GAM) $Y_i = \beta_0 + f_1(x_{i1}) + f_2(x_{i2}) + \varepsilon_i$ e explique por que se impõe a restrição de centragem $\sum_{i=1}^n \hat{f}_j(x_{ij}) = 0$ em cada iteração (Ex. 7.9.11).
- **Dica:** Em (b), observe que em cada passo atualiza-se $\hat{f}_1$ suavizando o resíduo parcial $r_i^{(1)} = y_i - \hat{\beta}_0 - \hat{f}_2(x_{i2})$ contra $X_1$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Análise da curva por partes $\hat{Y}(X) = 1 + X - 2(X - 1)^2\mathbb{I}(X \ge 1)$ (Ex. 7.9.3):**
   - **Para $X < 1$:** Como $\mathbb{I}(X \ge 1) = 0$, a curva é a **reta afim**:
     $$\hat{Y}(X) = \mathbf{1 + X},$$
     com intercepto $\hat{Y}(0) = 1$, inclinação constante $+1$, valendo $\hat{Y}(-2) = -1$ e $\hat{Y}(1^-) = 2$.
   - **Para $X \ge 1$:** Como $\mathbb{I}(X \ge 1) = 1$, a curva é a **parábola côncava**:
     $$\hat{Y}(X) = 1 + X - 2(X - 1)^2 = \mathbf{-2X^2 + 5X - 1}.$$
     Em $X = 1$, temos $\hat{Y}(1) = 2$ e $\hat{Y}'(1^+) = -4(1) + 5 = +1 = \hat{Y}'(1^-)$, logo a curva e sua tangente são contínuas na transição $X = 1$! O ponto de máximo global ocorre onde $\hat{Y}'(X) = -4X + 5 = 0 \implies \mathbf{X^* = 1{,}25}$, com valor máximo $\hat{Y}(1{,}25) = 1 + 1{,}25 - 2(0{,}25)^2 = \mathbf{2{,}125}$, caindo depois até $\hat{Y}(2) = 1 + 2 - 2(1)^2 = 1$.

2. **Item (b) — Algoritmo de *Backfitting* em GAMs (Ex. 7.9.11):**  
   Para ajustar $Y_i = \beta_0 + f_1(x_{i1}) + f_2(x_{i2}) + \varepsilon_i$:
   1. **Inicialização:** Fixa-se $\hat{\beta}_0 = \bar{y} = \frac{1}{n}\sum_{i=1}^n y_i$ e $\hat{f}_1^{(0)} \equiv 0$, $\hat{f}_2^{(0)} \equiv 0$.
   2. **Ciclo Iterativo ($t = 1, 2, \dots$ até convergência):**
      - Fixando $\hat{f}_2^{(t-1)}$, calcula-se o resíduo parcial $r_i^{(1)} = y_i - \hat{\beta}_0 - \hat{f}_2^{(t-1)}(x_{i2})$, ajusta-se um suavizador univariado (ou regressão linear) $\tilde{f}_1$ de $r^{(1)}$ sobre $X_1$, e centra-se: $\hat{f}_1^{(t)}(x_{i1}) \leftarrow \tilde{f}_1(x_{i1}) - \frac{1}{n}\sum_{k=1}^n \tilde{f}_1(x_{k1})$.
      - Fixando $\hat{f}_1^{(t)}$, calcula-se o novo resíduo parcial $r_i^{(2)} = y_i - \hat{\beta}_0 - \hat{f}_1^{(t)}(x_{i1})$, ajusta-se $\tilde{f}_2$ sobre $X_2$, e centra-se: $\hat{f}_2^{(t)}(x_{i2}) \leftarrow \tilde{f}_2(x_{i2}) - \frac{1}{n}\sum_{k=1}^n \tilde{f}_2(x_{k2})$.
   - **Por que centrar $\sum_{i=1}^n \hat{f}_j(x_{ij}) = 0$?** Sem a restrição de média zero, as funções $f_1$ e $f_2$ não seriam identificáveis a menos de constantes aditivas, pois $(f_1 + c) + (f_2 - c) = f_1 + f_2$. A centragem garante identificabilidade única e fixa $\hat{\beta}_0 = \bar{y}$. $\blacksquare$
</details>

---

### Exercício B6.4 *[ISLP, Seção 7.4 — Contagem de Graus de Liberdade em Splines Cúbicos vs. Splines Cúbicos Naturais]*
Considere um spline cúbico com $K$ nós internos $\xi_1 < \xi_2 < \dots < \xi_K$ no domínio de $X$.
(a) Calcule o número total de graus de liberdade (parâmetros livres) partindo de $(K + 1)$ polinômios cúbicos distintos nos $(K + 1)$ subintervalos e subtraindo as restrições de continuidade impostas em cada nó $\xi_k$, e verifique que o resultado coincide com o tamanho da base de potência truncada $\{1, x, x^2, x^3, (x-\xi_1)_+^3, \dots, (x-\xi_K)_+^3\}$.  
(b) Um **Spline Cúbico Natural** impõe adicionalmente que a função seja linear (isto é, $f''(x) = f'''(x) = 0$) nas duas caudas externas $x < \xi_1$ e $x > \xi_K$. Quantos graus de liberdade são economizados e qual é a vantagem estatística nas bordas do domínio?
- **Dica:** Em (a), cada polinômio cúbico tem $4$ parâmetros e cada nó impõe $3$ equações lineares ($C^0, C^1, C^2$).

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Graus de Liberdade do Spline Cúbico ($K + 4$):**  
   Com $K$ nós internos, o eixo real é dividido em $K + 1$ regiões. Um polinômio cúbico irrestrito $a_r + b_r x + c_r x^2 + d_r x^3$ em cada região requer $4(K + 1) = 4K + 4$ parâmetros.  
   Em cada um dos $K$ nós internos $\xi_k$, impomos $3$ restrições lineares independentes: continuidade de $f(\xi_k)$, de $f'(\xi_k)$ e de $f''(\xi_k)$, totalizando $3K$ restrições. Logo, o número de parâmetros livres (graus de liberdade) é:
   $$\operatorname{df}_{\text{cúbico}} = 4(K + 1) - 3K = \mathbf{K + 4},$$
   o que coincide exatamente com os $4$ termos polinomiais globais $\{1, x, x^2, x^3\}$ mais as $K$ funções de base truncadas $\{(x - \xi_k)_+^3\}_{k=1}^K$!
2. **Item (b) — Graus de Liberdade do Spline Cúbico Natural ($K$):**  
   Exigir linearidade para $x < \xi_1$ anula os coeficientes quadrático e cúbico na região extrema esquerda ($2$ restrições: $f''(\xi_1) = 0$ e $f'''(\xi_1^-) = 0$), e exigir linearidade para $x > \xi_K$ impõe mais $2$ restrições na região extrema direita ($f''(\xi_K) = 0$ e $f'''(\xi_K^+) = 0$). Economizam-se $4$ graus de liberdade:
   $$\operatorname{df}_{\text{natural}} = (K + 4) - 4 = \mathbf{K\text{ graus de liberdade}}$$
   (contando o intercepto). Isso elimina as oscilações erráticas de alta variância (*Runge's phenomenon*) que polinômios de grau $3$ exibem perto das fronteiras amostrais. $\blacksquare$
</details>

---

<a id="bloco-7"></a>
## Bloco 7 — Árvores de Decisão, Impureza de Gini/Entropia, Bagging, Random Forests e Boosting (Capítulo 8 + Raschka Cap. 7)

### Exercício B7.1 *[ISLP, Seção 8.4, Ex. 2 — Demonstração de que Boosting com Stumps Gera um Modelo Aditivo]*
Afirma-se na Seção 8.2.3 que o algoritmo de *Gradient Boosting* utilizando árvores de profundidade $d = 1$ (*decision stumps* — árvores com apenas uma divisão e duas folhas) produz um **modelo aditivo** da forma $f(X) = \sum_{j=1}^p f_j(X_j)$, sem termos de interação entre variáveis distintas. Prove essa afirmação matematicamente passo a passo.
- **Dica:** Escreva a expressão explícita de um *stump* $T_b(X)$ que divide em uma única variável $X_{j_b}$ no ponto de corte $s_b$, some $\hat{f}(X) = \sum_{b=1}^B \lambda \hat{f}^b(X)$ e agrupe os termos pelo índice da variável $j \in \{1, \dots, p\}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. Uma árvore de profundidade $d = 1$ (*stump*) na $b$-ésima iteração do Boosting faz uma única divisão em **uma única variável preditora** $X_{j_b}$ (onde $j_b \in \{1, \dots, p\}$) em um ponto de corte $s_b \in \mathbb{R}$:
   $$\hat{f}^b(X) = c_{b,1}\,\mathbb{I}(X_{j_b} < s_b) + c_{b,2}\,\mathbb{I}(X_{j_b} \ge s_b).$$
   Note que $\hat{f}^b(X)$ é uma função que depende **exclusivamente** da coordenada $X_{j_b}$, isto é, $\hat{f}^b(X) = g_b(X_{j_b})$.
2. No algoritmo de Boosting para regressão (Algoritmo 8.2 do ISLP), inicializamos $\hat{f}(X) = 0$ e, a cada passo $b = 1, \dots, B$, ajustamos um *stump* $\hat{f}^b$ aos resíduos correntes $r_i = y_i - \hat{f}(x_i)$ e atualizamos $\hat{f}(X) \leftarrow \hat{f}(X) + \lambda\hat{f}^b(X)$. Ao final das $B$ iterações:
   $$\hat{f}(X) = \sum_{b=1}^B \lambda\,\hat{f}^b(X) = \sum_{b=1}^B \lambda\,g_b(X_{j_b}).$$
3. Particionando o conjunto de índices de iteração $\{1, 2, \dots, B\}$ de acordo com qual variável $j \in \{1, \dots, p\}$ foi escolhida no corte $j_b = j$:
   $$\hat{f}(X) = \sum_{j=1}^p \underbrace{\left(\sum_{b \,:\, j_b = j} \lambda\,\big[c_{b,1}\mathbb{I}(X_j < s_b) + c_{b,2}\mathbb{I}(X_j \ge s_b)\big]\right)}_{f_j(X_j)} = \mathbf{\sum_{j=1}^p f_j(X_j)}.$$
4. Cada componente $f_j(X_j)$ é uma função escada univariada na variável $X_j$, e não há nenhum termo que multiplique $X_j$ e $X_k$ ($j \neq k$). Portanto, Boosting com $d = 1$ estima um **Modelo Aditivo Generalizado (GAM) não paramétrico por funções escada**! (Para capturar interações de ordem até $d$, é necessário usar árvores com $d$ divisões). $\blacksquare$
</details>

---

### Exercício B7.2 *[ISLP, Seção 8.4, Ex. 3 — Comparação Analítica entre Erro de Classificação, Gini e Entropia]*
Considere um problema de classificação binária ($K = 2$ classes) em um nó $m$ de uma árvore de decisão, onde $\hat{p}_{m1} = p \in [0, 1]$ é a proporção de observações da classe 1 e $\hat{p}_{m2} = 1 - p$ é a proporção da classe 2.
(a) Escreva, em função de $p \in [0, 1]$, as três medidas clássicas de impureza de nó: o **Erro de Classificação** $E(p)$, o **Índice de Gini** $G(p)$ e a **Entropia Cruzada** $D(p)$ (reescalonada na base 2 ou dividindo por $\ln 2$ para que todas atinjam o mesmo máximo ou compare seus máximos).  
(b) Calcule as derivadas primeira e segunda $G'(p), G''(p)$ e $D'(p), D''(p)$, e explique rigorosamente por que o Índice de Gini e a Entropia são preferíveis ao Erro de Classificação $E(p)$ durante o crescimento da árvore (*tree growing*).
- **Dica:** Verifique que $E(p) = 1 - \max(p, 1-p) = \min(p, 1-p)$ é linear por partes ($E''(p) = 0$ para $p \neq 0{,}5$), tornando-o insensível a ganhos de pureza quando ambos os nós filhos permanecem com a mesma classe majoritária!

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Expressões analíticas em função de $p \in [0, 1]$:**
   - **Erro de Classificação:** $E(p) = 1 - \max(p, 1 - p) = \min(p, 1 - p)$, que vale $0$ em $p \in \{0, 1\}$ e atinge máximo $E(0{,}5) = 0{,}5$.
   - **Índice de Gini:** $G(p) = p(1 - p) + (1 - p)p = \mathbf{2p(1 - p) = 2p - 2p^2}$, que vale $0$ em $p \in \{0, 1\}$ e atinge máximo $G(0{,}5) = 0{,}5$.
   - **Entropia (em nats / bits):** $D(p) = -p\ln p - (1 - p)\ln(1 - p)$ (com máximo $\ln 2 \approx 0{,}693$ em $p = 0{,}5$, ou $D_{\text{escalada}}(p) = \frac{D(p)}{2\ln 2}$ para ter máximo $0{,}5$).

2. **Item (b) — Estrita Concavidade ($G'' < 0, D'' < 0$) vs. Linearidade de $E(p)$:**  
   Calculando as segundas derivadas em $(0, 1)$:
   $$G'(p) = 2 - 4p \implies \mathbf{G''(p) = -4 < 0}; \qquad D'(p) = \ln\!\left(\frac{1 - p}{p}\right) \implies \mathbf{D''(p) = -\frac{1}{p(1 - p)} < 0}.$$
   Como $G(p)$ e $D(p)$ são **estritamente côncavas**, pela Desigualdade de Jensen qualquer divisão que separe um nó pai com proporção $p = \frac{n_L}{n}p_L + \frac{n_R}{n}p_R$ em dois nós filhos com $p_L \neq p_R$ reduz estritamente a impureza ponderada:
   $$\frac{n_L}{n}G(p_L) + \frac{n_R}{n}G(p_R) < G(p).$$
   Em contraste, $E(p) = \min(p, 1-p)$ é **linear** em $[0, 0{,}5]$ e em $[0{,}5, 1]$. Se um nó com $p = 0{,}3$ (400 observações) for dividido em dois filhos com $p_L = 0{,}1$ (200 obs., quase puro!) e $p_R = 0{,}5$ (200 obs.), o erro de classificação ponderado antes e depois é **idêntico**: $\frac{1}{2}(0{,}1) + \frac{1}{2}(0{,}5) = 0{,}30 = E(0{,}3)$ ($\Delta E = 0$!). Já o Gini cai de $G(0{,}3) = 0{,}42$ para $\frac{1}{2}(0{,}18) + \frac{1}{2}(0{,}50) = 0{,}34$ ($\Delta G = 0{,}08 > 0$), recompensando a criação do nó puro $p_L = 0{,}1$. Por isso, Gini e Entropia são usados para crescer a árvore, e $E(p)$ é usado na poda (*cost-complexity pruning*) quando o objetivo final é acurácia. $\blacksquare$
</details>

---

### Exercício B7.3 *[ISLP, Seção 8.4, Ex. 5 e Complemento — Raschka et al., Cap. 7]*
Suponha que geramos $B = 10$ amostras de *bootstrap* a partir de um conjunto de dados e ajustamos uma árvore de classificação em cada amostra. Para uma observação de teste $X$, as 10 estimativas de $\Pr(\text{Classe} = \text{Vermelho} \mid X)$ são:
$$\{0{,}1;\; 0{,}15;\; 0{,}2;\; 0{,}2;\; 0{,}55;\; 0{,}6;\; 0{,}6;\; 0{,}65;\; 0{,}7;\; 0{,}75\}.$$
(a) Qual é a classe predita para $X$ sob a abordagem de **Voto Majoritário (*Majority Vote*)** e sob a abordagem de **Probabilidade Média (*Average Probability*)**? Por que elas divergem aqui? (Ex. 8.4.5)  
(b) **[Complemento — Raschka et al., Cap. 7]** Considere um *ensemble* de $M = 11$ classificadores binários independentes, cada um com taxa de erro individual $\varepsilon = 0{,}25$. Calcule a probabilidade exata de erro do *ensemble* por voto majoritário $\varepsilon_{\text{ensemble}} = \sum_{k=6}^{11} \binom{11}{k}\varepsilon^k(1-\varepsilon)^{11-k}$.  
(c) **[Complemento — Raschka et al., Cap. 7]** No algoritmo **AdaBoost**, mostre que quando a taxa de erro ponderada do classificador fraco $j$ é $\varepsilon_j \in (0, 0{,}5)$, o peso do classificador $\alpha_j = \frac{1}{2}\ln\!\left(\frac{1 - \varepsilon_j}{\varepsilon_j}\right)$ é estritamente positivo, e determine o fator pelo qual os pesos das amostras classificadas incorretamente vs. corretamente são multiplicados antes da normalização.
- **Dica:** Em (a), conte quantas probabilidades excedem $0{,}50$ e depois calcule a média aritmética das 10 probabilidades.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Voto Majoritário vs. Probabilidade Média no Bagging (Ex. 8.4.5):**
   - **Voto Majoritário (*Hard Voting*):** Das 10 árvores, **6 árvores** preveem probabilidade $> 0{,}5$ ($\{0{,}55;\; 0{,}6;\; 0{,}6;\; 0{,}65;\; 0{,}7;\; 0{,}75\} \to \text{Vermelho}$) e apenas **4 árvores** preveem $< 0{,}5$ ($\{0{,}1;\; 0{,}15;\; 0{,}2;\; 0{,}2\} \to \text{Verde}$). Pelo voto majoritário ($6 \times 4$), a predição é **Vermelho**.
   - **Probabilidade Média (*Soft Voting*):** A média aritmética das 10 probabilidades estimadas é:
     $$\bar{p} = \frac{0{,}1 + 0{,}15 + 0{,}2 + 0{,}2 + 0{,}55 + 0{,}6 + 0{,}6 + 0{,}65 + 0{,}7 + 0{,}75}{10} = \frac{4{,}50}{10} = \mathbf{0{,}45 < 0{,}50}.$$
     Portanto, pela probabilidade média, a predição é **Verde**! Elas divergem porque as 4 árvores que votam Verde têm altíssima confiança ($\hat{p} \in [0{,}1; 0{,}2]$), enquanto as 6 árvores que votam Vermelho estão próximas da fronteira de incerteza ($\hat{p} \in [0{,}55; 0{,}75]$); o *soft voting* preserva essa informação de calibração.

2. **Item (b) — Erro Binomial do Ensemble (Raschka Cap. 7):**  
   Com $M = 11$ e $\varepsilon = 0{,}25$, o *ensemble* erra se e somente se pelo menos $6$ dos $11$ classificadores errarem simultaneamente:
   $$\varepsilon_{\text{ensemble}} = \sum_{k=6}^{11} \binom{11}{k}(0{,}25)^k(0{,}75)^{11-k} \approx 0{,}02677 + 0{,}00637 + 0{,}00106 + 0{,}00012 + 0{,}00001 + 0{,}00000 = \mathbf{0{,}0343 \;\; (3{,}43\%)},$$
   uma redução superior a $7$ vezes em relação ao erro individual de $25\%$!

3. **Item (c) — Pesos do AdaBoost (Raschka Cap. 7):**  
   Para $\varepsilon_j \in (0, 0{,}5)$, temos $1 - \varepsilon_j > \varepsilon_j \implies \frac{1 - \varepsilon_j}{\varepsilon_j} > 1 \implies \alpha_j = \frac{1}{2}\ln\!\left(\frac{1-\varepsilon_j}{\varepsilon_j}\right) > 0$.  
   Na atualização $w_i^{(j+1)} \propto w_i^{(j)}\exp(-\alpha_j y_i \hat{y}_{ij})$ com $y_i, \hat{y}_{ij} \in \{-1, +1\}$:
   - Se a amostra $i$ foi **errada** ($y_i \hat{y}_{ij} = -1$): seu peso é multiplicado por $e^{+\alpha_j} = \mathbf{\sqrt{\frac{1 - \varepsilon_j}{\varepsilon_j}} > 1}$ (amplificado);
   - Se a amostra $i$ foi **acertada** ($y_i \hat{y}_{ij} = +1$): seu peso é multiplicado por $e^{-\alpha_j} = \mathbf{\sqrt{\frac{\varepsilon_j}{1 - \varepsilon_j}} < 1}$ (reduzido). $\blacksquare$
</details>

---

### Exercício B7.4 *[ISLP, Seção 8.4, Ex. 4 — Dualidade entre Árvore de Decisão e Partição Retangular de $\mathbb{R}^2$]*
Considere uma árvore de regressão no plano $(X_1, X_2)$ definida pela seguinte estrutura hierárquica de cortes binários:
- **Raiz:** Testa $X_1 < 1$.
  - **Ramo Direito ($X_1 \ge 1$):** Testa $X_2 < 1$.
    - Se $X_2 < 1$: folha com predição $\mathbf{5}$.
    - Se $X_2 \ge 1$: folha com predição $\mathbf{15}$.
  - **Ramo Esquerdo ($X_1 < 1$):** Testa $X_2 < 2$.
    - Se $X_2 \ge 2$: testa $X_1 < 0$.
      - Se $X_1 < 0$: folha com predição $\mathbf{3}$.
      - Se $X_1 \ge 0$: folha com predição $\mathbf{10}$.
    - Se $X_2 < 2$: folha com predição $\mathbf{0}$.

Descreva algebricamente os 5 retângulos disjuntos $R_1, \dots, R_5$ que particionam o plano $(X_1, X_2)$ e escreva a função preditiva $\hat{f}(X_1, X_2) = \sum_{m=1}^5 \hat{c}_m\,\mathbb{I}((X_1, X_2) \in R_m)$.
- **Dica:** Percorra cada caminho da raiz até cada uma das 5 folhas intersectando as inequações de $X_1$ e $X_2$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. Percorrendo cada caminho da raiz até as 5 folhas terminais, obtemos os 5 retângulos alinhados aos eixos que particionam $\mathbb{R}^2$:
   - **$R_1$ (Predição $\hat{c}_1 = 0$):** Caminho $(X_1 < 1) \land (X_2 < 2) \implies \mathbf{R_1 = (-\infty, 1) \times (-\infty, 2)}$.
   - **$R_2$ (Predição $\hat{c}_2 = 3$):** Caminho $(X_1 < 1) \land (X_2 \ge 2) \land (X_1 < 0) \implies \mathbf{R_2 = (-\infty, 0) \times [2, +\infty)}$.
   - **$R_3$ (Predição $\hat{c}_3 = 10$):** Caminho $(X_1 < 1) \land (X_2 \ge 2) \land (X_1 \ge 0) \implies \mathbf{R_3 = [0, 1) \times [2, +\infty)}$.
   - **$R_4$ (Predição $\hat{c}_4 = 5$):** Caminho $(X_1 \ge 1) \land (X_2 < 1) \implies \mathbf{R_4 = [1, +\infty) \times (-\infty, 1)}$.
   - **$R_5$ (Predição $\hat{c}_5 = 15$):** Caminho $(X_1 \ge 1) \land (X_2 \ge 1) \implies \mathbf{R_5 = [1, +\infty) \times [1, +\infty)}$.
2. A função constante por partes representada pela árvore é:
   $$\mathbf{\hat{f}(X_1, X_2) = 0\cdot\mathbb{I}_{R_1} + 3\cdot\mathbb{I}_{R_2} + 10\cdot\mathbb{I}_{R_3} + 5\cdot\mathbb{I}_{R_4} + 15\cdot\mathbb{I}_{R_5}}. \quad \blacksquare$$
</details>

---

<a id="bloco-8"></a>
## Bloco 8 — Máquinas de Vetores de Suporte (SVM), Margem Máxima, Kernels e *Hinge Loss* (Capítulo 9)

### Exercício B8.1 *[ISLP, Seção 9.7, Ex. 1 e Ex. 2 — Fronteiras Afins e Imersão Quadrática]*
Considere a curva de fronteira não linear no plano $(X_1, X_2) \in \mathbb{R}^2$ definida por:
$$(1 + X_1)^2 + (2 - X_2)^2 = 4.$$
(a) Identifique geometricamente essa curva e classifique os pontos $(0, 0)$, $(-1, 1)$, $(2, 2)$ e $(3, 8)$ sabendo que o classificador atribui a classe **Azul** se $(1 + X_1)^2 + (2 - X_2)^2 > 4$ e **Vermelho** se $\le 4$.  
(b) Prove que essa fronteira de decisão não linear em $\mathbb{R}^2$ torna-se um **hiperplano linear (afim)** quando imersa no espaço de características expandido de dimensão $4$, $\Phi(X_1, X_2) = (X_1, X_1^2, X_2, X_2^2)^T \in \mathbb{R}^4$, explicitando os coeficientes $\beta_0, \beta_1, \beta_2, \beta_3, \beta_4$.
- **Dica:** Em (a), compare com a equação da circunferência $(X_1 - a)^2 + (X_2 - b)^2 = R^2$. Em (b), desenvolva os quadrados de $(1 + X_1)^2 + (2 - X_2)^2 - 4 = 0$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Geometria e Classificação dos 4 pontos:**  
   Escrevendo $(X_1 - (-1))^2 + (X_2 - 2)^2 = 2^2$, vemos que a fronteira é uma **circunferência de centro $C = (-1, 2)$ e raio $R = 2$**. O interior e a borda ($\le 4$) pertencem à classe **Vermelho** e o exterior ($> 4$) à classe **Azul**:
   - Para $(0, 0)$: $(1 + 0)^2 + (2 - 0)^2 = 1 + 4 = 5 > 4 \implies \mathbf{\text{Azul}}$;
   - Para $(-1, 1)$: $(1 - 1)^2 + (2 - 1)^2 = 0 + 1 = 1 \le 4 \implies \mathbf{\text{Vermelho}}$;
   - Para $(2, 2)$: $(1 + 2)^2 + (2 - 2)^2 = 9 + 0 = 9 > 4 \implies \mathbf{\text{Azul}}$;
   - Para $(3, 8)$: $(1 + 3)^2 + (2 - 8)^2 = 16 + 36 = 52 > 4 \implies \mathbf{\text{Azul}}$.

2. **Item (b) — Linearidade no Espaço de Características Expandido:**  
   Expandindo $(1 + X_1)^2 + (2 - X_2)^2 - 4 = 0$:
   $$(1 + 2X_1 + X_1^2) + (4 - 4X_2 + X_2^2) - 4 = 0 \iff \mathbf{1 + 2X_1 + 1\cdot X_1^2 - 4X_2 + 1\cdot X_2^2 = 0}.$$
   Definindo $Z_1 = X_1$, $Z_2 = X_1^2$, $Z_3 = X_2$ e $Z_4 = X_2^2$, a equação é o hiperplano linear:
   $$\beta_0 + \beta_1 Z_1 + \beta_2 Z_2 + \beta_3 Z_3 + \beta_4 Z_4 = 0, \quad \text{com } \mathbf{(\beta_0, \beta_1, \beta_2, \beta_3, \beta_4) = (1, 2, 1, -4, 1)}. \quad \blacksquare$$
</details>

---

### Exercício B8.2 *[ISLP, Seção 9.7, Ex. 3 — Cálculo Analítico Completo do Classificador de Margem Máxima]*
Considere um conjunto de treinamento em $p = 2$ dimensões com $n = 7$ observações:

| Obs. $i$ | $X_1$ | $X_2$ | Classe $Y$ |
| :---: | :---: | :---: | :---: |
| 1 | $3$ | $4$ | Vermelho ($-1$) |
| 2 | $2$ | $2$ | Vermelho ($-1$) |
| 3 | $4$ | $4$ | Vermelho ($-1$) |
| 4 | $1$ | $4$ | Vermelho ($-1$) |
| 5 | $2$ | $1$ | Azul ($+1$) |
| 6 | $4$ | $3$ | Azul ($+1$) |
| 7 | $4$ | $1$ | Azul ($+1$) |

(a) Encontre a equação exata do **hiperplano separador de margem máxima** na forma $\beta_0 + \beta_1 X_1 + \beta_2 X_2 = 0$ (normalizado com $\|\beta\|_2 = 1$).  
(b) Calcule a **margem máxima $M$**, indique as equações das linhas tracejadas da margem e identifique todos os **vetores de suporte**.  
(c) Explique por que mover a 7ª observação $(4, 1)$ não altera o hiperplano ótimo, e dê o exemplo de um hiperplano separador que **não** é o de margem máxima.
- **Dica:** Observe os pares mais próximos entre as duas classes: $(2,2), (4,4)$ na classe Vermelho e $(2,1), (4,3)$ na classe Azul. Ambos formam segmentos paralelos de inclinação $+1$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Equação do Hiperplano de Margem Máxima:**  
   Inspecionando a fronteira convexa das duas classes:
   - Na classe Vermelho ($Y = -1$), os pontos mais próximos da classe Azul são **Obs. 2 $(2, 2)$** e **Obs. 3 $(4, 4)$**, que jazem sobre a reta $X_2 = X_1 \iff X_1 - X_2 = 0$.
   - Na classe Azul ($Y = +1$), os pontos mais próximos da classe Vermelho são **Obs. 5 $(2, 1)$** e **Obs. 6 $(4, 3)$**, que jazem sobre a reta paralela $X_2 = X_1 - 1 \iff X_1 - X_2 - 1 = 0$.
   O hiperplano separador de margem máxima é a reta equidistante a essas duas retas paralelas:
   $$X_2 = X_1 - 0{,}5 \iff X_1 - X_2 - 0{,}5 = 0.$$
   Normalizando pelo comprimento do vetor normal $\|(1, -1)\|_2 = \sqrt{1^2 + (-1)^2} = \sqrt{2}$, obtemos os coeficientes normalizados ($\beta_1^2 + \beta_2^2 = 1$):
   $$\mathbf{-\frac{1}{2\sqrt{2}} + \frac{1}{\sqrt{2}}X_1 - \frac{1}{\sqrt{2}}X_2 = 0 \quad \left(\beta_0 = -\frac{\sqrt{2}}{4},\;\; \beta_1 = \frac{\sqrt{2}}{2},\;\; \beta_2 = -\frac{\sqrt{2}}{2}\right)}.$$
   A regra de decisão classifica como **Azul ($+1$)** se $-0{,}5 + X_1 - X_2 > 0$ e **Vermelho ($-1$)** se $-0{,}5 + X_1 - X_2 < 0$.

2. **Item (b) — Margem $M$ e Vetores de Suporte:**  
   A distância perpendicular do hiperplano $X_1 - X_2 - 0{,}5 = 0$ até qualquer um dos quatro pontos de fronteira — por exemplo, $(2, 2)$ — é a margem máxima:
   $$M = \frac{|1(2) - 1(2) - 0{,}5|}{\sqrt{1^2 + (-1)^2}} = \frac{0{,}5}{\sqrt{2}} = \mathbf{\frac{\sqrt{2}}{4} \approx 0{,}3536}.$$
   As retas das margens são $X_1 - X_2 = 0$ (margem superior/Vermelho) e $X_1 - X_2 - 1 = 0$ (margem inferior/Azul). Os **4 vetores de suporte** são exatamente os pontos sobre essas margens:
   $$\mathbf{\text{Obs. 2 } (2, 2), \quad \text{Obs. 3 } (4, 4), \quad \text{Obs. 5 } (2, 1), \quad \text{Obs. 6 } (4, 3)}.$$

3. **Item (c) — Propriedade de Esparsidade dos Vetores de Suporte:**  
   A **Obs. 7 $(4, 1)$** está estritamente além da margem de sua classe ($4 - 1 - 0{,}5 = 2{,}5 > 0{,}5$, logo não é vetor de suporte, tendo multiplicador dual $\alpha_7 = 0$). Pela propriedade fundamental das SVMs, o hiperplano ótimo depende **apenas** dos vetores de suporte; portanto, um leve deslocamento de $(4,1)$ não altera em nada o hiperplano!  
   Um exemplo de hiperplano que separa perfeitamente os dados mas **não** tem margem máxima é $X_1 - X_2 - 0{,}2 = 0$ (ou $0{,}9X_1 - X_2 - 0{,}3 = 0$). $\blacksquare$
</details>

---

### Exercício B8.3 *[ISLP, Seção 9.5 — Equivalência entre Support Vector Classifier e Hinge Loss $+\,\ell_2$]*
Prove que o problema de otimização do **Classificador de Vetores de Suporte (*Soft-Margin SVM*)** com variáveis de folga $\epsilon_i \ge 0$:
$$\min_{\beta_0, \tilde{\beta}, \epsilon} \frac{1}{2}\|\tilde{\beta}\|_2^2 + C \sum_{i=1}^n \epsilon_i \quad \text{sujeito a } y_i(\beta_0 + x_i^T\tilde{\beta}) \ge 1 - \epsilon_i, \;\; \epsilon_i \ge 0,$$
é matematicamente equivalente ao problema de regularização sem restrições com a perda **Hinge Loss**:
$$\min_{\beta_0, \tilde{\beta}} \sum_{i=1}^n \max\!\big(0,\; 1 - y_i(\beta_0 + x_i^T\tilde{\beta})\big) + \lambda \sum_{j=1}^p \tilde{\beta}_j^2, \quad \text{onde } \lambda = \frac{1}{2C}.$$
- **Dica:** Na formulação canônica com $C > 0$, para qualquer $(\beta_0, \tilde{\beta})$ fixado, determine o menor valor admissível de $\epsilon_i$ que satisfaz simultaneamente $\epsilon_i \ge 1 - y_i(\beta_0 + x_i^T\tilde{\beta})$ e $\epsilon_i \ge 0$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. Na formulação canônica de margem suave (onde reescalonamos o vetor normal como $\tilde{\beta} = \beta / M$, de modo que a margem geométrica é $M = 1/\|\tilde{\beta}\|_2$), as duas restrições sobre cada variável de folga $\epsilon_i$ são:
   $$\epsilon_i \ge 1 - y_i(\beta_0 + x_i^T\tilde{\beta}) \quad \text{e} \quad \epsilon_i \ge 0.$$
2. Como $C > 0$ e queremos **minimizar** $\frac{1}{2}\|\tilde{\beta}\|_2^2 + C\sum_{i=1}^n \epsilon_i$, para qualquer escolha fixa de $(\beta_0, \tilde{\beta})$, cada $\epsilon_i$ ótimo assumirá exatamente o menor valor não negativo compatível com a desigualdade:
   $$\epsilon_i^* = \max\!\big(0,\; 1 - y_i(\beta_0 + x_i^T\tilde{\beta})\big).$$
3. Substituindo $\epsilon_i^*$ na função objetivo e multiplicando toda a expressão pela constante positiva $\frac{1}{C} > 0$ (o que não altera o minimizador $(\hat{\beta}_0, \hat{\tilde{\beta}})$):
   $$\min_{\beta_0, \tilde{\beta}} \left\{\sum_{i=1}^n \max\!\big(0,\; 1 - y_i(\beta_0 + x_i^T\tilde{\beta})\big) + \frac{1}{2C}\|\tilde{\beta}\|_2^2\right\}.$$
4. Identificando $\lambda = \frac{1}{2C}$, concluímos a equivalência exata:
   - **$\lambda$ grande ($C$ pequeno):** forte penalização $\ell_2$, priorizando margem larga $M$ mesmo que mais pontos violem a margem (menor variância, maior viés);
   - **$\lambda$ pequeno ($C$ grande):** fraca penalização $\ell_2$, estreitando a margem para reduzir as violações $\epsilon_i$ (maior variância, menor viés). $\blacksquare$
</details>

---

### Exercício B8.4 *[ISLP, Seção 9.3.2 — O Truque do Kernel Polinomial e Radial (RBF) em SVMs]*
Considere a representação dual do classificador SVM: $f(x) = \beta_0 + \sum_{i \in \mathcal{S}} \alpha_i y_i K(x, x_i)$, onde $\mathcal{S} = \{i : \alpha_i > 0\}$ é o conjunto dos vetores de suporte.
(a) Para $p = 2$ e grau $d = 2$, expanda algebricamente o kernel polinomial $K(x, x') = (1 + x_1 x_1' + x_2 x_2')^2$ e explicite o mapa de características $\Phi: \mathbb{R}^2 \to \mathbb{R}^6$ tal que $K(x, x') = \langle \Phi(x), \Phi(x') \rangle$.  
(b) Para o **Kernel Radial (RBF)** $K(x, x') = \exp(-\gamma \|x - x'\|_2^2)$, mostre usando a expansão em série de Taylor de $e^{\,2\gamma \langle x, x' \rangle}$ que o espaço de características associado tem **dimensão infinita**, e explique o efeito geométrico de $\gamma$ muito grande sobre a fronteira de decisão.
- **Dica:** Em (b), escreva $\|x - x'\|_2^2 = \|x\|_2^2 + \|x'\|_2^2 - 2\langle x, x' \rangle$ e use $e^u = \sum_{k=0}^\infty \frac{u^k}{k!}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Mapa de Características Explícito do Kernel Polinomial Quadrático ($p=2, d=2$):**  
   Expandindo o quadrado do trinômio:
   $$K(x, x') = (1 + x_1 x_1' + x_2 x_2')^2 = 1 + 2x_1 x_1' + 2x_2 x_2' + x_1^2 (x_1')^2 + x_2^2 (x_2')^2 + 2x_1 x_2 x_1' x_2'.$$
   Isso é exatamente o produto interno canônico $\langle \Phi(x), \Phi(x') \rangle$ em $\mathbb{R}^6$ com o mapa de imersão:
   $$\mathbf{\Phi(x) = \big(1,\; \sqrt{2}\,x_1,\; \sqrt{2}\,x_2,\; x_1^2,\; x_2^2,\; \sqrt{2}\,x_1 x_2\big)^T \in \mathbb{R}^6}.$$
   Para $p$ e $d$ gerais, o espaço expandido tem dimensão $\binom{p+d}{d}$, mas avaliar $K(x, x') = (1 + x^T x')^d$ custa apenas $\mathcal{O}(p)$ operações!

2. **Item (b) — Dimensão Infinita do Kernel RBF e Papel de $\gamma$:**  
   Fatorando $K(x, x') = \exp(-\gamma\|x - x'\|_2^2)$ e expandindo em série de Taylor:
   $$K(x, x') = e^{-\gamma\|x\|_2^2}\,e^{-\gamma\|x'\|_2^2}\,\exp(2\gamma\langle x, x' \rangle) = e^{-\gamma\|x\|_2^2}\,e^{-\gamma\|x'\|_2^2}\sum_{k=0}^\infty \frac{(2\gamma)^k}{k!}\langle x, x' \rangle^k.$$
   Como a série contém todas as potências inteiras $k = 0, 1, 2, \dots, \infty$ de $\langle x, x' \rangle$, o mapa de características $\Phi(x) \in \ell^2(\mathbb{N})$ vive em um espaço de Hilbert de **dimensão infinita**. Quando $\gamma$ é muito grande, $\exp(-\gamma\|x - x_i\|_2^2)$ decai quase instantaneamente para zero fora de uma vizinhança minúscula de cada vetor de suporte $x_i$, criando "ilhas" isoladas de decisão ao redor dos pontos de treino (*overfitting* severo). $\blacksquare$
</details>

---

<a id="bloco-9"></a>
## Bloco 9 — Deep Learning: MLPs, CNNs, Otimização não Convexa, Self-Attention, GANs e Q-Learning (Capítulo 10 + Raschka Cap. 11–19)

### Exercício B9.1 *[ISLP, Seção 10.10, Ex. 1, Ex. 2 e Ex. 3]*
(a) Considere uma rede neural *feedforward* (MLP) para regressão com $p = 4$ variáveis de entrada, duas camadas ocultas contendo $K_1 = 2$ e $K_2 = 3$ unidades ocultas respectivamente (todas com função de ativação $\text{ReLU}(z) = \max(0, z)$), e 1 unidade de saída linear. Escreva a expressão funcional completa de $f(X)$ e calcule o **número total de parâmetros treináveis** (pesos + *biases*) (Ex. 10.10.1).  
(b) Mostre que a função **Softmax** $f_m(X) = \frac{e^{Z_m}}{\sum_{\ell=0}^9 e^{Z_\ell}}$ é invariante à adição de qualquer constante $c \in \mathbb{R}$ a todos os *logits* ($Z_\ell \mapsto Z_\ell + c$) (Ex. 10.10.2), e prove que a log-verossimilhança multinomial negativa $-\sum_{i=1}^n \sum_{m=0}^1 y_{im}\ln f_m(x_i)$ para $M = 2$ classes é equivalente à perda de entropia cruzada binária da regressão logística (Ex. 10.10.3).
- **Dica:** Em (a), lembre que uma camada densa com $d_{\text{in}}$ entradas e $d_{\text{out}}$ saídas possui $(d_{\text{in}} + 1) \times d_{\text{out}}$ parâmetros (incluindo o *bias* de cada neurônio).

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Equações e Contagem de Parâmetros da MLP $(4 \to 2 \to 3 \to 1)$ (Ex. 10.10.1):**
   - **1ª Camada Oculta ($k = 1, 2$):**
     $$A_k^{(1)} = \operatorname{ReLU}\!\left(w_{k0}^{(1)} + \sum_{j=1}^4 w_{kj}^{(1)} X_j\right) = \max\!\left(0,\; w_{k0}^{(1)} + \sum_{j=1}^4 w_{kj}^{(1)} X_j\right).$$
     Número de parâmetros da camada 1: $(4 + 1) \times 2 = \mathbf{10}$.
   - **2ª Camada Oculta ($\ell = 1, 2, 3$):**
     $$A_\ell^{(2)} = \operatorname{ReLU}\!\left(w_{\ell 0}^{(2)} + \sum_{k=1}^2 w_{\ell k}^{(2)} A_k^{(1)}\right) = \max\!\left(0,\; w_{\ell 0}^{(2)} + \sum_{k=1}^2 w_{\ell k}^{(2)} A_k^{(1)}\right).$$
     Número de parâmetros da camada 2: $(2 + 1) \times 3 = \mathbf{9}$.
   - **Camada de Saída Linear:**
     $$f(X) = \beta_0 + \sum_{\ell=1}^3 \beta_\ell A_\ell^{(2)}.$$
     Número de parâmetros da saída: $(3 + 1) \times 1 = \mathbf{4}$.
   - **Total de parâmetros treináveis:** $10 + 9 + 4 = \mathbf{23\text{ parâmetros}}$.

2. **Item (b) — Invariância da Softmax e Equivalência com Logística Binária (Ex. 10.10.2–3):**
   - Somando $c$ a cada $Z_\ell$:
     $$\frac{e^{Z_m + c}}{\sum_{\ell=0}^9 e^{Z_\ell + c}} = \frac{e^c e^{Z_m}}{e^c \sum_{\ell=0}^9 e^{Z_\ell}} = \frac{e^{Z_m}}{\sum_{\ell=0}^9 e^{Z_\ell}} = f_m(X).$$
   - Para $M = 2$ classes ($m \in \{0, 1\}$), com codificação *one-hot* $y_{i1} = y_i \in \{0, 1\}$ e $y_{i0} = 1 - y_i$, e definindo $p(x_i) = f_1(x_i) = \frac{e^{Z_1}}{e^{Z_0} + e^{Z_1}} = \frac{1}{1 + e^{-(Z_1 - Z_0)}}$ e $f_0(x_i) = 1 - p(x_i)$, a perda multinomial negativa torna-se:
     $$-\sum_{i=1}^n \big[y_{i0}\ln f_0(x_i) + y_{i1}\ln f_1(x_i)\big] = \mathbf{-\sum_{i=1}^n \big[y_i \ln p(x_i) + (1 - y_i)\ln(1 - p(x_i))\big]},$$
     que é exatamente o negativo da log-verossimilhança da regressão logística (Equação 4.5 do ISLP) com preditor linear $\eta_i = Z_{i1} - Z_{i0}$! $\blacksquare$
</details>

---

### Exercício B9.2 *[ISLP, Seção 10.10, Ex. 4 — Contagem de Parâmetros e Dualidade CNN vs. MLP]*
Considere uma camada convolucional aplicada a uma imagem de entrada de dimensão $32 \times 32$ com $C_{\text{in}} = 1$ canal (escala de cinza), utilizando filtros de tamanho $5 \times 5$ (com *padding* zero para manter a saída em $32 \times 32$).
(a) Se a camada possui $M$ filtros distintos (gerando um mapa de características de dimensão $32 \times 32 \times M$), quantos parâmetros treináveis existem nessa camada convolucional (incluindo um *bias* por filtro)?  
(b) Se achatássemos a imagem para um vetor de $32 \times 32 = 1.024$ entradas e usássemos uma camada densa (*fully connected*) comum com $32 \times 32 \times M = 1.024\,M$ neurônios ocultos, quantos parâmetros ela teria?  
(c) Explique como uma camada convolucional pode ser vista como uma camada densa ordinária submetida a duas famílias de restrições nos pesos.
- **Dica:** Compare $(5 \times 5 + 1)M = 26M$ com $(1.024 + 1) \times 1.024\,M$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Parâmetros na Camada Convolucional:**  
   Cada um dos $M$ filtros possui $5 \times 5 = 25$ pesos mais $1$ termo de *bias* compartilhado por todas as posições espaciais daquele mapa de características. Logo:
   $$N_{\text{CNN}} = (5 \times 5 + 1)\times M = \mathbf{26\,M \text{ parâmetros}}$$
   (ou $25\,M$ sem *bias*). Por exemplo, para $M = 1$, são apenas $26$ parâmetros; para $M = 10$, são $260$ parâmetros.

2. **Item (b) — Parâmetros na Camada Densa Equivalente:**  
   Uma camada densa conectando todas as $1.024$ entradas a cada uma das $1.024\,M$ unidades de saída possui:
   $$N_{\text{MLP}} = (1.024 + 1) \times (1.024\,M) = \mathbf{1.049.600\,M \text{ parâmetros}},$$
   ou seja, mais de **40.000 vezes mais parâmetros** do que a camada convolucional!

3. **Item (c) — Convolução como MLP Restrita:**  
   Uma camada convolucional é equivalente a uma camada totalmente conectada na qual a matriz de pesos $W \in \mathbb{R}^{1024M \times 1024}$ obedece a duas restrições estruturais fortes (*inductive biases*):
   1. **Conectividade Local (Esparsidade):** Todos os pesos fora da janela local $5 \times 5$ em torno do pixel $(i, j)$ são forçados identicamente a **zero** ($w = 0$).
   2. **Compartilhamento de Pesos (*Weight Sharing* / Estrutura de Toeplitz em blocos):** Os $25$ pesos não nulos que conectam a janela $5 \times 5$ ao neurônio $(i, j)$ são **exatamente iguais** para todas as coordenadas espaciais $(i, j) \in \{1,\dots,32\}^2$ dentro de um mesmo canal $m$. $\blacksquare$
</details>

---

### Exercício B9.3 *[ISLP, Seção 10.10, Ex. 6 — Dinâmica de Gradiente Descendente em Superfície Não Convexa]*
Considere a função objetivo univariada não convexa:
$$R(\beta) = \operatorname{sen}(\beta) + \frac{\beta}{10}, \quad \beta \in [-6, 6].$$
(a) Calcule a derivada $R'(\beta)$ e determine analiticamente todos os pontos críticos (mínimos e máximos locais) de $R(\beta)$ no intervalo $[-6, 6]$.  
(b) Execute a primeira atualização do algoritmo de **Gradiente Descendente** $\beta^{1} = \beta^{0} - \rho R'(\beta^{0})$ com taxa de aprendizado $\rho = 0{,}1$ partindo de $\beta^{0} = 2{,}3$ e, separadamente, partindo de $\beta^{0} = 1{,}4$. Para qual mínimo local cada trajetória converge quando $k \to \infty$? Que lição fundamental isso ilustra sobre otimização em *Deep Learning*?
- **Dica:** Observe onde se situa o máximo local entre $\beta \in [1, 2]$ resolvendo $\cos(\beta) = -0{,}1$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Derivada e Pontos Críticos:**  
   Derivando $R(\beta) = \operatorname{sen}(\beta) + \frac{\beta}{10}$:
   $$\mathbf{R'(\beta) = \cos(\beta) + 0{,}1}, \qquad R''(\beta) = -\operatorname{sen}(\beta).$$
   Os pontos críticos satisfazem $\cos(\beta) = -0{,}1 \iff \beta = \pm \arccos(-0{,}1) + 2k\pi \approx \pm 1{,}67096 + 2k\pi$:
   - **Máximo local em $\beta_{\max, 1} \approx +1{,}671$:** (pois $R''(1{,}671) = -\operatorname{sen}(1{,}671) \approx -0{,}995 < 0$);
   - **Mínimo local à direita em $\beta_{\min, R} = 2\pi - \arccos(-0{,}1) \approx +4{,}612$:** (pois $R''(4{,}612) \approx +0{,}995 > 0$, com $R(4{,}612) \approx -0{,}534$);
   - **Mínimo local à esquerda em $\beta_{\min, L} = -\arccos(-0{,}1) \approx -1{,}671$:** (pois $R''(-1{,}671) \approx +0{,}995 > 0$, com $R(-1{,}671) \approx -1{,}162$ — **melhor mínimo local**!).

2. **Item (b) — Sensibilidade à Inicialização ($\beta^0 = 2{,}3$ vs. $\beta^0 = 1{,}4$):**  
   O máximo local $\beta_{\max, 1} \approx 1{,}671$ atua como uma **crista divisora de águas (fronteira de bacias de atração)**:
   - **Partindo de $\beta^0 = 2{,}3 > 1{,}671$:**  
     Temos $R'(2{,}3) = \cos(2{,}3) + 0{,}1 \approx -0{,}6663 + 0{,}1 = -0{,}5663 < 0$. O primeiro passo é:
     $$\beta^1 = 2{,}3 - 0{,}1(-0{,}5663) = \mathbf{2{,}3566}.$$
     Como a derivada é negativa, $\beta^k$ move-se para a **direita** e converge para o mínimo local subótimo **$\beta_{\min, R} \approx 4{,}612$**.
   - **Partindo de $\beta^0 = 1{,}4 < 1{,}671$:**  
     Temos $R'(1{,}4) = \cos(1{,}4) + 0{,}1 \approx 0{,}16997 + 0{,}1 = +0{,}26997 > 0$. O primeiro passo é:
     $$\beta^1 = 1{,}4 - 0{,}1(0{,}26997) = \mathbf{1{,}3730}.$$
     Como a derivada é positiva, $\beta^k$ move-se para a **esquerda** e converge para o mínimo global no intervalo **$\beta_{\min, L} \approx -1{,}671$**.
   - **Lição:** Em superfícies de perda não convexas (redes neurais profundas), o destino do Gradiente Descendente depende criticamente da inicialização $\beta^0$ e do ruído do SGD para escapar de mínimos locais rasos. $\blacksquare$
</details>

---

### Exercício B9.4 *[Complemento — Raschka et al., ML with PyTorch and Scikit-Learn, Cap. 16, Cap. 17 e Cap. 19]*
(a) (**Variância na *Scaled Dot-Product Self-Attention* — Raschka Cap. 16:**) Sejam $q, k \in \mathbb{R}^{d_k}$ dois vetores de consulta (*query*) e chave (*key*) cujas componentes $q_j, k_j$ são variáveis aleatórias independentes com média $0$ e variância $1$. Calcule a média e a variância do produto escalar bruto $q^T k = \sum_{j=1}^{d_k} q_j k_j$, e demonstre por que a atenção de Vaswani et al. divide por $\sqrt{d_k}$ em $\operatorname{Attention}(Q,K,V) = \operatorname{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V$.  
(b) (**Discriminador Ótimo em GANs — Raschka Cap. 17:**) No jogo minimax de uma GAN $\min_G \max_D V(D, G) = \int p_{\text{data}}(x)\ln D(x)\,dx + \int p_g(x)\ln(1 - D(x))\,dx$, prove que, para um gerador $G$ fixo, o discriminador ótimo é $D^*(x) = \frac{p_{\text{data}}(x)}{p_{\text{data}}(x) + p_g(x)}$.  
(c) (**Equação de Atualização do *Q-Learning* — Raschka Cap. 19:**) Um agente em um grid-world no estado $s$ executa a ação $a$, recebe recompensa imediata $r = +10$ e transita para o estado $s'$, onde $\max_{a'} Q(s', a') = 20$. Se a estimativa atual era $Q(s, a) = 12$, a taxa de aprendizado é $\alpha = 0{,}5$ e o fator de desconto é $\gamma = 0{,}9$, calcule o erro de diferença temporal ($\text{TD-error}$) e o novo valor $Q_{\text{novo}}(s, a)$.
- **Dica:** Em (a), use $\operatorname{Var}(q_j k_j) = \mathbb{E}[q_j^2]\mathbb{E}[k_j^2] - (\mathbb{E}[q_j]\mathbb{E}[k_j])^2 = 1$ e a aditividade da variância para parcelas independentes. Em (b), maximize o integrando $g(y) = a\ln y + b\ln(1-y)$ em relação a $y = D(x) \in (0, 1)$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Justificativa Matemática do Fator $\frac{1}{\sqrt{d_k}}$ em Transformers (Raschka Cap. 16):**  
   Para cada coordenada $j \in \{1, \dots, d_k\}$, como $q_j$ e $k_j$ são independentes com média $0$ e variância $1$:
   $$\mathbb{E}[q_j k_j] = \mathbb{E}[q_j]\mathbb{E}[k_j] = 0, \qquad \operatorname{Var}(q_j k_j) = \mathbb{E}[q_j^2 k_j^2] - 0 = \mathbb{E}[q_j^2]\mathbb{E}[k_j^2] = 1 \times 1 = 1.$$
   Somando sobre as $d_k$ coordenadas independentes:
   $$\mathbb{E}[q^T k] = \sum_{j=1}^{d_k} \mathbb{E}[q_j k_j] = 0, \qquad \operatorname{Var}(q^T k) = \sum_{j=1}^{d_k} \operatorname{Var}(q_j k_j) = \mathbf{d_k}.$$
   Se $d_k$ for grande (ex.: $d_k = 64$ ou $512$), o desvio-padrão de $q^T k$ cresce como $\sqrt{d_k}$, empurrando os *logits* para regiões extremas onde a função $\operatorname{softmax}$ satura (probabilidades próximas de $0$ ou $1$) e **seus gradientes se anulam (*vanishing gradients*)**. Ao dividir por $\sqrt{d_k}$, restauramos variância unitária:
   $$\mathbf{\operatorname{Var}\!\left(\frac{q^T k}{\sqrt{d_k}}\right) = \frac{1}{d_k}\operatorname{Var}(q^T k) = \frac{d_k}{d_k} = 1}.$$

2. **Item (b) — Derivação do Discriminador Ótimo $D^*(x)$ em GANs (Raschka Cap. 17):**  
   Para maximizar a integral $\int \big[p_{\text{data}}(x)\ln D(x) + p_g(x)\ln(1 - D(x))\big]dx$ ponto a ponto para cada $x$, derivamos o integrando $h(D) = a\ln D + b\ln(1 - D)$ (onde $a = p_{\text{data}}(x)$ e $b = p_g(x)$) em relação a $D \in (0, 1)$:
   $$h'(D) = \frac{a}{D} - \frac{b}{1 - D} = 0 \iff a(1 - D) = bD \iff D^*(x) = \frac{a}{a + b} = \mathbf{\frac{p_{\text{data}}(x)}{p_{\text{data}}(x) + p_g(x)}}.$$
   (Nota: quando o gerador $G$ converge para a distribuição real $p_g = p_{\text{data}}$, temos $D^*(x) = \frac{1}{2}$ em toda parte).

3. **Item (c) — Atualização de *Q-Learning* Off-Policy (Raschka Cap. 19):**  
   O alvo temporal (*TD-target*) e o erro de diferença temporal ($\delta_{\text{TD}}$) são:
   $$y_{\text{TD}} = r + \gamma \max_{a'} Q(s', a') = 10 + 0{,}9(20) = 10 + 18 = \mathbf{28},$$
   $$\delta_{\text{TD}} = y_{\text{TD}} - Q(s, a) = 28 - 12 = \mathbf{+16}.$$
   Atualizando a tabela $Q$:
   $$Q_{\text{novo}}(s, a) = Q(s, a) + \alpha\,\delta_{\text{TD}} = 12 + 0{,}5(16) = \mathbf{20}. \quad \blacksquare$$
</details>

---

<a id="bloco-10"></a>
## Bloco 10 — Análise de Sobrevivência e Dados Censurados: Kaplan-Meier, Log-Rank e Cox (Capítulo 11)

### Exercício B10.1 *[ISLP, Seção 11.9, Ex. 2, Ex. 3, Ex. 4 e Ex. 6 — Estimador de Kaplan-Meier Passo a Passo]*
Considere um estudo clínico com $n = 6$ pacientes acompanhados ao longo do tempo, cujos tempos observados $Y_i = \min(T_i, C_i)$ (em meses) e indicadores de evento $\delta_i \in \{0, 1\}$ ($1 = \text{óbito/falha}$, $0 = \text{censurado à direita}$) são:
$$(Y_1, \delta_1) = (2,\; 1), \quad (Y_2, \delta_2) = (3,\; 0), \quad (Y_3, \delta_3) = (5,\; 1), \quad (Y_4, \delta_4) = (5,\; 0), \quad (Y_5, \delta_5) = (8,\; 1), \quad (Y_6, \delta_6) = (10,\; 0).$$
(a) Identifique os tempos únicos de falha ordenada $d_1 < d_2 < \dots < d_K$, calcule o tamanho do conjunto em risco $r_k$ e o número de eventos $q_k$ em cada $d_k$ (adotando a convenção padrão de que, em caso de empate entre falha e censura no mesmo instante $d_k$, a censura ocorre imediatamente após a falha).  
(b) Construa a curva de sobrevivência estimada de **Kaplan-Meier** $\hat{S}(t) = \prod_{d_k \le t} \frac{r_k - q_k}{r_k}$ em todos os subintervalos de $[0, 10]$ e determine a probabilidade estimada de sobrevivência além de $t = 6$ meses.
- **Dica:** Os instantes de falha ($\delta_i = 1$) são apenas $d_1 = 2$, $d_2 = 5$ e $d_3 = 8$. Nos instantes de censura pura ($t = 3$ e $t = 10$), $\hat{S}(t)$ **não** sofre queda, mas o conjunto de risco $r_k$ diminui para os eventos subsequentes!

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Tempos de evento $d_k$, conjunto de risco $r_k$ e falhas $q_k$:**  
   Os tempos únicos onde ocorre pelo menos um evento ($\delta_i = 1$) são $K = 3$ instantes: **$d_1 = 2$, $d_2 = 5$ e $d_3 = 8$**:
   - **Em $d_1 = 2$:** Todos os $6$ pacientes estão sob acompanhamento ($Y_i \ge 2$), logo **$r_1 = 6$**, e ocorre **$q_1 = 1$** falha (paciente 1). Fator de sobrevivência condicional: $\frac{r_1 - q_1}{r_1} = \frac{6 - 1}{6} = \frac{5}{6}$.
   - *(Em $t = 3$, o paciente 2 é censurado, saindo do conjunto de risco sem alterar $\hat{S}(t)$).*
   - **Em $d_2 = 5$:** Estão em risco os pacientes 3, 4, 5 e 6 ($Y_i \ge 5$), logo **$r_2 = 4$**, e ocorre **$q_2 = 1$** falha (paciente 3; o paciente 4 é censurado logo após a falha em $t=5$). Fator condicional: $\frac{r_2 - q_2}{r_2} = \frac{4 - 1}{4} = \frac{3}{4}$.
   - **Em $d_3 = 8$:** Estão em risco os pacientes 5 e 6 ($Y_i \ge 8$, pois os pacientes 1, 2, 3, 4 já falharam ou foram censurados em $t \le 5$), logo **$r_3 = 2$**, e ocorre **$q_3 = 1$** falha (paciente 5). Fator condicional: $\frac{r_3 - q_3}{r_3} = \frac{2 - 1}{2} = \frac{1}{2}$.

2. **Item (b) — Função Escada de Kaplan-Meier $\hat{S}(t)$:**
   - Para $0 \le t < 2$: $\hat{S}(t) = \mathbf{1{,}000}$ ($100\%$);
   - Para $2 \le t < 5$: $\hat{S}(t) = \frac{5}{6} \approx \mathbf{0{,}8333}$ ($83{,}3\%$);
   - Para $5 \le t < 8$: $\hat{S}(t) = \frac{5}{6} \times \frac{3}{4} = \frac{5}{8} = \mathbf{0{,}6250}$ ($62{,}5\%$);
   - Para $8 \le t \le 10$: $\hat{S}(t) = \frac{5}{8} \times \frac{1}{2} = \frac{5}{16} = \mathbf{0{,}3125}$ ($31{,}25\%$).
   Em particular, em $t = 6$ meses ($5 \le 6 < 8$), a probabilidade estimada de sobrevivência é **$\hat{S}(6) = 0{,}625$ ($62{,}5\%$)**. $\blacksquare$
</details>

---

### Exercício B10.2 *[ISLP, Seção 11.9, Ex. 8 e Ex. 9 — Taxa de Risco (Hazard) e MLE Sob Censura Exponencial]*
Seja $T \ge 0$ uma variável aleatória contínua de tempo até o evento com densidade $f(t)$, função de sobrevivência $S(t) = \Pr(T > t) = 1 - F(t)$ e taxa de risco instantânea (*hazard*) $h(t) = \lim_{\Delta t \to 0^+} \frac{\Pr(t < T \le t + \Delta t \mid T > t)}{\Delta t} = \frac{f(t)}{S(t)}$.
(a) Prove que $h(t) = -\frac{d}{dt}\ln S(t)$ e, consequentemente, que $S(t) = \exp\!\left(-\int_0^t h(u)\,du\right)$ (Ex. 11.9.8).  
(b) Suponha que $T_i \stackrel{\text{i.i.d.}}{\sim} \operatorname{Exponencial}(\lambda)$, isto é, $f(t) = \lambda e^{-\lambda t}$ e $S(t) = e^{-\lambda t}$ (taxa de risco constante $h(t) = \lambda$). Escreva a função de verossimilhança para $n$ observações com censura independente à direita $\{(y_i, \delta_i)\}_{i=1}^n$, onde cada falha contribui com $f(y_i)$ e cada censura contribui com $S(y_i)$, e prove que o Estimador de Máxima Verossimilhança (MLE) de $\lambda$ é:
$$\hat{\lambda}_{\text{MLE}} = \frac{\sum_{i=1}^n \delta_i}{\sum_{i=1}^n y_i}$$
(o número total de eventos observados dividido pelo tempo total de exposição em pessoa-tempo) (Ex. 11.9.9).
- **Dica:** Em (b), escreva a contribuição da $i$-ésima observação como $L_i(\lambda) = [f(y_i)]^{\delta_i}[S(y_i)]^{1-\delta_i} = \lambda^{\delta_i}e^{-\lambda y_i}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Relação Fundamental entre $h(t)$ e $S(t)$ (Ex. 11.9.8):**  
   Como $S(t) = 1 - F(t) = \int_t^\infty f(u)\,du$, pelo Teorema Fundamental do Cálculo temos $S'(t) = -f(t)$. Logo:
   $$-\frac{d}{dt}\ln S(t) = -\frac{S'(t)}{S(t)} = \frac{f(t)}{S(t)} = h(t).$$
   Integrando ambos os membros de $0$ a $t$ e usando $\ln S(0) = \ln(1) = 0$:
   $$\int_0^t h(u)\,du = -\big[\ln S(u)\big]_0^t = -\ln S(t) \iff \mathbf{S(t) = \exp\!\left(-\int_0^t h(u)\,du\right)}. \quad \blacksquare$$

2. **Item (b) — Derivação do MLE Exponencial sob Censura à Direita (Ex. 11.9.9):**  
   Para uma observação com evento observado ($\delta_i = 1$), sabemos que $T_i = y_i$, cuja densidade é $f(y_i) = \lambda e^{-\lambda y_i}$. Para uma observação censurada ($\delta_i = 0$), sabemos apenas que $T_i > y_i$, cuja probabilidade é $S(y_i) = e^{-\lambda y_i}$. Unificando ambas com o expoente $\delta_i \in \{0, 1\}$, a verossimilhança total é:
   $$L(\lambda) = \prod_{i=1}^n \big[f(y_i)\big]^{\delta_i}\big[S(y_i)\big]^{1-\delta_i} = \prod_{i=1}^n \big(\lambda e^{-\lambda y_i}\big)^{\delta_i}\big(e^{-\lambda y_i}\big)^{1-\delta_i} = \prod_{i=1}^n \lambda^{\delta_i} e^{-\lambda y_i}.$$
   Tomando o logaritmo natural (log-verossimilhança $\ell(\lambda) = \ln L(\lambda)$):
   $$\ell(\lambda) = \left(\sum_{i=1}^n \delta_i\right)\ln\lambda - \lambda\sum_{i=1}^n y_i.$$
   Derivando em relação a $\lambda$ e igualando a zero:
   $$\ell'(\lambda) = \frac{\sum_{i=1}^n \delta_i}{\lambda} - \sum_{i=1}^n y_i = 0 \implies \mathbf{\hat{\lambda}_{\text{MLE}} = \frac{\sum_{i=1}^n \delta_i}{\sum_{i=1}^n y_i}}.$$
   Como $\ell''(\lambda) = -\frac{\sum \delta_i}{\lambda^2} < 0$, trata-se do máximo global único! Note que se ignorássemos as observações censuradas, subestimaríamos o denominador $\sum_{i=1}^n y_i$ e superestimaríamos a taxa de mortalidade $\lambda$. $\blacksquare$
</details>

---

### Exercício B10.3 *[ISLP, Seção 11.5.2 e Seção 11.9, Ex. 10 — Verossimilhança Parcial de Cox e Hazard Ratios]*
Considere um modelo de Riscos Proporcionais de Cox $h(t \mid x_i) = h_0(t)\exp(\beta_1 x_{i1} + \beta_2 x_{i2})$ ajustado a dados clínicos em que $X_1 \in \{0, 1\}$ indica o grupo de tratamento ($1 = \text{Droga Nova}$, $0 = \text{Placebo}$) e $X_2$ é a idade em anos, obtendo $\hat{\beta}_1 = -0{,}693$ e $\hat{\beta}_2 = +0{,}04$.
(a) Calcule e interprete as razões de risco (*Hazard Ratios* — HR) associadas ao tratamento e a um aumento de $10$ anos na idade.  
(b) Explique como a **Verossimilhança Parcial de Cox** $PL(\beta) = \prod_{i : \delta_i = 1} \frac{\exp(x_i^T\beta)}{\sum_{i' \in \mathcal{R}(y_i)} \exp(x_{i'}^T\beta)}$ consegue estimar $\beta$ sem precisar especificar ou estimar a função de risco basal $h_0(t)$.
- **Dica:** Em (b), calcule a probabilidade condicional de que a falha observada no instante $y_i$ tenha ocorrido especificamente no indivíduo $i$, dado que exatamente um indivíduo do conjunto de risco $\mathcal{R}(y_i)$ falhou em $y_i$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Cálculo e Interpretação dos *Hazard Ratios* (HR):**
   - **Efeito do Tratamento ($X_1 = 1$ vs. $X_1 = 0$, mantendo idade $X_2$ fixa):**
     $$\operatorname{HR}_{\text{Trat}} = \frac{h(t \mid X_1 = 1, X_2)}{h(t \mid X_1 = 0, X_2)} = e^{\hat{\beta}_1} = e^{-0{,}693} \approx \mathbf{0{,}50}.$$
     *Interpretação:* Para pacientes da mesma idade, a Droga Nova **reduz a taxa instantânea de risco de óbito pela metade ($50\%$)** em qualquer instante $t$ em comparação ao Placebo.
   - **Efeito de $+10$ anos na Idade ($\Delta X_2 = 10$, mantendo tratamento fixo):**
     $$\operatorname{HR}_{+10\text{ anos}} = e^{10\,\hat{\beta}_2} = e^{10 \times 0{,}04} = e^{0{,}40} \approx \mathbf{1{,}4918}.$$
     *Interpretação:* Cada década adicional de idade **aumenta a taxa instantânea de risco em $49{,}2\%$**.

2. **Item (b) — Cancelamento de $h_0(t)$ na Verossimilhança Parcial de Cox:**  
   Dado que um evento ocorreu no instante exato $y_i$ (onde o conjunto de pacientes em risco é $\mathcal{R}(y_i) = \{i' : y_{i'} \ge y_i\}$), a probabilidade condicional de que o indivíduo que sofreu o evento seja especificamente o paciente $i$ é:
   $$\frac{h(y_i \mid x_i)\,dt}{\sum_{i' \in \mathcal{R}(y_i)} h(y_i \mid x_{i'})\,dt} = \frac{\cancel{h_0(y_i)}\exp(x_i^T\beta)}{\sum_{i' \in \mathcal{R}(y_i)} \cancel{h_0(y_i)}\exp(x_{i'}^T\beta)} = \mathbf{\frac{\exp(x_i^T\beta)}{\sum_{i' \in \mathcal{R}(y_i)} \exp(x_{i'}^T\beta)}}.$$
   A função de risco basal arbitrária $h_0(y_i)$ **fatora para fora da soma no denominador e cancela-se exatamente** com o numerador! Por isso, o modelo de Cox é **semiparamétrico**: depende apenas da ordem relativa dos tempos de falha e não requer nenhuma hipótese paramétrica (como Weibull ou Exponencial) sobre $h_0(t)$. $\blacksquare$
</details>

---

<a id="bloco-11"></a>
## Bloco 11 — Aprendizado Não Supervisionado: PCA, Cargas via Regressão, *K-Means* e Hierárquico (Capítulo 12)

### Exercício B11.1 *[ISLP, Seção 12.6, Ex. 1 — Identidade Fundamental da Variância Intra-Cluster e Convergência do K-Means]*
Seja $C_k \subset \{1, \dots, n\}$ o conjunto de índices das $|C_k|$ observações atribuídas ao $k$-ésimo cluster, e seja $\bar{x}_k = \frac{1}{|C_k|}\sum_{i \in C_k} x_i \in \mathbb{R}^p$ o centroide (vetor de médias) do cluster $C_k$.
(a) Prove algebricamente a identidade (Equação 12.18 do ISLP):
$$\frac{1}{|C_k|}\sum_{i, i' \in C_k} \sum_{j=1}^p (x_{ij} - x_{i'j})^2 = 2\sum_{i \in C_k} \sum_{j=1}^p (x_{ij} - \bar{x}_{kj})^2.$$
(b) Usando a identidade do item (a), prove que o algoritmo iterativo de **K-Means** (Algoritmo 12.2 do ISLP) faz o valor da função objetivo $\sum_{k=1}^K \frac{1}{|C_k|}\sum_{i, i' \in C_k} \|x_i - x_{i'}\|_2^2$ **decrescer (ou permanecer igual) monotonicamente** a cada passo de atualização de centroides e de reatribuição de clusters, garantindo convergência em número finito de passos.
- **Dica:** Em (a), escreva $x_{ij} - x_{i'j} = (x_{ij} - \bar{x}_{kj}) - (x_{i'j} - \bar{x}_{kj})$, eleve ao quadrado e some sobre $i \in C_k$ e $i' \in C_k$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Prova da Identidade (Equação 12.18):**  
   Fixemos a coordenada $j \in \{1, \dots, p\}$. Somando e subtraindo a média do cluster $\bar{x}_{kj} = \frac{1}{|C_k|}\sum_{i \in C_k} x_{ij}$:
   $$(x_{ij} - x_{i'j})^2 = \big[(x_{ij} - \bar{x}_{kj}) - (x_{i'j} - \bar{x}_{kj})\big]^2 = (x_{ij} - \bar{x}_{kj})^2 - 2(x_{ij} - \bar{x}_{kj})(x_{i'j} - \bar{x}_{kj}) + (x_{i'j} - \bar{x}_{kj})^2.$$
   Somando sobre todos os pares $(i, i') \in C_k \times C_k$:
   - O primeiro termo não depende de $i'$, logo somar sobre $i' \in C_k$ multiplica por $|C_k|$: $\sum_{i \in C_k}\sum_{i' \in C_k} (x_{ij} - \bar{x}_{kj})^2 = |C_k|\sum_{i \in C_k} (x_{ij} - \bar{x}_{kj})^2$.
   - O terceiro termo, por simetria de índices, vale igualmente $|C_k|\sum_{i' \in C_k} (x_{i'j} - \bar{x}_{kj})^2$.
   - O termo cruzado anula-se identicamente porque $\sum_{i \in C_k} (x_{ij} - \bar{x}_{kj}) = 0$:
     $$\sum_{i \in C_k}\sum_{i' \in C_k} (x_{ij} - \bar{x}_{kj})(x_{i'j} - \bar{x}_{kj}) = \left(\sum_{i \in C_k} (x_{ij} - \bar{x}_{kj})\right)\left(\sum_{i' \in C_k} (x_{i'j} - \bar{x}_{kj})\right) = 0 \times 0 = 0.$$
   Somando os três termos, dividindo por $|C_k|$ e somando sobre $j = 1, \dots, p$, concluímos:
   $$\mathbf{\frac{1}{|C_k|}\sum_{i, i' \in C_k} \sum_{j=1}^p (x_{ij} - x_{i'j})^2 = 2\sum_{i \in C_k} \sum_{j=1}^p (x_{ij} - \bar{x}_{kj})^2}. \quad \blacksquare$$

2. **Item (b) — Convergência Monótona do Algoritmo de *K-Means*:**  
   Pela identidade (a), minimizar a variação intra-cluster aos pares equivale a minimizar $W(C_1, \dots, C_K; \mu_1, \dots, \mu_K) = \sum_{k=1}^K \sum_{i \in C_k} \|x_i - \mu_k\|_2^2$:
   - **Passo 2(a) (Cálculo dos Centroides):** Mantendo as partições $C_1, \dots, C_K$ fixas, a função quadrática $\mu_{kj} \mapsto \sum_{i \in C_k} (x_{ij} - \mu_{kj})^2$ atinge seu único mínimo global exatamente na média aritmética $\mu_{kj}^* = \bar{x}_{kj}$, fazendo $W$ decrescer.
   - **Passo 2(b) (Reatribuição ao Centroide Mais Próximo):** Mantendo os centroides $\bar{x}_1, \dots, \bar{x}_K$ fixos, atribuir cada ponto $x_i$ ao cluster $k^*(i) = \arg\min_k \|x_i - \bar{x}_k\|_2^2$ minimiza individualmente cada parcela $\|x_i - \bar{x}_{k(i)}\|_2^2$, fazendo $W$ decrescer novamente.
   Como existem apenas finitas partições ($K^n$) e $W \ge 0$ decresce a cada passo, o algoritmo converge em número finito de iterações para um mínimo local. $\blacksquare$
</details>

---

### Exercício B11.2 *[ISLP, Seção 12.6, Ex. 2 — Agrupamento Hierárquico: Ligação Completa vs. Ligação Simples]*
Suponha que temos $n = 4$ observações com a seguinte matriz de dissimilaridades (distâncias) simétrica $D$:
$$D = \begin{pmatrix} 0 & 0{,}3 & 0{,}4 & 0{,}7 \\ 0{,}3 & 0 & 0{,}5 & 0{,}8 \\ 0{,}4 & 0{,}5 & 0 & 0{,}45 \\ 0{,}7 & 0{,}8 & 0{,}45 & 0 \end{pmatrix}.$$
(a) Execute passo a passo o algoritmo de **Agrupamento Hierárquico Aglomerativo** usando **Ligação Completa (*Complete Linkage* — máxima distância inter-cluster)**, indicando quais clusters se fundem em cada etapa e a altura (*height*) exata de cada fusão no dendrograma.  
(b) Repita o procedimento usando **Ligação Simples (*Single Linkage* — mínima distância inter-cluster)**.  
(c) Se cortarmos ambos os dendrogramas de modo a obter $K = 2$ clusters, quais são os clusters resultantes em (a) e em (b)?
- **Dica:** A primeira fusão é sempre o par com a menor distância na matriz $D$, isto é, $\{1, 2\}$ na altura $0{,}3$. Na etapa seguinte, compare como $d(\{1,2\}, \{3\})$ é calculada no *Complete Linkage* ($\max(0{,}4; 0{,}5) = 0{,}5$) vs. *Single Linkage* ($\min(0{,}4; 0{,}5) = 0{,}4$).

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Dendrograma com Ligação Completa (*Complete Linkage*):**
   - **Passo 1:** A menor dissimilaridade entre os 4 pontos individuais $\{1\}, \{2\}, \{3\}, \{4\}$ é $d(1, 2) = 0{,}3$. Fundimos **$\{1, 2\}$ na altura $h_1 = 0{,}30$**.
   - **Matriz reduzida (Ligação Completa — máximo):**
     $$d_{\text{comp}}(\{1,2\}, \{3\}) = \max\big(d(1,3), d(2,3)\big) = \max(0{,}4;\; 0{,}5) = 0{,}50,$$
     $$d_{\text{comp}}(\{1,2\}, \{4\}) = \max\big(d(1,4), d(2,4)\big) = \max(0{,}7;\; 0{,}8) = 0{,}80, \qquad d(\{3\}, \{4\}) = 0{,}45.$$
   - **Passo 2:** A menor dissimilaridade restante é $d(\{3\}, \{4\}) = 0{,}45 < 0{,}50$. Fundimos **$\{3, 4\}$ na altura $h_2 = 0{,}45$**!
   - **Passo 3:** Finalmente, fundimos $\{1, 2\}$ e $\{3, 4\}$ na altura:
     $$h_3 = d_{\text{comp}}(\{1,2\}, \{3,4\}) = \max(0{,}4;\; 0{,}7;\; 0{,}5;\; 0{,}8) = \mathbf{0{,}80}.$$

2. **Item (b) — Dendrograma com Ligação Simples (*Single Linkage*):**
   - **Passo 1:** Fundimos **$\{1, 2\}$ na altura $h_1 = 0{,}30$**.
   - **Matriz reduzida (Ligação Simples — mínimo):**
     $$d_{\text{single}}(\{1,2\}, \{3\}) = \min\big(d(1,3), d(2,3)\big) = \min(0{,}4;\; 0{,}5) = 0{,}40,$$
     $$d_{\text{single}}(\{1,2\}, \{4\}) = \min\big(d(1,4), d(2,4)\big) = \min(0{,}7;\; 0{,}8) = 0{,}70, \qquad d(\{3\}, \{4\}) = 0{,}45.$$
   - **Passo 2:** A menor dissimilaridade restante agora é $d_{\text{single}}(\{1,2\}, \{3\}) = 0{,}40 < 0{,}45$. Fundimos **$\{1, 2\}$ com $\{3\}$ para formar $\{1, 2, 3\}$ na altura $h_2 = 0{,}40$**!
   - **Passo 3:** Finalmente, fundimos $\{1, 2, 3\}$ com $\{4\}$ na altura:
     $$h_3 = d_{\text{single}}(\{1,2,3\}, \{4\}) = \min\big(d(1,4), d(2,4), d(3,4)\big) = \min(0{,}7;\; 0{,}8;\; 0{,}45) = \mathbf{0{,}45}.$$

3. **Item (c) — Corte para $K = 2$ Clusters:**
   - Na **Ligação Completa (a):** Os $2$ clusters antes da última fusão são equilibrados: **$\{1, 2\}$ e $\{3, 4\}$**.
   - Na **Ligação Simples (b):** Os $2$ clusters antes da última fusão são encadeados: **$\{1, 2, 3\}$ e $\{4\}$**. $\blacksquare$
</details>

---

### Exercício B11.3 *[ISLP, Seção 12.6, Ex. 6 e Ex. 7 — PCA via Regressões Lineares Simples e Distância de Correlação]*
Seja $X \in \mathbb{R}^{n \times p}$ uma matriz de dados centrada ($\sum_{i=1}^n x_{ij} = 0$ para todo $j$).
(a) Considere o problema de aproximação matricial da PCA (Equação 12.6): minimizar $\sum_{j=1}^p \sum_{i=1}^n \left(x_{ij} - \sum_{m=1}^M z_{im}\phi_{jm}\right)^2$. Suponha que os vetores de escores das componentes principais $z_m = (z_{1m}, \dots, z_{nm})^T$ sejam conhecidos e mutuamente ortogonais ($\sum_{i=1}^n z_{im}z_{im'} = 0$ para $m \neq m'$). Prove que, para cada variável $j$ e componente $m$, a carga ótima $\phi_{jm}$ é simplesmente o coeficiente angular da **regressão linear simples sem intercepto** da $j$-ésima coluna de $X$ sobre $z_m$ (Ex. 12.6.6).  
(b) Suponha agora que cada observação (linha $x_i \in \mathbb{R}^p$) foi padronizada para ter média zero ($\bar{x}_i = \frac{1}{p}\sum_{j=1}^p x_{ij} = 0$) e desvio-padrão unitário ($\sum_{j=1}^p x_{ij}^2 = p - 1$ ou $1$). Prove que a dissimilaridade baseada em correlação $1 - r_{ij} = 1 - \operatorname{Cor}(x_i, x_j)$ é estritamente proporcional ao quadrado da distância euclidiana $\|x_i - x_j\|_2^2$ (Ex. 12.6.7).
- **Dica:** Em (b), expanda $\|x_i - x_j\|_2^2 = \|x_i\|_2^2 + \|x_j\|_2^2 - 2\,x_i^T x_j$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Obtenção das Cargas $\phi_{jm}$ via Regressão Linear Simples Sem Intercepto (Ex. 12.6.6):**  
   A função objetivo desacopla-se como uma soma sobre cada variável $j = 1, \dots, p$:
   $$L_j(\phi_{j1}, \dots, \phi_{jM}) = \sum_{i=1}^n \left(x_{ij} - \sum_{m=1}^M z_{im}\phi_{jm}\right)^2.$$
   Derivando $L_j$ em relação a $\phi_{jm}$ e igualando a zero:
   $$\frac{\partial L_j}{\partial \phi_{jm}} = -2\sum_{i=1}^n z_{im}\left(x_{ij} - \sum_{m'=1}^M z_{im'}\phi_{jm'}\right) = 0 \implies \sum_{i=1}^n z_{im}x_{ij} = \sum_{m'=1}^M \phi_{jm'} \sum_{i=1}^n z_{im}z_{im'}.$$
   Pela ortogonalidade dos escores das componentes principais ($\sum_{i=1}^n z_{im}z_{im'} = 0$ para $m' \neq m$), todos os termos cruzados desaparecem, restando apenas $m' = m$:
   $$\mathbf{\hat{\phi}_{jm} = \frac{\sum_{i=1}^n z_{im}x_{ij}}{\sum_{i=1}^n z_{im}^2}},$$
   que é exatamente o estimador de mínimos quadrados da regressão linear simples sem intercepto de $x_{\cdot j}$ sobre $z_{\cdot m}$! (Isso fundamenta o algoritmo de Mínimos Quadrados Alternados para PCA e completamento de matrizes).

2. **Item (b) — Proporcionalidade $1 - r_{ij} \propto \|x_i - x_j\|_2^2$ para Observações Padronizadas (Ex. 12.6.7):**  
   Se cada vetor de observação $x_i \in \mathbb{R}^p$ tem média zero ($\bar{x}_i = 0$) e norma quadrática constante $\|x_i\|_2^2 = \sum_{k=1}^p x_{ik}^2 = c$ (onde $c = p - 1$ ou $c = 1$), o coeficiente de correlação de Pearson entre $x_i$ e $x_j$ é:
   $$r_{ij} = \frac{\sum_{k=1}^p (x_{ik} - \bar{x}_i)(x_{jk} - \bar{x}_j)}{\sqrt{\sum_{k=1}^p (x_{ik} - \bar{x}_i)^2}\sqrt{\sum_{k=1}^p (x_{jk} - \bar{x}_j)^2}} = \frac{x_i^T x_j}{\sqrt{c}\sqrt{c}} = \frac{x_i^T x_j}{c}.$$
   Por outro lado, expandindo o quadrado da distância euclidiana entre $x_i$ e $x_j$:
   $$\|x_i - x_j\|_2^2 = \|x_i\|_2^2 + \|x_j\|_2^2 - 2\,x_i^T x_j = c + c - 2(c\,r_{ij}) = \mathbf{2c(1 - r_{ij})}.$$
   Portanto, $\mathbf{1 - r_{ij} = \frac{1}{2c}\|x_i - x_j\|_2^2}$, provando que agrupar por distância de correlação equivale a agrupar por distância euclidiana após padronizar as linhas! $\blacksquare$
</details>

---

<a id="bloco-12"></a>
## Bloco 12 — Testes Múltiplos de Hipóteses: FWER, Bonferroni, Holm e Benjamini-Hochberg / FDR (Capítulo 13)

### Exercício B12.1 *[ISLP, Seção 13.7, Ex. 1, Ex. 2 e Ex. 3 — FWER e Prova da Desigualdade de Boole/Bonferroni]*
Suponha que testamos $m$ hipóteses nulas $H_{01}, \dots, H_{0m}$, das quais $m_0$ são verdadeiras, rejeitando cada $H_{0j}$ se seu $p$-valor for menor que $\alpha$.
(a) Se todas as $m_0$ hipóteses nulas verdadeiras forem mutuamente independentes, qual é a distribuição exata do número de falsos positivos $V$ (erros Tipo I), sua esperança $\mathbb{E}[V]$ e seu desvio-padrão $\operatorname{SD}(V)$? Calcule numericamente para $m_0 = 1.000$ e $\alpha = 0{,}05$ (Ex. 13.7.1–2).  
(b) Compare o $\operatorname{FWER} = \Pr(V \ge 1)$ para $m = 2$ testes sob independência ($\alpha = 0{,}05$) com o caso extremo em que os dois $p$-valores têm correlação positiva perfeita ($p_1 = p_2$) e correlação negativa perfeita ($p_2 = 1 - p_1$) (Ex. 13.7.2).  
(c) Prove rigorosamente a **Desigualdade de Boole / Bonferroni**: se a $j$-ésima hipótese nula for rejeitada ao nível $\alpha_j$, então, para qualquer estrutura de dependência entre os testes:
$$\operatorname{FWER} \le \sum_{j=1}^m \alpha_j$$
(em particular, escolhendo $\alpha_j = \alpha / m$, garante-se $\operatorname{FWER} \le \alpha$) (Ex. 13.7.3).
- **Dica:** Em (a), lembre que sob $H_{0j}$ verdadeira, $P(p_j \le \alpha) = \alpha$, logo $V \sim \operatorname{Binomial}(m_0, \alpha)$. Em (c), use a subaditividade da medida de probabilidade $\Pr\left(\bigcup_{j \in \mathcal{M}_0} A_j\right) \le \sum_{j \in \mathcal{M}_0} \Pr(A_j)$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — Distribuição, Esperança e Desvio-Padrão de $V$:**  
   Sob qualquer hipótese nula verdadeira $H_{0j}$, o $p$-valor tem distribuição $\operatorname{Uniforme}(0, 1)$, logo a probabilidade de rejeição falsa (Erro Tipo I) é $\Pr(p_j \le \alpha) = \alpha$. Pela linearidade da esperança (que vale **com ou sem independência**):
   $$\mathbb{E}[V] = \sum_{j \in \mathcal{M}_0} \Pr(p_j \le \alpha) = \mathbf{m_0 \alpha}.$$
   Sob independência entre os $m_0$ testes, $V$ é a soma de $m_0$ variáveis de Bernoulli i.i.d. de parâmetro $\alpha$, logo:
   $$V \sim \operatorname{Binomial}(m_0, \alpha), \qquad \operatorname{SD}(V) = \mathbf{\sqrt{m_0 \alpha (1 - \alpha)}}.$$
   Para $m_0 = 1.000$ e $\alpha = 0{,}05$: esperamos $\mathbb{E}[V] = 1.000 \times 0{,}05 = \mathbf{50\text{ falsos positivos}}$, com desvio-padrão $\operatorname{SD}(V) = \sqrt{1.000 \times 0{,}05 \times 0{,}95} = \sqrt{47{,}5} \approx \mathbf{6{,}89}$.

2. **Item (b) — Efeito da Correlação sobre a FWER ($m = 2, \alpha = 0{,}05$, Ex. 13.7.2):**
   - **Independência:** $\operatorname{FWER} = 1 - (1 - \alpha)^2 = 1 - 0{,}95^2 = \mathbf{0{,}0975}$ ($9{,}75\%$).
   - **Dependência positiva extrema ($p_1 = p_2$):** Os dois eventos $\{p_1 \le \alpha\}$ e $\{p_2 \le \alpha\}$ coincidem totalmente, logo $\operatorname{FWER} = \Pr(p_1 \le \alpha) = \alpha = \mathbf{0{,}05}$ ($5{,}0\%$).
   - **Dependência negativa extrema ($p_2 = 1 - p_1$, para $\alpha < 0{,}5$):** Os eventos $\{p_1 \le \alpha\}$ e $\{p_1 \ge 1 - \alpha\}$ são **mutuamente exclusivos (disjuntos)**, logo $\operatorname{FWER} = \alpha + \alpha = 2\alpha = \mathbf{0{,}10}$ ($10{,}0\%$, atingindo exatamente o limite superior de Bonferroni!).

3. **Item (c) — Prova da Desigualdade de Boole / Correção de Bonferroni (Ex. 13.7.3):**  
   Seja $\mathcal{M}_0 \subseteq \{1, \dots, m\}$ o subconjunto das $m_0$ hipóteses nulas verdadeiras, e seja $A_j = \{\text{rejeitar } H_{0j}\}$ o evento de erro Tipo I na $j$-ésima hipótese ($\Pr(A_j) \le \alpha_j$ para $j \in \mathcal{M}_0$). Pela definição de FWER e pela desigualdade de Boole (subaditividade finita da probabilidade):
   $$\operatorname{FWER} = \Pr(V \ge 1) = \Pr\!\left(\bigcup_{j \in \mathcal{M}_0} A_j\right) \le \sum_{j \in \mathcal{M}_0} \Pr(A_j) \le \sum_{j \in \mathcal{M}_0} \alpha_j \le \mathbf{\sum_{j=1}^m \alpha_j}.$$
   Tomando $\alpha_j = \alpha / m$ para todo $j = 1, \dots, m$, obtemos $\operatorname{FWER} \le m_0(\alpha / m) \le m(\alpha / m) = \alpha$. $\blacksquare$
</details>

---

### Exercício B12.2 *[ISLP, Seção 13.7, Ex. 4 e Ex. 5 — Aplicação Completa de Bonferroni, Holm e Benjamini-Hochberg]*
Suponha que testamos $m = 10$ hipóteses nulas simultaneamente, obtendo os seguintes $p$-valores:
$$p_1 = 0{,}0011, \quad p_2 = 0{,}031, \quad p_3 = 0{,}017, \quad p_4 = 0{,}32, \quad p_5 = 0{,}11,$$
$$p_6 = 0{,}90, \quad p_7 = 0{,}07, \quad p_8 = 0{,}006, \quad p_9 = 0{,}004, \quad p_{10} = 0{,}0009.$$
(a) Determine quais hipóteses nulas são rejeitadas ao controlar a **FWER no nível $\alpha = 0{,}05$** usando o método de **Bonferroni** e usando o método *step-down* de **Holm** (Ex. 13.7.4).  
(b) Determine quais hipóteses nulas são rejeitadas ao controlar a **Taxa de Falsas Descobertas (FDR)** usando o procedimento de **Benjamini-Hochberg (BH)** no nível $q = 0{,}05$ e no nível $q = 0{,}20$.  
(c) Construa um exemplo explícito com $m = 5$ $p$-valores em que o método de Holm rejeita $4$ hipóteses nulas no nível $\alpha = 0{,}10$, enquanto o método de Bonferroni rejeita apenas $1$ hipótese nula (Ex. 13.7.5).
- **Dica:** Primeiro ordene os 10 $p$-valores em ordem crescente $p_{(1)} \le p_{(2)} \le \dots \le p_{(10)}$ e compare cada $p_{(j)}$ com o limiar de Holm $\frac{\alpha}{m + 1 - j}$ e com a reta de Benjamini-Hochberg $\frac{q \cdot j}{m}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Ordenação dos $m = 10$ $p$-valores e Tabela Comparativa de Limiares:**

| Ordem $j$ | Hipótese Original | $p_{(j)}$ | Limiar Bonferroni ($\frac{0{,}05}{10}$) | Limiar de Holm ($\frac{0{,}05}{11 - j}$) | Limiar BH ($q=0{,}05$: $\frac{0{,}05\,j}{10}$) | Limiar BH ($q=0{,}20$: $\frac{0{,}20\,j}{10}$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $H_{0,10}$ | $0{,}0009$ | $0{,}005$ (**Rej.**) | $0{,}00500$ (**Rej.**) | $0{,}005$ ($\le$) | $0{,}02$ ($\le$) |
| $2$ | $H_{0,1}$ | $0{,}0011$ | $0{,}005$ (**Rej.**) | $0{,}00556$ (**Rej.**) | $0{,}010$ ($\le$) | $0{,}04$ ($\le$) |
| $3$ | $H_{0,9}$ | $0{,}0040$ | $0{,}005$ (**Rej.**) | $0{,}00625$ (**Rej.**) | $0{,}015$ ($\le$) | $0{,}06$ ($\le$) |
| $4$ | $H_{0,8}$ | $0{,}0060$ | $0{,}005$ *(Não)* | $0{,}00714$ (**Rej.**) | $0{,}020$ ($\le$) | $0{,}08$ ($\le$) |
| $5$ | $H_{0,3}$ | $0{,}0170$ | $0{,}005$ *(Não)* | $0{,}00833$ *(Para: $L=5$)* | $0{,}025$ ($\le$, $L=5$) | $0{,}10$ ($\le$) |
| $6$ | $H_{0,2}$ | $0{,}0310$ | $0{,}005$ *(Não)* | $0{,}01000$ | $0{,}030$ *(Não)* | $0{,}12$ ($\le$) |
| $7$ | $H_{0,7}$ | $0{,}0700$ | $0{,}005$ *(Não)* | $0{,}01250$ | $0{,}035$ | $0{,}14$ ($\le$) |
| $8$ | $H_{0,5}$ | $0{,}1100$ | $0{,}005$ *(Não)* | $0{,}01667$ | $0{,}040$ | $0{,}16$ ($\le$, $L=8$) |
| $9$ | $H_{0,4}$ | $0{,}3200$ | $0{,}005$ *(Não)* | $0{,}02500$ | $0{,}045$ | $0{,}18$ *(Não)* |
| $10$ | $H_{0,6}$ | $0{,}9000$ | $0{,}005$ *(Não)* | $0{,}05000$ | $0{,}050$ | $0{,}20$ |

2. **Item (a) — Rejeições para FWER $\le 0{,}05$:**
   - **Bonferroni ($\alpha/10 = 0{,}005$):** Rejeita apenas **3 hipóteses nulas**: $\mathbf{\{H_{0,10},\; H_{0,1},\; H_{0,9}\}}$.
   - **Holm ($\alpha/(11-j)$):** O primeiro índice onde $p_{(j)} > \frac{0{,}05}{11-j}$ é $L = 5$ ($0{,}0170 > 0{,}00833$). Logo, Holm rejeita **4 hipóteses nulas**: $\mathbf{\{H_{0,10},\; H_{0,1},\; H_{0,9},\; H_{0,8}\}}$ (capturando $H_{0,8}$, cujo $p$-valor $0{,}006$ era perdido por Bonferroni!).

3. **Item (b) — Rejeições para FDR via Benjamini-Hochberg:**
   - **Para $q = 0{,}05$:** O maior índice $j$ tal que $p_{(j)} \le 0{,}005\,j$ é $L = 5$ ($p_{(5)} = 0{,}017 \le 0{,}025$). Logo, BH rejeita **5 hipóteses nulas**: $\mathbf{\{H_{0,10},\; H_{0,1},\; H_{0,9},\; H_{0,8},\; H_{0,3}\}}$.
   - **Para $q = 0{,}20$:** O maior índice $j$ tal que $p_{(j)} \le 0{,}02\,j$ é $L = 8$ ($p_{(8)} = 0{,}11 \le 0{,}16$). Logo, BH rejeita **8 hipóteses nulas**: $\mathbf{\{H_{0,10},\; H_{0,1},\; H_{0,9},\; H_{0,8},\; H_{0,3},\; H_{0,2},\; H_{0,7},\; H_{0,5}\}}$.

4. **Item (c) — Exemplo para $m = 5$ e $\alpha = 0{,}10$ (Ex. 13.7.5):**  
   Para $m = 5$ e $\alpha = 0{,}10$, o limiar de Bonferroni é $\frac{0{,}10}{5} = 0{,}020$, enquanto os limiares de Holm para $j = 1, 2, 3, 4, 5$ são:
   $$\frac{0{,}10}{5} = 0{,}020, \quad \frac{0{,}10}{4} = 0{,}025, \quad \frac{0{,}10}{3} \approx 0{,}0333, \quad \frac{0{,}10}{2} = 0{,}050, \quad \frac{0{,}10}{1} = 0{,}100.$$
   Escolhendo os $p$-valores:
   $$\mathbf{p_1 = 0{,}010, \quad p_2 = 0{,}022, \quad p_3 = 0{,}030, \quad p_4 = 0{,}045, \quad p_5 = 0{,}500},$$
   Bonferroni rejeita apenas $H_{01}$ ($p_1 = 0{,}010 \le 0{,}020$), enquanto Holm rejeita $H_{01}, H_{02}, H_{03}$ e $H_{04}$ ($4$ hipóteses) controlando exatamente o mesmo FWER $\le 0{,}10$! $\blacksquare$
</details>

---

### Exercício B12.3 *[ISLP, Seção 13.7, Ex. 8e–f — A Armadilha de Cherry-Picking e Reamostragem Permutacional]*
Um analista avalia o desempenho mensal de $m = 100$ gestores de fundos de investimento. Sob a hipótese nula global de que nenhum gestor possui habilidade superior ao acaso ($H_{0j}: \mu_j = 0$ para todo $j = 1, \dots, 100$), o analista seleciona apenas o **melhor gestor observado** na amostra (aquele com o menor $p$-valor individual $p_{(1)} = \min_{1 \le j \le 100} p_j$) e reporta $p_{(1)} = 0{,}008 < 0{,}05$ como prova estatística de que esse gestor bate o mercado.
(a) Calcule a probabilidade exata de observar $\min_{1 \le j \le 100} p_j \le 0{,}008$ sob a hipótese nula global (assumindo independência entre os 100 gestores) e explique por que esse procedimento é falacioso (*cherry-picking* / *data snooping*).  
(b) Qual deveria ser o $p$-valor ajustado de Bonferroni / Šidák para $p_{(1)} = 0{,}008$ entre $m = 100$ gestores?  
(c) Explique como um **teste de permutação (reamostragem)** estima empiricamente a distribuição nula e a FDR quando os preditores ou testes possuem correlações complexas e o tamanho amostral é pequeno.
- **Dica:** Em (a), use $\Pr\big(\min_{1 \le j \le 100} p_j \le x\big) = 1 - \Pr(p_1 > x, \dots, p_{100} > x) = 1 - (1 - x)^{100}$.

<details>
<summary><strong>Ver Resolução Completa Passo a Passo</strong></summary>

1. **Item (a) — A Falácia do *Cherry-Picking* ($p_{(1)} = 0{,}008$ em $m = 100$):**  
   Se todos os $m = 100$ gestores operam puramente ao acaso ($p_j \stackrel{\text{i.i.d.}}{\sim} \operatorname{Uniforme}(0, 1)$), a probabilidade de que **pelo menos um** dos 100 gestores apresente um $p$-valor individual $\le 0{,}008$ é:
   $$\Pr\!\left(\min_{1 \le j \le 100} p_j \le 0{,}008\right) = 1 - (1 - 0{,}008)^{100} = 1 - (0{,}992)^{100} \approx \mathbf{0{,}5521 \;\; (55{,}2\%)}!$$
   Ou seja, mesmo que absolutamente nenhum gestor tenha habilidade real, há mais de **$55\%$ de chance** de o "melhor" gestor de um grupo de $100$ exibir um $p$-valor aparente $\le 0{,}008$. Testar apenas o máximo amostral usando a distribuição nula de uma variável individual sem corrigir pela busca sobre os $m = 100$ candidatos invalida completamente o nível de significância.

2. **Item (b) — $p$-valor Ajustado para $p_{(1)} = 0{,}008$:**
   - **Ajuste de Bonferroni:** $p_{(1)}^{\text{Bonf}} = \min(m \cdot p_{(1)},\; 1) = 100 \times 0{,}008 = \mathbf{0{,}80}$ (totalmente não significativo!).
   - **Ajuste exato de Šidák (sob independência):** $p_{(1)}^{\text{Šidák}} = 1 - (1 - 0{,}008)^{100} \approx \mathbf{0{,}552}$.

3. **Item (c) — Abordagem de Reamostragem Permutacional (Seção 13.5):**  
   Quando a distribuição teórica nula da estatística de teste $T_j$ é desconhecida ($n$ pequeno ou não normalidade) ou há forte correlação entre os $m$ testes, embaralhamos aleatoriamente os rótulos de classe (ou permutamos sinais em amostras pareadas) $B$ vezes ($b = 1, \dots, B$), recalculando as estatísticas $T_j^{*(b)}$ para todas as $m$ variáveis simultaneamente em cada permutação (o que preserva a estrutura de correlação entre as variáveis). Para um limiar $c > 0$, estimamos o número esperado de falsos positivos por $\widehat{\mathbb{E}[V(c)]} = \frac{1}{B}\sum_{b=1}^B \sum_{j=1}^m \mathbb{I}\!\left(|T_j^{*(b)}| \ge c\right)$ e a FDR empírica por $\widehat{\operatorname{FDR}}(c) = \frac{\widehat{\mathbb{E}[V(c)]}}{R(c)}$. $\blacksquare$
</details>
