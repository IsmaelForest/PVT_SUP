
WEBSITE_LIST = {"https://www.inuit.com/":
                    {"specifics":"ablock=true;",
                    "main_page": 'id;MegaNavMenuItem',
                    "endpoints":
                    { 
                    "login-page":'direct-link;sign-in',
                    "products": 'partial link;products/',
                    "supports_and_blog": 'menuitem[2]',
                    "Company":'id;menuitem[3]',
                    "Careers":'id;menuitem[4]',

                    },
                    "sub-endpoints":
                    {
                    
                            "login":{
                                "sign_in": ""
                            },
                            "product":{
                                "turbotax":'relies_prev:full-link;https://turbotax.intuit.ca/tax/software',
                                "credit_Karma":'relies_prev:full-link;https://www.creditkarma.ca/',
                                "quickbook_self_employed": 'relies_prev:full-link;https://quickbooks.intuit.com/ca/self-employed/?sc=seq_intuit_qbse_ca_click_nav',
                                "mint":  'relies_prev:full-link;https://mint.intuit.com/',
                                "small_business":  'relies_prev:partial link text;#smallbusiness',
                                "quickbooks":  'relies_prev:full-link;https://quickbooks.intuit.com/ca/?sc=seq_intuit_qb_ca_click_nav',
                                "payments":'relies_prev:full-link ;https://quickbooks.intuit.com/ca/stationery/?sc=seq_intuit_qb_ca_click_nav',
                                "accountants":'relies_prev:full-link;https://quickbooks.intuit.com/ca/payments/?sc=seq_intuit_qb_payments_ca_click_nav',
                                "Profile":'relies_prev:full-link;https://profile.intuit.ca/',
                                "QuickBookAccountants":'relies_prev:full-link;https://quickbooks.intuit.com/ca/accountants/',
                                },
                            "supports_and_blogs":{
                                "Overview":'relies_prev:partial link text;support/',
                                "Quickbook_music":'relies_prev:full-link;https://quickbooks.intuit.com/learn-support/ca-quickbooks-community/misc/03/community-ca',
                                "Mint_community":'relies_prev:full-link;https://mint.intuit.com/support/en-us',
                                "ProConnect_support":'relies_prev:full-link;https://proconnect.intuit.com/community/',
                                "blogs":'relies_prev:full-link;#blogs',
                                "intuit_blog":'relies_prev:full-link;https://www.intuit.com/blog/',
                                "tax_pro":'relies_prev:full-link;https://proconnect.intuit.com/taxprocenter/?s_cid=intuit.com_Homepage_taxprocenter',
                                "turbotax_blog":'relies_prev:full-link;https://blog.turbotax.intuit.com/',
                                "mint_blog":'relies_prev:full-link;https://mint.intuit.com/blog/',
                            },
                            "supports_and_blogs":{
                                "Overview":'relies_prev:full-link;support/',
                                "":'relies_prev:partial link text;',
                                "":'relies_prev:partial link text;',
                                "":'relies_prev:partial link text;',
                                "":'relies_prev:partial link text;',
                                "":'relies_prev:partial link text;',
                                "":'relies_prev:partial link text;',
                                "":'relies_prev:partial link text;',
                                "":'relies_prev:partial link text;',
                                "":'relies_prev:partial link text;',   
                                
                        
                            }
                        },
                    }
}