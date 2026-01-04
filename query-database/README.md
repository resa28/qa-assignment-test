# Query Database - Trading Analytics

A SQL database modeling a Foreign Exchange (Forex) trading system with analytical queries for trade reconciliation and liquidity provider analysis.

## Overview

This project simulates a multi-provider trading environment where liquidity providers (banks) submit buy/sell orders for various financial instruments including currency pairs (EUR/USD, GBP/USD) and commodities (Oil, Gold).

## Database Schema

```
lps (Liquidity Providers)
  ├── lp_id (PK)
  └── lp_name

symbols (Financial Instruments)
  ├── symbol_id (PK)
  ├── symbol_name
  └── core_symbol

orders (Trading Orders)
  ├── order_id (PK)
  ├── lp_id (FK → lps)
  ├── symbol_id (FK → symbols)
  ├── direction (BUY/SELL)
  └── volume
```

## Setup

```bash
# Create database
mysql -u root -p -e "CREATE DATABASE qa_assignment;"

# Import schema and seed data
mysql -u root -p qa_assignment < qa_assignment.sql

# Run analytical query
mysql -u root -p qa_assignment < query.txt
```

## Query Logic

The analytical query calculates **net trading position** by:

1. Assigning positive values to BUY volumes
2. Assigning negative values to SELL volumes
3. Summing to determine net direction
4. Returning absolute volume of net position

**Expected Result (EURUSD):**
- 2x SELL orders (500K + 500K = 1M)
- 1x BUY order (500K)
- Net: **SELL 500,000**

## Technologies

- MySQL 8.0+
- InnoDB with UTF-8 support
- Foreign key constraints with referential integrity
- Indexed queries for performance optimization
