# 🐞 Bug Bounty Notes by Olasunkanmi

Welcome to my bug bounty hunting knowledge vault. This repo contains:
- My methodology for web app hacking
- Useful payloads
- Recon steps
- Notes from labs and real-world practice

## 🔧 Recon Tools
- `subfinder`, `assetfinder`, `amass` — for subdomain enum
- `httpx`, `nmap`, `whatweb` — for service discovery
- `ffuf`, `dirsearch` — for directory brute-force

## 💥 Payloads
### XSS
```html
"><script>alert(document.domain)</script>

