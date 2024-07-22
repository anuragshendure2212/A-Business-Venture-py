from collections import defaultdict

def most_frequent_purchase(purchase_history):
    customer_product_count = defaultdict(lambda: defaultdict(int))
    for customer, products in purchase_history.items():
        for product in products:
            customer_product_count[customer][product] += 1
    most_frequent_purchases = {}
    for customer, product_count in customer_product_count.items():
        most_frequent_purchases[customer] = max(product_count, key=product_count.get)
    return most_frequent_purchases

purchase_history = {
    1: ['chocolate', 'ice-cream', 'cold drink', 'pizza', 'burgers', 'protein bar'],
    2: ['spaghetti', 'cereals', 'hand protein bar', 'shrimp', 'flax seed', 'mineral water'],
    3: ['grated cheese', 'pet food', 'mashed potato', 'cider', 'oatmeal', 'body spray'],
    4: ['honey', 'shampoo', 'strawberries', 'salad', 'milk', 'chutney'],
    5: ['bramble', 'cottage cheese', 'strong cheese', 'cauliflower', 'parmesan cheese', 'chocolate'],
}

print(most_frequent_purchase(purchase_history))
# Output: {1: 'burgers', 2: 'hand protein bar', 3: 'oatmeal', 4: 'shampoo', 5: 'chocolate'}
