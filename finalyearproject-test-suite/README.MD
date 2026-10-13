# HealthConnect QA Test Suite

Test documentation, unit tests and API tests for **HealthConnect**, my final year project (a telehealth platform for patients, doctors and admins). I built the platform as the full-stack developer and also designed and ran its test effort.

> **Note on independence:** I tested my own application, so this is not independent QA.

## At a glance

- **75 test cases** across four levels: unit, integration, system and acceptance (all documented in [`test-cases/`](test-cases/)).
- **74 passed, 1 partial** in the original run (final year project, 2026).
- **Mostly manual.** Automated: the Vitest unit tests. Manual: integration, system and acceptance testing.
- **API tests re-run in October 2026:** 5 of 7 passed. 2 failed because the AI model the app calls was retired (details in [Known issues](#known-issues)).

## Results

| Level | Cases | How it was tested | Original result |
|---|---|---|---|
| Unit | 20 | Vitest (19 automated tests in 2 files), plus unit-level checks of an edge function and access logic | 20 passed |
| Integration | 22 | Manual: Postman, curl, Supabase Table/SQL Editor, Stripe dashboard, browser DevTools | 21 passed, 1 partial |
| System (end-to-end) | 25 | Manual walkthroughs of patient, doctor and admin journeys on a staging setup with test accounts and Stripe test mode | 25 passed |
| Acceptance | 8 | Manual checks of the finished system against each role's requirements | 8 passed |
| **Total** | **75** | | **74 passed, 1 partial (98.7%)** |

The full list, with steps, expected and actual results, is in [`test-cases/HealthConnect-Test-Cases.xlsx`](test-cases/HealthConnect-Test-Cases.xlsx) (also as [`test-cases.csv`](test-cases/test-cases.csv) for viewing on GitHub). The workbook also has a requirements traceability sheet that links 20 functional requirements to their test IDs.

## Postman re-run (October 2026)

My original Postman collection was lost, so I rebuilt it from the documented test cases, added assertions, and re-ran it against the current deployment.

| Test | What it checks | Result |
|---|---|---|
| IT-05 | Row Level Security returns no rows when another user's appointments are requested with only the anon key | Passed |
| IT-11 | Emergency keyword ("chest pain") bypasses the AI and returns high urgency | Passed |
| UT-16 | Same emergency check in uppercase ("CHEST PAIN") | Passed |
| IT-15 | A forged Stripe webhook signature is rejected with HTTP 400 | Passed |
| IT-17 | The TURN credentials function rejects a request with no authentication | Passed |
| IT-10 | Symptom checker returns structured triage for a standard input | **Failed** (see below) |
| IT-12 | Condition explainer returns a short explanation | **Failed** (see below) |

Screenshots of every run, passes and failures, are in [`assets/postman/`](assets/postman/).

## Known issues

**IT-10 and IT-12 fail on re-run.** Both call a Groq-hosted AI model (`llama-3.1-8b-instant`). Groq retired that model on 16 August 2026, and I have not updated the functions to a supported replacement, so these requests fail. The emergency-keyword tests (IT-11, UT-16) still pass because that path skips the AI entirely.

Why I'm leaving it visible: this is a real example of a third-party dependency being retired with no change to my own code. It is the kind of failure a one-off test run misses and a regression run catches. The fix is to point the functions at a current model and re-run these two tests.


## What was and wasn't re-run

- **Postman/API tests:** re-built and re-run in October 2026 (above).
- **Vitest unit tests:** these are from the original project run. I did not re-run them for this repo. Screenshots of the original run are in [`assets/vitest/`](assets/vitest/).
- **Everything else (integration, system, acceptance):** original results from the report, copied unchanged.

## Repo contents

```
test-cases/     Spreadsheet (75 cases, summary, traceability, notes) and CSV
unit-tests/     Vitest test files for validateIC, normalizeMYPhone, formatTime, generateTimeSlots
api-tests/      Rebuilt Postman collection and a blank environment template
assets/       Screenshots: original run, and the Postman re-run
```

## Running the API tests

1. Import `api-tests/healthconnect-api-tests.postman_collection.json` and `api-tests/environment.template.json` into Postman.
2. Fill in the environment values (`SUPABASE_URL`, `SUPABASE_ANON_KEY`, `OTHER_USER_ID`) in the **Current value** column. No keys are stored in this repo.
3. Open the collection and run it with **Run collection**.

This needs a live Supabase project with the app's edge functions deployed. The AI-dependent requests also need a working Groq model.

## About the unit tests

The Vitest files were copied from the HealthConnect project and import the functions they test from it, so they run inside that project rather than standalone.

## What I'd improve

- Update the AI functions to a supported model, make the model name a configuration setting, and re-run IT-10 and IT-12.
- Add assertions and run the API tests automatically with Newman in CI.
- Automate more of the system tests (see my Selenium project below).
- Add load and performance testing.
- Have someone other than the developer run the tests.


## Notes on data

All testing used test accounts and Stripe test mode. No real patient data is included, and keys, tokens and project URLs have been removed or blurred from screenshots.

---

Viinesh Kerisnan | Software Engineering graduate, Universiti Sains Malaysia | neshviinesh@gmail.com 
