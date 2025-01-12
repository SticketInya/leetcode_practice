from typing import Dict, List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        for i in range(len(nums) - 1):
            products[i + 1] = products[i] * nums[i]

        post_fix = 1
        for i in range(len(nums) - 1, 0, -1):
            post_fix *= nums[i]
            products[i - 1] *= post_fix

        return products

    def product_except_self_division(self, nums: List[int]) -> List[int]:
        """
        The task specified not to use the divison operator, but depending on
        the site you use, this condition is a follow-up/optional.
        """
        product_of_array = 1
        zero_count = 0
        for i in range(0, len(nums), 1):
            if nums[i] != 0:
                product_of_array *= nums[i]
            else:
                zero_count += 1

        products: List[int] = [0] * len(nums)
        # If there is more than 1 zero the product is always zero
        if zero_count > 1:
            return products

        for i in range(0, len(nums), 1):
            if not zero_count:
                products[i] = int(product_of_array / nums[i])
            elif nums[i] == 0:
                products[i] = product_of_array

        return products
