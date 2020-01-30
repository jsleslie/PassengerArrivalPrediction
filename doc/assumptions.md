Project Log
================
Jarome Leslie
28/01/2020

## Assumptions

### Passengers per day estimates

On July 14, 2018, YVR customer care director Reg Krake noted that up to
90,000 passengers can transit through the airport during the peak summer
days ( [Global
News](https://globalnews.ca/news/4312254/90k-summer-passengers-a-day-yvr-check-in-early/)
) .

“But you can expect there will be times of day when, let’s say, lots of
aircraft come in off-schedule, and we have 10 wide-bodies arrive within
an hour. That can be up to 4,000 people arriving at the customs hall.”

## Data availability

1.  [YVR
    Website](https://www.yvr.ca/en/passengers/flights/arriving-flights)
    provides a daily schedule for flight arrivals

2.  [FlightStats](https://www.flightstats.com/v2/) sells flight arrival
    records for $0.10 per flight is a bit too expensive.

<!-- end list -->

  - 2016: 120,765 flights - $12,077
  - 2017: 124,962 flights - $12,496
  - 2018: 128,935 flights - $12,894
  - 2019: 125,119 flights - $12,512

<!-- end list -->

3.  [Aviation
    Edge](https://aviation-edge.com/flight-schedule-and-timetable-of-airlines-and-airports/)
    offers an api with different tiers however there may be potential
    issues with the terms and conditions for a doing a public project on
    github.

<!-- end list -->

  - Free
  - Developer: $5 / $99
  - Business: $10 / $199
  - Business gold: $25 / $499
  - Unlimited:

Note: The discounted price is for the initial month, allowing developers
to test and implement the API without being charged the full price. The
subscription is automatically renewed each month at the normal rate of
99$ for the developer, 199$ for the Business package and 499$ for
business gold package. In case the API is not what you are looking for,
you can cancel 10 days before renewal by emailing to
<support@aviation-edge.com> or by cancelling through your dashboard. If
you have questions about our premium monthly subscription packages,
contact <sales@aviation-edge.com>.

Potential concerns in terms and conditions:

    Section 6: Content
    a. Content Accessible Through our Database and APIs
    
    Content accessible through our Database and APIs may sometimes be subject to intellectual property
    rights, and, if so, you may not use it unless you are licensed to do so by the owner of that content
    or are otherwise permitted by law. Your access to the content provided by the Database and API may be
    restricted, limited, or filtered in accordance with applicable law, regulation, and policy.
    
    b. Data Portability
    
    Aviation-Edge supports data portability. For as long as you use or store any user data that you
    obtained through the APIs, you agree to enable your users to export their equivalent data to other
    services or applications of their choice in a way that’s substantially as fast and easy as exporting
    such data from Aviation-Edge products and services, subject to applicable laws, and you agree that you
    will not make that data available to third parties who do not also abide by this obligation.
    
    e. Prohibitions on Content
    
    Unless expressly permitted by the content owner or by applicable law, you will not, and will not
    permit your end users or others acting on your behalf to, do the following with content returned from
    the APIs:
    
    Scrape, build databases, or otherwise create permanent copies of such content;
    Copy, translate, modify, create a derivative work of, sell, lease, lend, convey, distribute, publicly
    display, or sublicense to any third party;
    Misrepresent the source or ownership; or
    Remove, obscure, or alter any copyright, trademark, or other proprietary rights notices; or falsify or
    delete any author attributions, legal notices, or other labels of the origin or source of material.
