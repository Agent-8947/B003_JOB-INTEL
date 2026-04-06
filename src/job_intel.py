#!/usr/bin/env python3
"""
NEXUS B003 - JOB-INTEL [AGNOSTIC-SCOUT V5.4]
-------------------------------------------
Mission: Global OSINT Job Harvester. 
Strategy: Scrape DuckDuckGo (No Captcha) for global/regional vacancies.
"""

import json, re, time, sys, urllib.request, random

def fetch_scout(url, timeout=15):
    """
    Standard fetch with stealth headers to minimize blocks.
    """
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    ]
    req = urllib.request.Request(url, headers={'User-Agent': random.choice(user_agents)})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error: {e}"

def scout_duck(keywords, region):
    """
    Collect job leads from DuckDuckGo HTML results (Captcha-Free).
    """
    # DuckDuckGo HTML-only search
    q = f"{keywords}+{region}+jobs".replace(" ", "+")
    url = f"https://duckduckgo.com/html/?q={q}"
    
    print(f"[*] NEXUS B003 SCOUT: Probing DuckDuckGo for '{keywords}' in '{region}'...")
    raw = fetch_scout(url)
    
    # Extract titles and links from DDG results
    # HTML results pattern: <a class="result__a" href="...">TITLE</a>
    matches = re.findall(r'result__a" href="([^"]+)">([^<]+)</a>', raw)
    
    results = []
    for link, title in matches:
        # Filter for job-related links
        if any(x in link.lower() for x in ['job', 'vacancy', 'career', 'hiring', 'linkedin', 'cv.lv', 'hh.ru']):
            # Clean redirect URLs if DuckDuckGo uses them
            real_link = link
            if 'uddg=' in link:
                real_link = urllib.parse.unquote(link.split('uddg=')[1].split('&')[0])
            
            results.append({
                "source": "DuckDuckGo",
                "title": title.strip(),
                "url": real_link
            })
    
    return results[:15]

def run(target: str) -> dict:
    if "|" not in target: return {"error": "Use 'Keywords | Region'"}
    kw, reg = [i.strip() for i in target.split("|")]
    
    leads = scout_duck(kw, reg)
    
    # Analyze and format leads
    final_leads = []
    for lead in leads:
        # Simple domain extraction for "Contacts"
        domain = re.search(r'https?://([^/]+)', lead["url"])
        site = domain.group(0) if domain else lead["url"]
        
        final_leads.append({
            "vacancy": lead["title"],
            "url": lead["url"],
            "company_site": site,
            "status": "Target Acquired",
            "type": "OSINT-Lead"
        })
    
    return {
        "status": "success",
        "timestamp": time.time(),
        "query": {"keywords": kw, "region": reg},
        "leads_count": len(final_leads),
        "leads": final_leads
    }

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "AI Engineer | Riga"
    print(json.dumps(run(query), indent=4))
