# Data Model Notes

This file records my current understanding of what one row represents in each source table.

These are observations from inspection, not permanent assumptions. I will update them as I learn more about the dataset.

---

## olist_customers_dataset.csv

One row represents one customer record.

Contains customer location information such as:

- ZIP code prefix,
- city,
- state.

---

## olist_geolocation_dataset.csv

One row represents a geolocation record associated with a ZIP code prefix.

During inspection, I found:

- **261,831 exact duplicate rows**.

This is currently an observation only.

I have **not yet decided** whether these duplicates should be removed. I want to understand how this table will be used before making that cleaning decision.

---

## olist_order_items_dataset.csv

One row represents one item within an order.

Contains information such as:

- order ID,
- product ID,
- seller ID,
- price,
- freight value.

This means one order can appear in multiple rows if it contains multiple items.

---

## olist_order_payments_dataset.csv

One row represents one payment record associated with an order.

Contains information such as:

- order ID,
- payment sequence,
- payment type,
- number of installments,
- payment value.

An order may have more than one payment record.

---

## olist_order_reviews_dataset.csv

One row represents a review record associated with an order.

Contains information such as:

- review score,
- review title,
- review message,
- review timestamps.

I will verify later whether every order has exactly one review record.

---

## olist_orders_dataset.csv

One row represents one order.

Contains information such as:

- customer ID,
- order status,
- purchase timestamp,
- approval timestamp,
- delivery timestamps,
- estimated delivery date.

---

## olist_products_dataset.csv

One row represents one product.

Contains product-level information such as:

- product category,
- product name length,
- product description length,
- number of photos,
- product dimensions and weight.

---

## olist_sellers_dataset.csv

One row represents one seller.

Contains seller location information such as:

- ZIP code prefix,
- city,
- state.

---

## product_category_name_translation.csv

This is a helper table used to translate product category names from Portuguese to English.

It connects the original Portuguese category name with its English translation.


---