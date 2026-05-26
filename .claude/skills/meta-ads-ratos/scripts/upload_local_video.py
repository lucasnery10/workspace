#!/usr/bin/env python3
"""Upload de vídeo local para Meta Ads."""
import os, sys, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import init_api, resolve_account, print_json, handle_fb_error, safe_delay
from facebook_business.adobjects.adaccount import AdAccount

@handle_fb_error
def main():
    parser = argparse.ArgumentParser(description="Upload de vídeo local para Meta Ads")
    parser.add_argument("--account", required=True, help="ID da conta (act_XXX)")
    parser.add_argument("--file", required=True, help="Caminho local do vídeo")
    parser.add_argument("--name", help="Nome do vídeo")
    args = parser.parse_args()

    init_api()
    account_id = resolve_account(args.account)

    if not os.path.exists(args.file):
        print(f"ERRO: arquivo não encontrado: {args.file}", file=sys.stderr)
        sys.exit(1)

    from facebook_business.adobjects.advideo import AdVideo

    print(f"Fazendo upload: {args.file}", file=sys.stderr)
    video = AdVideo(parent_id=account_id)
    video[AdVideo.Field.filepath] = args.file
    if args.name:
        video[AdVideo.Field.name] = args.name
    video.remote_create()
    safe_delay(1)
    print(f"Vídeo enviado com ID: {video['id']}", file=sys.stderr)
    print_json({"id": video["id"]})

main()
