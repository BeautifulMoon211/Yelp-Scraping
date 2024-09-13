<h1 align="center">Yelp-Scraping</h1>
<a href="https://www.yelp.com">
  <div align="center">
    <br><img align-"center" src="https://www.clipartmax.com/png/full/142-1429407_yelp-reviews-5-star-yelp-logo.png" width='300'/>
  </div><br>
</a>

>This project is mainly used to collect business and customer data from Yelp.com for getting information of [Solar companies](https://www.yelp.com/search?find_desc=Solar&find_loc=New+York%2C+NY%2C+United+States/).

### Why is Yelp Important for Business?
Yelp is essential for business because it allows customers to leave reviews and feedback about their experiences. This helps other potential customers make informed decisions about whether or not to patronize a particular business. In addition, companies can use Yelp to track their customer satisfaction levels and make necessary improvements.

Yelp also provides businesses with an advertising platform. Companies can create ads that target potential customers in their area. This is a great way to reach new customers and grow your business.

Overall, Yelp is essential for businesses to connect with their customers and grow their business.

### Is Yelp Helpful?
As a business owner, you may wonder if Yelp is worth your time. After all, there are a lot of reviews on there, and it can be tough to keep track of them all. And what if someone leaves a negative review?

Well, Yelp can be quite helpful for businesses. First, it’s a great way to get your business name out there. People are always searching for companies on Yelp, so if you’re not listed, you could miss out on potential customers.

Yelp can also be a great way to get feedback from customers. You can see what people liked and didn’t like about your business and make changes accordingly. And if you do get a negative review, you can use it as an opportunity to improve your business.

So if you’re wondering whether or not Yelp is worth your time, the answer is yes! It’s a great way to promote your business and get customer feedback.
<a href="https://www.enterpriseappstoday.com/stats/yelp-statistics.html">
  <div align="center">
    <img align-"center" src="https://media.licdn.com/dms/image/v2/D5612AQGuSurjRLKudA/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1712069297537?e=2147483647&v=beta&t=v2UBQrYRFoEUhj979QRzWBQ52JbDFb62QIUnZljRz0U"/>
  </div>
</a>
I hope this blog will help you understand. - <a href="https://www.enterpriseappstoday.com/stats/yelp-statistics.html">
  Yelp Statistics 2024 By Business Category, Star Rating Distribution, Visitors, Platform, Country and Consumers
</a> 

## Yelp Scraper
> You can scrape a bunch of comprehensive information of companies for specific field such as company name, website link, phone number, located address, owner name, provided services and several contact informations.

- *Name:* Sunation Energy
- *Website link:* sunation.com
- *Phone number:* +1 (631) 892-7245
- *Located address:* 171 Remington Blvd Ronkonkoma, NY 11779
- *Services offered:* EV charging stations, Add solar panels, Solar rooftop panel installation, Solar system maintenance, Add to existing system, Solar system installation, Solar shingle installation, Solar system repair
- *Owner name:* Scott Maskin
- *Supported area:* [(40.727172, 73.814309), (40.582027, 73.769150), (40.582027, 73.423253), (40.609850, 71.856214), (41.290122, 71.856214), (41.290122, 73.497061), (40.922801, 73.769150), (40.752494, 73.814309), (40.727172, 73.814309)] (with coordinates from...)



| Number | Name          | Website           | Phone          | Address                    | Owner   |
|--------|---------------|-------------------|----------------|----------------------------|---------|
| 1      | Sunation Energy| sunation.com      | (631) 892-7245 | 171 Remington Blvd Ronkonkoma, NY 11779 | Scitt M.  |
| 2      | Exact Solar   | exactsolar.com    | (267) 748-0596 | 82 Walker Ln Newtown, PA 18940 | Doug E. |
| 3      | EmPower Solar | empower-solar.com | (516) 837-3459 |                            | Daid S.   |
|...|...|...|...|...|...|

**Live Demo for Yelp Scraper is [here](https://www.loom.com/share/0ae6d558f6c94ba09b64bb1edf40a805?sid=0e0683fb-e212-4823-a84f-bfb120d3ac68)** 

## Cities Selector
> You can also get cities which located in service provided area.

### Coordinates Finder
You can get coordinates of cities using Google Search.

<a href="https://www.google.com/search?q=philadelphia+longitude+latitude">
  <div align="center">
    <img align-"center" src="https://global.discourse-cdn.com/cesium/original/3X/c/9/c972c590712aa63d29009b11a4577efeedaa819c.png" width='80%'/>
  </div>
</a>

It is required to use [smtplib](https://mailtrap.io/blog/python-send-email/) for Google Search.
```
NEW JERSEY, WOODLAND TOWNSHIP: 39.8537, -74.5229
ILLINOIS, OAK BROOK DU: 41.840794, -87.952377
CONNECTICUT, MERIDEN NEW: 41.53666666666666, -72.79472222222222
WASHINGTON, OMAK: 48.411, -119.5276
NEW HAMPSHIRE, FRANKLIN: 43.4442, -71.6473
...
```
**Live Demo for Coordinates Finder is [here](https://www.loom.com/share/36d816493f4a4f9db6bdef8ad27cf1a0?sid=9f49f28b-2f6b-4719-aa6f-95e96b46c5aa)** 

### Cities Selector
Based on coordinates from Yelp Scraper and Coordinates Finder, let's find cities which located in the area the company supported.

<a href="https://www.yelp.com/map/sunation-energy-ronkonkoma">
  </br><div align="center">
    <img align-"center" src="https://maps.googleapis.com/maps/api/staticmap?size=315x150&sensor=false&client=gme-yelp&language=en&scale=1&path=color%3A0x1F8EFF70%7Cweight%3A2%7Cfillcolor%3A0x1F8EFF40%7C40.727172%2C-73.814309%7C40.582027%2C-73.769150%7C40.582027%2C-73.423253%7C40.609850%2C-71.856214%7C41.290122%2C-71.856214%7C41.290122%2C-73.497061%7C40.922801%2C-73.769150%7C40.752494%2C-73.814309%7C40.727172%2C-73.814309&markers=scale%3A1%7Cicon%3Ahttps%3A%2F%2Fyelp-images.s3.amazonaws.com%2Fassets%2Fmap-markers%2Fannotation_32x43.png%7C40.790157%2C-73.130497&signature=zBbAcfjde_skqiuiSu9wE2RiNRQ=" width='315px'/>
  </div></br>
</a>

```
These cities are in the blue box!!!
The totla number of cities :  177
Cities are :  ['LARCHMONT', 'GREAT NECK ESTATES', 'KINGS POINT', 'MAMARONECK', 'LAWRENCE', 'GREAT NECK', 'CEDARHURST', 'SANDS POINT', 'HARRISON', 'MANORHAVEN', 'THOMASTON', 'ELMONT', 'WOODMERE', 'LAKE SUCCESS', 'VALLEY STREAM', 'FLORAL PARK', 'PORT WASHINGTON NORTH', 'NORTH VALLEY STREAM', 'MANHASSET', 'PORT WASHINGTON', 'HEWLETT', 'NORTH NEW HYDE PARK', 'NEW HYDE PARK', 'RYE', 'FLOWER HILL', 'MUNSEY PARK', 'FRANKLIN SQUARE', 'MALVERNE', 'LYNBROOK', 'EAST ROCKAWAY', 'PORT CHESTER', 'LONG BEACH', 'ISLAND PARK', 'LAKEVIEW', 'ROSLYN', 'WEST HEMSTEAD', 'ROSLYN HEIGHTS', 'WILLISTON PARK', 'SEA CLIFF', 'ALBERTSON', 'ROCKVILLE CENTRE', 'LOS PADRES NATIONAL FOREST SANTA', 'LAND', 'MINEOLA', 'OCEANSIDE', 'EAST WILLISTON', 'GARDEN CITY', 'GLEN COVE', 'GREENWICH', 'EAST HILLS', 'HEMPSTEAD', 'BALDWIN', 'CARLE PLACE', 'OLD BROOKVILLE', 'OLD WESTBURY', 'UNIONDALE', 'ROOSEVELT', 'WESTBURY', 'FREEPORT', 'BROOKVILLE', 'NORTH MERRICK', 'BAYVILLE', 'SOUTH WESTBURY', 'EAST MEADOW', 'MERRICK', 'JERICHO', 'STAMFORD', 'NORTH BELLMORE', 'OYSTER BAY', 'BELLMORE', 'HICKSVILLE', 'LEVITTOWN', 'WANTAGH', 'SYOSSET', 'RIDGEFIELD', 'NEW CANAAN', 'SEAFORD', 'BETHPAGE', 'MASSAPEQUA', 'DARIEN', 'PLAINVIEW', 'NORTH MASSAPEQUA', 'LLOYD HARBOR', 'COLD SPRING HARBOR', 'MASSAPEQUA PARK', 'OLDBETHPAGE', 'FARMINGDALE', 'SOUTH FARMINGDALE', 'WILTON', 'HUNTINGTON', 'EAST FARMINGDALE', 'AMITYVILLE', 'MELVILLE', 'HUNTINGTON BAY', 'HUNTINGTON STATION', 'NORWALK', 'COPIAGUE', 'SOUTH HUNTINGTON', 'MANATI', 'WESTON', 'LINDENHURST', 'CENTERPORT', 'GREENLAWN', 'WYANDANCH', 'WESTPORT', 'WEST BABYLON', 'NORTHPORT', 'DIX HILLS', 'ELWOOD', 'DEER PARK', 'BABYLON', 'EAST NORTHPORT', 'NORTH BABYLON', 'WEST ISLIP', 'FORT SALONGA', 'EASTON', 'COMMACK', 'BRIGHTWATERS', 'FAIRFIELD', 'KINGS PARK', 'BRENTWOOD', 'BAY SHORE', 'ISLIP', 'HAUPPAUGE', 'CENTRAL ISLIP', 'TRUMBULL', 'SMITHTOWN', 'BRIDGEPORT', 'ISLIP TERRACE', 'ETOWAH MC', 'EAST ISLIP', 'NESCONSET', 'ST. JAMES', 'STONY BROOK', 'OAKDALE', 'STRATFORD', 'BOHEMIA', 'LAKE GROVE', 'LAKE RONKONKOMA', 'SETAUKET-EAST SETAUKET', 'CENTEREACH', 'WEST SAYVILLE', 'SAYVILLE', 'HOLBROOK', 'PORT JEFFERSON', 'BAYPORT', 'PORT JEFFERSON STATION', 'HOLTSVILLE', 'SELDEN', 'FARMINGVILLE', 'LONG BEACH LA', 'MOUNT SINAI', 'ORANGE NEW', 'PATCHOGUE', 'CORAM', 'MEDFORD', 'EAST PATCHOGUE', 'MILLER PLACE', 'SOUND BEACH', 'NORTH BELLPORT', 'MIDDLE ISLAND', 'BELLPORT', 'ROCKY POINT', 'RIDGE', 'SHIRLEY', 'MASTIC BEACH', 'MASTIC', 'CENTER MORICHES', 'RIVERHEAD', 'NORTHVILLE', 'EAST QUOGUE', 'MATTITUCK', 'HAMPTON BAYS', 'SOUTHAMPTON', 'NOYACK', 'SAG HARBOR', 'MONTAUK']
```
**Live Demo for Cities Selector is [here](https://www.loom.com/share/c77591a0281a43f492fd668c65aec76b?sid=8def12cc-94da-450e-8f8d-b11199969059)** 

## Wordpress Detector
> If you append `/wp-admin` or `/wp-login.php` to the website's URL and it takes you to a login page, it is likely a WordPress site. Check whether the modified path is valid or not.

**Live Demo for Wordpress Detector is [here](https://www.loom.com/share/c0b84d6d56204ad28f4480365eec2076?sid=b0eb5766-c288-4a3a-87d2-22de00298adc)** 

## Social Contact Scraper
> Parse any website and find the spicific pattern for social contact information. Scrape them as much as possible.
```
Social contact information: https://www.youtube.com/@sunationenergy
                            https://www.instagram.com/sunationenergy
                            https://twitter.com/SUNation_Energy
                            https://www.linkedin.com/company/sunation-energy
                            https://www.tiktok.com/@sunationenergy
                            leads@sunation.com
                            https://www.facebook.com/SUNationEnergy
```

## Project Info
### Author 
Sweem

### Developers
 - [Sweem](https://github.com/beautifulmoon211)
 - [Oliver](https://github.com/HighAmbition211)
 - [Justing Wong](https://github.com/webghost241)
 - [Yuming Long](https://github.com/AI-General)

### Version
1.0.0

### License
This project is licensed under the MIT License - see teh [LICENSE](https://github.com/BeautifulMoon211/Yelp-Scraping/blob/dev/LICENSE) file for details.

<h3>
    If you found this project useful or interesting, please consider giving it a 
    <a href="https://github.com/BeautifulMoon211/Yelp-Scraping">
        <img src="https://camo.githubusercontent.com/180845d061c0e223ec293cc2fb1f01ed5a2ca248688b6682c851810d27489552/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f4f624e547738557a7779364b512f67697068792e676966" style="width:25px"> 
        Star
    </a>, or 
    <a href="https://github.com/BeautifulMoon211/">
        Following
    </a> 
    me.
    If you'd like to use this template, feel free to 
    <a href="https://github.com/BeautifulMoon211/Yelp-Scraping/fork">
        Fork
    </a> 
    it and customize it to your needs!
</h3>

###  Thank you for the help with [Johnson Takashi](https://github.com/HighAmbition211), [Justin Wong](https://github.com/webghost241), and [Oliver](https://github.com/AI-General).
