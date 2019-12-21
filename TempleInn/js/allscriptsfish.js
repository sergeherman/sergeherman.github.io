// Banner
  var d = new Date();
  var n = d.getDay()
             if ( n == 5) {
				
                    document.getElementById('topbanner').innerHTML = "Saturday = Preston Pancakes in the Park!  9:00 a.m. Saturday at the city park pavilion." ;
                } 
				
// Toggle Menu
function toggleMenu() {
    document.getElementsByClassName("navigation")[0].classList.toggle("responsive");
}				

// Wind Chill
function windChill(temp, wind) {
    if ((temp <= 50) && (wind > 4.8)) {
        ans = 35.74 + (0.6215 * temp) - (35.75 * (wind ** 0.16)) + (0.4275 * temp * (wind ** 0.16));
        return ans.toFixed(0);
    } else {
        return "N/A";
    }
}


// Weather summary and 5-day forecast

const apiURL = "https://api.openweathermap.org/data/2.5/weather?id=5585010&units=imperial&APPID=a01a11697bf0b81c9a84598e38f0c90f";
const apiURL2 = "https://api.openweathermap.org/data/2.5/forecast?id=5585010&units=imperial&APPID=a01a11697bf0b81c9a84598e38f0c90f";

fetchAPI = (apiURL, num) => {
    fetch(apiURL)
        .then((response) => response.json())
        .then((jsObject) => {

            switch (num) {
                case 1:
                    this.summaryBox(jsObject);
                    break;
                case 2:
                    this.fiveDay(jsObject);
                    break;
            }
        });
}

summaryBox = (jsObject) => {
    var mainObj = jsObject.main;

    let cityName = jsObject.name;
    let current = jsObject.weather[0].description;
    let high = mainObj.temp_max,
        temp = mainObj.temp,
        humidity = mainObj.humidity;
    let windSpeed = jsObject.wind.speed;

    document.getElementById('city-name').textContent = cityName;
    document.getElementById('current').textContent = current;
    document.getElementById('high').textContent = high.toFixed(0);
    document.getElementById('temp').textContent = temp.toFixed(0);
    document.getElementById('humidity').textContent = humidity;
    document.getElementById('wind-speed').textContent = windChill(jsonObject.main.temp, jsonObject.wind.speed);

    }

fiveDay = (jsObject) => {
    var count = 0;

    for (key in jsObject.list) {
        var textCheck = jsObject.list[key].dt_txt;
        if (textCheck.includes("18:00:00")) {
            count++;
            var varDay = "";
            var getDayVar = new Date(jsObject.list[key].dt_txt).getDay();

            switch (getDayVar) {
                case 1:
                    varDay = "Mon";
                    break;
                case 2:
                    varDay = "Tues";
                    break;
                case 3:
                    varDay = "Wed";
                    break;
                case 4:
                    varDay = "Thur";
                    break;
                case 5:
                    varDay = "Fri";
                    break;
                case 6:
                    varDay = "Sat";
                    break;
                case 0:
                    varDay = "Sun";
                    break;
            }

            const imagesrc = 'https://openweathermap.org/img/w/' + jsObject.list[key].weather[0].icon + '.png';
            const desc = jsObject.list[key].weather[0].description;

            document.getElementById('day' + count).textContent = jsObject.list[key].main.temp.toFixed(0);

            document.getElementById('icon' + count).setAttribute('src', imagesrc);
            document.getElementById('icon' + count).setAttribute('alt', desc);

            document.getElementById('forecast' + count).textContent = varDay;
        }
    }
}


fetchAPI(apiURL, 1);
fetchAPI(apiURL2, 2);

// Events
const requestURL = 'https://byui-cit230.github.io/weather/data/towndata.json';

fetch(requestURL)
    .then(function(response) {
        return response.json();
    })

.then(function(jsonObject) {
    console.table(jsonObject);

    const towns = jsonObject['towns'];
    for (let i = 0; i < towns.length; i++) {
        if (towns[i].name == 'Fish Haven') {
            let eventscard = document.createElement('section');
            let event1 = document.createElement('h5');
            let event2 = document.createElement('h5');
            let event3 = document.createElement('h5');


            event1.textContent = towns[i].events[0];
            eventscard.appendChild(event1);

            event2.textContent = towns[i].events[1];
            eventscard.appendChild(event2);

            event3.textContent = towns[i].events[2];
            eventscard.appendChild(event3);

            document.querySelector('div.event').appendChild(eventscard);
        }
    }
});