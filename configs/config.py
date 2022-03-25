
CONFIG = {
    "headers": [
        {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        },
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        },
        {
            "Connection": "keep-alive",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        },
        {
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"
        }
    ],
    "proxies_url": "https://free-proxy-list.net/",
    "argparse": {
        "description": "Ad Punisher: bringing fraudulent ads to justice",
        "file": "Receives a file path with ads urls",
        "help": "Show this help message and exit."
    },
    "logs": {
        "process_start": "[{}>{}] ~ Ad Punisher started!",
        "process_get_urls": "[{}>{}] ~ Acquiring targets...",
        "process_ads_empty": "[{}>{}] ~ Nothing url was found",
        "process_kill_prep": "[{}>{}] ~ Starting process to {}kill{} ads",
        "process_ip_get": "\t[{}>{}] ~ Proxies collected: {}",
        "process_ad_alive_check": "[{}>{}] ~ Checking if pages is alive",
        "process_body_unchanged": "\t[{}>{}] ~ The body of page {} is unchanged yet",
        "process_body_changed": "\t[{}>{}] ~ The body of page {} was changed!",
        "process_clicking_ad": "\t[{}>{}] ~ Url {} clicked with ip {}{}{}",
        "process_done": "[{}>{}] ~ Ad Punisher done!",

        "key_interrupt": "[{}!{}] ~ Well, it looks like someone interrupted the execution...",
        "error_start_bot": "[{}!{}] ~ An error occurred when starting bot: {}",
        "error_request_ad": "\t[{}>{}] ~ Error when trying to access page {}: {}",
        "error_proxy_fail": "\t\t[{}!{}] ~ The proxy {}{}{} can't connect on the page, maybe it was blocked. Rotating...",

        "presentation": {
            "logo": """{}

                                    .sNMMMMMMMMMMMMMMd+.     
                                  .sNMMMMMMMMMMMMMMMMMMMy.   
                                .hMMMMMMMMMMMMMMMMMMMMMMMNo  
                               `mMMMMMMMMMMMMMMMMMMMMMMMMMMs 
                               /MMMMMMMMMMMMMMMMMMMMMMMMMMMM:
                               +MNmNMMMMMMMMMMMMMMMMMMMMNmNM+
                               /My`./smNMMMMMMMMMMMMNds:-`+M:
                               `Mm`   `-odNMMMMMMNds:`    hm 
                                oMh:      ./yNMh+-`     :yM+ 
                                 +NMNmddhhdmd/+hmdhhddmNMMN` 
                                 yNMMMMNNMMN.+o.mMMMMNmMMMN` 
                                 dMMMy:.-MMMyMMsNMMM/../MNy  
                                 `+:::  `MMmMMmMymMN`  ./.   
                                         hMoMNoM:NM/         
                                         sMoMNoM+MM`         
                                         oMoMNsMoMN          
                                         /M+MNsMoMm          
                                         :M+NmoM+Mh          
                                          +-so/s-y:       
            """,
            "description": "\n\t\t\t[{}>{}] ~ Ad Punisher: bringing fraudulent ads to justice"
                           "\n\t\t\t[{}>{}] ~ by Eraldo Coyle\n"
        }
    }
}
