# RideMachan Knowledge Base (RAG source)

Markdown knowledge base for the RideMachan support chatbot.

| File | Covers | Audience |
|---|---|---|
| 01-about-ridemachan.md | What RideMachan is, user types, vehicle categories, coverage, hours | all |
| 02-customer-booking-guide.md | Sign-up, documents, age rules, booking, extensions, pick-up/return | customers |
| 03-pricing-payments-deposits.md | Rates, mileage, fuel, payment methods, deposits, fees, provider payouts | customers, providers |
| 04-cancellation-refund-policy.md | Cancellation tiers, refunds, emergencies, disputes | all |
| 05-vehicle-provider-guide.md | Individual providers vs rental companies, listing rules, penalties | providers |
| 06-driver-guide.md | Driver requirements, trips, conduct, pay | drivers |
| 07-insurance-damage-accidents.md | Insurance, excess, accidents, breakdowns, damage, theft | all |
| 08-account-security-support.md | Passwords, OTP, verification, suspension, privacy, contact | all |
| 09-faq.md | Short Q&A across all topics | all |
| 10-admin-operations.md | Admin dashboard, verification, disputes, reports | admins only |

## Ingestion tips

- **Chunking:** split on `##` headings. Each `##` section is written to stand on its own (no "as mentioned above"). Keep the `#` page title and prepend it to every chunk (e.g. `Cancellation and Refund Policy > Refunds when the customer cancels`) so the embedding has context.
- **FAQ file:** chunk per `**Q:**`/`**A:**` pair rather than per heading for sharper matches.
- **Metadata:** the YAML front matter (`category`, `audience`) can be stored as chunk metadata. Filter `audience: administrators` out of retrieval unless the logged-in user is an admin.
- **Tables:** keep each table in one chunk with its heading; don't split rows apart.

## Important

All prices, fees, percentages, time limits and policies here are **sample content** written for development and testing. Replace them with the real RideMachan business rules before going live. Emergency numbers 119 (police) and 1990 (Suwa Seriya ambulance) are real Sri Lankan numbers.
