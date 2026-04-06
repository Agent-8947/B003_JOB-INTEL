#  BRAIN DIRECTIVE: B003_JOB-INTEL
Date: 2026-04-06 14:00:00

## 1. STRATEGIC OVERSIGHT
Target identified: `B003_JOB-INTEL`. 
Mission: Specialized recruitment and corporate intelligence harvester.

## 2. HISTORICAL CONTEXT (CORE REFERENCES)
To ensure high-fidelity extraction, analyze patterns from these gold-standard repositories:
- **Scrapy**: github.com/scrapy/scrapy (Industrial crawling standards).
- **BeautifulSoup4**: pypi.org/project/beautifulsoup4 (Resilient HTML structure analysis).
- **TheHarvester**: github.com/laramies/theHarvester (Email and corporate entity discovery).
- **Google Search API**: developers.google.com/custom-search (Dorking for vacancies with contact details).

## 3. ENGINEER DIRECTIVE (For Agent 06 & 11)
Synthesize a modular pipeline with the following execution logic:
1. **job_harvester.py**: Scrapes major job boards by keyword/region.
2. **entity_enricher.py**: Resolves vacancy to a real company website.
3. **contact_miner.py**: Extracts verified emails and phone numbers from corporate domains.
4. **lead_validator.py**: Cross-references findings across LinkedIn/Other for verification.

**Architecture**: 
- Parallel processing (ThreadPool)
- Rate-limiting (Sleep between requests)
- Result validation (Only return verified corporate entities).

*Execute immediately.*
