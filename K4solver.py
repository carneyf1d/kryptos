
###
# K4 ciphertext
K4 = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
###
import numpy
from K3solver import rotate_clockwise
from K3solver import create_transposition_table

K3 = ("ENDyaHrOHNLSRHEOCPTEOIBIDYSHNA"
    "IACHTNREYULDSLLSLLNOHSNOSMRWXMNE"
    "TPRNGATIHNRARPESLNNELEBLPIIACAE"
    "WMTWNDITEENRAHCTENEUDRETNHAEOE"
    "TFOLSEDTIWENHAEIOYTEYQHEENCTAYCR"
    "EIFTBRSPAMHNEWENATAMATEGYEERLB"
    "TEEFOASFIOTUETUAEOTOARMAEERTNRTI"
    "BSEDDNIAAHTTMSTEWPIEROAGRIEWFEB"
    "AECTDDHILCEIHSITEGOEAOSDDRYDLORIT"
    "RKLMLEHAGTDHARDPNEOHMGFMFEUHE"
    "ECDMRIPFEIMEHNLSSTTRTVDOHW")
K3 = K3.upper()
    
Ktot = K3 + K4

input_string = K3
num_columns = 24
table = create_transposition_table(input_string, num_columns)
new_table = rotate_clockwise(table)
table = create_transposition_table(new_table, 24)
#new_table = rotate_clockwise(table)
#last_table = create_transposition_table(new_table,7)

#table = create_transposition_table(input_string, 8)
#table = rotate_clockwise(table)
