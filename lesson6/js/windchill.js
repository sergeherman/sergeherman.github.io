var DayTemp = document.getElementById('DayTemp').value;
var WindSpeed = document.getElementById('WindSpeed').value;

if (isNaN(WindSpeed) || isNaN(DayTemp)) {
    document.getElementById("chill").innerHTML = "N/A";
} else {
    document.getElementById("chill").innerHTML = WindChill(DayTemp, WindSpeed);
}

function WindChill(DayTemp, WindSpeed) {
    return ((35.74 + 0.6215 * DayTemp - 35.75 * Math.pow(WindSpeed, 0.16) + 0.4275 * DayTemp * Math.pow(WindSpeed, 0.16));
}