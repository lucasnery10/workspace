#!/usr/bin/env python3
"""
Cria ADS 4-6 para Valente Barber - Conjunto 4.1 (Filhos) - MAIO 2026
Mesmo template ADS 1/2/3: 3 textos + 5 headlines + CTA WhatsApp Filhos
Aprimoramentos do Facebook desativados.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import init_api, print_json, safe_delay
from facebook_business.adobjects.adaccount import AdAccount

ACCOUNT_ID = "act_1236585775277124"
ADSET_ID   = "120245040344740482"
PAGE_ID    = "962319483639514"
IG_ID      = "17841420754399626"

VIDEOS = [
    ("ADS 4 - VID - MAIO - Filhos", "1323323319900222", "https://scontent-gru1-2.xx.fbcdn.net/v/t15.5256-10/708215986_2350695185414962_6079684269600835337_n.jpg?stp=dst-jpg_p160x160_tt6&_nc_cat=103&ccb=1-7&_nc_sid=200999&_nc_ohc=s0jThwBMFT0Q7kNvwFryciO&_nc_oc=AdqfsO7QoO5bQE-xCZUb1XcFsTerLt44dzhj2hMDiUlGrdaQJzn3reePCyLtlVnpEBhTcd0Xu_mZmRc2mXQ7iHR0&_nc_zt=23&_nc_ht=scontent-gru1-2.xx&edm=APRAPSkEAAAA&_nc_gid=T04cjlfA8yT-LTv-Q95-yQ&_nc_tpa=Q5bMBQEk6l_WHIVfgisn0tKFDcPUEyB5Fq_u2RZLFGLtfG4_VDzJURvpr_jtlbKFKss6MsSjyh4Iv0hGTg&oh=00_Af51SKfkpVAgtYr6yfuqAQiZApvt9GS9yJMcotwLnnARHQ&oe=6A1CE2FF"),
    ("ADS 5 - VID - MAIO - Filhos", "1478886080645537", "https://scontent-gru2-2.xx.fbcdn.net/v/t15.5256-10/708229504_982282580842112_7183496469064385850_n.jpg?stp=dst-jpg_p160x160_tt6&_nc_cat=102&ccb=1-7&_nc_sid=200999&_nc_ohc=5BbXMgT3dsoQ7kNvwG7L3bk&_nc_oc=AdoOvW7Cibv3IOQw4Ayy-0mgS16AOOrdN2m6_U7Gs7cxYs30hF6DXnPsLEUg5yZZXA4o1LvtBT8Hw9Kd6vv4M04o&_nc_zt=23&_nc_ht=scontent-gru2-2.xx&edm=APRAPSkEAAAA&_nc_gid=Ae3VhLeIWgVdoYSQnCobqg&_nc_tpa=Q5bMBQEOcakF6-AVOxFfV97FR-bvfV79qG5NSAyo-2dO7tgv57l1p0hjC90FfBDqbRn5yPrv39N3lsHJMQ&oh=00_Af6Ic6J8heCfG_0AgNGth21HNSjUFmAokldhuqHvU699rQ&oe=6A1CF261"),
    ("ADS 6 - VID - MAIO - Filhos", "1336534691711306", "https://scontent-gru2-2.xx.fbcdn.net/v/t15.5256-10/707268674_970221392292461_9068870804972329628_n.jpg?stp=dst-jpg_p160x160_tt6&_nc_cat=105&ccb=1-7&_nc_sid=200999&_nc_ohc=-nHzPLrec8IQ7kNvwHYcI5l&_nc_oc=Ado-Qkkjp8rMtL-eDdMVnVMDoSFNDhtusQdaSJ671mtrApQdDqN4YVftPlPRY-sTb7hACIRXD_KnmskjJY5KDGAo&_nc_zt=23&_nc_ht=scontent-gru2-2.xx&edm=APRAPSkEAAAA&_nc_gid=5jJKvu9b43AZsi3iou6ELw&_nc_tpa=Q5bMBQFhvenUwZiMTnVdU7qDN7meJ7Ivx68H7hFK07l8a81bM5O6algddVJAiqSBmvlfpvoCayzUM5IqFQ&oh=00_Af4K7dxFqe6urHZ-9Y7_yw8Vy3IoUTROT4b8kdnOuFYMVw&oe=6A1CD0CE"),
]

PAGE_WELCOME_MESSAGE = json.dumps({
    "type": "VISUAL_EDITOR",
    "version": 2,
    "landing_screen_type": "welcome_message",
    "media_type": "text",
    "text_format": {
        "customer_action_type": "autofill_message",
        "message": {
            "autofill_message": {"content": "Gostaria de agendar um horário para o meu filho, pode me ajudar?"},
            "text": "Seja bem-vindo!\nEm instantes vamos te ajudar a melhorar sua imagem..."
        }
    },
    "image_format": {
        "customer_action_type": "quick_replies",
        "message": {
            "attachment": {"type": "template", "payload": {"template_type": "generic", "elements": [{"title": "", "buttons": [], "image_hash": ""}]}},
            "quick_replies": [{"title": "Gostaria de obter mais informações", "content_type": "text", "response_type": None}],
            "text": "Seja bem-vindo!\nEm instantes vamos te ajudar a melhorar sua imagem..."
        }
    },
    "video_format": {
        "customer_action_type": "quick_replies",
        "message": {
            "attachment": {"type": "video", "payload": {"attachment_id": ""}},
            "quick_replies": [{"title": "Gostaria de obter mais informações", "content_type": "text", "response_type": None}],
            "text": "Seja bem-vindo!\nEm instantes vamos te ajudar a melhorar sua imagem..."
        }
    },
    "ai_generated_icebreaker_toggle_enabled": None,
    "user_edit": True,
    "surface": "visual_editor_new",
    "welcome_message_edited": True,
    "has_ai_generated_welcome_message": False,
    "autofill_message_edited": True,
    "template_id": "954151547395857",
    "is_user_editing": False
})

ASSET_FEED_SPEC = {
    "bodies": [
        {"text": "Nem todo barbeiro sabe atender criança.\n\nE quem é pai e mãe sabe como uma experiência ruim pode transformar a hora do corte em estresse.\n\nAqui na Valente Barber Club, a gente entende cada tipo de cabelo, sabe lidar com os pequenos e ainda cria cortes que facilitam a rotina do dia a dia.\n\nClique no link e agende o horário do seu filho."},
        {"text": "Tem criança que sofre com redemoinho, franja desajustada ou cabelo difícil de arrumar todos os dias.\n\nE no fim, quem sofre junto é o pai e a mãe na correria da escola e da rotina.\n\nNa Valente Barber Club, nossos barbeiros são preparados pra criar cortes que funcionam no dia a dia e deixam o visual alinhado por muito mais tempo.\n\nClique aqui e agende um horário."},
        {"text": "Seu filho gosta de freestyle, risquinho ou cortes mais estilosos?\n\nEntão ele precisa de um barbeiro que realmente domine esse tipo de detalhe.\n\nAqui na Valente Barber Club, cada corte é feito com atenção, técnica e muito cuidado pra deixar o visual exatamente como ele imagina.\n\nClique no link e agende o horário dele."}
    ],
    "titles": [
        {"text": "Seu filho merece uma boa experiência"},
        {"text": "Cortes infantis feitos com cuidado"},
        {"text": "Mais praticidade no dia a dia"},
        {"text": "Especialistas em cortes infantis"},
        {"text": "Freestyle e risquinho é na Valente"}
    ],
    "optimization_type": "DEGREES_OF_FREEDOM"
}

DEGREES_OF_FREEDOM_SPEC = {
    "creative_features_spec": {
        "standard_enhancements": {
            "enroll_status": "OPT_OUT"
        }
    }
}

def main():
    init_api()
    account = AdAccount(ACCOUNT_ID)
    created_ads = []

    for ad_name, video_id, image_url in VIDEOS:
        print(f"\n{'='*60}", file=sys.stderr)
        print(f"Criando: {ad_name}", file=sys.stderr)

        object_story_spec = {
            "page_id": PAGE_ID,
            "instagram_user_id": IG_ID,
            "video_data": {
                "video_id": video_id,
                "image_url": image_url,
                "call_to_action": {
                    "type": "WHATSAPP_MESSAGE",
                    "value": {"app_destination": "WHATSAPP", "link": "https://api.whatsapp.com/send"}
                },
                "page_welcome_message": PAGE_WELCOME_MESSAGE
            }
        }

        creative = account.create_ad_creative(params={
            "name": ad_name,
            "object_story_spec": object_story_spec,
            "asset_feed_spec": ASSET_FEED_SPEC,
        })
        creative_id = creative["id"]
        print(f"  Criativo: {creative_id}", file=sys.stderr)
        safe_delay(1)

        ad = account.create_ad(params={
            "name": ad_name,
            "adset_id": ADSET_ID,
            "creative": {"creative_id": creative_id},
            "status": "PAUSED",
            "degrees_of_freedom_spec": DEGREES_OF_FREEDOM_SPEC,
        })
        ad_id = ad["id"]
        print(f"  Ad: {ad_id} (PAUSED)", file=sys.stderr)
        safe_delay(1)

        created_ads.append({"name": ad_name, "ad_id": ad_id, "creative_id": creative_id})

    print(f"\n{'='*60}", file=sys.stderr)
    print("RESUMO:", file=sys.stderr)
    for item in created_ads:
        print(f"  {item['name']} → {item['ad_id']}", file=sys.stderr)

    print_json(created_ads)

main()
