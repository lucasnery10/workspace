---
name: copy-meta
description: >
  Cria 3 textos principais e 5 headlines para anúncios no Meta Ads com base no
  briefing do cliente e no asset fornecido (imagem estática ou roteiro de vídeo).
  Use quando o usuário pedir "cria copy", "faz os textos do anúncio", "preciso de
  copy pro cliente X", "gera headlines", ou passar uma imagem/roteiro pra anunciar.
---

# /copy-meta — Copy para Meta Ads

## Dependências

- **Briefing do cliente:** `clientes/[cliente]/briefing.md`
- **Tom de voz:** `_contexto/preferencias.md`

---

## Workflow

### Passo 1 — Identificar o cliente e o asset

Se o usuário não informou na chamada, perguntar:

> "Qual cliente é esse? E me manda o asset — pode ser a imagem do anúncio ou o roteiro do vídeo."

Só seguir depois de ter os dois: **nome do cliente** e **asset**.

### Passo 2 — Ler o contexto do cliente

Ler `clientes/[cliente]/briefing.md`.

Se o arquivo não existir ou estiver vazio, avisar:

> "Não encontrei briefing pra esse cliente. Cria o arquivo `clientes/[cliente]/briefing.md` com as informações do negócio, produto e objetivo antes de gerar a copy."

Se existir, extrair:
- Produto/serviço e principal promessa
- Público-alvo (quem é, dor principal, desejo)
- Objetivo da campanha (conversão, tráfego, cadastro, etc.)
- Plataforma e formato do anúncio

### Passo 3 — Analisar o asset

**Se for imagem estática:**
- Identificar o elemento visual principal (produto, pessoa, cenário)
- Identificar se há texto na imagem (headline visual, oferta, CTA)
- A copy deve reforçar — não repetir — o que já está na imagem

**Se for roteiro de vídeo:**
- Identificar o gancho de abertura, a promessa central e o CTA do vídeo
- A copy deve preparar o clique antes do vídeo ser assistido — funciona como "pré-venda" do conteúdo

### Passo 4 — Gerar as copies

Gerar **3 textos principais** com ângulos distintos:

**Texto 1 — Direto ao ponto**
- Abre com o resultado ou benefício principal (sem rodeios)
- Prova ou especificidade que sustenta a promessa
- CTA direto no final
- Tamanho: 3-5 linhas (visível antes do "ver mais")

**Texto 2 — Problema / Solução**
- Primeira linha nomeia a dor ou situação do público (gancho de identificação)
- Apresenta o produto/serviço como solução com clareza
- CTA com senso de próximo passo
- Tamanho: 4-6 linhas

**Texto 3 — Prova social / Desejo**
- Abre com resultado real, número, transformação ou aspiração do público
- Conecta o resultado ao produto de forma crível
- CTA focado em ação imediata
- Tamanho: 4-6 linhas

---

Gerar **5 headlines** com variações:

1. Focada no benefício principal (o que o cliente ganha)
2. Focada no problema que resolve (dor do público)
3. Específica com número ou dado (resultado mensurável)
4. Curiosidade ou pergunta que força o clique
5. Urgência ou escassez (se aplicável ao contexto do cliente)

**Formato das headlines:** 25-40 caracteres. Diretas, sem pontuação desnecessária.

---

**Regras de escrita:**
- Primeira linha de cada texto é o mais importante — é o que aparece antes do "ver mais"
- Não usar emojis excessivos — no máximo 1 por texto, só se o tom do cliente permitir
- Linguagem do público-alvo, não da marca — escrever como o cliente pensa, não como a empresa fala
- Evitar superlativos vazios: "incrível", "revolucionário", "melhor do mercado"
- CTAs específicos: "Acesse o link", "Clique e saiba mais", "Garanta agora" — não "Saiba mais" genérico

### Passo 5 — Apresentar e salvar

Apresentar as copies no formato abaixo antes de salvar:

---

**TEXTOS PRINCIPAIS**

**Texto 1 — Direto ao ponto**
[texto]

**Texto 2 — Problema / Solução**
[texto]

**Texto 3 — Prova social / Desejo**
[texto]

---

**HEADLINES**

1. [headline]
2. [headline]
3. [headline]
4. [headline]
5. [headline]

---

Perguntar:

> "Quer ajustar alguma coisa antes de salvar?"

Se sim, aplicar os ajustes e apresentar novamente.
Se não, salvar em `clientes/[cliente]/copys/copy-[data].md`.

O arquivo salvo deve ter o mesmo formato da apresentação, com cabeçalho:

```
# Copy Meta Ads — [Nome do Cliente]
Data: [data]
Asset: [descrição curta do asset usado]
```

---

## Regras

- Nunca gerar copy sem ler o briefing do cliente primeiro
- Cada texto deve ter ângulo genuinamente diferente — não variações superficiais do mesmo texto
- Tom segue `_contexto/preferencias.md` do operador (Lucas), calibrado ao público do cliente
- Se o briefing estiver vago demais, fazer no máximo 2 perguntas de esclarecimento antes de gerar
- Após salvar, perguntar: "Quer gerar roteiros de vídeo pra esse mesmo cliente agora?"
