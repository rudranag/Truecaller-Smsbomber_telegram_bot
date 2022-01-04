from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext
from telegram import update,Update
from telegram.ext.dispatcher import run_async
import  logging,time,os
from sub import truecaller,smsbomber,databaseConnect


Flag=0
# flag is used to know where the input number should go 

#get tellegram bot api from environment variables
api=os.environ.get('api_key')

# create a log file
logging.basicConfig(filename='bot.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)
logger = logging.getLogger(__name__)

#initialize updater and dispatcher
updater=Updater(api)
dp=updater.dispatcher
db=databaseConnect.Database()

# /start calls this funtion
def Start(update: Update, context):
	update.message.reply_text(f'Welcome {update.effective_user.first_name}')
		

# /truecaller calls this funtion
def Truecaller(update: Update,context) -> None:
	update.message.reply_text('Enter a number without +91 or share contact')
	global Flag
	Flag = 1

# /smsbomber calls this funtion
def Smsbomber(update: Update,context) -> None:
	update.message.reply_text('Enter a number to spam or share contact')
	global Flag
	Flag = 2
		
# flag is used to determine which funtion should access phone number input
def Number(update: Update,context:CallbackContext) -> None:
	chat_id = update.message.chat_id
	mobile_number  = update.message.text			
	global Flag
	if Flag == 1:
		info=truecaller.main(update.message.text)
		for i in info:
			update.message.reply_text(i)
		Flag = 0
		

	elif Flag == 2:

		number_exists = db.check_before_bombing(mobile_number)

		if number_exists:
			update.message.reply_text('Sorry this number is protected')
		else:
			message=update.message.reply_text('messages sent  ')
			for i in range(1,51):
				time.sleep(0.4)
				smsbomber.Api(mobile_number)
				context.bot.edit_message_text(chat_id=update.message.chat_id,message_id=message.message_id,text='messages sent ' + str(i))
		Flag = 0

# this function is called when a contact is sent
def Contact(update,context: CallbackContext):

	chat_id = update.message.chat_id					
	contact = update.effective_message.contact
	phone_no = contact.phone_number

	if len(phone_no)==13:
		phoneNumber=phone_no[3:]
	else:
		phoneNumber=phone_no

	global Flag
	if Flag == 1:

		info=truecaller.main(phone_no)
		if info:
			for i in info:
				update.message.reply_text(i)
		else:
			update.message.reply_text('Sorry today\'s request limit has been reached')
			
	elif Flag == 2:

		number_exists = db.check_before_bombing(phoneNumber)

		if number_exists:
			update.message.reply_text('Sorry this number is protected')
		else:
			message=update.message.reply_text('messages sent 0')
			for i in range(1,51):
				time.sleep(0.4)
				smsbomber.Api(phoneNumber)
				context.bot.edit_message_text(chat_id=update.message.chat_id,message_id=message.message_id,text='messages sent ' + str(i))


		Flag = 0

# this will save your number and chat_id to database so it can check before bombing		
def protect(update: Update, context: CallbackContext) -> None:
    
    chat_id = update.message.chat_id
    
    try:
        mobileNo = context.args[0]

        exists = db.check_if_exists(chat_id,mobileNo)

        if mobileNo and exists:
            update.message.reply_text(f'{mobileNo} is in protected list')

        elif mobileNo and not exists:
            db.protect_number(chat_id,mobileNo)
            update.message.reply_text(f'{mobileNo} is protected')
    except IndexError:
        update.message.reply_text('Usage : /protect 9123456789')

# deletes your number from database so no protection   
def unprotect(update: Update, context: CallbackContext) -> None:
    
    chat_id = update.message.chat_id
    
    try:
        mobileNo = context.args[0]
        
        if mobileNo:
            count = db.unprotect_number(chat_id,mobileNo)
            if count:
                update.message.reply_text(f'{mobileNo} is unprotected')
            else:
                update.message.reply_text(f'Genjutsu of that level doesn\'t work on me')


    except IndexError:
        update.message.reply_text('Usage : /unprotect 9123456789')
		
def SourceCode(update: Update,context) -> None:
	print('Source code')
	update.message.reply_text('https://github.com/rudranag/Truecaller-telegram_bot')
	
# funtion to log errors         
def error(update, context):
	logger.warning('Update "%s" caused error "%s"', update, context.error)
	# This function will log the errors 
	
def unknown_command(update, context):
	update.message.reply_text("Sorry, I didn't understand that command.")
	# This function is used to tell the user it didnt recognize the command

def InvalidNumber(update, context):
	update.message.reply_text("Please enter a 10 digit number")
	# This function will detect phone number input with is not a 10 digit number 
	
dp.add_handler(CommandHandler('start', Start))
dp.add_handler(CommandHandler('truecaller', Truecaller,run_async=True))
dp.add_handler(CommandHandler('sourcecode', SourceCode))
dp.add_handler(CommandHandler("protect", protect))
dp.add_handler(CommandHandler("unprotect", unprotect))
dp.add_handler(MessageHandler(Filters.regex(r'^\d{10}$'),Number,run_async=True))
dp.add_handler(MessageHandler(Filters.regex(r'(\d{5}\s{1}\d{5})|(\d{3}-\d{3}-\d{4})|(\+\d{12})'),InvalidNumber))
dp.add_handler(CommandHandler('smsbomber',Smsbomber,run_async=True))
dp.add_handler(MessageHandler(Filters.contact, Contact,run_async=True))
dp.add_handler(MessageHandler(Filters.command, unknown_command))
dp.add_error_handler(error)
updater.start_polling()
updater.idle()

# To know more about handlers,updater,dispatchers please read the official documentation of python-telegram-bot
