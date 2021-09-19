from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext
from telegram import update,Update
import  logging,time
from sub import truecaller
from sub import smsbomber 
from threading import Thread

Flag=0
# flag is used to know where the input number should go 

api='YOUR API KEY'

help_txt='/truecaller - contact info\n/smsbomber - multiple sms spam\n/anime - latest anime episodes\n/sourcecode - Bot SourceCode\n'

logging.basicConfig(filename='bot.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)
logger = logging.getLogger(__name__)

updater=Updater(api)
dp=updater.dispatcher

# /start calls this funtion
def Start(update: Update, context) -> None:
	update.message.reply_text(f'Welcome {update.effective_user.first_name}')
	update.message.reply_text('Click /help for more info')
	print(update.effective_user.full_name)

		
# /help calls this funtion
def Help(update: Update,context) -> None:
	update.message.reply_text(help_txt)
	Flag = 0

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
	def smsCount(count):
		message=update.message.reply_text('messages sent  ')
		for i in range(1,count+1):
			context.bot.edit_message_text(chat_id=update.message.chat_id,message_id=message.message_id,text='messages sent ' + str(i))
			print(i)
			time.sleep(0.4)
				
	global Flag
	if Flag == 1:
		info=truecaller.main(update.message.text)
		for i in range(truecaller.length):
			update.message.reply_text(info[i])
		Flag = 0

	elif Flag == 2:
		t1=Thread(target=smsbomber.main,args=(update.message.text,))
		t2=Thread(target=smsCount, args=(50,))
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		Flag = 0


def Contact(update,context: CallbackContext):
	def smsCount(count):
		message=update.message.reply_text('messages sent  ')
		for i in range(1,count+1):
			context.bot.edit_message_text(chat_id=update.message.chat_id,message_id=message.message_id,text='messages sent ' + str(i))
			print(i)
			time.sleep(0.1)
					
	contact = update.effective_message.contact
	phone_no = contact.phone_number

	if len(phone_no)==13:
		phone=phone_no[3:] 

	global Flag
	if Flag == 1:
		info=truecaller.main(phone_no)
		for i in range(truecaller.length):
			update.message.reply_text(info[i])
		Flag = 0
			
	elif Flag == 2:
		t1=Thread(target=smsbomber.main,args=(phone_no,))
		t2=Thread(target=smsCount, args=(50,))
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		Flag = 0
		
		
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
dp.add_handler(CommandHandler('help', Help))
dp.add_handler(CommandHandler('truecaller', Truecaller))
dp.add_handler(CommandHandler('sourcecode', SourceCode))
dp.add_handler(MessageHandler(Filters.regex(r'^\d{10}$'),Number))
dp.add_handler(MessageHandler(Filters.regex(r'(\d{5}\s{1}\d{5})|(\d{3}-\d{3}-\d{4})|(\+\d{12})'),InvalidNumber))
dp.add_handler(CommandHandler('smsbomber',Smsbomber))
dp.add_handler(MessageHandler(Filters.contact, Contact))
dp.add_handler(MessageHandler(Filters.command, unknown_command))
dp.add_error_handler(error)
updater.start_polling()
updater.idle()

# To know more about handlers,updater,dispatchers please read the official documentation of python-telegram-bot
