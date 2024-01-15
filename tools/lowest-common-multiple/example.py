from lowest_common_multiple import LowestCommonMultiple

values_low	= [2,4,6,8,27]
values_high	= [181576,11653,21409,12737]

lcd	= LowestCommonMultiple()

lowest	= lcd.find_common(values_low)
print(f"The lowest common multiple for low values array is: {lowest}")

lowest	= lcd.find_common(values_high)
print(f"The lowest common multiple for low values array is: {lowest}")
