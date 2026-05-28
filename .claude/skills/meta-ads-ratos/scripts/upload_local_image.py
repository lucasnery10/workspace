#!/usr/bin/env python3
"""Upload de imagem local para Meta Ads."""
import os, sys, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import init_api, resolve_account, print_json, handle_fb_error, safe_delay
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adimage import AdImage

@handle_fb_error
def main():
    parser = argparse.ArgumentParser(description="Upload de imagem local para Meta Ads")
    parser.add_argument("--account", required=True, help="ID da conta (act_XXX)")
    parser.add_argument("--file", required=True, help="Caminho local da imagem")
    parser.add_argument("--name", help="Nome da imagem")
    args = parser.parse_args()

    init_api()
    account_id = resolve_account(args.account)

    if not os.path.exists(args.file):
        print(f"ERRO: arquivo não encontrado: {args.file}", file=sys.stderr)
        sys.exit(1)

    print(f"Fazendo upload: {args.file}", file=sys.stderr)
    img = AdImage(parent_id=account_id)
    img[AdImage.Field.filename] = args.file
    if args.name:
        img[AdImage.Field.name] = args.name
    img.remote_create()
    safe_delay(1)
    img_hash = img[AdImage.Field.hash]
    print(f"Imagem enviada — hash: {img_hash}", file=sys.stderr)
    print_json({"hash": img_hash, "id": img.get("id", "")})

main()
