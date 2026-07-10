# qa-automation-portfolio

![tests](https://github.com/USERNAME/qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Playwright](https://img.shields.io/badge/Playwright-UI-green)
![pytest](https://img.shields.io/badge/pytest-API-orange)

UI + API test suite built with Python, Playwright, and pytest. UI tests run against
[saucedemo.com](https://www.saucedemo.com); API tests run against
[restful-booker](https://restful-booker.herokuapp.com).

## Test strategy

**What I cover**

- **UI** — login (valid / invalid / locked-out, plus a parametrized set), cart badge
  behaviour, sort ordering (asserted against a computed expected order, not eyeballed),
  and a full checkout e2e that asserts the displayed subtotal equals the summed item
  prices. The total assertion is deliberate — a click-through that never checks a number
  isn't a test.
- **API** — a single CRUD lifecycle (POST → GET → PUT → PATCH → DELETE → GET 404) that
  proves the REST verbs and where auth is required (writes need the `Cookie: token=`
  header), plus negative cases: bad credentials, writes without a token (403), missing
  records (404), and incomplete payloads.

**What I deliberately left out** — visual/pixel testing, load/perf, cross-browser (that's
a Week 5 matrix-build upgrade), and JSON Schema contract validation (schema is stubbed in
`utils/schemas.py`, wired in Week 4). Scope is intentional; each is a tracked next step,
not an oversight.

**Design** — Page Object Model keeps locators in one place and tests readable; assertions
live in tests, never in page objects; fixtures (`conftest.py`) handle login and the
session-scoped API token so setup isn't repeated per test.

## Run it locally

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt && playwright install chromium
pytest
```

Run a subset: `pytest tests/api` (no browser needed) or `pytest tests/ui`.

## Structure

```
pages/     Page Objects (login, inventory, cart, checkout)
tests/ui/  saucedemo UI tests
tests/api/ restful-booker API tests
utils/     api_client wrapper, test data factory, response schema
conftest.py  fixtures: logged_in_page, session-scoped api_token
.github/workflows/tests.yml  CI: push/PR → pytest → upload artifacts
```

## CI

GitHub Actions runs the full suite on every push and PR, retains a Playwright trace on
failure, and uploads results as an artifact even when tests fail.
