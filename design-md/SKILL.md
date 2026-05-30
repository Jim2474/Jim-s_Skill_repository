---
name: design-md
description: Apply brand design systems to your project using DESIGN.md files from the awesome-design-md collection. Use when the user wants to style UI after a specific brand (e.g., "use Claude's design style", "apply Stripe's design system", "make it look like Notion"). Fetches the brand's DESIGN.md from GitHub and applies it as the project's design reference.
---

# Design MD Skill

Apply real brand design systems to your project via DESIGN.md files — the format LLMs read best.

Source: [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)

## Usage

```
/design-md <brand-name>     # Apply a brand's design system
/design-md list              # List all available brands
/design-md preview <brand>   # Fetch and show a brand's design tokens
```

## How It Works

1. Fetch the brand's `DESIGN.md` from GitHub
2. Save it to the project root as `DESIGN.md`
3. All subsequent UI work references this file for colors, typography, components, layout, etc.

## Fetch URL Pattern

```
https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/{brand}/DESIGN.md
```

Preview files (optional):
```
https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/{brand}/preview.html
https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/{brand}/preview-dark.html
```

## Available Brands (71)

### AI & LLM Platforms
claude, cohere, elevenlabs, minimax, mistral-ai, ollama, opencode-ai, replicate, runwayml, together-ai, voltagent, xai

### Developer Tools & IDEs
cursor, expo, lovable, raycast, superhuman, vercel, warp

### Backend, Database & DevOps
clickhouse, composio, hashicorp, mongodb, posthog, sanity, sentry, supabase

### Productivity & SaaS
cal-com, intercom, linear, mintlify, notion, resend, zapier

### Design & Creative Tools
airtable, clay, figma, framer, miro, webflow

### Fintech & Crypto
binance, coinbase, kraken, mastercard, revolut, stripe, wise

### E-commerce & Retail
airbnb, meta, nike, shopify, starbucks

### Media & Consumer Tech
apple, ibm, nvidia, pinterest, playstation, spacex, spotify, the-verge, uber, vodafone, wired

### Automotive
bmw, bmw-m, bugatti, ferrari, lamborghini, renault, tesla

## Brand Name Normalization

User input may vary. Normalize to the folder name (lowercase, hyphenated):

| User says | Folder name |
|-----------|-------------|
| Claude / claude | claude |
| Stripe / stripe | stripe |
| Notion / notion | notion |
| Tesla / tesla | tesla |
| BMW M / bmw-m | bmw-m |
| The Verge / the-verge | the-verge |
| Mistral AI / mistral | mistral-ai |
| OpenCode / opencode | opencode-ai |
| Cal.com / cal | cal-com |

When in doubt, try the lowercase hyphenated version first. If it 404s, list available brands.

## Workflow

### Step 1: Identify the brand

If the user provides a brand name, normalize it. If they describe a style (e.g., "warm and minimal like a luxury brand"), suggest matching brands from the list.

### Step 2: Fetch the DESIGN.md

Use WebFetch to get the file from the raw GitHub URL. Confirm it loaded successfully.

### Step 3: Save to project

Write the fetched content to `./DESIGN.md` in the project root. If a DESIGN.md already exists, ask before overwriting.

### Step 4: Confirm and preview

Show the user a summary of the design system:
- Brand name and description
- Primary/accent colors
- Typography choices
- Key design principles

### Step 5: Apply in subsequent work

When building UI after applying a DESIGN.md, always reference it for:
- Color tokens (never hardcode off-palette colors)
- Typography scale and font families
- Component styles (buttons, cards, inputs, nav)
- Spacing and layout principles
- Do's and Don'ts guardrails

## Fallback: Brand Not Found

If the brand isn't in the collection:
1. Tell the user it's not available
2. Suggest the closest match (e.g., "We don't have Uber, but we have Lyft's style")
3. Offer to create a custom DESIGN.md by analyzing the brand's actual website using WebFetch

## Custom DESIGN.md Generation

When a brand isn't in the collection, generate one:

1. Fetch the brand's website with WebFetch
2. Extract: colors, fonts, spacing, component patterns, visual mood
3. Generate a DESIGN.md following the same 9-section format
4. Save to project root

This produces a best-effort approximation — real DESIGN.md files from the collection are higher quality.
