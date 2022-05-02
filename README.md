# ENGO551 FinalProject: PEDAL
ENGO 551 - Adv. Topics on Geospatial Technologies

# Summary
This project aims to utilize web application development and geospatial practices to solve a real-life problem that many people may face in their daily lives.
PEDAL is a web application designed for and dedicated to the bicycle community of City of Calgary. This app aims to assist the cyclists in planning their trips by providing various helpful and easy-to-execut functionalities and the information necessary for finalizng their trips. 

![image](https://user-images.githubusercontent.com/61097726/166212133-73981d9f-5b00-45ae-97b4-7d3622a36433.png)

# Structure
- Back-end: The back-end developement associted with this app includes SQL and Database Management. Database is used to store and access the user's creditionals that are used for setting up accounts which would hold their personal information and build a profile. This functionality also enables authenticaltion and session control implementations  which are deemed essential for applications that have registrations and account management infrastructure.
- Front-end: The front-end development is the majority of the web application as the primary functionalities of the app are implemented via front-end and mapping implementations. Front-end developemnt of this application uses the combination of HTML, CSS, Javascript, and Python. These languages coexists to provdide the users a clean and smooth experience. The mapping implementations include the main  functionalities of the app as all of the infromation and users' interactions are through the mapping interface

# Primary Functionlaities
- Users can plan their trips by inputting their start and destination points. This can be done by click the desired locations on the map. The map would then display the most optimal and fastest routes for cycling and walking:

![image](https://user-images.githubusercontent.com/61097726/166210361-5c376f64-fa87-45ad-9863-a083af0df3a9.png)

The displayed routes are based on data sets and calculations that consider the available bike lanes, bike accessible areas (i.e, parks) and roads that allow bicycles. This also applies to the walking route as they are based on the available sidewalks, corsswalks, bridges, and any accessible 

- Users can acquire their current location by activiating the GPS function. This function acquires the user's current location from their smartphones which act as IoT sensors. The information is then displayed on the map. This functionality aims to help the users with determining the start points of their trip:

![image](https://user-images.githubusercontent.com/61097726/166211408-d539f90a-cda1-4363-9111-db1b20d66388.png)

# Features
- Various map features are implemented based on open data sources. These data sets are displayed on the map to provide more information to the user, help them in planning their trips, and helping them with getting a better sense of where they are and where they want to be. These features include:
  -  Hospitals and Health-care Centres
  -  Community Services
  -  Schools, Universities, and campuses
  -  LRT Stations
  -  Recreational Facilities
 
 ![image](https://user-images.githubusercontent.com/61097726/166211826-d8c67fd0-a3c4-4b1e-98d1-ad0bcd90d97c.png)

- The traffic heat map of City of Calgary is created based on acquired data from the corresponding website and is implemented as a seperate layer that the user can toggle. This feature is implemented as a seperate layer as it is too dense and crowded to be included in the basemap. With the provided informatiion, the user can readjust and replan their trips by considering the traffic density associted with their trip.
