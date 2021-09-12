from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import update,Update
import  logging
from sub import truecaller
from sub import smsbomber 

T=0
S=0
# S,T are flags to know where the input number should go 

api='Your Api key here'

list1='/truecaller - contact info\n/smsbomber - multiple sms spam\n/anime - latest anime episodes\n/sourcecode - Bot SourceCode\n'

logging.basicConfig(filename='bot.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

updater=Updater(api)
dp=updater.dispatcher

# /start calls this funtion
def Start(update: Update,context) -> None:
    update.message.reply_text(f'Welcome {update.effective_user.first_name}')
    update.message.reply_text('Click /help for more info')
    print(str(update.message.chat.username),update.effective_user.full_name)
    
        
# /help calls this funtion
def Help(update: Update,context) -> None:
    update.message.reply_text(list1)

# /truecaller calls this funtion
def Truecaller(update: Update,context) -> None:
    update.message.reply_text('Enter a number without +91')
    global T,S
    T=1
    S=0

# /smsbomber calls this funtion
def Smsbomber(update: Update,context) -> None:
    update.message.reply_text('Enter a number to spam 50 msgs')
    global S,T
    S=1
    T=0

# flags are used to determine which funtion should access phone number input
def Number(update: Update,context) -> None:
    global S,T
    if T==1 and S==0:
        x=truecaller.main(update.message.text)
        for i in range(truecaller.length):
            update.message.reply_text(x[i])
    elif T==0 and S==1:
        update.message.reply_text(smsbomber.main(update.message.text))


def Contact(update,context):
    contact = update.effective_message.contact
    phone = contact.phone_number
    if len(phone)==13:
        phone=phone[3:] 

    global S,T
    if T==1 and S==0:
        x=truecaller.main(phone)
        #print(truecaller.length)
        for i in range(truecaller.length):
            
            update.message.reply_text(x[i])
            
    elif T==0 and S==1:
        update.message.reply_text(smsbomber.main(phone))
        
    
def SourceCode(update: Update,context) -> None:
    print('Source code')
    update.message.reply_text('https://github.com/rudranag/Truecaller-telegram_bot')
    
# funtion to log errors         
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
def unknown(update, context):
    update.message.reply_text("Sorry, I didn't understand that command.")
    
dp.add_handler(CommandHandler('start', Start))
dp.add_handler(CommandHandler('help', Help))
dp.add_handler(CommandHandler('truecaller', Truecaller))
dp.add_handler(CommandHandler('sourcecode', SourceCode))
dp.add_handler(MessageHandler(Filters.regex(r'\d{10}'),Number))
dp.add_handler(CommandHandler('smsbomber',Smsbomber))
dp.add_handler(MessageHandler(Filters.contact, Contact))
dp.add_handler(MessageHandler(Filters.command, unknown))
dp.add_error_handler(error)
updater.start_polling()
updater.idle()
