# Guia: Pixel Meta + GTM + Evento WhatsApp em WordPress

Guia completo para instalar o Meta Pixel via Google Tag Manager em sites WordPress e configurar o rastreamento de cliques no WhatsApp como evento de conversão.

Usado com: José Prestes, Nicolli Turqueti, Explore Milão, Okta Filmes (Edu + Okta).

---

## PRÉ-REQUISITOS

- Acesso ao painel WordPress do cliente
- Acesso ao container GTM do cliente (já criado)
- Acesso ao Gerenciador de Eventos do Meta (pixel já criado na conta)
- ID do pixel Meta (número de 15 dígitos visível no Gerenciador de Eventos)

---

## ETAPA 1 — Instalar o GTM no WordPress via WPCode

1. WordPress → **Plugins → Adicionar novo** → pesquisa **WPCode** → instala e ativa
2. No GTM, vai em **Administrador → Instalar o Google Tag Manager**
3. Copia o bloco de código do `<head>`
4. No WordPress, vai em **WPCode → Cabeçalho e Rodapé**
5. Cola o código do `<head>` no campo **Cabeçalho**
6. Copia o bloco de código do `<body>` no GTM
7. Cola no campo **Rodapé** do WPCode
8. Salva

---

## ETAPA 2 — Instalar o Pixel base via GTM

O pixel vai dentro do GTM como tag — não colocar nada direto no HTML do site.

1. GTM → **Tags → Nova**
2. Tipo: **HTML Personalizado**
3. Cole o código abaixo substituindo `SEU_PIXEL_ID` pelo ID do pixel do cliente:

```html
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'SEU_PIXEL_ID');
fbq('track', 'PageView');
</script>
```

4. Acionamento: **Todas as Páginas**
5. Nome da tag: `Meta Pixel - Base`
6. Salva

---

## ETAPA 3 — Configurar o evento de clique no WhatsApp

### Passo 1 — Ativar variáveis de clique
GTM → **Variáveis → Configurar** → ativa:
- `Click Element`
- `Click URL`
- `Click Classes`

### Passo 2 — Criar a variável personalizada
GTM → **Variáveis → Nova → JavaScript personalizado**
- Nome: `É Botão WhatsApp`
- Código:

```javascript
function() {
  var el = {{Click Element}};
  while (el) {
    if (el.tagName === 'A' && el.href && (el.href.indexOf('wa.me') !== -1 || el.href.indexOf('whatsapp.com') !== -1)) {
      return true;
    }
    el = el.parentElement;
  }
  return false;
}
```

Essa variável percorre todos os elementos pai do elemento clicado e verifica se algum é um link `<a>` apontando para `wa.me` ou `api.whatsapp.com`. Funciona independente de classe CSS ou estrutura do site.

**Atenção:** alguns sites usam `api.whatsapp.com/send/` no lugar de `wa.me` — o código acima já cobre os dois formatos. Sempre inspecionar o botão antes de configurar.

### Passo 3 — Criar o acionador
GTM → **Acionadores → Novo**
- Nome: `click_wpp`
- Tipo: **Clique - Todos os elementos**
- Condição: `É Botão WhatsApp` **é igual a** `true`
- Salva

### Passo 4 — Criar a tag do evento
GTM → **Tags → Nova**
- Nome: `tag_wpp`
- Tipo: **HTML Personalizado**
- Código: `<script>fbq("trackCustom","Clique no WhatsApp");</script>`
- Acionamento: `click_wpp`
- Salva

### Passo 5 — Publicar
GTM → **Enviar → Publicar**
Descrição da versão: `"Meta Pixel base + evento WhatsApp"`

---

## ETAPA 4 — Testes

### Teste 1 — GTM Preview
1. GTM → **Preview** → cola a URL do site → Connect
2. Na aba que abrir, clica em um botão de WhatsApp
3. Volta no Tag Assistant e confirma:
   - `Meta Pixel - Base` → **Disparada** na abertura da página
   - `tag_wpp` → **Disparada** ao clicar no WhatsApp

### Teste 2 — Pixel não está bloqueado
1. Abre o site em **aba anônima**
2. DevTools (`Cmd + Option + I`) → aba **Network** → filtra por `facebook`
3. `fbevents.js` com status **200** → OK
4. `fbevents.js` com status **(blocked)** → tem CSP bloqueando

Se estiver bloqueado: WPCode → Cabeçalho e Rodapé → apaga qualquer linha com `Content-Security-Policy` → Salva → testa de novo.

### Teste 3 — Meta Events Manager
1. Gerenciador de Eventos → **Eventos de teste**
2. Cola a URL do site → clica em **"Eventos de Teste"** (abre o site em nova aba)
3. Nessa nova aba, clica em um botão de WhatsApp
4. Volta no Events Manager — confirma se `Clique no WhatsApp` aparece como processado

---

## ETAPA 5 — Verificar domínio no Meta

Se aparecer alerta "Confirme o domínio que pertence a você" no Diagnóstico:

1. Clica em **"Analisar domínio(s)"**
2. Vai em **Configurações → Permissões de tráfego**
3. Remove domínios antigos que não estão mais em uso
4. Adiciona o domínio atual do site
5. Verifica o domínio pelo método disponível (meta tag, arquivo HTML ou registro DNS)

---

## ETAPA 6 — Confirmar o evento personalizado

Após os primeiros disparos reais, o Meta vai exibir um aviso pedindo confirmação do evento `Clique no WhatsApp`.

1. Gerenciador de Eventos → **Visão geral** → localiza o evento com aviso de confirmação
2. Confirma o evento
3. Aguarda 15-30 minutos para ficar disponível nas campanhas

---

## ETAPA 7 — Usar nas campanhas

Meta Ads → criação de campanha → conjunto de anúncios → **Evento de conversão** → seleciona `Clique no WhatsApp`.

Se o evento não aparecer imediatamente após a confirmação, aguarda mais 15-30 minutos.

---

## COMPORTAMENTOS ESPECÍFICOS POR PLUGIN

### Elementor (botão de WhatsApp)
O Elementor não usa `<a>` tag padrão para os botões — ele empurra um evento personalizado para o dataLayer chamado `Compartilhe no WhatsApp`. A variável JS não captura esse caso.

**Acionador correto:**
- Tipo: **Evento personalizado**
- Nome do evento: `Compartilhe no WhatsApp`
- Disparado em: **Todos os eventos personalizados**
- Sem condições adicionais

Confirmar o nome exato do evento no GTM Preview antes de configurar — pode variar conforme versão do plugin.

---

### JoinChat (botão flutuante de WhatsApp)
O JoinChat é um plugin WordPress popular de botão flutuante. Ele usa um `<div role="button">`, não um `<a>` tag — a variável JS não funciona.

O JoinChat empurra o evento `JoinChat` para o dataLayer ao ser clicado.

**Acionador correto:**
- Tipo: **Evento personalizado**
- Nome do evento: `JoinChat`
- Disparado em: **Todos os eventos personalizados**
- Sem condições adicionais

---

### Elementor (formulário)
Formulários do Elementor usam Ajax — a página não recarrega ao enviar. Isso causa dois comportamentos específicos:

1. O evento `form_submit` dispara **duas vezes** no dataLayer (não usar como trigger)
2. O trigger "Envio de formulário" com **"Verificar validação" ativado não funciona** — o Elementor valida via JavaScript, não via HTML5 padrão, então o GTM não consegue confirmar a validação

**Acionador correto para formulários Elementor:**
- Tipo: **Envio de formulário**
- **Desmarcar "Verificar validação"**
- Disparado em: **Todos os formulários**
- Condição obrigatória para salvar: `Page URL` — `contém` — `[domínio do site]`

---

## PROBLEMAS COMUNS

| Problema | Causa | Solução |
|---|---|---|
| Tag não dispara — botão Elementor | Evento é `Compartilhe no WhatsApp`, não clique em link | Usar acionador "Evento personalizado" com esse nome |
| Tag não dispara — botão JoinChat | Botão é `<div>`, não `<a>` | Usar acionador "Evento personalizado" com `JoinChat` |
| Tag não dispara | Botões usam `api.whatsapp.com` em vez de `wa.me` | Variável JS já cobre os dois — verificar se está atualizada |
| `form_submit` dispara 2x | Elementor tem dois listeners no mesmo evento | Usar "Envio de formulário" sem "Verificar validação" |
| "Envio de formulário" não dispara | "Verificar validação" ativado com Elementor | Desmarcar "Verificar validação" |
| `fbevents.js` bloqueado | CSP no WPCode | Remover meta tag CSP do WPCode |
| Pixel duplicado | Pixel no HTML + pixel no GTM | Pausar tag do Pixel no GTM ou remover do HTML |
| Evento não aparece no Events Manager | Ad blocker ativo | Usar aba anônima para testar |
| Evento não aparece na campanha | Ainda processando | Aguardar 15-30 min após confirmar |
| Eventos de teste não aparecem | Domínio não verificado | Adicionar e verificar domínio nas permissões de tráfego |
| Evento some da lista de conversões | Pouco volume de disparo | Acionar o evento manualmente algumas vezes pelo teste |
