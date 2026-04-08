# Slack Configuration — Kin's Minion

## Workspace

- **Name:** Lights On Digital
- **URL:** lightsondigital.slack.com
- **Team ID:** T0KLLC3U3
- **Bot:** Kin's Minion (kins-minion)
- **Bot User ID:** U0AP0F46FNK
- **Bot ID:** B0AQA6WFV8Q

## Team Slack IDs

| Name | Role | Slack ID | Timezone |
|---|---|---|---|
| Kin Sio | CEO | U08BDNCGA94 | HST (UTC-10) |
| Emily Easton | Director of Client Success | U05KHPN4KCM | HST |
| Emanuel Moura | Director of Growth | U07KAANH8G0 | HST |
| Margaret Heggan | Director of Revenue Management | U09PNJXKKNF | Central (UTC-6) |
| Keri Brown | VP Commercial Strategy | U0A004QB7A9 | HST |
| Jemmerio Kimble | Revenue Manager | U08UYQFNSCS | HST |
| Conor Doi | Revenue | U02RE8VJ5ST | HST |

## Key Channels

| Channel | ID | Purpose |
|---|---|---|
| #general | C0KLPFLET | Company-wide announcements |
| #team-revenue | C9XRA1WCC | Revenue team ops |
| #team-marketing | C0106J41W7P | Marketing team ops |
| #client-kauai-shores | CHHQQMZ1Q | KSH client channel |
| #client-twin-farms | C08F17TGN7Q | TWF client channel |
| #design | C02L1QA0NTY | Design projects |
| #webflow | C02M01MT05A | Website dev |

Note: `#client-twf` (C0KPM90S0) is archived. Use `#client-twin-farms` for Twin Farms.

## Channel Naming Conventions

- `#client-xxx` — Client conversations
- `#team-xxx` — Team conversations
- `#project-xxx` — Projects or initiatives

## Scheduling Norms

- **Default:** 8:00 AM HST
- **Timezone-adjusted:** Schedule for team member's 9 AM local
  - Margaret (Central): 5:00 AM HST
  - East Coast contacts: 4:00 AM HST
- **API:** Use `chat.scheduleMessage` with Unix timestamp
- **HST to UTC:** Add 10 hours (HST = UTC-10)

## Messaging Norms

- Always @tag people when a response is needed: `<@SLACK_ID>`
- Channels over DMs (per internal comms guidelines)
- Use threads to keep discussions organized
- Don't assume someone will see a message without a tag

## Bot Scopes

channels:history, channels:read, groups:history, groups:read, im:history, im:read, mpim:history, mpim:read, chat:write, chat:write.public, reactions:read, reactions:write, files:read, files:write, users:read, users.profile:read, bookmarks:read, pins:read, usergroups:read, app_mentions:read

## API Notes

- Bot token starts with `xoxb-`, stored in `lights-on/lights-on-ea/.env`
- Rate limit: 1 msg/sec for `chat.postMessage`
- Slack uses mrkdwn, not Markdown: bold is `*text*`, links are `<url|text>`
- Bot must be invited to channels to read history
- `search:read` is user-token only — read channel history directly instead
