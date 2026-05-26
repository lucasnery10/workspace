# Aprendizados — Meta Ads Ratos

Regras aprendidas durante o uso. O Claude DEVE ler este arquivo antes de criar qualquer objeto.

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
