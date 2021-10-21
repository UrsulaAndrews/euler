#correct answer = 21124 

ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
           7: 'seven', 8: 'eight', 9: 'nine'}
teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninety'}

toOneThousand = ''
toOneThousandList = []
for i in ones:  #for 1 - 0
    toOneThousand += ones[i]
    toOneThousandList.append(ones[i])
for i in teens: #for 10 - 19
    toOneThousand += teens[i]
    toOneThousandList.append(teens[i])
for i in tens:  #for 20 - 99
    for j in ones:
        toOneThousand += tens[i] + ones[j]
        toOneThousandList.append(tens[i] + ones[j])
for i in ones:  #for ?00 - ?99
    if ones[i] == '':
        continue
    for j in ones:
        if ones[j] == '':
            toOneThousand += ones[i] + 'hundred'
            toOneThousandList.append(ones[i] + 'hundred')
        else:
            toOneThousand += ones[i] + 'hundredand' + ones[j]
            toOneThousandList.append(ones[i] + 'hundredand' + ones[j])
for i in ones:  #for ?11 - ?19
    if ones[i] == '':
        continue
    for j in teens:
        toOneThousand += ones[i] + 'hundredand' + teens[j]
        toOneThousandList.append(ones[i] + 'hundredand' + teens[j])
for i in ones:  #for ??1 - ??9
    if ones[i] == '':
        continue
    for j in tens:
        for k in ones:
            toOneThousand += ones[i] + 'hundredand' + tens[j] + ones[k]
            toOneThousandList.append(ones[i] + 'hundredand' + tens[j] + ones[k])
toOneThousand += 'onethousand'
toOneThousandList.append('onethousand')

print(len(toOneThousand))
for n in toOneThousandList:
    print(n)
