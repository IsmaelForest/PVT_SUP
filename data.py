WEBSITE_LIST = {
                "https://www.intuit.com/":
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
                                "turbotax":':full-link;https://turbotax.intuit.ca/tax/software',
                                "credit_Karma":':full-link;https://www.creditkarma.ca/',
                                "quickbook_self_employed": ':full-link;https://quickbooks.intuit.com/ca/self-employed/?sc=seq_intuit_qbse_ca_click_nav',
                                "mint":  ':full-link;https://mint.intuit.com/',
                                "small_business":  ':partial link text;#smallbusiness',
                                "quickbooks":  ':full-link;https://quickbooks.intuit.com/ca/?sc=seq_intuit_qb_ca_click_nav',
                                "payments":':full-link ;https://quickbooks.intuit.com/ca/stationery/?sc=seq_intuit_qb_ca_click_nav',
                                "accountants":':full-link;https://quickbooks.intuit.com/ca/payments/?sc=seq_intuit_qb_payments_ca_click_nav',
                                "Profile":':full-link;https://profile.intuit.ca/',
                                "QuickBookAccountants":':full-link;https://quickbooks.intuit.com/ca/accountants/',
                                },
                            "supports_and_blogs":{
                                "Overview":':partial link text;support/',
                                "Quickbook_music":':full-link;https://quickbooks.intuit.com/learn-support/ca-quickbooks-community/misc/03/community-ca',
                                "Mint_community":':full-link;https://mint.intuit.com/support/en-us',
                                "ProConnect_support":':full-link;https://proconnect.intuit.com/community/',
                                "blogs":':full-link;#blogs',
                                "intuit_blog":':full-link;https://www.intuit.com/blog/',
                                "tax_pro":':full-link;https://proconnect.intuit.com/taxprocenter/?s_cid=intuit.com_Homepage_taxprocenter',
                                "turbotax_blog":':full-link;https://blog.turbotax.intuit.com/',
                                "mint_blog":':full-link;https://mint.intuit.com/blog/',
                            },
                            "supports_and_blogs":{
                                "Overview":':full-link;support/',
                            }
                        },
                    },
                "https://playstation.com/en-ca":{
                    "specifics":"ablock=true;",
                    "endpoints":
                    { 
                        "login":'css selector;#sb-social-toolbar-root > div > button',
                        "games": 'id;menu-button-primary--msg-games',
                        "hardware": 'id;menu-button-primary--msg-hardware',
                        "services": 'id;menu-button-primary--msg-services',
                        "shop": 'id;menu-button-primary--msg-shop',
                        "support": 'id;menu-button-primary--msg-support',
                        "sony":'full link;https://www.sony.com/en/',
                        "find-out-more":'css selector;a.cta__primary[data-dtm-label="Find out more"]',
                        "list-games":'rand_ind:css selector;a.media-block.media-block--image[data-component="image-block"]',
                        "footer":'',
                        "merch": 'rand_ind:css selector;a.cta__purchase[data-uuid="eb0141d7-48d2-304a-b9cd-36bd66d8d567"]'
                    },
                    "sub-endpoints":
                    {
                        "games":
                                {
                                    "Ps5":'id;link-secondary--msg-ps5',
                                    "Ps4":'id;link-secondary--msg-ps4',
                                    "Ps-vr2":'id;link-secondary--msg-ps-vr2',
                                    "Ps-plus":'id;link-secondary--msg-ps-plus',
                                    "buy-games":'id;link-secondary--msg-buy-games',
                                    "Ps-Indies":'id;link-link-list--msg-games-0',
                                    "Ps4-on-Ps5":'id;link-link-list--msg-games-1',
                                    "Free":'id;link-link-list--msg-games-2',
                                    "Ps-on-Pc":'id;link-link-list--msg-games-3',
                                    "Deals-Offers":'id;link-link-list--msg-games-4'
                                },
                        "hardware": 
                                {
                                    "dualsense":'id;link-link-list--msg-hardware-0',
                                    "pulse-3d-wireless":'id;link-link-list--msg-hardware-1',
                                    "DualShock":'id;link-link-list--msg-hardware-2',
                                    "Ps4-Ps5-accessories":'id;link-link-list--msg-hardware-3',
                                    "vr":'id;link-link-list--msg-hardware-4',
                                },
                        "services": 
                                {
                                    "Ps-Stars":'id;link-secondary--msg-ps-stars',
                                    "Ps5-entertainement":'id;link-link-list--msg-services-0',
                                    "Ps4-entertainement":'id;link-link-list--msg-services-1',

                                },
                        "news": 
                                {
                                    "Ps-Blog":'id;link-secondary--msg-ps-blog',
                                    "month-ps":'id;link-secondary--msg-ps-month-ps',
                                    "competition":'id;link-link-list--msg-news0',
                                    "competition":'id;link-link-list--msg-news1',
                                    "privacy":'id;link-link-list--msg-news2',
                                },
                        "shop": 
                                {
                                    "Ps-store":'id;link-secondary--msg-ps-store',
                                    "ps-gear":'id;link-secondary--msg-ps-gear',
                                    "new-release":'id;link-link-list--msg-shop-0',
                                    "discounts":'id;link-link-list--msg-shop-1',
                                    "collections":'id;link-link-list--msg-shop-2',
                                    "gift-cards":'id;link-link-list--msg-shop-3',
                                    "ps-plus-subscribe":'id;link-link-list--msg-shop-4',
                                    
                                },
                        "support": 
                                {
                                    "support":'id;link-secondary--msg-support',
                                    "psn-status":'id;link-secondary--msg-psn-status',
                                    "account":'id;link-link-list--msg-support-0',
                                    "store":'id;link-link-list--msg-support-1',
                                    "subscription":'id;link-link-list--msg-support-3',
                                    "hardware":'id;link-link-list--msg-store-4',                                    
                                },
                                
                        "list-games":  
                                {
                                "buy-now":'class name;tertiary-cta'
                                },
                        "footer":
                                {
                                    #about
                                    "SIE":'rand_ind;css selector;#accordion-panel-1 > ul > li:nth-child(1) > a',
                                    "careers":'rand_ind;css selector;#accordion-panel-1 > ul > li:nth-child(2) > a',
                                    "Ps-studios":'rand_ind;css selector;#accordion-panel-1 > ul > li:nth-child(3) > a',
                                    "corporate":'rand_ind;css selector;#accordion-panel-1 > ul > li:nth-child(4) > a',
                                    #values
                                    "Environement":'rand_ind;css selector;#accordion-panel-3 > ul > li:nth-child(1) > a',
                                    "Accessibility":'rand_ind;css selector;#accordion-panel-3 > ul > li:nth-child(2) > a',
                                    "Online Safety":'rand_ind;css selector;#accordion-panel-3 > ul > li:nth-child(3) > a',
                                    "diversity":'rand_ind;css selector;#accordion-panel-3 > ul > li:nth-child(4) > a',
                                    #support    
                                    "support-hub":'rand_ind;css selector;#accordion-panel-4 > ul > li:nth-child(1) > a',
                                    "ps-safety":'rand_ind;css selector;#accordion-panel-4 > ul > li:nth-child(2) > a',
                                    "psn-status":'rand_ind;css selector;#accordion-panel-4 > ul > li:nth-child(3) > a',
                                    "ps-repairs":'rand_ind;css selector;#accordion-panel-4 > ul > li:nth-child(4) > a',
                                    "password-reset":'rand_ind;css selector;#accordion-panel-4 > ul > li:nth-child(5) > a',
                                    "Manuals":'rand_ind;css selector;#accordion-panel-4 > ul > li:nth-child(6) > a',
                                    #Resources
                                    "psn-tos":'rand_ind;css selector;#accordion-panel-5 > ul > li:nth-child(1) > a',
                                    "psn-cancellation":'rand_ind;css selector;#accordion-panel-5 > ul > li:nth-child(2) > a',
                                    "age-ratings":'rand_ind;css selector;#accordion-panel-5 > ul > li:nth-child(3) > a',
                                    "health-warnings":'rand_ind;css selector;#accordion-panel-5 > ul > li:nth-child(4) > a',
                                    "developers":'rand_ind;css selector;#accordion-panel-5 > ul > li:nth-child(5) > a',
                                    "glossary":'rand_ind;css selector;#accordion-panel-5 > ul > li:nth-child(6) > a',
                                    "ios":'css selector;#accordion-panel-connect > ul > li:nth-child(2) > a',
                                    #connect
                                    "facebook":'css selector;#accordion-panel-connect > ul > li.social-links > a:nth-child(1)',
                                    "twitter":'css selector;#accordion-panel-connect > ul > li.social-links > a:nth-child(2)',
                                    "Instagram":'css selector;#accordion-panel-connect > ul > li.social-links > a:nth-child(3)',
                                    "youtube":'css selector;#accordion-panel-connect > ul > li.social-links > a:nth-child(4)',
                                    #apps 
                                    "ios":'css selector;#accordion-panel-connect > ul > li:nth-child(2) > a',
                                    "android":'css selector;#accordion-panel-connect > ul > li:nth-child(3) > a',
                                    #privacy
                                    "privacy":'css selector; #gdk__content > div > div.experiencefragment > div > div > div > div > div.footer-v2 > footer > div.grid.site-footer-v2__logos > div.site-footer-v2__badges > a',
                                    #footer's footer
                                    "legal":'css selector;gdk__content > div > div.experiencefragment > div > div > div > div > div.footer-v2 > footer > nav.grid.site-footer-v2__country > ul > li:nth-child(1) > a',
                                    "privacy":'css selector;gdk__content > div > div.experiencefragment > div > div > div > div > div.footer-v2 > footer > nav.grid.site-footer-v2__country > ul > li:nth-child(2) > a',
                                    "terms-of-use":'css selector;gdk__content > div > div.experiencefragment > div > div > div > div > div.footer-v2 > footer > nav.grid.site-footer-v2__country > ul > li:nth-child(3) > a',   
                                    "site-map":'css selector;gdk__content > div > div.experiencefragment > div > div > div > div > div.footer-v2 > footer > nav.grid.site-footer-v2__country > ul > li:nth-child(4) > a',   
                                },
                        "merch": 
                                {
                                    "buy-now":'css selector;#addToCartButton',
                                    "shopping-info":'css selector,#footer_panel__static-page-0-lnk',
                                    "custom-orders":'css selector,#footer_panel__static-page-1-lnk',
                                    "contact":'css selector,#footer_panel__static-page-2-lnk',
                                    "ps-privacy":'css selector,#footer_panel__static-page-3-lnk',
                                    "terms-of-use":'css selector,#footer_panel__static-page-4-lnk',
                                    "chat":'css selector;#reset-bootstrap > a.bda-btn.btn.chat-button'
                                }
                            
                        
                        
                    }
                 },
                 "https://urbandictionary.com/":
                    {
                        "specifics":"ablock=true;",
                        "endpoints":
                            { 
                                "browse":'css selector;button.cursor-pointer.flex.items-center.text-white.font-bold.px-3.gap-1[data-x-bind="toggleBrowse"][type="button"][aria-label="Show browse menu"]',
                                "store":'css selector;#ud-root > header > div.px-2.hidden.md\\:block.container.mx-auto.py-3.max-w-\\[970px\\] > div.flex.items-center.mb-2.flex-nowrap > div > div > ul > li:nth-child(2) > a',                                "store":'css selector;#ud-root > header > div.px-2.hidden.md\\:block.container.mx-auto.py-3.max-w-\\[970px\\] > div.flex.items-center.mb-2.flex-nowrap > div > div > ul > li:nth-child(2) > a',
                                "blog":'css selector;#ud-root > header > div.px-2.hidden.md\\:block.container.mx-auto.py-3.max-w-\\[970px\\] > div.flex.items-center.mb-2.flex-nowrap > div > div > ul > li:nth-child(2) > a',                                "store":'css selector;#ud-root > header > div.px-2.hidden.md\\:block.container.mx-auto.py-3.max-w-\\[970px\\] > div.flex.items-center.mb-2.flex-nowrap > div > div > ul > li:nth-child(3) > a',
                                "discord":'css selector;#ud-root > header > div.px-2.hidden.md\\:block.container.mx-auto.py-3.max-w-\\[970px\\] > div.flex.items-center.mb-2.flex-nowrap > div > div > ul > li:nth-child(2) > a',                                "store":'css selector;#ud-root > header > div.px-2.hidden.md\\:block.container.mx-auto.py-3.max-w-\\[970px\\] > div.flex.items-center.mb-2.flex-nowrap > div > div > ul > li:nth-child(4) > a',
                                "advertise":'css selector;#ud-root > header > div.px-2.hidden.md\\:block.container.mx-auto.py-3.max-w-\\[970px\\] > div.flex.items-center.mb-2.flex-nowrap > div > div > ul > li:nth-child(2) > a',                                "store":'css selector;#ud-root > header > div.px-2.hidden.md\\:block.container.mx-auto.py-3.max-w-\\[970px\\] > div.flex.items-center.mb-2.flex-nowrap > div > div > ul > li:nth-child(2) > a',
                                "define-word":'css selector;#ud-root > div > main > div > div.flex.flex-col.lg\:flex-row.mx-0.gap-4 > aside > div.mb-1.hidden.lg\:flex.lg\:flex-col > div > a',
                                "single":'rand_ind:css selector;a[href*="define"]'
                            },
                    "sub-endpoints":
                    {
                            #Navbar
                            "browse":
                            {
                                "letters":'rand_ind:css selector;#ud-root > header > div.px-2.hidden.md\:block.container.mx-auto.py-3.max-w-\[970px\] > div.flex.items-center.mb-2.flex-nowrap > div > div > ul > li.relative > div > div > ul  > li > a',                        
                            },
                            "store":
                            {
                                "more-merch":'rand_ind:css selector;#alpineInit > div:nth-child(3) > div > ul > li > a',
                                "buy-today":'css selector;#alpineInit > div:nth-child(3) > div > div > a',
                                "buy-ugly":'rand_ind:css selector;#alpineInit > div:nth-child(4) > div > ul > li > a',
                                "more-stuff":'css selector;#alpineInit > ul > li:nth-child(4) > a',
                                
                            },
                            "blog":
                            {
                                "post":'css selector;a[href*="post"]',
                                "next":'css selector;#content > main > div > div > a'
                            },
                            "advertise":
                            {
                                "contact-us":'css selector;body > div.p-5.bg-zircon > div > div > button',
                                "click meeeeeeee":'css selector;body > div.pt-2.px-5.bg-zircon > div > div > div:nth-child(1) > form > button',
                                "socials":'rand_ind:css selector;body > div.pt-2.px-5.bg-zircon > div > div > div:nth-child(1) > div.bg-white.rounded-full.inline-flex.px-2.mb-5 > div',
                                "chat":'css selector;#crisp-chatbox > div > a',
                            },
                            #Nested
                            "letters":
                            {
                                "words":'rand_ind:css selector;#ud-root > div > main > div > div.flex.flex-col.lg\:flex-row.mx-0.gap-4 > section > div.bg-white.dark\:bg-yankees.p-5.mb-5.rounded-md > ul > li > a'    
                            },
                            "word":
                            {
                                "merch":'css selector;#ud-root div main > div > section > div.definition > a'  
                            },
                            "merch":
                            {
                            "buy-now":'css selector;a.buy-button'
                            },
                    }
                },
                
                "https://www.fedex.com/en-ca/home.html/":
                    {
                        "specifics":"ablock=true;",
                        "endpoints":
                            { 
                                #Navbar
                                "shipping":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(1) > ul > li > a',
                                "tracking":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(2) > ul > li > a',
                                "servies":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(3) > ul > li > a',
                                "support":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(4) > ul > li > a',
                                #login
                                "sign-in":'css selector;#fxg-dropdown-signIn',
                                #Main page 
                                "online-shipping-tools":'id;#envelopepackages',
                                "freight":'id;#freight',
                                "additional-service-options":'id;#AdditionalOptions',
                                "by-industry":'id;#ByIndustry',
                                #shipping weight
                                "lite":'  :;css selector;#\#envelopepackages > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(1) > div > div > div.button_v1.aem-GridColumn.aem-GridColumn--default--12 > div > a',
                                "advanced":'  :;css selector;#\#envelopepackages > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(2) > div > div > div.button_v1.aem-GridColumn.aem-GridColumn--default--12 > div > a',
                                "learn-more":'  :;css selectorbody > div.fxg-main-content > div.root.responsivegrid > div > div > div > div.container.responsivegrid.fxg-wrapper.aem-GridColumn.aem-GridColumn--default--12 > div > div.button_v1 > div > a;',
                                #footer
                                "why-us":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div.fxg-col.fxg-col--mt20.fxg-col-mobile_position0.fxg-col--mb20.col-sm-4 > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(1) > div > div > div:nth-child(1) > div > a',
                                "about-us":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div.fxg-col.fxg-col--mt20.fxg-col-mobile_position0.fxg-col--mb20.col-sm-4 > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(1) > div > div > div:nth-child(2) > div > a',
                                "contact-us":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div.fxg-col.fxg-col--mt20.fxg-col-mobile_position0.fxg-col--mb20.col-sm-4 > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(1) > div > div > div:nth-child(3) > div > a',
                                "careeres":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div.fxg-col.fxg-col--mt20.fxg-col-mobile_position0.fxg-col--mb20.col-sm-4 > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(1) > div > div > div:nth-child(4) > div > a',
                                "sus":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div.fxg-col.fxg-col--mt20.fxg-col-mobile_position0.fxg-col--mb20.col-sm-4 > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(1) > div > div > div:nth-child(5) > div > a',
                                "privacy-code":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div.fxg-col.fxg-col--mt20.fxg-col-mobile_position0.fxg-col--mb20.col-sm-4 > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(2) > div > div > div:nth-child(1) > div > a',
                                "internet-privacy-policy":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div.fxg-col.fxg-col--mt20.fxg-col-mobile_position0.fxg-col--mb20.col-sm-4 > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(2) > div > div > div:nth-child(2) > div > a',
                                "services-guide":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div.fxg-col.fxg-col--mt20.fxg-col-mobile_position0.fxg-col--mb20.col-sm-4 > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(2) > div > div > div:nth-child(3) > div > a',
                                "faq":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div.fxg-col.fxg-col--mt20.fxg-col-mobile_position0.fxg-col--mb20.col-sm-4 > div > div > div.column_control_v1.aem-GridColumn.aem-GridColumn--default--12 > div > div:nth-child(2) > div > div > div:nth-child(4) > div > a',
                                "fedex-slave-trade-network":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div > div:nth-child(2) > div > a',
                                "fuel-surcharge":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div > div:nth-child(3) > div > a',
                                "global-newsroom":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div > div:nth-child(4) > div > a',
                                "regulatory-news":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div > div:nth-child(5) > div > a',
                                "developer":':;css selector;body > div.fxg-main-content > div.experiencefragment_1.HFexperiencefragment > div > div > div > div > footer > div.fxg-footer__primary > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div > div:nth-child(6) > div > a',
                            },
                    "sub-endpoints":
                    {
                            #Navbar
                            "shipping":
                            {
                                "ship-now":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(1) > ul > li > div > div > div:nth-child(1) > div > a',                        
                                "open-account":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(1) > ul > li > div > div > div:nth-child(2) > div > a',                        
                                "shipping-rates":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(1) > ul > li > div > div > div:nth-child(3) > div > a',                        
                                "schedule":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(1) > ul > li > div > div > div:nth-child(4) > div > a',                        
                                "order-supplies":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(1) > ul > li > div > div > div:nth-child(5) > div > a',                        
                                "return-package":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(1) > ul > li > div > div > div:nth-child(6) > div > a',                        
                                "pickup-location":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(1) > ul > li > div > div > div:nth-child(7) > div > a',                        
                                "all-shipping":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(1) > ul > li > div > div > div:nth-child(8) > div > a',                        
                            
                            },
                            "tracking":
                            {
                                "track":'css selector;#HeaderTrackingModule > button',
                                "personal-delivery-option":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(2) > ul > li > div > div > div:nth-child(2) > div > a',                        
                                "mobile-tracking-alerts":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(2) > ul > li > div > div > div:nth-child(3) > div > a',                        
                                "advance-tracking-alert":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(2) > ul > li > div > div > div:nth-child(4) > div > a',                        
                                "all-tracking":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(2) > ul > li > div > div > div:nth-child(5) > div > a',                        
                            },
                            "services":
                            {
                                "international":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(3) > ul > li > div > div > div:nth-child(1) > div > a',                        
                                "intra-canada":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(3) > ul > li > div > div > div:nth-child(2) > div > a',                        
                                "freight":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(3) > ul > li > div > div > div:nth-child(3) > div > a',                        
                                "by-industtry":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(3) > ul > li > div > div > div:nth-child(4) > div > a',                        
                                "shipping-service-finder":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(3) > ul > li > div > div > div:nth-child(5) > div > a',                        
                                "all-services":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(3) > ul > li > div > div > div:nth-child(6) > div > a',                        
                            },
                            "support":
                            {
                                "billing-center":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(4) > ul > li > div > div > div:nth-child(1) > div > a',                        
                                "FAQs":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(4) > ul > li > div > div > div:nth-child(2) > div > a',                        
                                "E-commerce-centre":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(4) > ul > li > div > div > div:nth-child(3) > div > a',                        
                                "small-business-centre":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(4) > ul > li > div > div > div:nth-child(4) > div > a',                        
                                "account-management":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(4) > ul > li > div > div > div:nth-child(5) > div > a',                        
                                "file-claim":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(4) > ul > li > div > div > div:nth-child(6) > div > a',                        
                                "tools":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(4) > ul > li > div > div > div:nth-child(7) > div > a',                        
                                "customer-support":'css selector;body > div.fxg-main-content > div.experiencefragment.HFexperiencefragment > div > div > div > div > header > nav > div > div.fxg-dropdown.fxg-global-nav > div > div:nth-child(4) > ul > li > div > div > div:nth-child(8) > div > a',                        
                            },
                            "sign-in":
                            {
                                "sign-up":':css selector;#global-login-wrapper > div > div > div > div:nth-child(1) > div > a',                        
                                "open-account":':css selector;#global-login-wrapper > div > div > div > div:nth-child(1) > div > a',                        
                                "create-user-idd":':css selector;#global-login-wrapper > div > div > div > div:nth-child(1) > div > a',                        
                                "profile":':css selector;#global-login-wrapper > div > div > div > div:nth-child(1) > div > a',                        
                                "admin-tools":':css selector;#global-login-wrapper > div > div > div > div:nth-child(1) > div > a',                        
                                "email-pref":':css selector;#global-login-wrapper > div > div > div > div:nth-child(1) > div > a',                        
                                "address-book":':css selector;#global-login-wrapper > div > div > div > div:nth-child(1) > div > a',                        
                                "view-pay-bill":':css selector;#global-login-wrapper > div > div > div > div:nth-child(1) > div > a',                        
                                "fedEX-reporting-online":':css selector;#global-login-wrapper > div > div > div > div:nth-child(1) > div > a',                        
                            },
                            #Shipping 
                            "open-account":
                            {
                                "start-saving":':css selector;body > div.fxg-main-content.fxg-content-wrapper > div:nth-child(2) > div > div.fxg-landing-hero__background-image.focal-x1y2--tablet.focal-x3y1--desktop > div > div > div:nth-child(4) > a.fxg-button.fxg-button--orange.fxg-mobile--hide.fxg-align-left',                        
                                "open-account-frl":':css selector;body > div.fxg-main-content.fxg-content-wrapper > div:nth-child(4) > div:nth-child(1) > div.link.section > div > a',
                                "support-pls":':css selectorbody > div.fxg-main-content.fxg-content-wrapper > div:nth-child(4) > div:nth-child(1) > div:nth-child(20) > div > div:nth-child(2) > div.link.section > div > a',                        
                            }, 
                            "schedule": { 
                                "various-endpoints":':refresh_sens:rand_ind: css selector;a[href*="fedex.com"]',                        
                            } 
                    }, 
                    #sportbible
                    "https://www.sportbible.com":
                    {
                        "specifics":"ablock=true;",
                        "endpoints":
                            { 
                                #Main page 
                                "today":'css selector;#root > div > div.css-yp9swi > div > div > div.heroArticle.css-jtiv7e > article > div.image-wrapper > a',
                                "Spotlight":'rand_ind:css selector;#root > div > div.css-yp9swi > section.css-1hb3ec6 > section > div > article > div.image-wrapper > a',
                                "list": 'rand_ind:css selector;#root > div > div.css-yp9swi > div > div > div.css-sx1r5m-HeroContentWrapper > div > section > article> div.contentWrapper.css-23fwot > a',
                                "football":'direct-link;football',
                                "boxing":'direct-link;boxing',
                                "mma":'direct-link,MMA'
                                #footer
                            },
                    "sub-endpoints":
                    {
                            #Navbar
                            "football":
                            {
                                "breaking-news":'rand_ind;#root > div > div.css-yp9swi > div > main > section.spotlight-section.css-iw1oi4 > div:nth-child > article > div.image-wrapper > a',
                                "reviews":'id;headlessui-disclosure-button-:r4:',
                                "science":'id;headlessui-disclosure-button-:r5:',
                                "entertainement":'id;headlessui-disclosure-button-:r6:',
                                "videos":'id;headlessui-disclosure-button-:r7:',
                                "podcasts":'id;headlessui-disclosure-button-:r8:',
                                "newsletter":'id;headlessui-disclosure-button-:r9:',
                                "store":'css selector;#headlessui-dialog-panel-\:r2\: > aside > nav > ul > li:nth-child(9) > a',
                                "log-in":'css selector;#headlessui-dialog-panel-\:r2\: > aside > div.mb-60 > div.relative.flex.items-baseline.font-polysans.text-33.text-franklin > a:nth-child(2)',
                                "sign-up":'css selector;#headlessui-dialog-panel-\:r2\: > aside > div.mb-60 > div.relative.flex.items-baseline.font-polysans.text-33.text-franklin > a:nth-child(4)',
                            },


                    }
}
}
}