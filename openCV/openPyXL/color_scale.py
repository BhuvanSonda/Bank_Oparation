from openpyxl.formatting.rule import ColorScale, FormatObject

from openpyxl.styles import Color

first = FormatObject(type='min')

last = FormatObject(type='max')

# colors match the format objects:

colors = [Color('AA0000'), Color('00AA00')]

cs2 = ColorScale(cfvo=[first, last], color=colors)

# a three color scale would extend the sequences

mid = FormatObject(type='num', val=40)

colors.insert(1, Color('00AA00'))

cs3 = ColorScale(cfvo=[first, mid, last], color=colors)

# create a rule with the color scale

from openpyxl.formatting.rule import Rule

rule = Rule(type='colorScale', colorScale=cs3)