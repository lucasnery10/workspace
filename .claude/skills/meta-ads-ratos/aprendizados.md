# Aprendizados — Meta Ads Ratos

Regras aprendidas durante o uso. O Claude DEVE ler este arquivo antes de criar qualquer objeto.

---

### 2026-06-08 — OUTCOME_SALES não suporta Dynamic Creative (is_dynamic_creative)
**Regra:** Nunca criar adset com `is_dynamic_creative: true` em campanhas com objetivo OUTCOME_SALES. A API retorna erro 1885392 ("Objetivo incompatível com anúncios de criativo dinâmico") ao tentar criar o ad. Para testar múltiplas cópias, criar 3 ads separados (um por texto) no mesmo adset, cada um com criativo próprio.
**Contexto:** Eduardo Embraed — campanha de vendas WhatsApp para Tonino Lamborghini. Solução adotada: 3 creatives + 3 ads com object_story_spec/video_data + CTA WHATSAPP_MESSAGE.

### 2026-06-08 — Criativo de vídeo WhatsApp OUTCOME_SALES: usar object_story_spec com video_data
**Regra:** Para campanhas OUTCOME_SALES com destino WhatsApp e vídeo, usar object_story_spec com video_data (video_id + image_url + message + title + call_to_action WHATSAPP_MESSAGE). Não usar asset_feed_spec com ad_formats para esse tipo de campanha — incompatível com OUTCOME_SALES. O instagram_user_id vai como campo top-level no criativo.
**Contexto:** Eduardo Embraed — múltiplas tentativas com AUTOMATIC_FORMAT e SINGLE_VIDEO no asset_feed_spec falharam. O que funcionou foi object_story_spec simples com video_data.

### 2026-06-03 — asset_feed_spec REGULAR exige adset com is_dynamic_creative=true
**Regra:** Para usar `asset_feed_spec` com `optimization_type: REGULAR` (DCO com múltiplos textos/títulos), o adset DEVE ter sido criado com `is_dynamic_creative: true`. Adsets existentes sem essa flag retornam erro 100 subcode 1885553 ao criar o ad. Não há como ativar retroativamente. Para adsets existentes sem DCO, usar criativo simples (single body + title no object_story_spec). O `optimization_type: "CREATIVE"` é inválido — os valores aceitos são: REGULAR, LANGUAGE, PLACEMENT, BRAND, LOCALIZED_PLACEMENTS, FORMAT_AUTOMATION, DOF_MESSAGING_DESTINATION, ACO_AUTOFLOW, MULTI_CREATOR, UNIFIED_PROFILE_VISIT_DESTINATION.
**Contexto:** Papa Leone JUN/2026 — tentativa de criar criativos DCO com 3 textos + 5 headlines falhou nos adsets existentes. Solução: criativo simples com texto principal e headline primária.

---

### 2026-06-03 — Nomenclatura de ads Papa Leone — promoções especiais
**Regra:** Ads de promoção/campanha especial (Happy Hour, promoção semanal, etc.) devem seguir o padrão: `ADS XX - VID - [MÊS] - (promoção [dia])`. Ex: `ADS XX - VID - JUN - (promoção terça)`. Usar "XX" no lugar do número sequencial quando o ad é uma promoção fora da sequência regular de criativos.
**Contexto:** Papa Leone — ads de Happy Hour 10% off criados em JUN/2026. Nomenclatura corrigida pelo usuário após criação.

---

### 2026-04-03 — Sempre incluir CTA no criativo
**Regra:** Ao criar criativos (create.py creative), SEMPRE incluir call_to_action_type. Padrão: LEARN_MORE pra tráfego, SIGN_UP pra leads, SHOP_NOW pra vendas. Nunca criar criativo sem CTA.
**Contexto:** Criou carrossel sem botão de CTA. Usuário teve que corrigir manualmente.

### 2026-04-03 — Carrossel Instagram: multi_share_end_card=false
**Regra:** Em campanhas de visita ao perfil Instagram, SEMPRE usar multi_share_end_card=false e multi_share_optimized=false no criativo.
**Contexto:** Cartão "Ver mais" sem URL quebrou o anúncio em 10 posicionamentos. O end_card exige uma URL de destino que não existe em campanhas de perfil.

### 2026-04-03 — Sempre passar instagram_user_id no criativo
**Regra:** Ao criar criativos pra Instagram, SEMPRE usar --instagram-user-id com o ID da conta Instagram do cliente (do contas.yaml).
**Contexto:** Sem instagram_user_id, o ad não publica no Instagram. Erro: "Seu anúncio deve ser associado a uma conta do Instagram."

### 2026-04-03 — Desligar format options em carrosséis
**Regra:** Ao criar ads de carrossel, SEMPRE passar --degrees-of-freedom-spec com OPT_OUT pra carousel_to_video, image_touchups e standard_enhancements.
**Contexto:** "Blocos de coleção" e "mídia única" distorcem o carrossel sequencial. Desligar pra manter ordem dos slides.

### 2026-05-26 — Objetivo de campanha para WhatsApp: OUTCOME_SALES > OUTCOME_ENGAGEMENT
**Regra:** Para campanhas com objetivo real de conversas no WhatsApp, usar OUTCOME_SALES com otimização CONVERSATIONS. Nunca usar OUTCOME_ENGAGEMENT pra esse fim — o sinal fica sujo (Meta tenta maximizar engajamento de post junto com conversas).
**Contexto:** C07 das Lojas Piana usava OUTCOME_ENGAGEMENT + CONVERSATIONS. 1.694 engajamentos de post vs apenas 23 conversas — taxa de conversão de engajamento para conversa de 1,36%. Objetivo desalinhado dilui o sinal de otimização.

### 2026-05-26 — App Meta deve estar em modo Live para criar ads de imagem
**Regra:** Para criar criativos com `link_data` (dark posts de imagem), o app Meta DEVE estar em modo Live no developers.facebook.com. Ads de vídeo (`video_data`) não exigem isso — por isso campanhas com vídeo funcionam mesmo com app em Development.
**Contexto:** Papa Leone — `link_data` retornava erro 1885183 ("app em modo desenvolvimento"). Vídeos das Lojas Piana funcionavam pois usam `video_data`. Solução: publicar o app no Meta Developer Dashboard.

### 2026-05-26 — asset_feed_spec com placement customization exige is_dynamic_creative no adset
**Regra:** `asset_feed_spec` com `asset_customization_rules` (imagem diferente por posicionamento Story vs Feed) EXIGE que o adset tenha sido criado com `is_dynamic_creative: true`. Adsets existentes sem essa flag retornam erro 100 subcode 2490497. Não há como ativar retroativamente — é necessário criar novos adsets.
**Contexto:** Papa Leone — tentativa de usar Story (9:16) e Feed (4:5) separados no mesmo criativo foi bloqueada. Solução temporária: criar criativo com imagem Feed (4:5) única para todos os posicionamentos. Para fazer certinho, criar adsets novos com `is_dynamic_creative: true`.

### 2026-05-26 — CBO pode travar orçamento no criativo errado
**Regra:** Em ad sets com CBO e múltiplos criativos, monitorar distribuição de gasto nas primeiras 72h. Se um criativo dominar >60% do orçamento com CTR abaixo da média dos outros, pausá-lo e forçar redistribuição.
**Contexto:** AdSet 01 da C07 (Lojas Piana): ADS 6 consumiu 74% do gasto com CTR 1,47%, enquanto ADS 5 (CTR 3,20%) e ADS 4 (CTR 2,51%) mal saíram do lugar. Pausar ADS 6 e ADS 8 redistribuiu orçamento para os criativos mais eficientes.

### 2026-05-26 — Criativo de vídeo exige thumbnail (image_url ou image_hash)
**Regra:** Ao criar criativos com `video_data` em `object_story_spec`, SEMPRE incluir `image_url` ou `image_hash` no `video_data`. Sem eles, a API retorna erro 100 subcode 1443226 ("Seu anúncio precisa de uma miniatura de vídeo"). Para obter a thumbnail automaticamente: após o upload, buscar `picture` do vídeo com `AdVideo(id).api_get(fields=['picture'])` e usar o valor como `image_url`.
**Contexto:** Valente Barber — criação de ADS 9-12 falhou na primeira tentativa por falta de thumbnail. Solução: buscar `picture` de cada vídeo logo após o upload e incluir no criativo.

### 2026-05-26 — Upload de vídeo local: usar upload_local_video.py
**Regra:** O `create.py video` só aceita `--url` (URL pública). Para arquivos locais (.mp4, .mov, etc.), usar `scripts/upload_local_video.py --account act_XXX --file /caminho/do/video.mp4 --name "Nome"`. O script usa `AdVideo(parent_id).remote_create()` com `filepath`. Retorna o `video_id` que deve ser usado na criação do criativo.
**Contexto:** Valente Barber — vídeos em `/Downloads/` não podiam ser enviados via URL. Script criado em 2026-05-26.

### 2026-05-27 — Fluxo padrão de renovação de vídeos (substituir criativos em conjunto existente)
**Regra:** Quando o cliente envia novos vídeos para substituir criativos ativos, seguir este fluxo:
1. Ler os ads do conjunto: `read.py ads-by-adset --adset ID`
2. Ler o criativo de um ad para pegar `asset_feed_spec` completo (3 textos + 5 headlines): `read.py creative --id ID --fields "id,asset_feed_spec,object_story_spec,body,title,call_to_action_type"`
3. Fazer upload de cada vídeo: `upload_local_video.py --account act_XXX --file /caminho.MOV --name "Nome"`
4. Buscar thumbnail de cada vídeo: `AdVideo(id).api_get(fields=['picture'])` — se retornar `rsrc.php` (GIF de loading), aguardar com loop `until` antes de continuar
5. Criar criativo com `object_story_spec` (page_id, instagram_user_id, video_data com video_id + image_url + CTA + page_welcome_message) + `asset_feed_spec` (bodies + titles + optimization_type)
6. Criar ad com `status: PAUSED` e `degrees_of_freedom_spec: {creative_features_spec: {standard_enhancements: {enroll_status: OPT_OUT}}}`
7. Ativar novos ads; pausar os antigos se for substituição completa
**Contexto:** Usado em Valente Barber (ADS 9-12 na C03 e ADS 4-6 na C04) em 2026-05-27. Padrão replicável para qualquer cliente.

### 2026-05-27 — duplicate-adset NÃO copia os ads do conjunto
**Regra:** `advanced.py duplicate-adset` copia apenas a estrutura do ad set (targeting, budget, optimization_goal, etc.). Os ads dentro do conjunto original NÃO são copiados. Após duplicar, criar os ads manualmente no novo conjunto com os criativos desejados.
**Contexto:** Valente Barber C04 — conjunto "04" duplicado para "4.1". Os ads ADS 1, 2, 3 permaneceram no conjunto original; ADS 4, 5, 6 foram criados do zero no conjunto 4.1 com os novos vídeos.

### 2026-05-28 — Upload de imagem local: usar upload_local_image.py
**Regra:** O `create.py image` só aceita `--url` (URL pública). Para arquivos locais (.jpeg, .png, etc.), usar `scripts/upload_local_image.py --account act_XXX --file /caminho/da/imagem.jpeg --name "Nome"`. O script usa `AdImage(parent_id).remote_create()` com `filename`. Retorna o `hash` que deve ser usado na criação do criativo.
**Contexto:** Arcari Odontologia — imagens estáticas de implantes (ADS 7, 7.1, 8, 8.1) em `/Downloads/`. Script criado em 2026-05-28.

### 2026-05-28 — asset_customization_rules não aceita hash duplicado
**Regra:** No `asset_feed_spec` com `asset_customization_rules`, NUNCA usar o mesmo hash de imagem em dois itens do array `images`. A API retorna erro 100 subcode 1815629 ("Valor duplicado"). Solução: usar apenas 2 regras de placement quando há só 2 imagens distintas (story e feed) — regra 1: story/reels, regra 2: fallback (customization_spec vazio).
**Contexto:** Arcari Odontologia — tentativa de usar feed hash como feed + fallback causou erro. Solução: eliminar regra de fallback redundante ou usar imagem diferente para cada regra.

### 2026-05-28 — Detectar formato de imagem pela proporção, não pelo nome do arquivo
**Regra:** Nunca assumir qual imagem é feed e qual é story pelo nome do arquivo (ex: "7" = feed, "7.1" = story não é um padrão garantido). SEMPRE verificar as dimensões reais de cada arquivo antes de criar o criativo. Imagem com proporção 9:16 (altura > largura) → story/reels. Imagem com proporção 4:5, 1:1 ou paisagem → feed. Usar `python3 -c "from PIL import Image; img=Image.open('/path'); print(img.size)"` ou equivalente para checar antes de montar o asset_feed_spec.
**Contexto:** Arcari Odontologia — ADS 7 e ADS 8 de facetas foram criados com feed e story trocados. Usuário corrigiu manualmente. A origem do erro foi assumir padrão de nomenclatura que não é fixo.

### 2026-05-28 — Criar ads sempre PAUSED, ativar somente com comando explícito
**Regra:** SEMPRE criar ads com `status: PAUSED`. Nunca ativar ads automaticamente após a criação — aguardar comando explícito do usuário ("pode ativar", "publica", "deixa ativo"). Só após a confirmação do usuário ativar: adset → ads, nessa ordem.
**Contexto:** Fluxo definido pelo usuário em 2026-05-28. O usuário precisa revisar os criativos antes de publicar para garantir que tudo está correto.

### 2026-05-28 — Fluxo completo para criar anúncio estático com placement feed+story
**Regra:** Para criar 1 ad estático com versão feed (4:5 ou 1:1) e story (9:16), usar `asset_feed_spec` com `optimization_type: "PLACEMENT"` e 2 `asset_customization_rules`:
1. Upload imagens com `upload_local_image.py` → obter hash de cada versão
2. Gerar labels únicos com `uuid.uuid4().hex[:12]` — usar prefixos `l_story_`, `l_feed_`, etc.
3. Criar criativo com `object_story_spec` (page_id + instagram_user_id apenas) + `asset_feed_spec` (2 imagens com labels, bodies, titles, link_urls, customization_rules: story/reels → L_story, fallback `{}` → L_feed)
4. Criar ad com `status: PAUSED` + `degrees_of_freedom_spec` OPT_OUT
**Contexto:** Arcari Odontologia — ADS 7 e ADS 8 criados em 2026-05-28. Cada ad usa imagem feed (7.jpeg) para todos os posicionamentos exceto story/reels, que usa a versão 7.1.jpeg.

### 2026-06-03 — Criar campanha OUTCOME_SALES requer is_adset_budget_sharing_enabled
**Regra:** Ao criar campanha com `OUTCOME_SALES` via API, SEMPRE incluir `is_adset_budget_sharing_enabled: False` (ABO) ou `True` (CBO). Sem esse campo a API retorna erro 100 subcode 4834011.
**Contexto:** Sorria Mais — duplicate-campaign e create_campaign falhavam com esse erro. Solução: adicionar o campo na criação.

### 2026-06-03 — Criar adset WhatsApp requer promoted_object com page_id
**Regra:** Ao criar adset com `destination_type: WHATSAPP`, SEMPRE incluir `promoted_object: {"page_id": "PAGE_ID"}`. Sem isso retorna erro 100 subcode 1815807.
**Contexto:** Sorria Mais — adset de facetas falhava sem o promoted_object.

### 2026-06-03 — degrees_of_freedom_spec: standard_enhancements foi descontinuado
**Regra:** Remover `standard_enhancements` do `creative_features_spec` no `degrees_of_freedom_spec`. O campo foi descontinuado e retorna erro 100 subcode 3858504 ao criar criativos. Definir apenas os recursos individuais (advantage_plus_creative, cv_transformation, enhance_cta, image_touchups, etc.).
**Contexto:** Sorria Mais — todos os criativos novos falhavam com esse campo presente.

### 2026-06-03 — Nome do ad estático usa só o número base, sem o .1
**Regra:** Ao nomear ads estáticos com feed + story (ex: ADS 4 feed + ADS 4.1 story), o nome do ad deve ser apenas o número base: "ADS 4 - EST - JUN - IMPLANTES". Não usar "ADS 4+4.1" nem "ADS 4.1". Isso vale para qualquer conta e qualquer campanha.
**Contexto:** Definido pelo usuário em 2026-06-03 após subida da Sorria Mais.

### 2026-06-03 — asset_feed_spec PLACEMENT exige ad_formats e labels em bodies/titles/link_urls
**Regra:** No `asset_feed_spec` com `optimization_type: PLACEMENT` e `asset_customization_rules`:
1. Incluir `"ad_formats": ["AUTOMATIC_FORMAT"]` (sem isso: erro 1885374)
2. Cada body, title e link_url DEVE ter `adlabels` com um label compartilhado
3. Cada `asset_customization_rule` DEVE incluir `body_label`, `title_label` e `link_url_label` além do `image_label`
4. Ambas as regras (story + fallback) podem referenciar os MESMOS labels de body/title/link_url
**Contexto:** Sorria Mais — erros 1885374, 1885878 ao criar estáticos com story+feed. Solução usada com sucesso em 2026-06-03.

### 2026-06-08 — OUTCOME_SALES + CONVERSATIONS exige bid_strategy explícito no adset
**Regra:** Ao criar adset com `optimization_goal: CONVERSATIONS` dentro de campanha `OUTCOME_SALES`, SEMPRE incluir `bid_strategy: LOWEST_COST_WITHOUT_CAP`. Sem esse campo a API retorna erro 100 subcode 2490487 ("valor ou restrições de lance obrigatórios").
**Contexto:** Lojas Piana C08 — adset de Dia dos Namorados falhava sem o bid_strategy. Solução: adicionar o campo explicitamente.

---

### 2026-06-08 — asset_feed_spec REGULAR com vídeo exige vídeo referenciado no feed spec
**Regra:** Ao criar criativo com `asset_feed_spec` + `optimization_type: REGULAR` e vídeo, o vídeo DEVE aparecer no próprio `asset_feed_spec` (dentro de `videos` ou similar), além do `object_story_spec`. Referenciar apenas no `object_story_spec` retorna erro 1885373 ("É necessário pelo menos 1 images or videos para o formato AUTOMATIC_FORMAT").
**Contexto:** Lojas Piana C08 — tentativa de criar criativo DCO com 3 textos + 5 headlines + vídeo falhou. O vídeo estava só no object_story_spec, não no asset_feed_spec.

---

### 2026-06-08 — Fluxo para duplicar conjunto e trocar público + vídeos
**Regra:** Quando precisar criar variação de conjunto com público diferente e novos criativos:
1. `advanced.py duplicate-adset --id ID --name "novo nome"` → retorna novo adset_id
2. `update.py adset --id NOVO_ID --targeting '{...}'` com os novos parâmetros de público (genders, age_min, age_max, geo)
3. Seguir o fluxo padrão de renovação de vídeos (ver regra acima) para criar os ads no novo conjunto
4. Ativar o conjunto: `update.py adset --id NOVO_ID --status ACTIVE`
O conjunto original permanece intacto e ativo.
**Contexto:** Valente Barber C04 — conjunto "04" (feminino, 27-60) duplicado para "4.1" (ambos, 25-55) com 3 novos criativos de vídeo.
