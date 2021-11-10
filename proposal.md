
# Proposal:Unifying fare payments across services in Philadelphia

**By**:
* Jeff Stern, jeffster@design.upenn.edu

## Abstract

There’s an increasing interest in moving toward unifying fare payments across transit services and private mobility operators. For example, San Francisco recently made a $300 million dollar investment into improving [Clipper Card][1] service which can be used on any of 24 different services in the Bay Area. Chicago is piloting a program with Uber where riders can pay for an Uber ride and transit ticket with a single payment. Pittsburgh recently launched [Move PGH][2], a first-of-its-kind initiative to promote many different mobility services to residents through the Transit App and digital signage.

What might it look like to unify fare payment in Philadelphia? This dashboard can help stakeholders in Philadelphia assess and visualize the viability and utility of unifying fare payments within the city.  

The dashboard will visualize rides across a variety of services that are available to riders in central Philadelphia. In particular:
- SEPTA subway and buses
- PATCO trains
- Indego bike share

These services are not inclusive of all options that are currently available for riders (eg. rideshare, commuter rail, taxis), but this dashboard is an initial analysis. Particular attention will be paid to multi-modal trips (eg. Incorporating two or more services in a ride) and how a unified fare system may increase overall mobility for riders, providing them with access to more destinations and opportunities.  

These metrics will allow stakeholders to explore some of the following questions:
- low rates of local business ownership may prompt business education programs for community residents
- increasing average time since
- low foot traffic in the face of other positively trending metrics may prompt public space activation events

## Stakeholders

* Transit officials who want to identify commercial districts where additional resources might be helpful.
* Private mobility operators that want to work with and support public transit.
* Riders and residents that advocate for improved mobility options.

## Data sources

* SEPTA rail stops
* PATCO rail stops ([https://transitfeeds.com/p/patco/533][3])
* Live feed of Indego kiosks and bicycle availability [https://kiosks.bicycletransit.workers.dev/phl][4]
* Philadelphia neighborhoods ([https://github.com/azavea/geo-data][5])
* **US Census Block Group demographics** -- BigQuery public datasets, updated with the national census, i.e. yearly estimates at its most frequent

## Wireframe of dashboard

### Main overview page
![][image-1]

This is the main overview page. It contains one map showing all transit locations (SEPTA, PATCO, INDEGO) in Philadelphia using a different style for each mode. There’s general overview text describing the current potential of unified transit in Philadelphia (eg. “On the whole, there are usually about XX stops/stations of different transit modes within a 5-minute walk from any given station. The most connected station is the XXXX.”)

Users can then use a dropdown to navigate to an individual station. Being able to dig in on specific neighborhoods is a stretch goal, but the navigation for that is represented here in this mockup.

The dashboard will always stay up-to-date with the most recent available station and ridership information.

### Individual station detail page

![][image-2]

Each station will have a detailed view. The view includes one map that will show that station and all stations within a particular radius (eg. 5 minute walk). A bar chart at the top of the page will provide a visualization of either the:  

- a) total ridership at this and nearby stations and how this compares to the neighborhood and city averages (Stretch)
- b) total number of nearby stations, by type

There will also be navigation links to dig in on the nearby stations.

[1]:	https://www.clippercard.com/ClipperWeb/where-to-use.html
[2]:	https://move-pgh.com/what-is-move-pgh
[3]:	https://transitfeeds.com/p/patco/533
[4]:	https://kiosks.bicycletransit.workers.dev/phl
[5]:	https://github.com/azavea/geo-data

[image-1]:	/images/overview.jpg
[image-2]:	/images/individual-station.jpg