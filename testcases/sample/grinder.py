# The Grinder 3.4
# HTTP script recorded by TCPProxy at Aug 25, 2010 11:50:23 PM

from net.grinder.script import Test as StandardTest

##
## offset test numbers TODO
##
SCENARIO_OFFSET = 10000
def Test(number, description):
  return StandardTest(SCENARIO_OFFSET + number, description)

from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

##
## import custom libraries
##
import sys
sys.path.append('../../common')
import rampup
import commonhelper

##
## get the testcase specific parameters
##
from java.lang import System
SEARCH_STRING1 = System.getenv().get('TESTCASE_PARAM1')
SEARCH_STRING2 = System.getenv().get('TESTCASE_PARAM2')

## get current date as a string in the default 'yyyy.MM.dd' format
currentDate = commonhelper.currentDate()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Language', 'en-us,en;q=0.5'),
    NVPair('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),
    NVPair('Accept-Encoding', ''),
    NVPair('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.19) Gecko/2010072023 Iceweasel/3.0.6 (Debian-3.0.6-3)'), ]

headers0= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers1= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://www.amazon.com/'), ]

headers2= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://www.amazon.com/'), ]

headers3= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://www.amazon.com/'), ]

headers4= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://www.amazon.com/'), ]

headers5= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://www.amazon.com/aan/2009-09-09/static/amazon/iframeproxy-2.html'), ]

headers6= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://www.amazon.com/aan/2009-09-09/static/amazon/iframeproxy-2.html'), ]

headers7= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'), ]

headers8= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'), ]

headers9= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://www.amazon.com/aan/2009-09-09/static/amazon/iframeproxy-2.html'), ]

headers10= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://d3l3lkinz3f56t.cloudfront.net/turn-proxy.html?'), ]

headers11= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://view.atdmt.com/MNY/iview/248834930/direct;wi.300;hi.250/01/8006087/8006087?click=http://ad.doubleclick.net/click%3Bh%3Dv8/3a01/3/0/%2a/e%3B227339043%3B0-0%3B0%3B18273354%3B4307-300/250%3B37741618/37759470/1%3Bu%3D8525e462ff3d422f9c95b0fda5dcf848%3B%7Esscs%3D%3f'), ]

headers12= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://www.amazon.com/dvds-used-hd-action-comedy-oscar/b/ref=sa_menu_mov1/191-5896311-1113436?ie=UTF8&node=130'), ]

headers13= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://www.amazon.com/dvds-used-hd-action-comedy-oscar/b/ref=sa_menu_mov1/191-5896311-1113436?ie=UTF8&node=130'), ]

headers14= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://z-ecx.images-amazon.com/images/G/01/zeitgeist/static/css/zeitgeist-chart.2._V186842733_.css'), ]

headers15= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://www.amazon.com/dvds-used-hd-action-comedy-oscar/b/ref=sa_menu_mov1/191-5896311-1113436?ie=UTF8&node=130'), ]

headers16= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://z-ecx.images-amazon.com/images/G/01/s9-campaigns/s9-widget._V184604009_.css'), ]

headers17= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://www.amazon.com/dvds-used-hd-action-comedy-oscar/b/ref=sa_menu_mov1/191-5896311-1113436?ie=UTF8&node=130'), ]

headers18= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://www.amazon.com/Advanced-Search-DVD/b/ref=sv_d_0?ie=UTF8&node=241586011'), ]

headers19= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://www.amazon.com/Advanced-Search-DVD/b/ref=sv_d_0?ie=UTF8&node=241586011'),
    NVPair('Cache-Control', 'no-cache'), ]

headers20= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://www.amazon.com/Advanced-Search-DVD/b/ref=sv_d_0?ie=UTF8&node=241586011'), ]

headers21= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://www.amazon.com/Advanced-Search-DVD/b/ref=sv_d_0?ie=UTF8&node=241586011'), ]

headers22= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://www.amazon.com/gp/search/ref=sr_adv_d/?search-alias=dvd&unfiltered=1&field-keywords=&field-title=&field-actor='+SEARCH_STRING1+'+'+SEARCH_STRING2+'&field-director=&field-price=0-1000&field-mpaa=unrated&node=&field-original=English&field-subtitled=&field-picture-format=&field-audio-type=&field-dvd-region=&field-dvd-supplements=&sort=relevancerank&Adv-Srch-DVD-Submit.x=36&Adv-Srch-DVD-Submit.y=13'), ]

headers23= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://www.amazon.com/gp/search/ref=sr_adv_d/?search-alias=dvd&unfiltered=1&field-keywords=&field-title=&field-actor='+SEARCH_STRING1+'+'+SEARCH_STRING2+'&field-director=&field-price=0-1000&field-mpaa=unrated&node=&field-original=English&field-subtitled=&field-picture-format=&field-audio-type=&field-dvd-region=&field-dvd-supplements=&sort=relevancerank&Adv-Srch-DVD-Submit.x=36&Adv-Srch-DVD-Submit.y=13'), ]

headers24= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://www.amazon.com/gp/search/ref=sr_adv_d/?search-alias=dvd&unfiltered=1&field-keywords=&field-title=&field-actor='+SEARCH_STRING1+'+'+SEARCH_STRING2+'&field-director=&field-price=0-1000&field-mpaa=unrated&node=&field-original=English&field-subtitled=&field-picture-format=&field-audio-type=&field-dvd-region=&field-dvd-supplements=&sort=relevancerank&Adv-Srch-DVD-Submit.x=36&Adv-Srch-DVD-Submit.y=13'), ]

headers25= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://www.amazon.com/gp/search/ref=sr_adv_d/?search-alias=dvd&unfiltered=1&field-keywords=&field-title=&field-actor='+SEARCH_STRING1+'+'+SEARCH_STRING2+'&field-director=&field-price=0-1000&field-mpaa=unrated&node=&field-original=English&field-subtitled=&field-picture-format=&field-audio-type=&field-dvd-region=&field-dvd-supplements=&sort=relevancerank&Adv-Srch-DVD-Submit.x=36&Adv-Srch-DVD-Submit.y=13'), ]

headers26= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://www.amazon.com/aan/2009-09-09/static/amazon.us/iframeproxy.html'), ]

headers27= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://www.amazon.com/aan/2009-09-09/static/amazon.us/iframeproxy.html'), ]

headers28= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://view.atdmt.com/MNY/iview/248834933/direct;wi.160;hi.600/01/4640208?click=http://ad.doubleclick.net/click%3Bh%3Dv8/3a01/3/0/%2a/z%3B227339040%3B0-0%3B0%3B18273384%3B2321-160/600%3B37741837/37759689/1%3Bu%3D7fddd1bf4bcc4b5abda58d555e525115%3B%7Esscs%3D%3f'), ]

headers29= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://view.atdmt.com/MNY/iview/248834933/direct;wi.160;hi.600/01/4640208?click=http://ad.doubleclick.net/click%3Bh%3Dv8/3a01/3/0/%2a/z%3B227339040%3B0-0%3B0%3B18273384%3B2321-160/600%3B37741837/37759689/1%3Bu%3D7fddd1bf4bcc4b5abda58d555e525115%3B%7Esscs%3D%3f'), ]

##
## this is where we can use TARGET_URL parameter: System.getenv().get('TARGET_URL')
##
url0 = 'http://www.amazon.com:80'
url1 = 'http://z-ecx.images-amazon.com:80'
url2 = 'http://g-ecx.images-amazon.com:80'
url3 = 'http://ecx.images-amazon.com:80'
url4 = 'http://ad.doubleclick.net:80'
url5 = 'http://s0.2mdn.net:80'
url6 = 'http://d3l3lkinz3f56t.cloudfront.net:80'
url7 = 'http://view.atdmt.com:80'
url8 = 'http://r.turn.com:80'
url9 = 'http://spe.atdmt.com:80'
url10 = 'http://g-ec2.images-amazon.com:80'
url11 = 'http://ec1.images-amazon.com:80'
url12 = 'http://g-ec1.images-amazon.com:80'
url13 = 'http://client-log.amazon.com:80'
url14 = 'http://rmd.atdmt.com:80'

# Create an HTTPRequest for each request, then replace the
# reference to the HTTPRequest with an instrumented version.
# You can access the unadorned instance using request101.__target__.
# get main page of amazon.com
request101 = HTTPRequest(url=url0, headers=headers0)
request101 = Test(101, 'GET /').wrap(request101)

request201 = HTTPRequest(url=url1, headers=headers1)
request201 = Test(201, 'GET navbarCSSUSSA185-navbarUSSA185-29254.css._V188482287_.css').wrap(request201)

request202 = HTTPRequest(url=url1, headers=headers1)
request202 = Test(202, 'GET websiteGridCSS-websiteGridCSS-26613._V186355211_.css').wrap(request202)

request203 = HTTPRequest(url=url1, headers=headers1)
request203 = Test(203, 'GET core-3726680825.css._V186741523_.css').wrap(request203)

request204 = HTTPRequest(url=url1, headers=headers1)
request204 = Test(204, 'GET amazonShoveler-amazonShovelerCss-12802._V235369351_.css').wrap(request204)

request205 = HTTPRequest(url=url1, headers=headers2)
request205 = Test(205, 'GET core-7224254877.js._V186741521_.js').wrap(request205)

request301 = HTTPRequest(url=url2, headers=headers3)
request301 = Test(301, 'GET shasta-reviews-C1-COM-GW-INTL-01._V184950673_.jpg').wrap(request301)

request302 = HTTPRequest(url=url2, headers=headers3)
request302 = Test(302, 'GET transparent-pixel._V192234675_.gif').wrap(request302)

request303 = HTTPRequest(url=url2, headers=headers3)
request303 = Test(303, 'GET navPackedSprites-US-16._V212310439_.png').wrap(request303)

request304 = HTTPRequest(url=url2, headers=headers3)
request304 = Test(304, 'GET donate-pakistan_300x120._V186640421_.gif').wrap(request304)

request305 = HTTPRequest(url=url2, headers=headers3)
request305 = Test(305, 'GET visit_amazon_de_tcg._V229026937_.gif').wrap(request305)

request306 = HTTPRequest(url=url2, headers=headers3)
request306 = Test(306, 'GET sprites-h._V192570380_.gif').wrap(request306)

request307 = HTTPRequest(url=url2, headers=headers3)
request307 = Test(307, 'GET sprites-v._V192570383_.gif').wrap(request307)

request401 = HTTPRequest(url=url1, headers=headers2)
request401 = Test(401, 'GET navbarJS-jQuery-navbarJQ-48403._V212501460_.js').wrap(request401)

request402 = HTTPRequest(url=url1, headers=headers2)
request402 = Test(402, 'GET search-js-autocomplete-autocomplete-15273._V188633242_.js').wrap(request402)

request403 = HTTPRequest(url=url1, headers=headers1)
request403 = Test(403, 'GET s9-widget-seeded._V184604011_.css').wrap(request403)

request404 = HTTPRequest(url=url1, headers=headers2)
request404 = Test(404, 'GET s9-multipack-layout-seeded._V210353195_.js').wrap(request404)

request501 = HTTPRequest(url=url2, headers=headers3)
request501 = Test(501, 'GET B001A62M04._V192212155_.jpg').wrap(request501)

request502 = HTTPRequest(url=url2, headers=headers3)
request502 = Test(502, 'GET B0019FP47E._V192598089_.jpg').wrap(request502)

request503 = HTTPRequest(url=url2, headers=headers3)
request503 = Test(503, 'GET B000EQR6H0._V192598437_.jpg').wrap(request503)

request504 = HTTPRequest(url=url2, headers=headers3)
request504 = Test(504, 'GET asus-2._V189604747_.gif').wrap(request504)

request505 = HTTPRequest(url=url2, headers=headers3)
request505 = Test(505, 'GET dell._V189604740_.gif').wrap(request505)

request601 = HTTPRequest(url=url1, headers=headers2)
request601 = Test(601, 'GET clog-platform._V213973670_.js').wrap(request601)

request602 = HTTPRequest(url=url1, headers=headers2)
request602 = Test(602, 'GET d16g-0.6.14.nl.yui._V186549516_.js').wrap(request602)

request701 = HTTPRequest(url=url2, headers=headers3)
request701 = Test(701, 'GET asus._V189604750_.gif').wrap(request701)

request702 = HTTPRequest(url=url2, headers=headers3)
request702 = Test(702, 'GET navAmazonLogoFooter._V192570482_.gif').wrap(request702)

request703 = HTTPRequest(url=url2, headers=headers3)
request703 = Test(703, 'GET visa_gateway_300_4._V192208236_.gif').wrap(request703)

request704 = HTTPRequest(url=url2, headers=headers3)
request704 = Test(704, 'GET advertisement-sm-head._V192575712_.gif').wrap(request704)

request705 = HTTPRequest(url=url2, headers=headers3)
request705 = Test(705, 'GET bluebox-corners._V192187813_.gif').wrap(request705)

request801 = HTTPRequest(url=url3, headers=headers3)
request801 = Test(801, 'GET 51y8Ow-npiL._SL135_.jpg').wrap(request801)

request802 = HTTPRequest(url=url3, headers=headers3)
request802 = Test(802, 'GET 41M+S6UQX3L._SL135_.jpg').wrap(request802)

request803 = HTTPRequest(url=url3, headers=headers3)
request803 = Test(803, 'GET 51993R08WLL._SL135_.jpg').wrap(request803)

request804 = HTTPRequest(url=url3, headers=headers3)
request804 = Test(804, 'GET 51oEJGNH-xL._SL75_.jpg').wrap(request804)

request805 = HTTPRequest(url=url3, headers=headers3)
request805 = Test(805, 'GET 417XQ0XwQuL._SL135_.jpg').wrap(request805)

request901 = HTTPRequest(url=url0, headers=headers4)
request901 = Test(901, 'GET iframeproxy-2.html').wrap(request901)

request1001 = HTTPRequest(url=url2, headers=headers3)
request1001 = Test(1001, 'GET bluebox-sides._V192187807_.gif').wrap(request1001)

request1002 = HTTPRequest(url=url2, headers=headers3)
request1002 = Test(1002, 'GET loadIndicator-large._V192195480_.gif').wrap(request1002)

request1101 = HTTPRequest(url=url4, headers=headers5)
request1101 = Test(1101, 'GET amzn.us.gw.atf').wrap(request1101)

request1201 = HTTPRequest(url=url5, headers=headers6)
request1201 = Test(1201, 'GET advertisement-sm-head_US.gif').wrap(request1201)

request1202 = HTTPRequest(url=url5, headers=headers6)
request1202 = Test(1202, 'GET TTlifetimemaps300x250.jpg').wrap(request1202)

request1301 = HTTPRequest(url=url1, headers=headers7)
request1301 = Test(1301, 'GET search-css-search-2279._V186518594_.css').wrap(request1301)

request1302 = HTTPRequest(url=url1, headers=headers7)
request1302 = Test(1302, 'GET combined-3446052479._V214198738_.css').wrap(request1302)

request1401 = HTTPRequest(url=url2, headers=headers3)
request1401 = Test(1401, 'GET sprite-communities._V201759850_.png').wrap(request1401)

request1501 = HTTPRequest(url=url1, headers=headers7)
request1501 = Test(1501, 'GET combined-1240099087._V210574564_.css').wrap(request1501)

request1502 = HTTPRequest(url=url1, headers=headers2)
request1502 = Test(1502, 'GET twister-dpf.c20ec6bc970396fc67cebc53deb1beaf._V1_.js').wrap(request1502)

request1503 = HTTPRequest(url=url1, headers=headers2)
request1503 = Test(1503, 'GET tmmJS-combined-core-29871._V189245115_.js').wrap(request1503)

request1601 = HTTPRequest(url=url4, headers=headers5)
request1601 = Test(1601, 'GET amzn.us.gw.btf').wrap(request1601)

request1701 = HTTPRequest(url=url0, headers=headers8)
request1701 = Test(1701, 'GET favicon.ico').wrap(request1701)

request1801 = HTTPRequest(url=url6, headers=headers4)
request1801 = Test(1801, 'GET turn-proxy.html').wrap(request1801)

request1901 = HTTPRequest(url=url7, headers=headers9)
request1901 = Test(1901, 'GET 8006087').wrap(request1901)

request2001 = HTTPRequest(url=url8, headers=headers10)
request2001 = Test(2001, 'GET bd').wrap(request2001)

request2101 = HTTPRequest(url=url9, headers=headers11)
request2101 = Test(2101, 'GET 20100801_DB_IP_FLIP_23_300_250.gif').wrap(request2101)

# movies menu
request2201 = HTTPRequest(url=url0, headers=headers4)
request2201 = Test(2201, 'GET 191-5896311-1113436').wrap(request2201)

request2301 = HTTPRequest(url=url1, headers=headers12)
request2301 = Test(2301, 'GET s9-widget._V184604009_.css').wrap(request2301)

request2401 = HTTPRequest(url=url2, headers=headers13)
request2401 = Test(2401, 'GET dp-on-demand-logo._V233830985_.gif').wrap(request2401)

request2402 = HTTPRequest(url=url2, headers=headers13)
request2402 = Test(2402, 'GET theoffice_season6_ss._V188135687_.gif').wrap(request2402)

request2403 = HTTPRequest(url=url2, headers=headers13)
request2403 = Test(2403, 'GET lozenge_armchair._V230191894_.jpg').wrap(request2403)

request2404 = HTTPRequest(url=url2, headers=headers13)
request2404 = Test(2404, 'GET armchair-commentary_blog_90x90._V192258809_.gif').wrap(request2404)

request2501 = HTTPRequest(url=url3, headers=headers13)
request2501 = Test(2501, 'GET B002JVWR7M.01._SL110_PE37_OU01_SCLZZZZZZZ_V185856073_.jpg').wrap(request2501)

request2502 = HTTPRequest(url=url3, headers=headers13)
request2502 = Test(2502, 'GET B002Q4VBPQ.01._SL75_PE52_OU01_SCLZZZZZZZ_V217583187_.jpg').wrap(request2502)

request2503 = HTTPRequest(url=url3, headers=headers13)
request2503 = Test(2503, 'GET B000W7F5SS.01._SL75_PE60_OU01_SCLZZZZZZZ_V217281925_.jpg').wrap(request2503)

request2504 = HTTPRequest(url=url3, headers=headers13)
request2504 = Test(2504, 'GET 51Da+R1iGSL._SL75_.jpg').wrap(request2504)

request2601 = HTTPRequest(url=url1, headers=headers12)
request2601 = Test(2601, 'GET zeitgeist-chart.2._V186842733_.css').wrap(request2601)

request2701 = HTTPRequest(url=url3, headers=headers13)
request2701 = Test(2701, 'GET 51Bq5wopzvL._SL75_.jpg').wrap(request2701)

request2702 = HTTPRequest(url=url3, headers=headers13)
request2702 = Test(2702, 'GET 51f2XzDeL3L._SL75_.jpg').wrap(request2702)

request2703 = HTTPRequest(url=url3, headers=headers13)
request2703 = Test(2703, 'GET 51YBEEb+LvL._SL75_.jpg').wrap(request2703)

request2801 = HTTPRequest(url=url2, headers=headers13)
request2801 = Test(2801, 'GET bluray._V192598306_.gif').wrap(request2801)

request2901 = HTTPRequest(url=url3, headers=headers13)
request2901 = Test(2901, 'GET 51zW3BrfegL._SL75_.jpg').wrap(request2901)

request3001 = HTTPRequest(url=url2, headers=headers13)
request3001 = Test(3001, 'GET dvd._V192598333_.gif').wrap(request3001)

request3101 = HTTPRequest(url=url3, headers=headers13)
request3101 = Test(3101, 'GET 61hVWKe2AML._SL75_.jpg').wrap(request3101)

request3102 = HTTPRequest(url=url3, headers=headers13)
request3102 = Test(3102, 'GET 517viGC516L._SL75_.jpg').wrap(request3102)

request3103 = HTTPRequest(url=url3, headers=headers13)
request3103 = Test(3103, 'GET 51QlqI3yaOL._SL75_.jpg').wrap(request3103)

request3104 = HTTPRequest(url=url3, headers=headers13)
request3104 = Test(3104, 'GET 61FCRvfKYgL._SL75_.jpg').wrap(request3104)

request3105 = HTTPRequest(url=url3, headers=headers13)
request3105 = Test(3105, 'GET 51OfO6I-qsL._SL75_.jpg').wrap(request3105)

request3106 = HTTPRequest(url=url3, headers=headers13)
request3106 = Test(3106, 'GET 51G35CahIML._SL75_.jpg').wrap(request3106)

request3107 = HTTPRequest(url=url3, headers=headers13)
request3107 = Test(3107, 'GET 51EKgLUIENL._SL69_PE24_OU01_.jpg').wrap(request3107)

request3108 = HTTPRequest(url=url3, headers=headers13)
request3108 = Test(3108, 'GET 51XVloeMTaL._SL69_PE09_OU01_.jpg').wrap(request3108)

request3109 = HTTPRequest(url=url3, headers=headers13)
request3109 = Test(3109, 'GET 51XKNUudeJL._SL69_PE20_OU01_.jpg').wrap(request3109)

request3201 = HTTPRequest(url=url2, headers=headers14)
request3201 = Test(3201, 'GET up_down_arrows._V245851576_.png').wrap(request3201)

request3301 = HTTPRequest(url=url1, headers=headers15)
request3301 = Test(3301, 'GET s9-multipack-min._V185037641_.js').wrap(request3301)

request3401 = HTTPRequest(url=url3, headers=headers13)
request3401 = Test(3401, 'GET B003XKPPOU.01._SL75_PE37_OU01_SCLZZZZZZZ_V185828238_.jpg').wrap(request3401)

request3402 = HTTPRequest(url=url3, headers=headers13)
request3402 = Test(3402, 'GET B002N5N5M0.01._SL110_PE40_OU01_SCLZZZZZZZ_V191724279_.jpg').wrap(request3402)

request3501 = HTTPRequest(url=url2, headers=headers13)
request3501 = Test(3501, 'GET orange-arrow._V192240581_.gif').wrap(request3501)

request3601 = HTTPRequest(url=url3, headers=headers13)
request3601 = Test(3601, 'GET B0036EH3XE.01._SL110_PE37_OU01_SCLZZZZZZZ_V185747176_.jpg').wrap(request3601)

request3602 = HTTPRequest(url=url3, headers=headers13)
request3602 = Test(3602, 'GET 51ZVhFmvIbL._SX160_SY120_.jpg').wrap(request3602)

request3603 = HTTPRequest(url=url3, headers=headers13)
request3603 = Test(3603, 'GET 51QlqI3yaOL._SS135_PI43-percent,BottomRight,0,0_OU01_SS135_.jpg').wrap(request3603)

request3604 = HTTPRequest(url=url3, headers=headers13)
request3604 = Test(3604, 'GET 51fCBFMTGnL._SS135_PI63-percent,BottomRight,0,0_OU01_SS135_.jpg').wrap(request3604)

request3605 = HTTPRequest(url=url3, headers=headers13)
request3605 = Test(3605, 'GET 51-3gyzp1GL._SS135_.jpg').wrap(request3605)

request3606 = HTTPRequest(url=url3, headers=headers13)
request3606 = Test(3606, 'GET B002N5N5QQ.01._SL110_PE47_OU01_SCLZZZZZZZ_V212176037_.jpg').wrap(request3606)

request3701 = HTTPRequest(url=url1, headers=headers15)
request3701 = Test(3701, 'GET s9-shoveler-min._V185037643_.js').wrap(request3701)

request3801 = HTTPRequest(url=url3, headers=headers13)
request3801 = Test(3801, 'GET 51zn8ZTH4AL._SL120_.jpg').wrap(request3801)

request3802 = HTTPRequest(url=url3, headers=headers13)
request3802 = Test(3802, 'GET 51MGWPWYU4L._SL120_.jpg').wrap(request3802)

request3803 = HTTPRequest(url=url3, headers=headers13)
request3803 = Test(3803, 'GET 51j6t6f02fL._SL120_.jpg').wrap(request3803)

request3901 = HTTPRequest(url=url2, headers=headers13)
request3901 = Test(3901, 'GET todays-deals_120._V224628603_.png').wrap(request3901)

request3902 = HTTPRequest(url=url2, headers=headers13)
request3902 = Test(3902, 'GET best-2010-so-far_120._V192571830_.gif').wrap(request3902)

request3903 = HTTPRequest(url=url2, headers=headers13)
request3903 = Test(3903, 'GET dvd_emmys08_120._V192565529_.gif').wrap(request3903)

request3904 = HTTPRequest(url=url2, headers=headers13)
request3904 = Test(3904, 'GET new-releases_cat._V192572827_.gif').wrap(request3904)

request3905 = HTTPRequest(url=url2, headers=headers13)
request3905 = Test(3905, 'GET tvshows_cat._V192572822_.gif').wrap(request3905)

request3906 = HTTPRequest(url=url2, headers=headers13)
request3906 = Test(3906, 'GET bluray_cat._V192572827_.gif').wrap(request3906)

request4001 = HTTPRequest(url=url3, headers=headers13)
request4001 = Test(4001, 'GET B002VPE1AW.01._SL110_PE33_OU01_SCLZZZZZZZ_V215102563_.jpg').wrap(request4001)

request4002 = HTTPRequest(url=url3, headers=headers13)
request4002 = Test(4002, 'GET B003LL3N1I.01._SL110_PE48_OU01_SCLZZZZZZZ_V211526623_.jpg').wrap(request4002)

request4003 = HTTPRequest(url=url3, headers=headers13)
request4003 = Test(4003, 'GET 51bWiRuJb6L._SL110_.jpg').wrap(request4003)

request4004 = HTTPRequest(url=url3, headers=headers13)
request4004 = Test(4004, 'GET B003FSTN52.01._SL110_PE31_OU01_SCLZZZZZZZ_V214776188_.jpg').wrap(request4004)

request4005 = HTTPRequest(url=url3, headers=headers13)
request4005 = Test(4005, 'GET 51STDj5eM3L._SL110_.jpg').wrap(request4005)

request4006 = HTTPRequest(url=url3, headers=headers13)
request4006 = Test(4006, 'GET B001IBIHQ4.01._SL110_PE35_OU01_SCLZZZZZZZ_V187414510_.jpg').wrap(request4006)

request4007 = HTTPRequest(url=url3, headers=headers13)
request4007 = Test(4007, 'GET B0021L8V1G.01._SL110_PE34_OU01_SCLZZZZZZZ_V184946071_.jpg').wrap(request4007)

request4008 = HTTPRequest(url=url3, headers=headers13)
request4008 = Test(4008, 'GET B00275EHJG.01._SL110_PE43_OU01_SCLZZZZZZZ_V186081659_.jpg').wrap(request4008)

request4009 = HTTPRequest(url=url3, headers=headers13)
request4009 = Test(4009, 'GET 51dmG8W8DOL._SL120_.jpg').wrap(request4009)

request4010 = HTTPRequest(url=url3, headers=headers13)
request4010 = Test(4010, 'GET 51zW3BrfegL._SL120_.jpg').wrap(request4010)

request4011 = HTTPRequest(url=url3, headers=headers13)
request4011 = Test(4011, 'GET 51VqqUJ11tL._SL120_.jpg').wrap(request4011)

request4012 = HTTPRequest(url=url3, headers=headers13)
request4012 = Test(4012, 'GET 51K9gRUIZ2L._SL120_.jpg').wrap(request4012)

request4013 = HTTPRequest(url=url3, headers=headers13)
request4013 = Test(4013, 'GET 51s9td+zJOL._SL120_.jpg').wrap(request4013)

request4014 = HTTPRequest(url=url3, headers=headers13)
request4014 = Test(4014, 'GET 51t3jSau4eL._SL120_.jpg').wrap(request4014)

request4101 = HTTPRequest(url=url1, headers=headers16)
request4101 = Test(4101, 'GET loading-indicator._V31970667_.gif').wrap(request4101)

request4102 = HTTPRequest(url=url1, headers=headers16)
request4102 = Test(4102, 'GET left-arrow-semi-rd._V17361814_.gif').wrap(request4102)

request4103 = HTTPRequest(url=url1, headers=headers16)
request4103 = Test(4103, 'GET right-arrow-semi-rd._V17361809_.gif').wrap(request4103)

# advanced search
request4201 = HTTPRequest(url=url0, headers=headers17)
request4201 = Test(4201, 'GET ref=sv_d_0').wrap(request4201)

request4301 = HTTPRequest(url=url10, headers=headers18)
request4301 = Test(4301, 'GET search-md-sec._V33237624_.gif').wrap(request4301)

request4401 = HTTPRequest(url=url11, headers=headers18)
request4401 = Test(4401, 'GET grey-dot-vert-border._V44209678_.gif').wrap(request4401)

request4501 = HTTPRequest(url=url0, headers=headers19)
request4501 = Test(4501, 'POST full-rhf-rec-handler.html').wrap(request4501)

request4601 = HTTPRequest(url=url2, headers=headers18)
request4601 = Test(4601, 'GET stars-4-0._V192251205_.gif').wrap(request4601)

request4602 = HTTPRequest(url=url2, headers=headers18)
request4602 = Test(4602, 'GET stars-3-0._V192238413_.gif').wrap(request4602)

request4603 = HTTPRequest(url=url2, headers=headers18)
request4603 = Test(4603, 'GET stars-4-5._V192238104_.gif').wrap(request4603)

request4701 = HTTPRequest(url=url3, headers=headers18)
request4701 = Test(4701, 'GET 41f6tpRVssL._SL500_SS120_.jpg').wrap(request4701)

request4702 = HTTPRequest(url=url3, headers=headers18)
request4702 = Test(4702, 'GET 41ThJ66fhbL._SL500_PIsitb-sticker-arrow-big,TopRight,35,-73_OU01_SS120_.jpg').wrap(request4702)

request4703 = HTTPRequest(url=url3, headers=headers18)
request4703 = Test(4703, 'GET 41PuUigDokL._SL500_SS120_.jpg').wrap(request4703)

request4704 = HTTPRequest(url=url3, headers=headers18)
request4704 = Test(4704, 'GET 51QWwGRXouL._SL500_SS120_.jpg').wrap(request4704)

request4705 = HTTPRequest(url=url3, headers=headers18)
request4705 = Test(4705, 'GET 511ZEohSj6L._SL500_SS120_.jpg').wrap(request4705)

request4801 = HTTPRequest(url=url1, headers=headers20)
request4801 = Test(4801, 'GET amazonShoveler-amazonShoveler-44847._V190802495_.js').wrap(request4801)

request4901 = HTTPRequest(url=url2, headers=headers18)
request4901 = Test(4901, 'GET left-right-arrow-semi-rd._V236573507_.gif').wrap(request4901)

request5001 = HTTPRequest(url=url12, headers=headers18)
request5001 = Test(5001, 'GET amzn-logo-118w.gif').wrap(request5001)

request5101 = HTTPRequest(url=url13, headers=headers18)
request5101 = Test(5101, 'GET /').wrap(request5101)

# filter
request5201 = HTTPRequest(url=url0, headers=headers21)
request5201 = Test(5201, 'GET /').wrap(request5201)

request5301 = HTTPRequest(url=url3, headers=headers22)
request5301 = Test(5301, 'GET 518zJy2BPEL._AA115_.jpg').wrap(request5301)

request5401 = HTTPRequest(url=url2, headers=headers22)
request5401 = Test(5401, 'GET stars-3-5.gif').wrap(request5401)

request5402 = HTTPRequest(url=url2, headers=headers22)
request5402 = Test(5402, 'GET stars-4-5.gif').wrap(request5402)

request5501 = HTTPRequest(url=url3, headers=headers22)
request5501 = Test(5501, 'GET 51bvZUJpI3L._AA115_.jpg').wrap(request5501)

request5502 = HTTPRequest(url=url3, headers=headers22)
request5502 = Test(5502, 'GET 51qCKxkmRnL._AA115_.jpg').wrap(request5502)

request5601 = HTTPRequest(url=url2, headers=headers22)
request5601 = Test(5601, 'GET stars-5-0.gif').wrap(request5601)

request5602 = HTTPRequest(url=url2, headers=headers22)
request5602 = Test(5602, 'GET searchSprite._V186644917_.gif').wrap(request5602)

request5701 = HTTPRequest(url=url1, headers=headers23)
request5701 = Test(5701, 'GET search-js-general-search_general-19776._V185838463_.js').wrap(request5701)

request5801 = HTTPRequest(url=url3, headers=headers22)
request5801 = Test(5801, 'GET 51cvHR7EODL._AA115_.jpg').wrap(request5801)

request5901 = HTTPRequest(url=url2, headers=headers22)
request5901 = Test(5901, 'GET stars-4-0.gif').wrap(request5901)

request6001 = HTTPRequest(url=url3, headers=headers22)
request6001 = Test(6001, 'GET 51yo6aw0BWL._AA115_.jpg').wrap(request6001)

request6101 = HTTPRequest(url=url2, headers=headers22)
request6101 = Test(6101, 'GET stars-3-0.gif').wrap(request6101)

request6102 = HTTPRequest(url=url2, headers=headers22)
request6102 = Test(6102, 'GET no-img-sm._AA75_.gif').wrap(request6102)

request6201 = HTTPRequest(url=url3, headers=headers22)
request6201 = Test(6201, 'GET 51KYRQA8WHL._AA115_.jpg').wrap(request6201)

request6202 = HTTPRequest(url=url3, headers=headers22)
request6202 = Test(6202, 'GET 51Mt7RRXYDL._AA115_.jpg').wrap(request6202)

request6203 = HTTPRequest(url=url3, headers=headers22)
request6203 = Test(6203, 'GET 51U7UnCsjXL._AA115_.jpg').wrap(request6203)

request6204 = HTTPRequest(url=url3, headers=headers22)
request6204 = Test(6204, 'GET 51SUsI0fXsL._AA115_.jpg').wrap(request6204)

request6205 = HTTPRequest(url=url3, headers=headers22)
request6205 = Test(6205, 'GET 518jPzMUrIL._AA115_.jpg').wrap(request6205)

request6206 = HTTPRequest(url=url3, headers=headers22)
request6206 = Test(6206, 'GET 21RM3SW3AGL._AA115_.jpg').wrap(request6206)

request6301 = HTTPRequest(url=url2, headers=headers22)
request6301 = Test(6301, 'GET powered-by-a9.gif').wrap(request6301)

request6302 = HTTPRequest(url=url2, headers=headers22)
request6302 = Test(6302, 'GET checkbox_unselected_enabled.jpg').wrap(request6302)

request6303 = HTTPRequest(url=url2, headers=headers22)
request6303 = Test(6303, 'GET prime-check-badge-14.gif').wrap(request6303)

request6401 = HTTPRequest(url=url1, headers=headers24)
request6401 = Test(6401, 'GET style-3._V248984170_.css').wrap(request6401)

request6501 = HTTPRequest(url=url2, headers=headers22)
request6501 = Test(6501, 'GET 4star.gif').wrap(request6501)

request6601 = HTTPRequest(url=url3, headers=headers22)
request6601 = Test(6601, 'GET 518zJy2BPEL._AA75_.jpg').wrap(request6601)

request6602 = HTTPRequest(url=url3, headers=headers22)
request6602 = Test(6602, 'GET 51cvHR7EODL._AA75_.jpg').wrap(request6602)

request6701 = HTTPRequest(url=url2, headers=headers22)
request6701 = Test(6701, 'GET 3star.gif').wrap(request6701)

request6702 = HTTPRequest(url=url2, headers=headers22)
request6702 = Test(6702, 'GET 2star.gif').wrap(request6702)

request6703 = HTTPRequest(url=url2, headers=headers22)
request6703 = Test(6703, 'GET 1star.gif').wrap(request6703)

request6704 = HTTPRequest(url=url2, headers=headers22)
request6704 = Test(6704, 'GET checkbox_selected_enabled.jpg').wrap(request6704)

request6705 = HTTPRequest(url=url2, headers=headers22)
request6705 = Test(6705, 'GET go._V192195849_.gif').wrap(request6705)

request6706 = HTTPRequest(url=url2, headers=headers22)
request6706 = Test(6706, 'GET btn-yes._V192545584_.gif').wrap(request6706)

request6707 = HTTPRequest(url=url2, headers=headers22)
request6707 = Test(6707, 'GET btn-no._V192545588_.gif').wrap(request6707)

request6708 = HTTPRequest(url=url2, headers=headers22)
request6708 = Test(6708, 'GET box-line-tl._V192545536_.gif').wrap(request6708)

request6709 = HTTPRequest(url=url2, headers=headers22)
request6709 = Test(6709, 'GET box-blue-tm._V192184663_.gif').wrap(request6709)

request6710 = HTTPRequest(url=url2, headers=headers22)
request6710 = Test(6710, 'GET btn-yes-inactive._V192545585_.gif').wrap(request6710)

request6711 = HTTPRequest(url=url2, headers=headers22)
request6711 = Test(6711, 'GET btn-no-inactive-ns._V192545588_.gif').wrap(request6711)

request6712 = HTTPRequest(url=url2, headers=headers22)
request6712 = Test(6712, 'GET btn-yes-inactive-ns._V192545585_.gif').wrap(request6712)

request6713 = HTTPRequest(url=url2, headers=headers22)
request6713 = Test(6713, 'GET btn-no-inactive._V192545591_.gif').wrap(request6713)

request6714 = HTTPRequest(url=url2, headers=headers22)
request6714 = Test(6714, 'GET btn-submit-sm._V192545553_.gif').wrap(request6714)

request6715 = HTTPRequest(url=url2, headers=headers22)
request6715 = Test(6715, 'GET box-line-tr._V192545536_.gif').wrap(request6715)

request6716 = HTTPRequest(url=url2, headers=headers22)
request6716 = Test(6716, 'GET box-line-bl._V192545543_.gif').wrap(request6716)

request6717 = HTTPRequest(url=url2, headers=headers22)
request6717 = Test(6717, 'GET box-blue-bm._V192184657_.gif').wrap(request6717)

request6718 = HTTPRequest(url=url2, headers=headers22)
request6718 = Test(6718, 'GET box-line-br._V192545543_.gif').wrap(request6718)

request6719 = HTTPRequest(url=url2, headers=headers22)
request6719 = Test(6719, 'GET carrot._V192251235_.gif').wrap(request6719)

request6720 = HTTPRequest(url=url2, headers=headers22)
request6720 = Test(6720, 'GET loadIndicator-label._V192195535_.gif').wrap(request6720)

request6721 = HTTPRequest(url=url2, headers=headers22)
request6721 = Test(6721, 'GET box-gray-tl._V192184760_.gif').wrap(request6721)

request6722 = HTTPRequest(url=url2, headers=headers22)
request6722 = Test(6722, 'GET box-gray-tr._V192184429_.gif').wrap(request6722)

request6723 = HTTPRequest(url=url2, headers=headers22)
request6723 = Test(6723, 'GET box-gray-tm._V192184721_.gif').wrap(request6723)

request6724 = HTTPRequest(url=url2, headers=headers22)
request6724 = Test(6724, 'GET box-gray-bl._V192184824_.gif').wrap(request6724)

request6725 = HTTPRequest(url=url2, headers=headers22)
request6725 = Test(6725, 'GET box-gray-bm._V192184603_.gif').wrap(request6725)

request6726 = HTTPRequest(url=url2, headers=headers22)
request6726 = Test(6726, 'GET box-gray-br._V192545463_.gif').wrap(request6726)

request6801 = HTTPRequest(url=url1, headers=headers23)
request6801 = Test(6801, 'GET search-js-ajax2-combined-core-60868._V189170300_.js').wrap(request6801)

request6802 = HTTPRequest(url=url1, headers=headers23)
request6802 = Test(6802, 'GET script-13-min._V224617671_.js').wrap(request6802)

request6901 = HTTPRequest(url=url2, headers=headers22)
request6901 = Test(6901, 'GET loading-large.gif').wrap(request6901)

request7001 = HTTPRequest(url=url4, headers=headers5)
request7001 = Test(7001, 'GET amzn.us.sr.dvd').wrap(request7001)

request7101 = HTTPRequest(url=url6, headers=headers25)
request7101 = Test(7101, 'GET turn-proxy.html').wrap(request7101)

request7201 = HTTPRequest(url=url0, headers=headers25)
request7201 = Test(7201, 'GET iframeproxy.html').wrap(request7201)

request7301 = HTTPRequest(url=url4, headers=headers26)
request7301 = Test(7301, 'GET amzn.us.sr.dvd').wrap(request7301)

request7401 = HTTPRequest(url=url8, headers=headers10)
request7401 = Test(7401, 'GET bd').wrap(request7401)

request7501 = HTTPRequest(url=url7, headers=headers27)
request7501 = Test(7501, 'GET 4640208').wrap(request7501)

request7601 = HTTPRequest(url=url14, headers=headers28)
request7601 = Test(7601, 'GET DocumentDotWrite.js').wrap(request7601)

request7701 = HTTPRequest(url=url9, headers=headers29)
request7701 = Test(7701, 'GET 20100801_DB_IP_FLIP_23_160_600.gif').wrap(request7701)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET / (request 101)."""
    result = request101.GET('/')

    return result

  def page2(self):
    """GET navbarCSSUSSA185-navbarUSSA185-29254.css._V188482287_.css (requests 201-205)."""
    result = request201.GET('/images/G/01/nav2/gamma/navbarCSSUSSA185/navbarCSSUSSA185-navbarUSSA185-29254.css._V188482287_.css')

    request202.GET('/images/G/01/nav2/gamma/websiteGridCSS/websiteGridCSS-websiteGridCSS-26613._V186355211_.css')

    request203.GET('/images/G/01/browser-scripts/mergedCore-1.2.6/core-3726680825.css._V186741523_.css')

    grinder.sleep(73)
    request204.GET('/images/G/01/nav2/gamma/amazonShoveler/amazonShoveler-amazonShovelerCss-12802._V235369351_.css')

    grinder.sleep(125)
    request205.GET('/images/G/01/browser-scripts/mergedCore-1.2.6/core-7224254877.js._V186741521_.js')

    return result

  def page3(self):
    """GET shasta-reviews-C1-COM-GW-INTL-01._V184950673_.jpg (requests 301-307)."""
    result = request301.GET('/images/G/01/kindle/merch/gw/shasta-reviews-C1-COM-GW-INTL-01._V184950673_.jpg')

    request302.GET('/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif')

    request303.GET('/images/G/01/gno/images/orangeBlue/navPackedSprites-US-16._V212310439_.png')

    request304.GET('/images/G/01/img10/other/giving/donate-pakistan_300x120._V186640421_.gif')

    request305.GET('/images/G/01/gateway/visit_amazon_de_tcg._V229026937_.gif')

    grinder.sleep(157)
    request306.GET('/images/G/01/gno/popover/sprites-h._V192570380_.gif')

    request307.GET('/images/G/01/gno/popover/sprites-v._V192570383_.gif')

    return result

  def page4(self):
    """GET navbarJS-jQuery-navbarJQ-48403._V212501460_.js (requests 401-404)."""
    result = request401.GET('/images/G/01/nav2/gamma/navbarJS-jQuery/navbarJS-jQuery-navbarJQ-48403._V212501460_.js')

    request402.GET('/images/G/01/nav2/gamma/search-js-autocomplete/search-js-autocomplete-autocomplete-15273._V188633242_.js')

    grinder.sleep(85)
    request403.GET('/images/G/01/s9-campaigns/s9-widget-seeded._V184604011_.css')

    grinder.sleep(81)
    request404.GET('/images/G/01/s9-campaigns/s9-multipack-layout-seeded._V210353195_.js')

    return result

  def page5(self):
    """GET B001A62M04._V192212155_.jpg (requests 501-505)."""
    result = request501.GET('/images/G/01/watches/B001A62M04._V192212155_.jpg')

    request502.GET('/images/G/01/watches/B0019FP47E._V192598089_.jpg')

    request503.GET('/images/G/01/watches/B000EQR6H0._V192598437_.jpg')

    request504.GET('/images/G/01/electronics/detail-page/asus-2._V189604747_.gif')

    request505.GET('/images/G/01/electronics/detail-page/dell._V189604740_.gif')

    return result

  def page6(self):
    """GET clog-platform._V213973670_.js (requests 601-602)."""
    result = request601.GET('/images/G/01/wma/clog/clog-platform._V213973670_.js')

    request602.GET('/images/G/01/da/common/d16g-0.6.14.nl.yui._V186549516_.js')

    return result

  def page7(self):
    """GET asus._V189604750_.gif (requests 701-705)."""
    result = request701.GET('/images/G/01/electronics/detail-page/asus._V189604750_.gif')

    request702.GET('/images/G/01/gno/images/general/navAmazonLogoFooter._V192570482_.gif')

    grinder.sleep(29)
    request703.GET('/images/G/01/amazon-credit/consumer/visa_gateway_300_4._V192208236_.gif')

    request704.GET('/images/G/01/gateway/iab/advertisement-sm-head._V192575712_.gif')

    request705.GET('/images/G/01/x-locale/personalization/yourstore/bluebox/bluebox-corners._V192187813_.gif')

    return result

  def page8(self):
    """GET 51y8Ow-npiL._SL135_.jpg (requests 801-805)."""
    result = request801.GET('/images/I/51y8Ow-npiL._SL135_.jpg')

    request802.GET('/images/I/41M+S6UQX3L._SL135_.jpg')

    request803.GET('/images/I/51993R08WLL._SL135_.jpg')

    request804.GET('/images/I/51oEJGNH-xL._SL75_.jpg')

    request805.GET('/images/I/417XQ0XwQuL._SL135_.jpg')

    return result

  def page9(self):
    """GET iframeproxy-2.html (request 901)."""
    result = request901.GET('/aan/2009-09-09/static/amazon/iframeproxy-2.html')

    return result

  def page10(self):
    """GET bluebox-sides._V192187807_.gif (requests 1001-1002)."""
    result = request1001.GET('/images/G/01/x-locale/personalization/yourstore/bluebox/bluebox-sides._V192187807_.gif')

    request1002.GET('/images/G/01/ui/loadIndicators/loadIndicator-large._V192195480_.gif')

    return result

  def page11(self):
    """GET amzn.us.gw.atf (request 1101)."""
    self.token_sz = \
      '300x250'
    self.token_bn = \
      '507846'
    self.token_u = \
      'ff6e2d9815cd4b27b0286d0be73e01a5'
    self.token_ord = \
      '1X7HZ43B9QM0Y1RPWVX3'
    self.token_s = \
      '1009'
    self.token_s = \
      '32'
    self.token_s = \
      'u14'
    self.token_s = \
      'm1'
    self.token_s = \
      'u2'
    self.token_s = \
      'u3'
    self.token_s = \
      'u4'
    self.token_s = \
      'm4'
    self.token_z = \
      '3'
    self.token_tile = \
      '1'
    result = request1101.GET('/adj/amzn.us.gw.atf;sz=' +
      self.token_sz +
      ';bn=' +
      self.token_bn +
      ';u=' +
      self.token_u +
      ';ord=' +
      self.token_ord +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';z=' +
      self.token_z +
      ';tile=' +
      self.token_tile)

    return result

  def page12(self):
    """GET advertisement-sm-head_US.gif (requests 1201-1202)."""
    result = request1201.GET('/2022817/advertisement-sm-head_US.gif')

    request1202.GET('/2022817/TTlifetimemaps300x250.jpg')

    return result

  def page13(self):
    """GET search-css-search-2279._V186518594_.css (requests 1301-1302)."""
    result = request1301.GET('/images/G/01/nav2/gamma/search-css/search-css-search-2279._V186518594_.css')

    request1302.GET('/images/G/01/nav2/gamma/fruitCSS/US/combined-3446052479._V214198738_.css')

    return result

  def page14(self):
    """GET sprite-communities._V201759850_.png (request 1401)."""
    result = request1401.GET('/images/G/01/common/sprites/sprite-communities._V201759850_.png')

    return result

  def page15(self):
    """GET combined-1240099087._V210574564_.css (requests 1501-1503)."""
    result = request1501.GET('/images/G/01/nav2/gamma/dpCSS/US/combined-1240099087._V210574564_.css')

    request1502.GET('/images/G/01/twister/beta/twister-dpf.c20ec6bc970396fc67cebc53deb1beaf._V1_.js')

    request1503.GET('/images/G/01/nav2/gamma/tmmJS/tmmJS-combined-core-29871._V189245115_.js')

    return result

  def page16(self):
    """GET amzn.us.gw.btf (request 1601)."""
    self.token_u = \
      '8525e462ff3d422f9c95b0fda5dcf848'
    self.token_s = \
      '1009'
    self.token_s = \
      '32'
    self.token_s = \
      'u14'
    self.token_s = \
      'u4'
    self.token_s = \
      'u3'
    self.token_s = \
      'u2'
    self.token_s = \
      'm4'
    self.token_s = \
      'm1'
    self.token_z = \
      '1'
    self.token_tile = \
      '3'
    result = request1601.GET('/adj/amzn.us.gw.btf;sz=' +
      self.token_sz +
      ';bn=' +
      self.token_bn +
      ';u=' +
      self.token_u +
      ';ord=' +
      self.token_ord +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';z=' +
      self.token_z +
      ';tile=' +
      self.token_tile)

    return result

  def page17(self):
    """GET favicon.ico (request 1701)."""
    result = request1701.GET('/favicon.ico')

    return result

  def page18(self):
    """GET turn-proxy.html (request 1801)."""
    result = request1801.GET('/turn-proxy.html')

    return result

  def page19(self):
    """GET 8006087 (request 1901)."""
    self.token_click = \
      'http://ad.doubleclick.net/click;h=v8/3a01/3/0/*/e;227339043;0-0;0;18273354;4307-300/250;37741618/37759470/1;u=8525e462ff3d422f9c95b0fda5dcf848;~sscs=?'
    result = request1901.GET('/MNY/iview/248834930/direct;wi.300;hi.250/01/8006087/8006087' +
      '?click=' +
      self.token_click)

    return result

  def page20(self):
    """GET bd (request 2001)."""
    self.token_pid = \
      '40'
    self.token_evt = \
      '99'
    self.token_cat = \
      '1009,32'
    result = request2001.GET('/r/bd' +
      '?&pid=' +
      self.token_pid +
      '&evt=' +
      self.token_evt +
      '&cat=' +
      self.token_cat)

    return result

  def page21(self):
    """GET 20100801_DB_IP_FLIP_23_300_250.gif (request 2101)."""
    self.token_ver = \
      '1'
    result = request2101.GET('/ds/9MMNYCAP1CPS/migration/20100801_DB_IP_FLIP_23_300_250.gif' +
      '?ver=' +
      self.token_ver)

    return result

  def page22(self):
    """GET 191-5896311-1113436 (request 2201)."""
    self.token_ref = \
      'sa_menu_mov1'
    self.token_ie = \
      'UTF8'
    self.token_node = \
      '130'
    result = request2201.GET('/dvds-used-hd-action-comedy-oscar/b/ref=' +
      self.token_ref +
      '/191-5896311-1113436' +
      '?ie=' +
      self.token_ie +
      '&node=' +
      self.token_node)

    return result

  def page23(self):
    """GET s9-widget._V184604009_.css (request 2301)."""
    result = request2301.GET('/images/G/01/s9-campaigns/s9-widget._V184604009_.css')

    return result

  def page24(self):
    """GET dp-on-demand-logo._V233830985_.gif (requests 2401-2404)."""
    result = request2401.GET('/images/G/01/digital/video/disc_plus/dp-on-demand-logo._V233830985_.gif')

    request2402.GET('/images/G/01/img10/movies-tv/stripe/theoffice_season6_ss._V188135687_.gif')

    request2403.GET('/images/G/01/daily/lozenge/lozenge_armchair._V230191894_.jpg')

    request2404.GET('/images/G/01/daily/90x90/armchair-commentary_blog_90x90._V192258809_.gif')

    return result

  def page25(self):
    """GET B002JVWR7M.01._SL110_PE37_OU01_SCLZZZZZZZ_V185856073_.jpg (requests 2501-2504)."""
    result = request2501.GET('/images/P/B002JVWR7M.01._SL110_PE37_OU01_SCLZZZZZZZ_V185856073_.jpg')

    request2502.GET('/images/P/B002Q4VBPQ.01._SL75_PE52_OU01_SCLZZZZZZZ_V217583187_.jpg')

    request2503.GET('/images/P/B000W7F5SS.01._SL75_PE60_OU01_SCLZZZZZZZ_V217281925_.jpg')

    request2504.GET('/images/I/51Da+R1iGSL._SL75_.jpg')

    return result

  def page26(self):
    """GET zeitgeist-chart.2._V186842733_.css (request 2601)."""
    result = request2601.GET('/images/G/01/zeitgeist/static/css/zeitgeist-chart.2._V186842733_.css')

    return result

  def page27(self):
    """GET 51Bq5wopzvL._SL75_.jpg (requests 2701-2703)."""
    result = request2701.GET('/images/I/51Bq5wopzvL._SL75_.jpg')

    request2702.GET('/images/I/51f2XzDeL3L._SL75_.jpg')

    request2703.GET('/images/I/51YBEEb+LvL._SL75_.jpg')

    return result

  def page28(self):
    """GET bluray._V192598306_.gif (request 2801)."""
    result = request2801.GET('/images/G/01/video/icons/bluray._V192598306_.gif')

    return result

  def page29(self):
    """GET 51zW3BrfegL._SL75_.jpg (request 2901)."""
    result = request2901.GET('/images/I/51zW3BrfegL._SL75_.jpg')

    return result

  def page30(self):
    """GET dvd._V192598333_.gif (request 3001)."""
    result = request3001.GET('/images/G/01/video/icons/dvd._V192598333_.gif')

    return result

  def page31(self):
    """GET 61hVWKe2AML._SL75_.jpg (requests 3101-3109)."""
    result = request3101.GET('/images/I/61hVWKe2AML._SL75_.jpg')

    request3102.GET('/images/I/517viGC516L._SL75_.jpg')

    request3103.GET('/images/I/51QlqI3yaOL._SL75_.jpg')

    request3104.GET('/images/I/61FCRvfKYgL._SL75_.jpg')

    request3105.GET('/images/I/51OfO6I-qsL._SL75_.jpg')

    request3106.GET('/images/I/51G35CahIML._SL75_.jpg')

    request3107.GET('/images/I/51EKgLUIENL._SL69_PE24_OU01_.jpg')

    request3108.GET('/images/I/51XVloeMTaL._SL69_PE09_OU01_.jpg')

    request3109.GET('/images/I/51XKNUudeJL._SL69_PE20_OU01_.jpg')

    return result

  def page32(self):
    """GET up_down_arrows._V245851576_.png (request 3201)."""
    result = request3201.GET('/images/G/01/x-locale/common/icons/up_down_arrows._V245851576_.png')

    return result

  def page33(self):
    """GET s9-multipack-min._V185037641_.js (request 3301)."""
    result = request3301.GET('/images/G/01/s9-campaigns/s9-multipack-min._V185037641_.js')

    return result

  def page34(self):
    """GET B003XKPPOU.01._SL75_PE37_OU01_SCLZZZZZZZ_V185828238_.jpg (requests 3401-3402)."""
    result = request3401.GET('/images/P/B003XKPPOU.01._SL75_PE37_OU01_SCLZZZZZZZ_V185828238_.jpg')

    request3402.GET('/images/P/B002N5N5M0.01._SL110_PE40_OU01_SCLZZZZZZZ_V191724279_.jpg')

    return result

  def page35(self):
    """GET orange-arrow._V192240581_.gif (request 3501)."""
    result = request3501.GET('/images/G/01/x-locale/common/orange-arrow._V192240581_.gif')

    return result

  def page36(self):
    """GET B0036EH3XE.01._SL110_PE37_OU01_SCLZZZZZZZ_V185747176_.jpg (requests 3601-3606)."""
    result = request3601.GET('/images/P/B0036EH3XE.01._SL110_PE37_OU01_SCLZZZZZZZ_V185747176_.jpg')

    request3602.GET('/images/I/51ZVhFmvIbL._SX160_SY120_.jpg')

    request3603.GET('/images/I/51QlqI3yaOL._SS135_PI43-percent,BottomRight,0,0_OU01_SS135_.jpg')

    request3604.GET('/images/I/51fCBFMTGnL._SS135_PI63-percent,BottomRight,0,0_OU01_SS135_.jpg')

    request3605.GET('/images/I/51-3gyzp1GL._SS135_.jpg')

    request3606.GET('/images/P/B002N5N5QQ.01._SL110_PE47_OU01_SCLZZZZZZZ_V212176037_.jpg')

    return result

  def page37(self):
    """GET s9-shoveler-min._V185037643_.js (request 3701)."""
    result = request3701.GET('/images/G/01/s9-campaigns/s9-shoveler-min._V185037643_.js')

    return result

  def page38(self):
    """GET 51zn8ZTH4AL._SL120_.jpg (requests 3801-3803)."""
    result = request3801.GET('/images/I/51zn8ZTH4AL._SL120_.jpg')

    request3802.GET('/images/I/51MGWPWYU4L._SL120_.jpg')

    request3803.GET('/images/I/51j6t6f02fL._SL120_.jpg')

    return result

  def page39(self):
    """GET todays-deals_120._V224628603_.png (requests 3901-3906)."""
    result = request3901.GET('/images/G/01/img09/movies-tv/120/todays-deals_120._V224628603_.png')

    request3902.GET('/images/G/01/img10/movies-tv/120/best-2010-so-far_120._V192571830_.gif')

    request3903.GET('/images/G/01/dvd/emmys/2008/dvd_emmys08_120._V192565529_.gif')

    request3904.GET('/images/G/01/img09/movies-tv/category/new-releases_cat._V192572827_.gif')

    request3905.GET('/images/G/01/img09/movies-tv/category/tvshows_cat._V192572822_.gif')

    request3906.GET('/images/G/01/img09/movies-tv/category/bluray_cat._V192572827_.gif')

    return result

  def page40(self):
    """GET B002VPE1AW.01._SL110_PE33_OU01_SCLZZZZZZZ_V215102563_.jpg (requests 4001-4014)."""
    result = request4001.GET('/images/P/B002VPE1AW.01._SL110_PE33_OU01_SCLZZZZZZZ_V215102563_.jpg')

    request4002.GET('/images/P/B003LL3N1I.01._SL110_PE48_OU01_SCLZZZZZZZ_V211526623_.jpg')

    request4003.GET('/images/I/51bWiRuJb6L._SL110_.jpg')

    request4004.GET('/images/P/B003FSTN52.01._SL110_PE31_OU01_SCLZZZZZZZ_V214776188_.jpg')

    request4005.GET('/images/I/51STDj5eM3L._SL110_.jpg')

    request4006.GET('/images/P/B001IBIHQ4.01._SL110_PE35_OU01_SCLZZZZZZZ_V187414510_.jpg')

    request4007.GET('/images/P/B0021L8V1G.01._SL110_PE34_OU01_SCLZZZZZZZ_V184946071_.jpg')

    request4008.GET('/images/P/B00275EHJG.01._SL110_PE43_OU01_SCLZZZZZZZ_V186081659_.jpg')

    request4009.GET('/images/I/51dmG8W8DOL._SL120_.jpg')

    request4010.GET('/images/I/51zW3BrfegL._SL120_.jpg')

    request4011.GET('/images/I/51VqqUJ11tL._SL120_.jpg')

    request4012.GET('/images/I/51K9gRUIZ2L._SL120_.jpg')

    request4013.GET('/images/I/51s9td+zJOL._SL120_.jpg')

    request4014.GET('/images/I/51t3jSau4eL._SL120_.jpg')

    return result

  def page41(self):
    """GET loading-indicator._V31970667_.gif (requests 4101-4103)."""
    result = request4101.GET('/images/G/01/x-locale/personalization/shoveler/loading-indicator._V31970667_.gif')

    request4102.GET('/images/G/01/x-locale/personalization/shoveler/left-arrow-semi-rd._V17361814_.gif')

    request4103.GET('/images/G/01/x-locale/personalization/shoveler/right-arrow-semi-rd._V17361809_.gif')

    return result

  def page42(self):
    """GET ref=sv_d_0 (request 4201)."""
    self.token_ref = \
      'sv_d_0'
    self.token_node = \
      '241586011'
    result = request4201.GET('/Advanced-Search-DVD/b/ref=' +
      self.token_ref +
      '?ie=' +
      self.token_ie +
      '&node=' +
      self.token_node)

    return result

  def page43(self):
    """GET search-md-sec._V33237624_.gif (request 4301)."""
    result = request4301.GET('/images/G/01/nav2/buttons/search-md-sec._V33237624_.gif')

    return result

  def page44(self):
    """GET grey-dot-vert-border._V44209678_.gif (request 4401)."""
    result = request4401.GET('/images/G/01/nav2/images/gui/grey-dot-vert-border._V44209678_.gif')

    return result

  def page45(self):
    """POST full-rhf-rec-handler.html (request 4501)."""
    result = request4501.POST('/gp/history/external/full-rhf-rec-handler.html',
      ( NVPair('shovelerName', 'rhf'),
        NVPair('key', 'rhf'),
        NVPair('numToPreload', '5'),
        NVPair('isGateway', '0'),
        NVPair('refTag', 'pd_rhf_shvl'),
        NVPair('parentSession', '191-5896311-1113436'),
        NVPair('excludeASIN', ''),
        NVPair('renderPopover', '0'),
        NVPair('forceSprites', '0'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page46(self):
    """GET stars-4-0._V192251205_.gif (requests 4601-4603)."""
    result = request4601.GET('/images/G/01/x-locale/common/customer-reviews/ratings/stars-4-0._V192251205_.gif')

    request4602.GET('/images/G/01/x-locale/common/customer-reviews/ratings/stars-3-0._V192238413_.gif')

    request4603.GET('/images/G/01/x-locale/common/customer-reviews/ratings/stars-4-5._V192238104_.gif')

    return result

  def page47(self):
    """GET 41f6tpRVssL._SL500_SS120_.jpg (requests 4701-4705)."""
    result = request4701.GET('/images/I/41f6tpRVssL._SL500_SS120_.jpg')

    request4702.GET('/images/I/41ThJ66fhbL._SL500_PIsitb-sticker-arrow-big,TopRight,35,-73_OU01_SS120_.jpg')

    request4703.GET('/images/I/41PuUigDokL._SL500_SS120_.jpg')

    request4704.GET('/images/I/51QWwGRXouL._SL500_SS120_.jpg')

    request4705.GET('/images/I/511ZEohSj6L._SL500_SS120_.jpg')

    return result

  def page48(self):
    """GET amazonShoveler-amazonShoveler-44847._V190802495_.js (request 4801)."""
    result = request4801.GET('/images/G/01/nav2/gamma/amazonShoveler/amazonShoveler-amazonShoveler-44847._V190802495_.js')

    return result

  def page49(self):
    """GET left-right-arrow-semi-rd._V236573507_.gif (request 4901)."""
    result = request4901.GET('/images/G/01/x-locale/personalization/shoveler/left-right-arrow-semi-rd._V236573507_.gif')

    return result

  def page50(self):
    """GET amzn-logo-118w.gif (request 5001)."""
    result = request5001.GET('/images/G/01/nav/amazon/amzn-logo-118w.gif')

    return result

  def page51(self):
    """GET / (request 5101)."""
    self.token_src = \
      'http://g-ec1.images-amazon.com/images/G/01/nav/amazon/amzn-logo-118w.gif'
    self.token_s = \
      's'
    self.token_l = \
      '367'
    self.token_tz = \
      '-2'
    self.token_b = \
      'undefined'
    self.token_sy = \
      'undefined'
    self.token_u = \
      'undefined'
    result = request5101.GET('/clog/1.0.1/mediaservices/edgecache/ATVPDKIKX0DER/191-5896311-1113436/0GWGQ62KERDKWXG4SAF5/2773/1/' +
      '?src=' +
      self.token_src +
      '&s=' +
      self.token_s +
      '&l=' +
      self.token_l +
      '&tz=' +
      self.token_tz +
      '&b=' +
      self.token_b +
      '&sy=' +
      self.token_sy +
      '&u=' +
      self.token_u)

    return result

  def page52(self):
    """GET / (request 5201)."""
    self.token_ref = \
      'sr_adv_d'
    self.token_searchalias = \
      'dvd'
    self.token_unfiltered = \
      '1'
    self.token_fieldkeywords = \
      ''
    self.token_fieldtitle = \
      ''
    self.token_fieldactor = \
      ''+SEARCH_STRING1+'+'+SEARCH_STRING2+''
    self.token_fielddirector = \
      ''
    self.token_fieldprice = \
      '0-1000'
    self.token_fieldmpaa = \
      'unrated'
    self.token_node = \
      ''
    self.token_fieldoriginal = \
      'English'
    self.token_fieldsubtitled = \
      ''
    self.token_fieldpictureformat = \
      ''
    self.token_fieldaudiotype = \
      ''
    self.token_fielddvdregion = \
      ''
    self.token_fielddvdsupplements = \
      ''
    self.token_sort = \
      'relevancerank'
    self.token_AdvSrchDVDSubmitx = \
      '36'
    self.token_AdvSrchDVDSubmity = \
      '13'
    result = request5201.GET('/gp/search/ref=' +
      self.token_ref +
      '/' +
      '?search-alias=' +
      self.token_searchalias +
      '&unfiltered=' +
      self.token_unfiltered +
      '&field-keywords=' +
      self.token_fieldkeywords +
      '&field-title=' +
      self.token_fieldtitle +
      '&field-actor=' +
      self.token_fieldactor +
      '&field-director=' +
      self.token_fielddirector +
      '&field-price=' +
      self.token_fieldprice +
      '&field-mpaa=' +
      self.token_fieldmpaa +
      '&node=' +
      self.token_node +
      '&field-original=' +
      self.token_fieldoriginal +
      '&field-subtitled=' +
      self.token_fieldsubtitled +
      '&field-picture-format=' +
      self.token_fieldpictureformat +
      '&field-audio-type=' +
      self.token_fieldaudiotype +
      '&field-dvd-region=' +
      self.token_fielddvdregion +
      '&field-dvd-supplements=' +
      self.token_fielddvdsupplements +
      '&sort=' +
      self.token_sort +
      '&Adv-Srch-DVD-Submit.x=' +
      self.token_AdvSrchDVDSubmitx +
      '&Adv-Srch-DVD-Submit.y=' +
      self.token_AdvSrchDVDSubmity)

    ## write response to disk
    commonhelper.logResponse(result)

    return result

  def page53(self):
    """GET 518zJy2BPEL._AA115_.jpg (request 5301)."""
    result = request5301.GET('/images/I/518zJy2BPEL._AA115_.jpg')

    return result

  def page54(self):
    """GET stars-3-5.gif (requests 5401-5402)."""
    result = request5401.GET('/images/G/01/x-locale/common/customer-reviews/ratings/stars-3-5.gif')

    request5402.GET('/images/G/01/x-locale/common/customer-reviews/ratings/stars-4-5.gif')

    return result

  def page55(self):
    """GET 51bvZUJpI3L._AA115_.jpg (requests 5501-5502)."""
    result = request5501.GET('/images/I/51bvZUJpI3L._AA115_.jpg')

    request5502.GET('/images/I/51qCKxkmRnL._AA115_.jpg')

    return result

  def page56(self):
    """GET stars-5-0.gif (requests 5601-5602)."""
    result = request5601.GET('/images/G/01/x-locale/common/customer-reviews/ratings/stars-5-0.gif')

    request5602.GET('/images/G/01/nav2/images/gui/searchSprite._V186644917_.gif')

    return result

  def page57(self):
    """GET search-js-general-search_general-19776._V185838463_.js (request 5701)."""
    result = request5701.GET('/images/G/01/nav2/gamma/search-js-general/search-js-general-search_general-19776._V185838463_.js')

    return result

  def page58(self):
    """GET 51cvHR7EODL._AA115_.jpg (request 5801)."""
    result = request5801.GET('/images/I/51cvHR7EODL._AA115_.jpg')

    return result

  def page59(self):
    """GET stars-4-0.gif (request 5901)."""
    result = request5901.GET('/images/G/01/x-locale/common/customer-reviews/ratings/stars-4-0.gif')

    return result

  def page60(self):
    """GET 51yo6aw0BWL._AA115_.jpg (request 6001)."""
    result = request6001.GET('/images/I/51yo6aw0BWL._AA115_.jpg')

    return result

  def page61(self):
    """GET stars-3-0.gif (requests 6101-6102)."""
    result = request6101.GET('/images/G/01/x-locale/common/customer-reviews/ratings/stars-3-0.gif')

    request6102.GET('/images/G/01/x-site/icons/no-img-sm._AA75_.gif')

    return result

  def page62(self):
    """GET 51KYRQA8WHL._AA115_.jpg (requests 6201-6206)."""
    result = request6201.GET('/images/I/51KYRQA8WHL._AA115_.jpg')

    request6202.GET('/images/I/51Mt7RRXYDL._AA115_.jpg')

    request6203.GET('/images/I/51U7UnCsjXL._AA115_.jpg')

    request6204.GET('/images/I/51SUsI0fXsL._AA115_.jpg')

    request6205.GET('/images/I/518jPzMUrIL._AA115_.jpg')

    request6206.GET('/images/I/21RM3SW3AGL._AA115_.jpg')

    return result

  def page63(self):
    """GET powered-by-a9.gif (requests 6301-6303)."""
    result = request6301.GET('/images/G/01/search-browse/powered-by-a9.gif')

    request6302.GET('/images/G/01/nav2/buttons/checkbox_unselected_enabled.jpg')

    request6303.GET('/images/G/01/nav2/images/gui/prime-check-badge-14.gif')

    return result

  def page64(self):
    """GET style-3._V248984170_.css (request 6401)."""
    result = request6401.GET('/images/G/01/x-locale/communities/profile/customer-popover/style-3._V248984170_.css')

    return result

  def page65(self):
    """GET 4star.gif (request 6501)."""
    result = request6501.GET('/images/G/01/nav2/images/gui/4star.gif')

    return result

  def page66(self):
    """GET 518zJy2BPEL._AA75_.jpg (requests 6601-6602)."""
    result = request6601.GET('/images/I/518zJy2BPEL._AA75_.jpg')

    request6602.GET('/images/I/51cvHR7EODL._AA75_.jpg')

    return result

  def page67(self):
    """GET 3star.gif (requests 6701-6726)."""
    result = request6701.GET('/images/G/01/nav2/images/gui/3star.gif')

    request6702.GET('/images/G/01/nav2/images/gui/2star.gif')

    request6703.GET('/images/G/01/nav2/images/gui/1star.gif')

    request6704.GET('/images/G/01/nav2/buttons/checkbox_selected_enabled.jpg')

    request6705.GET('/images/G/01/x-locale/common/buttons/go._V192195849_.gif')

    request6706.GET('/images/G/01/nav2/buttons/btn-yes._V192545584_.gif')

    request6707.GET('/images/G/01/nav2/buttons/btn-no._V192545588_.gif')

    request6708.GET('/images/G/01/nav2/dp/box-line-tl._V192545536_.gif')

    request6709.GET('/images/G/01/nav2/images/gui/box-blue-tm._V192184663_.gif')

    request6710.GET('/images/G/01/nav2/buttons/btn-yes-inactive._V192545585_.gif')

    request6711.GET('/images/G/01/nav2/buttons/btn-no-inactive-ns._V192545588_.gif')

    request6712.GET('/images/G/01/nav2/buttons/btn-yes-inactive-ns._V192545585_.gif')

    request6713.GET('/images/G/01/nav2/buttons/btn-no-inactive._V192545591_.gif')

    request6714.GET('/images/G/01/nav2/dp/btn-submit-sm._V192545553_.gif')

    request6715.GET('/images/G/01/nav2/dp/box-line-tr._V192545536_.gif')

    request6716.GET('/images/G/01/nav2/dp/box-line-bl._V192545543_.gif')

    request6717.GET('/images/G/01/nav2/images/gui/box-blue-bm._V192184657_.gif')

    request6718.GET('/images/G/01/nav2/dp/box-line-br._V192545543_.gif')

    request6719.GET('/images/G/01/x-locale/common/carrot._V192251235_.gif')

    request6720.GET('/images/G/01/ui/loadIndicators/loadIndicator-label._V192195535_.gif')

    request6721.GET('/images/G/01/nav2/images/gui/box-gray-tl._V192184760_.gif')

    request6722.GET('/images/G/01/nav2/images/gui/box-gray-tr._V192184429_.gif')

    request6723.GET('/images/G/01/nav2/images/gui/box-gray-tm._V192184721_.gif')

    request6724.GET('/images/G/01/nav2/images/gui/box-gray-bl._V192184824_.gif')

    request6725.GET('/images/G/01/nav2/images/gui/box-gray-bm._V192184603_.gif')

    request6726.GET('/images/G/01/nav2/images/gui/box-gray-br._V192545463_.gif')

    return result

  def page68(self):
    """GET search-js-ajax2-combined-core-60868._V189170300_.js (requests 6801-6802)."""
    result = request6801.GET('/images/G/01/nav2/gamma/search-js-ajax2/search-js-ajax2-combined-core-60868._V189170300_.js')

    grinder.sleep(70)
    request6802.GET('/images/G/01/x-locale/communities/profile/customer-popover/script-13-min._V224617671_.js')

    return result

  def page69(self):
    """GET loading-large.gif (request 6901)."""
    result = request6901.GET('/images/G/01/ui/loadIndicators/loading-large.gif')

    return result

  def page70(self):
    """GET amzn.us.sr.dvd (request 7001)."""
    self.token_sz = \
      '728x90'
    self.token_sn = \
      '130'
    self.token_u = \
      'f037e450b2f4421a9690577213277ac8'
    self.token_ord = \
      '09VG7TZGJV06GSMKDZ0D'
    self.token_s = \
      '1009'
    self.token_s = \
      '32'
    self.token_s = \
      'u3'
    self.token_s = \
      'u4'
    self.token_s = \
      'u2'
    self.token_s = \
      'm4'
    self.token_s = \
      'u14'
    self.token_s = \
      'm1'
    self.token_z = \
      '622'
    self.token_tile = \
      '2'
    result = request7001.GET('/adj/amzn.us.sr.dvd;sz=' +
      self.token_sz +
      ';sn=' +
      self.token_sn +
      ';u=' +
      self.token_u +
      ';ord=' +
      self.token_ord +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';z=' +
      self.token_z +
      ';tile=' +
      self.token_tile)

    return result

  def page71(self):
    """GET turn-proxy.html (request 7101)."""
    result = request7101.GET('/turn-proxy.html', None,
      ( NVPair('If-Modified-Since', 'Fri, 09 Jul 2010 03:05:23 GMT'),
        NVPair('If-None-Match', '\"42134f257eaeb9900cd55b413a278628\"'), ))

    return result

  def page72(self):
    """GET iframeproxy.html (request 7201)."""
    result = request7201.GET('/aan/2009-09-09/static/amazon.us/iframeproxy.html')

    return result

  def page73(self):
    """GET amzn.us.sr.dvd (request 7301)."""
    self.token_sz = \
      '160x600'
    self.token_u = \
      '7fddd1bf4bcc4b5abda58d555e525115'
    self.token_s = \
      '1009'
    self.token_s = \
      '32'
    self.token_s = \
      'u3'
    self.token_s = \
      'u4'
    self.token_s = \
      'm4'
    self.token_s = \
      'u2'
    self.token_s = \
      'u14'
    self.token_s = \
      'm1'
    self.token_tile = \
      '1'
    result = request7301.GET('/adj/amzn.us.sr.dvd;sz=' +
      self.token_sz +
      ';sn=' +
      self.token_sn +
      ';u=' +
      self.token_u +
      ';ord=' +
      self.token_ord +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';s=' +
      self.token_s +
      ';z=' +
      self.token_z +
      ';tile=' +
      self.token_tile)

    return result

  def page74(self):
    """GET bd (request 7401)."""
    result = request7401.GET('/r/bd' +
      '?&pid=' +
      self.token_pid +
      '&evt=' +
      self.token_evt +
      '&cat=' +
      self.token_cat)

    return result

  def page75(self):
    """GET 4640208 (request 7501)."""
    self.token_click = \
      'http://ad.doubleclick.net/click;h=v8/3a01/3/0/*/z;227339040;0-0;0;18273384;2321-160/600;37741837/37759689/1;u=7fddd1bf4bcc4b5abda58d555e525115;~sscs=?'
    result = request7501.GET('/MNY/iview/248834933/direct;wi.160;hi.600/01/4640208' +
      '?click=' +
      self.token_click)

    return result

  def page76(self):
    """GET DocumentDotWrite.js (request 7601)."""
    result = request7601.GET('/tl/DocumentDotWrite.js')

    return result

  def page77(self):
    """GET 20100801_DB_IP_FLIP_23_160_600.gif (request 7701)."""
    result = request7701.GET('/ds/9MMNYCAP1CPS/migration/20100801_DB_IP_FLIP_23_160_600.gif' +
      '?ver=' +
      self.token_ver)

    return result

  def __call__(self):
    """This method is called for every run performed by the worker thread."""
    self.page1()      # GET / (request 101)

    grinder.sleep(320)
    self.page2()      # GET navbarCSSUSSA185-navbarUSSA185-29254.css._V188482287_.css (requests 201-205)
    self.page3()      # GET shasta-reviews-C1-COM-GW-INTL-01._V184950673_.jpg (requests 301-307)
    self.page4()      # GET navbarJS-jQuery-navbarJQ-48403._V212501460_.js (requests 401-404)

    grinder.sleep(88)
    self.page5()      # GET B001A62M04._V192212155_.jpg (requests 501-505)

    grinder.sleep(45)
    self.page6()      # GET clog-platform._V213973670_.js (requests 601-602)
    self.page7()      # GET asus._V189604750_.gif (requests 701-705)
    self.page8()      # GET 51y8Ow-npiL._SL135_.jpg (requests 801-805)

    grinder.sleep(11)
    self.page9()      # GET iframeproxy-2.html (request 901)
    self.page10()     # GET bluebox-sides._V192187807_.gif (requests 1001-1002)

    grinder.sleep(40)
    self.page11()     # GET amzn.us.gw.atf (request 1101)

    grinder.sleep(41)
    self.page12()     # GET advertisement-sm-head_US.gif (requests 1201-1202)

    grinder.sleep(177)
    self.page13()     # GET search-css-search-2279._V186518594_.css (requests 1301-1302)
    self.page14()     # GET sprite-communities._V201759850_.png (request 1401)
    self.page15()     # GET combined-1240099087._V210574564_.css (requests 1501-1503)

    grinder.sleep(51)
    self.page16()     # GET amzn.us.gw.btf (request 1601)
    self.page17()     # GET favicon.ico (request 1701)
    self.page18()     # GET turn-proxy.html (request 1801)

    grinder.sleep(40)
    self.page19()     # GET 8006087 (request 1901)
    self.page20()     # GET bd (request 2001)

    grinder.sleep(80)
    self.page21()     # GET 20100801_DB_IP_FLIP_23_300_250.gif (request 2101)

    grinder.sleep(7943)
    self.page22()     # GET 191-5896311-1113436 (request 2201)

    grinder.sleep(192)
    self.page23()     # GET s9-widget._V184604009_.css (request 2301)

    grinder.sleep(234)
    self.page24()     # GET dp-on-demand-logo._V233830985_.gif (requests 2401-2404)
    self.page25()     # GET B002JVWR7M.01._SL110_PE37_OU01_SCLZZZZZZZ_V185856073_.jpg (requests 2501-2504)
    self.page26()     # GET zeitgeist-chart.2._V186842733_.css (request 2601)
    self.page27()     # GET 51Bq5wopzvL._SL75_.jpg (requests 2701-2703)
    self.page28()     # GET bluray._V192598306_.gif (request 2801)
    self.page29()     # GET 51zW3BrfegL._SL75_.jpg (request 2901)
    self.page30()     # GET dvd._V192598333_.gif (request 3001)
    self.page31()     # GET 61hVWKe2AML._SL75_.jpg (requests 3101-3109)
    self.page32()     # GET up_down_arrows._V245851576_.png (request 3201)
    self.page33()     # GET s9-multipack-min._V185037641_.js (request 3301)
    self.page34()     # GET B003XKPPOU.01._SL75_PE37_OU01_SCLZZZZZZZ_V185828238_.jpg (requests 3401-3402)
    self.page35()     # GET orange-arrow._V192240581_.gif (request 3501)
    self.page36()     # GET B0036EH3XE.01._SL110_PE37_OU01_SCLZZZZZZZ_V185747176_.jpg (requests 3601-3606)
    self.page37()     # GET s9-shoveler-min._V185037643_.js (request 3701)

    grinder.sleep(119)
    self.page38()     # GET 51zn8ZTH4AL._SL120_.jpg (requests 3801-3803)
    self.page39()     # GET todays-deals_120._V224628603_.png (requests 3901-3906)
    self.page40()     # GET B002VPE1AW.01._SL110_PE33_OU01_SCLZZZZZZZ_V215102563_.jpg (requests 4001-4014)

    grinder.sleep(11)
    self.page41()     # GET loading-indicator._V31970667_.gif (requests 4101-4103)

    grinder.sleep(9885)
    self.page42()     # GET ref=sv_d_0 (request 4201)

    grinder.sleep(615)
    self.page43()     # GET search-md-sec._V33237624_.gif (request 4301)

    grinder.sleep(219)
    self.page44()     # GET grey-dot-vert-border._V44209678_.gif (request 4401)
    self.page45()     # POST full-rhf-rec-handler.html (request 4501)

    grinder.sleep(162)
    self.page46()     # GET stars-4-0._V192251205_.gif (requests 4601-4603)
    self.page47()     # GET 41f6tpRVssL._SL500_SS120_.jpg (requests 4701-4705)

    grinder.sleep(18)
    self.page48()     # GET amazonShoveler-amazonShoveler-44847._V190802495_.js (request 4801)

    grinder.sleep(126)
    self.page49()     # GET left-right-arrow-semi-rd._V236573507_.gif (request 4901)

    grinder.sleep(1357)
    self.page50()     # GET amzn-logo-118w.gif (request 5001)

    grinder.sleep(215)
    self.page51()     # GET / (request 5101)

    grinder.sleep(25101)
    self.page52()     # GET / (request 5201)

    grinder.sleep(658)
    self.page53()     # GET 518zJy2BPEL._AA115_.jpg (request 5301)
    self.page54()     # GET stars-3-5.gif (requests 5401-5402)
    self.page55()     # GET 51bvZUJpI3L._AA115_.jpg (requests 5501-5502)
    self.page56()     # GET stars-5-0.gif (requests 5601-5602)

    grinder.sleep(311)
    self.page57()     # GET search-js-general-search_general-19776._V185838463_.js (request 5701)

    grinder.sleep(40)
    self.page58()     # GET 51cvHR7EODL._AA115_.jpg (request 5801)
    self.page59()     # GET stars-4-0.gif (request 5901)
    self.page60()     # GET 51yo6aw0BWL._AA115_.jpg (request 6001)
    self.page61()     # GET stars-3-0.gif (requests 6101-6102)
    self.page62()     # GET 51KYRQA8WHL._AA115_.jpg (requests 6201-6206)
    self.page63()     # GET powered-by-a9.gif (requests 6301-6303)
    self.page64()     # GET style-3._V248984170_.css (request 6401)
    self.page65()     # GET 4star.gif (request 6501)

    grinder.sleep(17)
    self.page66()     # GET 518zJy2BPEL._AA75_.jpg (requests 6601-6602)
    self.page67()     # GET 3star.gif (requests 6701-6726)

    grinder.sleep(210)
    self.page68()     # GET search-js-ajax2-combined-core-60868._V189170300_.js (requests 6801-6802)

    grinder.sleep(12)
    self.page69()     # GET loading-large.gif (request 6901)

    grinder.sleep(266)
    self.page70()     # GET amzn.us.sr.dvd (request 7001)
    self.page71()     # GET turn-proxy.html (request 7101)
    self.page72()     # GET iframeproxy.html (request 7201)
    self.page73()     # GET amzn.us.sr.dvd (request 7301)
    self.page74()     # GET bd (request 7401)

    grinder.sleep(41)
    self.page75()     # GET 4640208 (request 7501)

    grinder.sleep(186)
    self.page76()     # GET DocumentDotWrite.js (request 7601)

    grinder.sleep(45)
    self.page77()     # GET 20100801_DB_IP_FLIP_23_160_600.gif (request 7701)


def instrumentMethod(test, method_name, c=TestRunner):
  """Instrument a method with the given Test."""
  unadorned = getattr(c, method_name)
  import new
  method = new.instancemethod(test.wrap(unadorned), None, c)
  setattr(c, method_name, method)

# Replace each method with an instrumented version.
# You can call the unadorned method using self.page1.__target__().
instrumentMethod(Test(100, 'Page 1'), 'page1')
instrumentMethod(Test(200, 'Page 2'), 'page2')
instrumentMethod(Test(300, 'Page 3'), 'page3')
instrumentMethod(Test(400, 'Page 4'), 'page4')
instrumentMethod(Test(500, 'Page 5'), 'page5')
instrumentMethod(Test(600, 'Page 6'), 'page6')
instrumentMethod(Test(700, 'Page 7'), 'page7')
instrumentMethod(Test(800, 'Page 8'), 'page8')
instrumentMethod(Test(900, 'Page 9'), 'page9')
instrumentMethod(Test(1000, 'Page 10'), 'page10')
instrumentMethod(Test(1100, 'Page 11'), 'page11')
instrumentMethod(Test(1200, 'Page 12'), 'page12')
instrumentMethod(Test(1300, 'Page 13'), 'page13')
instrumentMethod(Test(1400, 'Page 14'), 'page14')
instrumentMethod(Test(1500, 'Page 15'), 'page15')
instrumentMethod(Test(1600, 'Page 16'), 'page16')
instrumentMethod(Test(1700, 'Page 17'), 'page17')
instrumentMethod(Test(1800, 'Page 18'), 'page18')
instrumentMethod(Test(1900, 'Page 19'), 'page19')
instrumentMethod(Test(2000, 'Page 20'), 'page20')
instrumentMethod(Test(2100, 'Page 21'), 'page21')
instrumentMethod(Test(2200, 'Page 22'), 'page22')
instrumentMethod(Test(2300, 'Page 23'), 'page23')
instrumentMethod(Test(2400, 'Page 24'), 'page24')
instrumentMethod(Test(2500, 'Page 25'), 'page25')
instrumentMethod(Test(2600, 'Page 26'), 'page26')
instrumentMethod(Test(2700, 'Page 27'), 'page27')
instrumentMethod(Test(2800, 'Page 28'), 'page28')
instrumentMethod(Test(2900, 'Page 29'), 'page29')
instrumentMethod(Test(3000, 'Page 30'), 'page30')
instrumentMethod(Test(3100, 'Page 31'), 'page31')
instrumentMethod(Test(3200, 'Page 32'), 'page32')
instrumentMethod(Test(3300, 'Page 33'), 'page33')
instrumentMethod(Test(3400, 'Page 34'), 'page34')
instrumentMethod(Test(3500, 'Page 35'), 'page35')
instrumentMethod(Test(3600, 'Page 36'), 'page36')
instrumentMethod(Test(3700, 'Page 37'), 'page37')
instrumentMethod(Test(3800, 'Page 38'), 'page38')
instrumentMethod(Test(3900, 'Page 39'), 'page39')
instrumentMethod(Test(4000, 'Page 40'), 'page40')
instrumentMethod(Test(4100, 'Page 41'), 'page41')
instrumentMethod(Test(4200, 'Page 42'), 'page42')
instrumentMethod(Test(4300, 'Page 43'), 'page43')
instrumentMethod(Test(4400, 'Page 44'), 'page44')
instrumentMethod(Test(4500, 'Page 45'), 'page45')
instrumentMethod(Test(4600, 'Page 46'), 'page46')
instrumentMethod(Test(4700, 'Page 47'), 'page47')
instrumentMethod(Test(4800, 'Page 48'), 'page48')
instrumentMethod(Test(4900, 'Page 49'), 'page49')
instrumentMethod(Test(5000, 'Page 50'), 'page50')
instrumentMethod(Test(5100, 'Page 51'), 'page51')
instrumentMethod(Test(5200, 'Page 52'), 'page52')
instrumentMethod(Test(5300, 'Page 53'), 'page53')
instrumentMethod(Test(5400, 'Page 54'), 'page54')
instrumentMethod(Test(5500, 'Page 55'), 'page55')
instrumentMethod(Test(5600, 'Page 56'), 'page56')
instrumentMethod(Test(5700, 'Page 57'), 'page57')
instrumentMethod(Test(5800, 'Page 58'), 'page58')
instrumentMethod(Test(5900, 'Page 59'), 'page59')
instrumentMethod(Test(6000, 'Page 60'), 'page60')
instrumentMethod(Test(6100, 'Page 61'), 'page61')
instrumentMethod(Test(6200, 'Page 62'), 'page62')
instrumentMethod(Test(6300, 'Page 63'), 'page63')
instrumentMethod(Test(6400, 'Page 64'), 'page64')
instrumentMethod(Test(6500, 'Page 65'), 'page65')
instrumentMethod(Test(6600, 'Page 66'), 'page66')
instrumentMethod(Test(6700, 'Page 67'), 'page67')
instrumentMethod(Test(6800, 'Page 68'), 'page68')
instrumentMethod(Test(6900, 'Page 69'), 'page69')
instrumentMethod(Test(7000, 'Page 70'), 'page70')
instrumentMethod(Test(7100, 'Page 71'), 'page71')
instrumentMethod(Test(7200, 'Page 72'), 'page72')
instrumentMethod(Test(7300, 'Page 73'), 'page73')
instrumentMethod(Test(7400, 'Page 74'), 'page74')
instrumentMethod(Test(7500, 'Page 75'), 'page75')
instrumentMethod(Test(7600, 'Page 76'), 'page76')
instrumentMethod(Test(7700, 'Page 77'), 'page77')
