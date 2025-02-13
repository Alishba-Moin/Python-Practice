# Write a Python program to replace placeholders <|Name|> and <|Date|> in a letter template with specific values.

letter = '''   Dear <|Name|>,
        You are selected! 
        <|Date|>'''
print(letter.replace("<|Name|>", "Alishba").replace("<|Date|>", "18-November-2025"))