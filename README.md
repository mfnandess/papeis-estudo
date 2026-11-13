# Papers de Estudo

Materiais de estudo organizados por matéria. Leitura online pelo GitHub Pages: **https://mfnandess.github.io/papeis-estudo/**

## Estrutura

```
papers/
├── index.html                 # portal (lista todas as matérias)
├── calculo-1/
│   ├── guidorizzi/            # paper teórico + caderno de exercícios
│   │   ├── index.html         #   paper (gerado a partir de paper.md)
│   │   ├── exercicios.html    #   exercícios (gerado a partir de exercicios.md)
│   │   ├── paper.md
│   │   ├── exercicios.md
│   │   └── figuras/           #   SVGs usados pelo paper
│   ├── claude/                # versão celular/tablet (ver claude/README.md)
│   └── referencias/           # livros-texto em PDF (só local, ignorado pelo git)
└── machine-learning/
    └── referencias/           # livros-texto em PDF (só local, ignorado pelo git)
```

## Adicionar uma nova matéria

1. Crie `<materia>/` (nome em minúsculas, com hífen: `algebra-linear`, `machine-learning`).
2. Coloque os PDFs de referência em `<materia>/referencias/` — o `.gitignore` já os exclui.
3. Cada paper fica numa subpasta própria (`<materia>/<paper>/index.html`), com suas figuras e fontes dentro dela.
4. Adicione o link no `index.html` da raiz.

## Cálculo I

- **Referência principal:** GUIDORIZZI, H. L. *Um Curso de Cálculo — Vol. 1*. 5ª ed. LTC.
- **Referência complementar:** APOSTOL, T. M. *Cálculo I*. 2ª ed. Reverté.

| Paper | Online |
|---|---|
| Paper teórico (17 capítulos + 6 apêndices, 12 figuras) | [`calculo-1/guidorizzi/`](https://mfnandess.github.io/papeis-estudo/calculo-1/guidorizzi/) |
| Caderno de exercícios (45 resolvidos) | [`calculo-1/guidorizzi/exercicios.html`](https://mfnandess.github.io/papeis-estudo/calculo-1/guidorizzi/exercicios.html) |
| Cálculo 1 sem sofrimento (versão Claude) | [`calculo-1/claude/`](https://mfnandess.github.io/papeis-estudo/calculo-1/claude/) |
