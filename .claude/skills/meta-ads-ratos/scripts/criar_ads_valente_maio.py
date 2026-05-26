#!/usr/bin/env python3
"""
Cria ADS 9-12 para Valente Barber - Conjunto 3.1 - MAIO 2026
Mesmo template ADS 7/8: 3 textos + 5 headlines + CTA WhatsApp
Todos os aprimoramentos do Facebook desativados.
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import init_api, print_json, safe_delay
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad

ACCOUNT_ID = "act_1236585775277124"
ADSET_ID   = "120244060639060482"
PAGE_ID    = "962319483639514"
IG_ID      = "17841420754399626"

# IDs dos vídeos enviados + thumbnails auto-geradas
VIDEOS = [
    ("ADS 9 - VID - MAIO - Agendamento",  "1602870264107492",  "https://scontent-gru2-1.xx.fbcdn.net/v/t15.5256-10/706719140_2258494551626039_8729842586514785314_n.jpg?stp=dst-jpg_p160x160_tt6&_nc_cat=111&ccb=1-7&_nc_sid=200999&_nc_ohc=-5U7A4jrBfsQ7kNvwGInYgr&_nc_oc=AdpWt_ptqFukrERXaGokFs-vZimBsaFXWphDDQYXf4ykrJ--8rhrdwlUbQa25ryXeKquQn6KvrKqS9sXZg_OTVpq&_nc_zt=23&_nc_ht=scontent-gru2-1.xx&edm=APRAPSkEAAAA&_nc_gid=_1MvhM9LSxaViFQEipn1Gw&_nc_tpa=Q5bMBQF2UW4shEg3Rc4lOCxTa0sorz0uWSk-kw2DOAQv6Rh2IvnE_C3YHGlwHgHOL8v6IgahMzFudnqHfg&oh=00_Af5nsIYNdu0uzAm-P1Sd09bUD2dMac4ForYR5HRVtdcoHA&oe=6A1BDC84"),
    ("ADS 10 - VID - MAIO - Agendamento", "1304112655258413",  "https://scontent-gru2-1.xx.fbcdn.net/v/t15.5256-10/706744452_1355818173067725_7029663512637197699_n.jpg?stp=dst-jpg_p160x160_tt6&_nc_cat=109&ccb=1-7&_nc_sid=200999&_nc_ohc=HdRnpq3vzycQ7kNvwGapuFM&_nc_oc=AdqcfugqyX54VSEDTkL7b3qjaRdE2XzmIoJzzhCFzmFRFdexSE_liZRbR51EYLz_35UJG3eU5xKI9_5dfplO9dZI&_nc_zt=23&_nc_ht=scontent-gru2-1.xx&edm=APRAPSkEAAAA&_nc_gid=OUbm11yq10V02hZrJZBg4g&_nc_tpa=Q5bMBQGZjrvtMxQBV0934VGnU-BT_cJPt2YreEcI25K17580mLUBlbZMPYYDWlvwHj4JQo2li-WU-5rabg&oh=00_Af4598FNce0900izBd6ocWz6rAWW_XVGODLVvvF3-xdhEw&oe=6A1BD5B4"),
    ("ADS 11 - VID - MAIO - Agendamento", "1642241087036561",  "https://scontent-gru1-2.xx.fbcdn.net/v/t15.5256-10/705717925_1009870644833937_5742380385934046697_n.jpg?stp=dst-jpg_p160x160_tt6&_nc_cat=103&ccb=1-7&_nc_sid=200999&_nc_ohc=3-urSTPEQTkQ7kNvwG9cK83&_nc_oc=AdrQ5yNLv4eIhcZbbe0GU4lPtJMHAtcZ3X7G-q9b4rPEv9xdpB5AMktzLlW8uZ6zMO3aVyJ90uIunoYa8fdN11Mu&_nc_zt=23&_nc_ht=scontent-gru1-2.xx&edm=APRAPSkEAAAA&_nc_gid=MM7C9gc-vR9nVJskrbKj7Q&_nc_tpa=Q5bMBQE6Nbufn7SOmKgR5XizM8DGnFyB9nsZmbp1yW_1FG1z49jVy_QWGU-SvsSNF9V2-Nyt_UUEX7Z7VQ&oh=00_Af6BUZVHWowuy27y26N94mOwst4fM0rK7s80iFDGuytQQg&oe=6A1BB5E8"),
    ("ADS 12 - VID - MAIO - Agendamento", "983587380884923",   "https://scontent-gru2-2.xx.fbcdn.net/v/t15.5256-10/708363075_2161477877758086_5956158891973236283_n.jpg?stp=dst-jpg_p160x160_tt6&_nc_cat=102&ccb=1-7&_nc_sid=200999&_nc_ohc=tgzED0clGX4Q7kNvwE22OFn&_nc_oc=AdoK10vYqVn0o95YedZc6TC4ayn9MEYJ4SZgKT8TG-tV-GO5CNm09xOyojdcLz4JRtXw8oonKG9RlYAjEF2HU6ZT&_nc_zt=23&_nc_ht=scontent-gru2-2.xx&edm=APRAPSkEAAAA&_nc_gid=_f23eeDWIPfqeH6DcP6IKA&_nc_tpa=Q5bMBQE03cAp_LQYKbnRwc6p4BuglWyuHsTOSW9PrCCrtpryIiWsaHXlrETMKaJuC6XMwG9VKQaJifMmOw&oh=00_Af7TP3BnLR-lwP3K40u8JXMW4fbLyXwUghvsLBnB6z8K9Q&oe=6A1BE50F"),
]

PAGE_WELCOME_MESSAGE = json.dumps({
    "type": "VISUAL_EDITOR",
    "version": 2,
    "landing_screen_type": "welcome_message",
    "media_type": "text",
    "text_format": {
        "customer_action_type": "autofill_message",
        "message": {
            "autofill_message": {"content": "Gostaria de agendar um horário, pode me ajudar?"},
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
    "template_id": "2274638112946414",
    "is_user_editing": False
})

ASSET_FEED_SPEC = {
    "bodies": [
        {"text": "A forma como você se apresenta muda completamente a forma como as pessoas te enxergam.\n\nNa Valente Barber Club, você consegue manter seu visual alinhado com praticidade, liberdade e um atendimento pensado na rotina do homem moderno.\n\nAgende seu horário em poucos segundos pelo aplicativo, WhatsApp ou Instagram. Sua imagem merece esse cuidado."},
        {"text": "Tem homem que deixa pra cortar o cabelo só quando já perdeu totalmente o alinhamento.\n\nAqui na Valente Barber Club, sua rotina funciona diferente. Nossa agenda fica disponível 24 horas por dia, 7 dias por semana, pra você agendar quando quiser e do jeito mais fácil possível.\n\nClique aqui e mantenha sua imagem sempre alinhada."},
        {"text": "Seu corte não é só estética.\n\nEle transmite presença, cuidado e a forma como você se posiciona no dia a dia.\n\nNa Valente Barber Club, você agenda rápido, sem complicação, e mantém seu visual alinhado sempre que precisar.\n\nClique no link e agende seu horário."}
    ],
    "titles": [
        {"text": "Sua imagem fala antes de você"},
        {"text": "Agenda aberta 24h por dia"},
        {"text": "Mantenha seu visual sempre alinhado"},
        {"text": "Agende seu horário em segundos"},
        {"text": "O homem moderno precisa de praticidade"}
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

        # --- 1. Criativo ---
        object_story_spec = {
            "page_id": PAGE_ID,
            "instagram_user_id": IG_ID,
            "video_data": {
                "video_id": video_id,
                "image_url": image_url,
                "call_to_action": {
                    "type": "WHATSAPP_MESSAGE",
                    "value": {
                        "app_destination": "WHATSAPP",
                        "link": "https://api.whatsapp.com/send"
                    }
                },
                "page_welcome_message": PAGE_WELCOME_MESSAGE
            }
        }

        creative_params = {
            "name": ad_name,
            "object_story_spec": object_story_spec,
            "asset_feed_spec": ASSET_FEED_SPEC,
        }

        creative = account.create_ad_creative(params=creative_params)
        creative_id = creative["id"]
        print(f"  Criativo criado: {creative_id}", file=sys.stderr)
        safe_delay(1)

        # --- 2. Ad ---
        ad_params = {
            "name": ad_name,
            "adset_id": ADSET_ID,
            "creative": {"creative_id": creative_id},
            "status": "PAUSED",
            "degrees_of_freedom_spec": DEGREES_OF_FREEDOM_SPEC,
        }

        ad = account.create_ad(params=ad_params)
        ad_id = ad["id"]
        print(f"  Ad criado: {ad_id} (PAUSED)", file=sys.stderr)
        safe_delay(1)

        created_ads.append({"name": ad_name, "ad_id": ad_id, "creative_id": creative_id})

    print(f"\n{'='*60}", file=sys.stderr)
    print("RESUMO:", file=sys.stderr)
    for item in created_ads:
        print(f"  {item['name']} → ad_id={item['ad_id']}", file=sys.stderr)

    print_json(created_ads)

main()
