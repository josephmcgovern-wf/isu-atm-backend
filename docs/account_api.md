## Account API

### Get all accounts

#### Request:
```
GET
URL: /api/account/<int:customer_id>/
REQUIRED HEADERS:
  {
    "X-Api-ATM-Key": "<session_id>",
  }
```

#### Response:
```
[
  {
    "bank": "USBank",
    "interest": "0.7",
    "owner": "John Doe",
    "pin": 1234,
    "nickname": "Emergency Fund",
    "total_money": 5000
  }
  ...
]
```

---

### Transfer Funds

#### Request:
```
PUT
URL: /api/account/<int:account_id>/transfer/
REQUIRED HEADERS:
  {
    "X-Api-ATM-Key": "<session_id>",
    "Content-Type": "application/json"
  }
REQUIRED JSON BODY:
  {
    "target_account_id": 1234,
    "amount": 500
  }
```

#### Response:
```
{
  "message": "Transfer Successful",
  "account": {
      "bank": "USBank",
      "interest": "0.7",
      "owner": "John Doe",
      "pin": 1234,
      "nickname": "Emergency Fund",
      "total_money": 5000
  },
  "target_account": {
      "bank": "USBank",
      "interest": "0.7",
      "owner": "John Doe",
      "pin": 1234,
      "nickname": "Emergency Fund",
      "total_money": 5000
  }
}
```

---

### Withdraw Funds

#### Request:
```
PUT
URL: /api/account/<int:account_id>/withdraw/
REQUIRED HEADERS:
  {
    "X-Api-ATM-Key": "<session_id>",
    "Content-Type": "application/json"
  }
REQUIRED JSON BODY:
  {
    "amount": 500
  }
```

#### Response:
```
{
  "message": "Withdraw Successful",
  "account": {
      "bank": "USBank",
      "interest": "0.7",
      "owner": "John Doe",
      "pin": 1234,
      "nickname": "Emergency Fund",
      "total_money": 5000
  },
}
```

---

### Deposit Funds

#### Request:
```
PUT
URL: /api/account/<int:account_id>/deposit/
REQUIRED HEADERS:
  {
    "X-Api-ATM-Key": "<session_id>",
    "Content-Type": "application/json"
  }
REQUIRED JSON BODY:
  {
    "amount": 500
  }
```

#### Response:
```
{
  "message": "Deposit Successful",
  "account": {
      "bank": "USBank",
      "interest": "0.7",
      "owner": "John Doe",
      "pin": 1234,
      "nickname": "Emergency Fund",
      "total_money": 5000
  },
}
```
