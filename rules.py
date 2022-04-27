
rules = [

        {"value": "from:POC19881988", "tag": "POC"},
        #Telecom
        {"value": "from:Omantel OR from:OoredooOman OR from:VodafoneOMN OR from:AwasrOm", "tag": "Telecom Tweets"},
        {"value": "@Omantel OR @OoredooOman OR @VodafoneOMN OR @AwasrOm", "tag": "Telecom Mentions"},
        {"value": "to:Omantel OR to:OoredooOman OR to:VodafoneOMN OR to:AwasrOm", "tag": "Telecom Replies"},
        #banking
        {"value": "from:BankMuscat OR from:BankDhofar OR from:Bank_Nizwa OR from:sohar_intl OR from:nbobank", "tag": "Banking Tweets"},
        {"value": "@BankMuscat OR @BankDhofar OR @Bank_Nizwa OR @sohar_intl OR @nbobank", "tag": "Banking Mentions"},
        {"value": "to:BankMuscat OR to:BankDhofar OR to:Bank_Nizwa OR to:sohar_intl OR to:nbobank", "tag": "Banking Replies"},
    ]




# rules = [

#         {"value": "from:POC19881988", "tag": "POC"},
#         #CPA
#         {"value": "from:cpa_oman", "tag": "CPA Tweets"},
#         {"value": "@cpa_oman", "tag": "CPA Mentions"},
#         {"value": "to:cpa_oman ", "tag": "CPA Replies"},
#     ]
