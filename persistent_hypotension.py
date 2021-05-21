
# starting @ time that fluid bolus was completed and for the ensueing hour; create a list of blood pressures in chronilogical order from flowsheet data
vitals = [[100, 60, 70, 1350], [99, 50, 67, 1400], [89, 62, 70, 1410], [110, 40, 60, 1420], [110, 55, 66, 1430], [111, 49, 67, 1440],[111, 49, 67, 1450]]
# set parameters(optional, but CMS likes to change things)
lowmap = 65
lowsbp = 90
# identify vital sets in which either a sbp<90 or map < 65, insert a 1 at [0] if present, 0 if not.
for x in vitals:
    if x[0] < lowsbp or x[2] < lowmap:
        x.insert(0, 1)
    else:
        x.insert(0, 0)

# using an iterator, generate lists containing consecutive elements, loop through them looking for two that are both flagged with a 1 at [0]
for i in range(len(vitals) - 1):
    r = [vitals[i], vitals[i+1]]
    if r[0][0] == 1 and r[1][0] == 1:

        # if two hypotensive episodes are noted in a row, add element "vasopressor order" and "vasopressor initiated" to the
        print(
            f'Your patient had a blood pressure of {r[0][1]}/{r[0][2]}({r[0][3]}) at {r[0][4]} and {r[1][1]}/{r[1][2]}({r[1][3]}) at {r[1][4]}.. You need to start vasopressors')
