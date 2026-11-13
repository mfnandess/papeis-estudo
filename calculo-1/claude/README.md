# Cálculo 1 sem sofrimento (versão Claude)

Paper de estudo de Cálculo I, pensado para leitura no celular e no tablet.

- **Abrir:** `calculo-1/claude/index.html` (no GitHub Pages: `/calculo-1/claude/`)
- **Referência principal:** Guidorizzi, *Um Curso de Cálculo*, Vol. 1, 5ª ed. Capítulos, seções e exercícios citados como `Guidorizzi §x.y` / `Ex. x.y – n`.
- **Referência secundária:** Apostol, *Cálculo I* (Reverté). Sempre marcada em caixas laranja `Apostol §x.y`.
- 14 capítulos, 16 figuras (SVG que acompanham o tema claro/escuro), 16 exemplos resolvidos e 51 exercícios (35 tirados das listas do Guidorizzi, quase todos com vários itens, e 16 extras), com respostas escondidas.

## Editar

O texto fica em `src/paper.html`; as figuras são geradas em `build.py`.
Depois de editar, rode:

```sh
python3 calculo-1/claude/build.py
```

Isso regenera `calculo-1/claude/index.html`. Uma figura é inserida no texto com `{{fig:nome|legenda}}`.
