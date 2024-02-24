# Signals
### generate_sku_num
Signal that is used in Supplier(2) Product(3) and Invoice(3) table to generate
the sku_num field respectively.
- This function generates a unique SKU (Stock Keeping Unit) number for a given
instance of a sender (which typically corresponds to a Supplier, Product or Invoice object).
-   If the instance already has a SKU number assigned, this function does nothing.

- Parameters:
    - sender: The model class from which the signal is sent.
    - instance: The instance of the model (Supplier, Product or Invoice) for which the SKU is generated.
    - k (optional): The length of the SKU number to be generated. Default is 2.
    - *args, **kwargs: Additional arguments that can be passed to the function.
- Returns:
    - None. The SKU number is generated and assigned to the instance in-place.
- Time Complexity:
    - O(nk), where n is the number of iterations required to generate
     a unique SKU number and k is the length of the SKU number generated.

    - Space Complexity:
        O(k), where k is the length of the SKU number generated.

