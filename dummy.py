import random
import json
from datetime import date, timedelta

def rand_date(start: date, end: date) -> str:
    return (start + timedelta(days=random.randint(0, (end - start).days))).isoformat()

def pick_months():
    return ["2026-01", "2026-02", "2026-03"]

def generate_nested_finance_dataset(seed=42):
    random.seed(seed)

    months = pick_months()

    # ---- smaller dataset config ----
    USER_COUNT = random.randint(10, 15)
    CATEGORIES_PER_USER = (2, 4)

    # Total per user (NOT per month)
    EXPENSES_TOTAL_PER_USER = (5, 6)
    BUDGETS_TOTAL_PER_USER = (2, 3)

    names = ["John", "Sarah", "Ahmed", "Emma", "David", "Mia", "Ali", "Sophia", "Daniel", "Olivia", "Noah", "Ava"]
    domains = ["gmail.com", "outlook.com", "yahoo.com"]

    expense_categories = ["Food", "Transport", "Bills", "Rent", "Shopping", "Entertainment", "Health"]
    income_categories = ["Salary", "Freelance"]

    merchants = ["Tesco", "Amazon", "Uber", "Netflix", "Shell", "Lidl", "KFC"]
    bill_merchants = ["British Gas", "Octopus Energy", "Vodafone"]
    payment_methods = ["cash", "card"]

    users = []

    # global unique ids
    category_id = 1
    expense_id = 1
    budget_id = 1
    alert_id = 1

    for u in range(1, USER_COUNT + 1):
        user = {
            "user_id": u,
            "name": random.choice(names),
            "email": f"user{u}@{random.choice(domains)}",
            "password_hash": "hashed_password_example",
            "created_at": rand_date(date(2025, 1, 1), date(2025, 12, 31)),
            "categories": [],
            "expenses": [],
            "monthly_budgets": [],
            "alerts": []
        }

        # ---- categories ----
        user_expense_cats = random.sample(expense_categories, random.randint(*CATEGORIES_PER_USER))
        user_income_cats = random.sample(income_categories, 1)

        user_expense_cat_ids = []

        for cat in user_expense_cats + user_income_cats:
            ctype = "income" if cat in income_categories else "expense"

            user["categories"].append({
                "category_id": category_id,
                "user_id": u,
                "name": cat,
                "type": ctype
            })

            if ctype == "expense":
                user_expense_cat_ids.append(category_id)

                # 1 alert per expense category (keeps it simple)
                user["alerts"].append({
                    "alert_id": alert_id,
                    "user_id": u,
                    "category_id": category_id,
                    "threshold_percent": random.choice([70, 80, 90]),
                    "enabled": True
                })
                alert_id += 1

            category_id += 1

        # ---- budgets (ONLY 2-3 total per user) ----
        # pick 2-3 random (month, category) pairs
        budget_count = random.randint(*BUDGETS_TOTAL_PER_USER)
        possible_pairs = [(m, cid) for m in months for cid in user_expense_cat_ids]
        chosen_pairs = random.sample(possible_pairs, k=min(budget_count, len(possible_pairs)))

        for (m, cid) in chosen_pairs:
            cat_name = next(c["name"] for c in user["categories"] if c["category_id"] == cid)
            base = 1000 if cat_name == "Rent" else 300

            user["monthly_budgets"].append({
                "budget_id": budget_id,
                "user_id": u,
                "month": m,
                "category_id": cid,
                "budget_amount": random.randint(int(base * 0.7), int(base * 1.2))
            })
            budget_id += 1

        # ---- expenses (ONLY 5-6 total per user) ----
        expense_count = random.randint(*EXPENSES_TOTAL_PER_USER)

        for _ in range(expense_count):
            m = random.choice(months)
            y, mo = map(int, m.split("-"))
            start = date(y, mo, 1)
            end = date(y, mo, 28)

            cid = random.choice(user_expense_cat_ids)
            cat_name = next(c["name"] for c in user["categories"] if c["category_id"] == cid)

            if cat_name == "Rent":
                amt = round(random.uniform(700, 1200), 2)
                merchant = "Landlord"
            elif cat_name == "Bills":
                amt = round(random.uniform(60, 220), 2)
                merchant = random.choice(bill_merchants)
            else:
                amt = round(random.uniform(5, 180), 2)
                merchant = random.choice(merchants)

            user["expenses"].append({
                "expense_id": expense_id,
                "user_id": u,
                "category_id": cid,
                "amount": amt,
                "date": rand_date(start, end),
                "merchant": merchant,
                "note": "",
                "payment_method": random.choice(payment_methods)
            })
            expense_id += 1

        users.append(user)

    return users

# ---- SAVE FILE ----
data = generate_nested_finance_dataset()

with open("finance_nested_users_only.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("✅ finance_nested_users_only.json generated (smaller)")