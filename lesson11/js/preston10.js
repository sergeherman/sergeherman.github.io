const apiURL = "https://api.openweathermap.org/data/2.5/weather?id=5604473&units=imperial&APPID=a01a11697bf0b81c9a84598e38f0c90f";

const apiURL2 = "https://api.openweathermap.org/data/2.5/forecast?id=5604473&units=imperial&APPID=a01a11697bf0b81c9a84598e38f0c90f";

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
    document.getElementById('wind-speed').textContent = windSpeed;

    this.checkWindchill(temp, windSpeed);
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

checkWindchill = (temp, windSpeed) => {
    let t = (temp <= 50) ? true : false;
    let s = (windSpeed > 3.0) ? true : false;
    var chillDiv = document.getElementById("wind-chill");

    if (t && s) {

        let exp = Math.pow(windSpeed, 0.16);
        let feh = 35.74 + (0.6215 * temp) - (35.75 * exp) + (0.4275 * temp * exp);

        chillDiv.innerHTML = feh.toFixed(0) + ' F';

    } else {
        chillDiv.innerHTML = 'N/A';
    }
}

fetchAPI(apiURL, 1);
fetchAPI(apiURL2, 2);