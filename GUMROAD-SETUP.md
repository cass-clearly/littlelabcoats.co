# Gumroad Setup Guide — Little Lab Coats

**Time required:** ~20-30 minutes  
**Goal:** Take real payments for curriculum units and subscriptions

---

## Step 1: Create Your Account

1. Go to **gumroad.com**
2. Sign up with your email (use `cass.clearly@gmail.com` or your own)
3. Choose username: `littlelabcoats` (makes your URL `gumroad.com/littlelabcoats`)
4. Connect a bank account or PayPal to receive payouts
5. Gumroad takes 10% + payment processing (~3%) per sale

---

## Step 2: Create These 3 Products

### Product 1: Individual Unit — Kindergarten Bundle
- **Type:** Digital product (PDF download)
- **Name:** Little Lab Coats — Complete Kindergarten Science Curriculum
- **Price:** $18 (or "pay what you want" with $18 minimum)
- **Description:**
  > 42 hands-on science lessons for Kindergarten, built by a PhD scientist and homeschooling mom. Covers forces & motion, life science, earth science, weather, and engineering design. Every lesson uses only household materials, takes 30-45 minutes, and includes a student worksheet, parent answer key, and discussion questions. NGSS-aligned. Totally secular.
  >
  > What you get: 42 PDF lesson plans across 7 complete units, print-ready at home.
- **Files to upload:** All 42 K lesson PDFs (generate these with the Chrome print-to-PDF command; they're in `/home/cass/.openclaw/workspace/pdfs/`)
- **Early bird note:** Add "Early bird pricing — first 50 buyers" to the product name or description

---

### Product 2: Annual Subscription — Digital Library Access
- **Type:** Subscription (recurring)
- **Name:** Little Lab Coats — Full Library Subscription (Early Bird)
- **Price:** $67/year (early bird, was $89)
- **Description:**
  > Unlock the entire Little Lab Coats curriculum library for one year. Currently includes 42 Kindergarten lessons, with Grade 1 and Grade 2 units being added continuously. All lessons are hands-on, secular, NGSS-aligned, and use only household materials.
  >
  > Early bird rate: first 50 subscribers lock in $67/year forever (regular price $89/year).
  >
  > What you get: instant PDF download access to every current and future unit added during your subscription.
- **Tier name:** Early Bird Subscriber

---

### Product 3: Free Sample — Animal Needs Lesson 1
- **Type:** Digital product (PDF download)
- **Name:** FREE — What Do Animals Need to Survive? (Kindergarten Science Lesson)
- **Price:** $0
- **Description:**
  > A free sample from the Little Lab Coats Kindergarten curriculum. This 30-45 minute hands-on lesson explores what animals need to survive, using only household materials. Includes student worksheet, parent answer key, and guided discussion questions. NGSS-aligned (K-LS1-1). Secular.
  >
  > No email required. Just download and teach.
- **File to upload:** `/home/cass/.openclaw/workspace/pdfs/k-animal-needs/k-ls1-unit3-lesson1-what-do-animals-need.pdf`
- **Purpose:** Capture email addresses of interested parents; funnel to paid products

---

## Step 3: Update Buy Links on the Site

Once products are created, Gumroad gives you a link for each product like:
`https://littlelabcoats.gumroad.com/l/kindergarten-bundle`

Replace the placeholder `https://littlelabcoats.gumroad.com/` links in `littlelabcoats.co/index.html` with the actual product URLs. Tell Cass the URLs and she'll update the site immediately.

---

## Step 4: Optional but Recommended

- **Profile photo:** Upload the Little Lab Coats badge (`llc-badge-cream.jpg`)
- **Bio:** "PhD microbiologist + homeschooling mom of 3. Building the science curriculum I always wished existed."
- **Cover image:** Use the hero image from the landing page
- **Custom domain:** Can point `shop.littlelabcoats.co` to Gumroad (optional, looks more professional)

---

## Revenue Math

| Scenario | Conversions | Monthly Revenue |
|----------|-------------|-----------------|
| 10% of 150 monthly contacts | 15 subscribers/mo | ~$84/mo (growing) |
| 20% of 150 monthly contacts | 30 subscribers/mo | ~$168/mo (growing) |
| 100 active subscribers | (cumulative) | ~$558/mo |
| 180 active subscribers | (cumulative) | ~$1,005/mo ✅ |

The free sample on Gumroad captures emails even from people who don't buy yet. That list compounds over time.

---

## Notes for Cass

- Once Serena creates the account and products, ask her for the Gumroad product URLs
- Update all 3 "Get Digital", "Get Kit + Digital", and "Subscribe & Save" buttons in `index.html` with correct URLs
- Also add the free sample as a CTA somewhere on the landing page (below the hero or in the pricing section)
