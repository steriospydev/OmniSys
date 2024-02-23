import re
import random
import string

def generate_sku_num(sender, instance, k=2, *args, **kwargs):
    """Signal that is used in Supplier and Product table to generate
       the sku_num field respectively.
    Time Complexity:
        O(nk), where n is the number of iterations required to generate
        a unique sku_num and k is the length of the sku_num generated.
    Space Complexity:
        O(k), where k is the length of the sku_num generated.
    """
    if not instance.sku_num:
        while True:
            identifier = ''.join(random.choices(string.ascii_uppercase, k=k))
            if not sender.objects.filter(sku_num=identifier).exists():
                break
        instance.sku_num = identifier
