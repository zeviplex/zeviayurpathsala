import telebot
import os

# Replace 'your_token_here' with your actual bot token
bot_token = '6595930371:AAEpa4_PDY_fE8i9Lr7JM33oF4tCyojYllo'

# Initialize the bot
bot = telebot.TeleBot(bot_token)

# Create a dictionary to map user queries to PDF file paths
query_to_pdf = {
    "treatment of cold": "pdfs/cold_treatment.pdf",
    "ayurvedic remedies": "pdfs/ayurvedic_remedies.pdf",
    "some other query": "pdfs/some_other.pdf",
    "Panchakarma(Short book)@Bamsbooksin": "pdf/Panchakarma(Short book)@Bamsbooksin.pdf",
    # Add mappings for all your PDF files (100 PDFs)
    # For example:
    "keyword1": "pdfs/pdf1.pdf",
    "keyword2": "pdfs/pdf2.pdf",
    "panchakarma": "pdf/Panchakarma(Short book)@Bamsbooksin.pdf",
    # Continue adding mappings for all 100 PDF files
}

# Define a function to handle user queries
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Welcome to the Ayurvedic PDF Bot! Send me a keyword to search for PDFs.")

@bot.message_handler(func=lambda message: message.text.lower() in ['hi', 'hello'])
def handle_greeting(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}!")

@bot.message_handler(func=lambda message: message.text.lower() == 'who are you')
def handle_whoami(message):
    bot.send_message(message.chat.id, "I am the Ayurvedic PDF Bot. I'm here to help you find and download PDFs.")

@bot.message_handler(func=lambda message: message.text.lower() == 'thanks')
def handle_thanks(message):
    bot.send_message(message.chat.id, "You're welcome! If you have any more questions or need PDFs, feel free to ask.")

@bot.message_handler(func=lambda message: message.text.lower() == 'what is this')
def handle_whatisthis(message):
    bot.send_message(message.chat.id, "This is the Ayurvedic PDF Bot. You can use it to search for and download Ayurvedic PDFs by sending keywords.")

@bot.message_handler(func=lambda message: True)
def handle_query(message):
    search_query = message.text.lower()
    
    if search_query in query_to_pdf:
        pdf_path = query_to_pdf[search_query]
        with open(pdf_path, 'rb') as pdf_file:
            bot.send_document(message.chat.id, pdf_file, caption=f"PDF: {search_query}")
    else:
        # Send a GIF with the message "No PDFs found" when no matching PDF is found
        gif_path = 'no_matching_pdf.gif'  # Replace with the actual path to your GIF
        with open(gif_path, 'rb') as gif_file:
            bot.send_animation(message.chat.id, gif_file, caption="No PDFs found")

# Start the bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
