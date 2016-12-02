## Account API

### Get all accounts

#### Request:
```
/api/account/<int:customer_id>/
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

**

### Transfer Funds

#### Request:
```
/api/account/<int:account_id>/transfer/
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

**

### Withdraw Funds

#### Request:
```
/api/account/<int:account_id>/withdraw/
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

**

### Deposit Funds

#### Request:
```
/api/account/<int:account_id>/deposit/
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
