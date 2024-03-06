import pandas as pd

# Step 1: Read Data from CSV File
def read_data(file_path):
    try:
        if not file_path:
            raise ValueError("Empty file path provided")
        data = pd.read_csv(file_path)
        # Check if the file is empty
        if data.empty:
            print("Warning: Empty file")
            return None
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except pd.errors.ParserError as pe:
        print("Error: Invalid file format.")
        return None
    except Exception as e:
        print("Error:", e)
        return None


# Step 2: Compute Total Revenue by Month
def total_revenue_by_month(data):
    try:
        data['order_date'] = pd.to_datetime(data['order_date'])
        data['month'] = data['order_date'].dt.to_period('M')
        revenue_by_month = data.groupby('month')['product_price'].sum()
        return revenue_by_month
    except ValueError as ve:
        print("Invalid date encountered:", ve)
        raise ValueError("Invalid date encountered in the dataset")
    except Exception as e:
        print("Error:", e)
        return None

# Step 3: Compute Total Revenue by Product
def total_revenue_by_product(data):
    try:
        revenue_by_product = data.groupby('product_name')['product_price'].sum()
        return revenue_by_product
    except Exception as e:
        print("Error:", e)
        return None

# Step 4: Compute Total Revenue by Customer
def total_revenue_by_customer(data):
    try:
        revenue_by_customer = data.groupby('customer_id')['product_price'].sum()
        return revenue_by_customer
    except Exception as e:
        print("Error:", e)
        return None

# Step 5: Identify Top 10 Customers by Revenue
def top_10_customers(data):
    try:
        revenue_by_customer = data.groupby('customer_id')['product_price'].sum()
        sorted_customers = revenue_by_customer.sort_values(ascending=False)
        if len(sorted_customers) <= 10:
            return sorted_customers
        else:
            top_10_customers = sorted_customers.head(10)
            return top_10_customers
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    file_path = 'orders.csv'
    data = read_data(file_path)
    if data is not None:
        revenue_by_month = total_revenue_by_month(data)
        if revenue_by_month is not None:
            print("Total Revenue by Month:")
            print(revenue_by_month)

        revenue_by_product = total_revenue_by_product(data)
        if revenue_by_product is not None:
            print("\nTotal Revenue by Product:")
            print(revenue_by_product)

        revenue_by_customer = total_revenue_by_customer(data)
        if revenue_by_customer is not None:
            print("\nTotal Revenue by Customer:")
            print(revenue_by_customer)

        top_customers = top_10_customers(data)
        if top_customers is not None:
            print("\nTop 10 Customers by Revenue:")
            print(top_customers)

