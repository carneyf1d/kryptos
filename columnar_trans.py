def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
    order = {int(val): num for num, val in enumerate(key)}
    num_columns = len(key)
    chunk_length = len(plaintext) // num_columns
    chunks = split_len(plaintext, chunk_length)
    
    # Create the transposition table (list of lists)
    transposition_table = [list(chunk) for chunk in chunks]
    
    # Arrange columns according to the key order
    encoded_columns = ["".join(transposition_table[order[col]]) for col in range(1, num_columns + 1)]
    
    # Read off the ciphertext column by column
    ciphertext = "".join(encoded_columns)
    return ciphertext

# Example usage:
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
key = (1,4,7,3,6,2,5)
ciphertext = encode(key, K3)
print("Ciphertext:", ciphertext)