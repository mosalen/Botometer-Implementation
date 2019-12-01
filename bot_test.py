import botometer

rapidapi_key = "```" # now it's called rapidapi key
twitter_app_auth = {
    'consumer_key': '```',
    'consumer_secret': '```',
    'access_token': '```',
    'access_token_secret': '```',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

file_name = 'D:/twitterdata/real/ulist.txt'
user_list = open(file_name, encoding='utf-8').read().split('\n')

for screen_name, result in bom.check_accounts_in(user_list):
    print(screen_name)
    str_result = str(result.get('scores'))
    bot_result = open('D:/twitterdata/real/botresult.txt', "a")

    bot_result.write(screen_name + ' ')
    bot_result.write(str_result)
    bot_result.write("\n")
    bot_result.close()

# Check a single account by screen name
#result2 = bom.check_account('@realDonaldTrump')

# Check a single account by id
#result = bom.check_account(1548959833)

# Check a sequence of accounts
#accounts = ['@clayadavis', '@onurvarol', '@jabawack']
