import resistance
import multiplier as m
import resistance_value as r
import tolerance as t

r1_digit = r.banddigit()
r1_multiplier = m.multiplier_calc(r1_digit)
r1_tolerance = t.tolerance_calc(r1_multiplier)
Resistance1 = resistance.Resistance(r1_digit,r1_multiplier,r1_tolerance)

print()
Resistance1.displayinfo()






