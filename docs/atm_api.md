## ATM API

### Start new ATM session

#### Request:
```
POST
URL: /api/atm/<str:bank_name>/start_session/
REQUIRED HEADERS:
  {
    "Content-Type": "application/json"
  }

REQUIRED JSON BODY:
  {
    "card_number": 1402298193829183,
    "security_code": 202,
    "expiration_date": "12/18",
    "pin": 1234
  }
```

#### Response:
```
{
  "token": "<token>"
  "accounts": [
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
}
```

---

### End ATM session

#### Request:
```
POST
URL: /api/atm/<str:session_id>/end/
```

#### Response:
```
Status message
```
