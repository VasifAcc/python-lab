txns = [
    {"txn_id": "T101", "user_id": "U1", "amount": 600, "location": "NY", "history": ["NY", "NY"]},
    {"txn_id": "T102", "user_id": "U2", "amount": 12000, "location": "NY", "history": ["NY"]},
    {"txn_id": "T103", "user_id": "U1", "amount": 100, "location": "London", "history": ["NY", "NY"]},
]

def check_fraud(txn_data: list[dict], amount_limit: int = 10000) -> None:
    for txn in txn_data:
        high_amount = txn["amount"] > amount_limit
        new_location = txn["location"] not in txn["history"]

        if high_amount and new_location:
            status = "BLOCKED"
        elif high_amount:
            status = "FLAGGED"
        elif new_location:
            status = "REVIEW_REQUIRED"
        else:
            status = "OK"

        txn["fraud_metrics"] = {
            "high_amount": high_amount,
            "new_location": new_location,
            "status": status,
        }
    return None


check_fraud(txns)
for txn in txns:
    print(txn["txn_id"], txn["fraud_metrics"])

    