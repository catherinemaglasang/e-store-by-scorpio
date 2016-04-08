/*
 stock_location
 - stock_location_id serial primary key,
 - stock_location_name text

 item_stock_locations
 - stock_on_hand
 - re_order_level
 - re_order_quantity

 - stock_location_id
 - item_variation_id references item_variations

 item_variation
 - item_variation_id
 - sku
 - cost_price
 - selling_price
 - tax_class
 - is_active
 - item_id references items

 item_variation_options
 // This will serve as the m2m intermediary between item_variations and options
 // An item_variation instance has many options, and an option can belong to many item_variations
 - item_variation_id references item_variations
 - option_id references options

 options
 - option_id
 - option_group_id references option_groups
 - option_value // e.g. small, medium, large

 option_groups
 - option_group_id
 - option_group_name

 tax_class
 - tax_class_id
 - tax_name
 - tax_rate
 */

/*
 * Adding an item
 * 1. Add item basic details
 *      - name, description, sku
 * 2. Add Option Group
 * 3. Add option group values
 * 4. Generate item_variations if any
 *  4.1 add item_variations
 *  4.2 add item_variation_options
 *  4.3 If no variations are created, then, only item_variation will be created. No item_variation_options and options nor option_groups
 * 5. input item_stock_location details for each item variant.
 *  5.1 user will input item_stock_location for all stock_locations
 *
 */

/*
 * Viewing inventory Goals
 * 1. View item variants
 * 2. View item variant stocks per location
 * 3. Calculate total stock on hand per location, and across all locations
 * 4.
 */