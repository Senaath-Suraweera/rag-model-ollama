---
title: Admin Operations Guide
category: admin
audience: administrators
last_updated: 2026-11-03
---

# Admin Operations Guide

This document is for RideMachan administrators. The chatbot should only use it when answering questions from users with the admin role.

## Admin dashboard overview

The admin dashboard has a fixed sidebar with these sections:

- **Dashboard** – key figures: active rentals, bookings today, revenue this month, pending verifications, open disputes.
- **Ongoing Orders** – all active rentals with live status and location.
- **Customers** – customer accounts, verification status and booking history.
- **Individual Providers** – private vehicle owners and their vehicles.
- **Rental Companies** – company accounts, join requests and fleets.
- **Drivers** – driver accounts, verification and assignments.
- **Maintenance Staff** – staff accounts under rental companies.
- **Vehicle Fleet** – all vehicles on the platform, with document status.
- **Provider Requests** – pending registrations and change requests.
- **Messages & Notifications** – platform-wide messaging and announcements.
- **Reports** – revenue, bookings, utilisation and user growth reports.
- **Admin Management** – admin accounts and permissions.

All lists support search, filters and pagination (10, 25 or 50 rows per page).

## Verification checklist

**Customers:** NIC/passport photo matches the selfie and name; licence is valid and covers the vehicle class; foreign licences have a valid permit.

**Individual providers:** NIC is valid; proof of address is less than 3 months old; bank account name matches the NIC name.

**Rental companies:** BR certificate is valid and matches the company name; the authorised person's NIC is valid; a verification phone call has been made.

**Drivers:** licence is held for at least 3 years with the right classes; police report is less than 6 months old; medical certificate is valid; phone interview completed.

**Vehicles:** CR book matches the registration number and owner (or there is an authorisation letter); revenue licence, insurance (with rental use) and emission certificate are valid; photos are clear and match the listing; vehicle meets the age limit.

Target turnaround: customers 2 hours, providers 1–2 working days, rental companies 2–3 working days, drivers 2–3 working days.

When rejecting, always select a rejection reason so the user knows what to fix.

## Handling provider requests

Provider requests include new registrations, rental company join requests, and changes to bank details. Bank detail changes require a new OTP verification by the provider and a 48-hour hold on payouts, to protect against account takeover.

## Dispute resolution

1. Review the pick-up and return inspection photos, messages and receipts.
2. Give the other party 48 hours to respond.
3. Decide within 5 working days. Possible outcomes: charge upheld, charge reduced, charge removed.
4. Record the reason in the dispute notes. Both parties are notified automatically.

Disputes involving more than LKR 100,000 or suspected fraud must be escalated to a senior admin.

## Suspensions

Admins can suspend a user or a vehicle from their profile page with **Suspend** and a reason. Suspended users cannot log in to the role that is suspended. Active bookings must be reassigned or cancelled first; provider-side cancellations caused by a suspension are refunded in full to the customer.

## Reports

Available reports:
- **Revenue** – gross booking value, commission, refunds, by day/week/month.
- **Bookings** – counts by status, category, district and booking mode.
- **Fleet utilisation** – percentage of available days booked per vehicle and company.
- **User growth** – new sign-ups by role.
- **Cancellations** – by party (customer, provider, driver) and reason.

Reports can be exported as CSV or PDF.

## Admin accounts and permissions

Admin roles:
- **Super Admin** – full access, including managing other admins.
- **Operations Admin** – verifications, bookings, disputes, suspensions.
- **Finance Admin** – payouts, refunds, revenue reports.
- **Support Admin** – messages, customer issues, read-only access to bookings.

Admins can change their own name, profile photo and password. Only a Super Admin can create or remove admin accounts or change roles.
