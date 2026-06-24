# Lucas Nery — Claude Code OS

## O que é esse workspace

Workspace de trabalho de Lucas Nery, freelancer de tráfego pago e copywriting. Aqui ficam clientes, entregas, roteiros, estratégias e ferramentas de trabalho.

**Estrutura de pastas:**
- `_contexto/` — memória do sistema (não apagar)
- `clientes/` — organizado em três grupos:
  - `Grupo TR/` — clientes da agência Grupo TR
    - `explore-milao/` — passeios e transfers premium em Milão
    - `nicolli/` — fotografia em Milão e Lago di Como
    - `robson-oliveira-arq/` — arquitetura
    - `jose-prestes/`
    - `okta-filmes/` — produtora audiovisual, Florianópolis/SC (Google Ads ativo)
    - `pizzaria-papa-leone/` — pizzaria food service, Chapecó/SC (Meta Ads + Google Ads)
    - `walter-matos/` — fotografia de casamento documental, Aracaju/SE (Meta Ads)
    - `lar-art-maison/` — fotografia, velas artesanais e eventos íntimos, Munique/Alemanha (Meta Ads)
    - `nathalia-acahu/` — fotografia de parto e gestantes, Baixada Santista/SP (Meta Ads)
  - `Create/` — clientes da agência Create
    - `sorria-mais/` — clínica odontológica, Joaçaba/SC (implantes e facetas)
    - `arcari-odontologia/` — clínica odontológica premium, Chapecó/SC (implantes e facetas)
    - `barbearia-portugal/` — barbearia masculina premium (agendamentos via Meta Ads)
    - `rama-odontologia/` — clínica odontológica, Chapecó/SC (implantes, facetas, clareamento)
    - `valente-barber/` — barbearia + curso de barbeiro, Videira/SC
    - `ludik/` — marca de cosméticos masculinos para barbearias
    - `ancoras-tattoo/` — estúdio de tatuagem e piercing premium, Cascavel/PR
    - `comel-construcoes/` — engenharia civil e construção, obras residenciais completas
    - `cacau-show/` — loja física Cacau Show, chocolates e presentes, Chapecó/SC
    - `usaflex/` — loja física Usaflex, calçados e bolsas femininos, Chapecó/SC
  - `Meus Clientes/` — clientes próprios (fora de agência)
    - `lojas-piana/`, `essencialmed/`, `matheus-grando/`, `pixel-perfect/`, `fabricio-revest-decor/`
    - `eduardo-embraed/` — corretor de imóveis da Embraed, Balneário Camboriú/SC (Meta Ads ativo)
- `conteudo/` — produção de roteiros, copys e estratégias
- `tarefas.md` — controle de pendências operacionais (MCPs a instalar, tarefas por cliente)

- `templates/` — modelos reutilizáveis
- `dados/` — arquivos para análise (CSV, PDF, relatórios de plataforma)
- `templates/skills/` — templates de skills prontos pra personalizar com /mapear
- `templates/ferramentas/catalogo.md` — APIs e ferramentas disponíveis pra usar em skills

## Sobre o negócio

Lucas Nery, freelancer de gestão de tráfego pago e copywriting. Atende clientes externos com foco em Meta Ads e Google Ads, produzindo relatórios de performance, copies, roteiros para anúncios e estratégias de campanha.

## O que mais fazemos aqui

- Gestão de campanhas no Meta Ads e Google Ads
- Criação de copies e roteiros para anúncios
- Relatórios de performance de campanha
- Desenvolvimento de estratégias de mídia paga

## Clientes e contexto

Atende clientes externos. Trabalha solo.

## Tom de voz

Direto, lógico, estruturado e orientado à execução. Respostas práticas com hierarquia clara. Análise crítica com identificação de riscos e contrapontos — sem validação automática de ideias. Linguagem simples e profissional, sem clichês ou frases motivacionais.

Evitar: abstrações desnecessárias, explicações longas sem aplicação prática, validação automática, frases genéricas motivacionais.

## Ferramentas conectadas

- [x] Meta Ads (skill meta-ads-ratos — SDK facebook-business, token válido até 17/07/2026)
- [x] Google Ads (skill google-ads-ratos — SDK google-ads, OAuth configurado em 19/05/2026, token renovado em 03/06/2026)
- [ ] Google Drive
- [ ] WhatsApp
- [ ] Gmail
- [ ] Google Calendar

*(Marcar conforme for instalando os MCPs)*

## Skills instaladas

- `find-skills` — localiza skills disponíveis no registro (instalada via `npx skills add`)
- `meta-ads-ratos` — gestão completa de campanhas via SDK (leitura, criação, insights, duplicação)
- `google-ads-ratos` — gestão completa de Google Ads via SDK (leitura, criação, insights, GAQL)
- `ads-ratos` — diagnóstico, relatório, auditoria e estratégia com benchmarks brasileiros e Health Score (global)
- `copy-meta` — cria 3 textos principais e 5 headlines para anúncios no Meta Ads com base em briefing e asset
- `novo-projeto` — cria nova pasta de projeto com CLAUDE.md personalizado via entrevista guiada

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (se existirem e estiverem configurados):

1. `_contexto/empresa.md` — quem é o usuário, o que faz, como funciona o negócio
2. `_contexto/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_contexto/estrategia.md` — foco atual, prioridades, o que pode esperar

Usar essas informações como base pra qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considerar o foco atual descrito em `estrategia.md`.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas usar o contexto naturalmente.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe uma skill relevante em `.claude/skills/` ou `.claude/commands/`.
Se encontrar, seguir as instruções da skill.
Se não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível (o usuário provavelmente vai pedir de novo no futuro), perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o padrão de repetição for claro.

---

## Aprender com correções

Quando o usuário corrigir algo, melhorar uma resposta ou dar uma instrução que parece permanente (frases como "na verdade é assim", "não faça mais isso", "prefiro assim", "sempre que...", "evita...", "da próxima vez..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde faz mais sentido salvar:

- **Sobre o negócio** (quem são os clientes, como funciona a empresa, serviços, mercado) → adicionar em `_contexto/empresa.md`
- **Sobre preferências e estilo** (tom de voz, formato de resposta, o que evitar, como estruturar textos) → adicionar em `_contexto/preferencias.md`
- **Sobre prioridades e foco atual** (projetos em andamento, metas do momento, prazos importantes, o que é prioridade agora) → adicionar em `_contexto/estrategia.md`
- **Regra de comportamento nessa pasta** (onde salvar arquivos, como nomear, fluxos específicos) → adicionar no próprio `CLAUDE.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro. Confirmar o que foi salvo mostrando a linha adicionada.

Não perguntar se a correção for óbvia de contexto imediato (ex: "na verdade o arquivo se chama X"). Só perguntar quando a informação tiver valor duradouro.

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante no projeto (novo cliente, nova skill, mudança de foco, novo processo, ferramenta instalada, estrutura de pastas alterada), perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize os arquivos de memória?"

Se sim, identificar o que precisa atualizar:

- **Novo cliente, serviço, ferramenta, equipe** → `_contexto/empresa.md`
- **Mudança de prioridade ou foco** → `_contexto/estrategia.md`
- **Correção de tom ou estilo** → `_contexto/preferencias.md`
- **Nova pasta, regra de organização, skill criada** → `CLAUDE.md`
- **Mudança visual (cores, fontes, logo)** → `marca/design-guide.md`

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo inteiro, só adicionar ou editar a linha relevante.

**Quando NÃO perguntar:**
- Tarefas pontuais que não mudam o contexto (ex: escrever um email, criar um post avulso)
- Perguntas simples ou conversas sem ação
- Mudanças que já foram salvas pelo bloco "Aprender com correções"

**Dica:** se não sabe se algo mudou, rode `/atualizar` pra uma varredura completa.

---

## Onboarding de novo cliente — IDs Meta Ads

Ao concluir o `/novo-projeto` para um cliente, sempre enviar esta mensagem exatamente assim (sem nenhum texto adicional):

```
ID da conta: 
ID da página: 
ID do instagram: 
@ do instagram: 
```

O usuário vai copiar e mandar pro cliente. Quando os dados voltarem, cadastrar no `contas.yaml` da skill meta-ads-ratos e atualizar o `CLAUDE.md` do cliente.

---

## Criação de skills

Quando o usuário pedir pra criar uma nova skill:

1. Verificar se existe um template relevante em `templates/skills/`. Se existir, usar como base e adaptar pro contexto do usuário
2. Perguntar: "Essa skill é específica pra esse projeto ou vai ser útil em qualquer projeto?"
   - Específica desse negócio → salvar em `.claude/skills/nome-da-skill/SKILL.md` (local)
   - Útil em qualquer projeto → salvar em `~/.claude/skills/nome-da-skill/SKILL.md` (global)
3. Ler `_contexto/empresa.md` e `_contexto/preferencias.md` pra calibrar o conteúdo da skill ao contexto do negócio
4. Se a skill precisar de arquivos de apoio (templates, referências, exemplos), criar dentro da pasta da skill
5. Seguir o fluxo da skill-creator nativa do Claude Code
