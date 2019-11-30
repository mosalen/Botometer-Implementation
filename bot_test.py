import botometer

rapidapi_key = "451607b1e0msh25b2412730c45c8p11508djsn9676e0259193" # now it's called rapidapi key
twitter_app_auth = {
    'consumer_key': 'tVfwIeDM4d4Pq6GnrsHHbpBlE',
    'consumer_secret': 'ghMvvhw0BmId7AdU6iyUk6Jei2FaI9dGMDiDU79jftzbDY6XfX',
    'access_token': '1180778301414989824-IvztT5SV2hMWx45yHAScbodTtOLcJ4',
    'access_token_secret': '52yv8LKQKtuSqMtfQs7ij5xhxgQ6hYsefE3O0akBuIzkV',
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
