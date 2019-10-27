Temperature = parseFloat(document.getElementById('Temperature').textContent);
WindSpeed = parseFloat(document.getElementById('WindSpeed').textContent);

if ((Temperature <= 50) && (WindSpeed > 4.8)) {
    WindChill = 35.74 + (0.6215 * Temperature) - (35.75 * (WindSpeed ** 0.16)) + (0.4275 * Temperature * (WindSpeed ** 0.16));
} else {
    WindChill = "N/A";
}

document.getElementById('WindChill').innerHTML = WindChill.toFixed(0);