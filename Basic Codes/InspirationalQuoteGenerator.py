import random

def generate_inspirational_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("Inspirational Quote Generator")
    input("Press Enter to generate an inspirational quote...")

    quote = generate_inspirational_quote()
    print("Inspirational Quote:", quote)
