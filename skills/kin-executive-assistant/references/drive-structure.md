# Google Drive Structure — ZenPilot 3-Folder Model

LOD uses three shared drives aligned with the ZenPilot ClickUp design: Delivery (billable), Growth (business development), Operation (internal).

## Core Shared Drives

| Drive | ID | Purpose |
|---|---|---|
| **Delivery** | `0AO0WkkM0lbnVUk9PVA` | Billable client work. 39 client folders. |
| **Growth** | `0AGVFNg7Aa4t7Uk9PVA` | Business development, sales, partnerships, marketing. |
| **Operation** | `0AK9fw52ANqYKUk9PVA` | Internal ops, HR, finance, legal, admin. |

## Decision Guide: Which Drive?

| Content Type | Drive | Example |
|---|---|---|
| Client deliverables, meeting notes, strategy docs | **Delivery** / [Client Folder] | KAH revenue report |
| Partner agreements, referral deals | **Growth** / Agreements 📑 | Duetto referral agreement |
| Proposals, scopes, pitches | **Growth** / Scope 📋 | Twin Farms proposal |
| Podcast files | **Growth** / Podcast 🎙️ | Episode recordings |
| Sales collateral | **Growth** / Sales 🤝 | Pitch decks |
| Sponsorships | **Growth** / Sponsorships 🏆 | HSMAI sponsorship |
| Employee docs, payroll, legal | **Operation** | Employment agreements |
| Don't know yet | Drive's `_Inbox` folder | Sort later |

## Growth Drive Key Folders

| Folder | ID |
|---|---|
| _Inbox | `1yKJrLDli_Bisqp0Fez6SsthaUJgEbQnb` |
| _Archive | `1vXSJwrTQFCP4tOjPz_aUcWe_cqheviIr` |
| Agreements 📑 | `1k88B0W3w0LhUEVoFMC8qbbNHXZVV51B7` |
| Podcast 🎙️ | `1f0K_h90GjIlQBPy6WYjwvXW27hlhuTar` |
| Sales 🤝 | `1MAt-g1WNZyJit0u8LJog4NmaeCM3zudt` |
| Scope 📋 | `1wJEb649fY6eYdbaznWWsKZ62zvrEuFo7` |
| Commission 💰 | `1n_YZ6Jae2CszJI-ufS0xYnzeIIOYC_tC` |

## Operation Drive Key Folders

| Folder | ID |
|---|---|
| _Inbox | `1IsBjmhxL4dR-0vpdT7bQ4GybJT8A5nB5` |
| _Archive | `1j5aBXvYsKRSxGmv3ZQTm1_4SSPz9frcS` |

## Delivery Drive Client Folder Structure

Each of the 39 client folders follows this template:
```
[CODE] - [Client Name]/
├── 0. Inbox
├── 1. Active Projects
├── 2. Ongoing
├── 3. Resources
├── 4. Reporting
└── 5. Archive
```

## File Naming Conventions

**Client documents:** `YYYYMMDD - [CODE] - [Description].[ext]`
Example: `20260315 - KAH - Revenue Strategy Deck.pdf`

**Non-client documents (partners, vendors):** `YYYYMMDD - [Company Name] - [Document Type] ([Status]).[ext]`
Example: `20260324 - Duetto - Referral Partner Agreement (Signed).pdf`

Status values: Signed, Draft, Expired, Executed, Final

## Other Shared Drives

| Drive | ID | Purpose |
|---|---|---|
| Revenue Data (Automated) | `0AB5MUWWsD_t5Uk9PVA` | Pace pipeline ingestion |
| Revenue Data | `0ANbU1pY9uMAtUk9PVA` | Manual revenue data |
| Revenue Management | `0AC26Qrc6IR6vUk9PVA` | Revenue team resources |
| Creative Team | `0AD_wBWXSbDvVUk9PVA` | Design assets |
| Client Collab | `0AN7Mt4oN-nNsUk9PVA` | Client-facing collaboration |
| HR and Office | `0ANu1d_AXp-Z2Uk9PVA` | HR documents |

## API Notes

- Always pass `corpora="allDrives"`, `includeItemsFromAllDrives=True`, `supportsAllDrives=True` for shared drives
- Always append `and trashed = false` to Drive queries
- Use `kin@lightson.co` delegation for Drive API (dev-only)
