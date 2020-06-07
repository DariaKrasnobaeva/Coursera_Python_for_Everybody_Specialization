text = "X-DSPAM-Confidence:    0.8475";

text.find('0')

text_new=text[text.find('0'):]

f=float(text_new)

print(f)
