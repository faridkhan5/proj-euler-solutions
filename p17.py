#Number letter counts
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

letters = {
    0:'',
    1: 'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    100:'onehundred',
    200:'twohundred',
    300:'threehundred',
    400:'fourhundred',
    500:'fivehundred',
    600:'sixhundred',
    700:'sevenhundred',
    800:'eighthundred',
    900:'ninehundred',
    1000:'onethousand'
}

def number_letter_counts(n):
    count = 0
    for i in range(1,n+1):
        if i in letters:
            count += len(letters[i])
        else:
            if 20<=i<100: #20 to 100
                if i//10 == 2:
                    l = 'twenty'+ letters[i%10]
                    count += len(l)
                if i//10 == 3:
                    l = 'thirty'+ letters[i%10]
                    count += len(l)
                if i//10 == 4:
                    l = 'forty'+ letters[i%10]
                    count += len(l)
                if i//10 == 5:
                    l = 'fifty'+ letters[i%10]
                    count += len(l)
                if i//10 == 6:
                    l = 'sixty'+ letters[i%10]
                    count += len(l)
                if i//10 == 7:
                    l = 'seventy'+ letters[i%10]
                    count += len(l)
                if i//10 == 8:
                    l = 'eighty'+ letters[i%10]
                    count += len(l)
                if i//10 == 9:
                    l = 'ninety'+ letters[i%10]
                    count += len(l)
                letters[i] = l  #adding to dict for future use
            else: #100 to 999
                if i//100 == 1:
                    h = 'onehundredand' + letters[i%100]
                    count += len(h)
                if i//100 == 2:
                    h = 'twohundredand' + letters[i%100]
                    count += len(h)
                if i//100 == 3:
                    h = 'threehundredand' + letters[i%100]
                    count += len(h)
                if i//100 == 4:
                    h = 'fourhundredand' + letters[i%100]
                    count += len(h)
                if i//100 == 5:
                    h = 'fivehundredand' + letters[i%100]
                    count += len(h)
                if i//100 == 6:
                    h = 'sixhundredand' + letters[i%100]
                    count += len(h)
                if i//100 == 7:
                    h = 'sevenhundredand' + letters[i%100]
                    count += len(h)
                if i//100 == 8:
                    h = 'eighthundredand' + letters[i%100]
                    count += len(h)
                if i//100 == 9:
                    h = 'ninehundredand' + letters[i%100]
                    count += len(h)

    return count

print(number_letter_counts(1000))
